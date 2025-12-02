import os
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import plotly.express as px
from pymongo import MongoClient
import dash
from dash import dcc, html, Input, Output, callback, clientside_callback
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

# Import custom components
from components.sidebar import create_sidebar
from components.cards import create_stat_card, create_chart_card
from components.charts import (
    create_bar_chart, create_line_chart, create_dual_axis_chart,
    create_pie_chart, create_scatter_chart, COLORS, apply_chart_theme
)

# Load environment variables
load_dotenv()

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "yellow_taxi_stats")

# Initialize MongoDB connection
try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    print("✓ Connected to MongoDB successfully")
except Exception as e:
    print(f"✗ MongoDB connection failed: {e}")
    db = None

# Initialize Dash app with external stylesheets and scripts
app = dash.Dash(
    __name__, 
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap"
    ],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
)
app.title = "NYC Yellow Taxi Analytics"
server = app.server

# Helper function to fetch data from MongoDB
def fetch_collection_data(collection_name):
    """Fetch data from MongoDB collection"""
    try:
        if db is None:
            return pd.DataFrame()
        
        collection = db[collection_name]
        data = list(collection.find({}, {'_id': 0}))
        
        if not data:
            print(f"⚠ No data found in {collection_name}")
            return pd.DataFrame()
        
        df = pd.DataFrame(data)
        print(f"✓ Loaded {len(df)} records from {collection_name}")
        return df
    
    except Exception as e:
        print(f"✗ Error fetching {collection_name}: {e}")
        return pd.DataFrame()

# App Layout
app.layout = html.Div([
    # Toast for notifications
    html.Div(id="toast-container", className="toast-container"),
    
    # Main Container
    html.Div([
        # Sidebar
        create_sidebar(),
        
        # Main Content Area
        html.Div([
            # Header removed
            
            # Scrollable Content
            html.Div([
                dcc.Loading(
                    id="loading",
                    type="default",
                    parent_className="loading-wrapper",
                    children=[
                        html.Div(id='stats-cards', className="grid-container stats-grid"),
                        html.Div(id='main-content', className="animate-fade-in-up delay-200")
                    ]
                )
            ], className="content-scroll-area")
            
        ], className="main-content")
        
    ], className="app-container")
])

# Callback to update content based on selected collection
@callback(
    [Output('stats-cards', 'children'),
     Output('main-content', 'children')],
    Input('collection-selector', 'value')
)
def update_dashboard(selected_collection):
    """Update dashboard based on selected collection"""
    
    df = fetch_collection_data(selected_collection)
    
    if df.empty:
        return (
            html.Div("No data available", className="col-span-12 text-center p-8 text-danger"),
            html.Div()
        )
    
    # Generate stats cards
    stats_cards = generate_stats_cards(df, selected_collection)
    
    # Generate visualizations based on collection
    charts = generate_charts(df, selected_collection)
    
    return stats_cards, charts

def generate_stats_cards(df, collection_name):
    """Generate summary statistics cards"""
    
    cards = []
    
    if 'trip_count' in df.columns:
        total_trips = df['trip_count'].sum()
        cards.append(create_stat_card(
            "Total Trips", 
            f"{total_trips:,.0f}", 
            "lucide:car-taxi-front", 
            COLORS['primary'],
            trend="up", trend_value="12%",
            index=0
        ))
    
    if 'avg_fare' in df.columns:
        avg_fare = df['avg_fare'].mean()
        cards.append(create_stat_card(
            "Avg Fare", 
            f"${avg_fare:.2f}", 
            "lucide:banknote", 
            COLORS['success'],
            trend="up", trend_value="5.3%",
            index=1
        ))
    
    if 'total_revenue' in df.columns:
        total_revenue = df['total_revenue'].sum()
        cards.append(create_stat_card(
            "Total Revenue", 
            f"${total_revenue:,.0f}", 
            "lucide:dollar-sign", 
            COLORS['warning'],
            trend="down", trend_value="2.1%",
            index=2
        ))
    
    if 'avg_distance' in df.columns:
        avg_distance = df['avg_distance'].mean()
        cards.append(create_stat_card(
            "Avg Distance", 
            f"{avg_distance:.2f} mi", 
            "lucide:map-pin", 
            COLORS['info'],
            index=3
        ))
    
    # If we don't have enough specific metrics, add a generic one
    if len(cards) < 4:
        cards.append(create_stat_card(
            "Data Points", 
            f"{len(df):,}", 
            "lucide:database", 
            COLORS['secondary'],
            index=len(cards)
        ))
    
    # Wrap in grid columns
    # Force col-span-3 to ensure 4 cards always fit in one row (12/3 = 4)
    return [html.Div(card, className="col-span-3") for card in cards]

def generate_charts(df, collection_name):
    """Generate appropriate charts based on collection"""
    
    charts_layout = []
    
    if collection_name == 'hourly_demand':
        # Trip count by hour
        fig1 = create_bar_chart(
            df, 'pickup_hour', 'trip_count', 
            'Trip Count by Hour', 
            labels={'pickup_hour': 'Hour of Day', 'trip_count': 'Trips'}
        )
        charts_layout.append(html.Div(
            create_chart_card("Hourly Demand", dcc.Graph(figure=fig1, config={'displayModeBar': False}), index=0),
            className="col-span-12 lg:col-span-8"
        ))
        
        # Average fare and distance
        fig2 = create_dual_axis_chart(
            df, 'pickup_hour', 'avg_fare', 'avg_distance',
            'Avg Fare', 'Avg Distance', 'Fare vs Distance'
        )
        charts_layout.append(html.Div(
            create_chart_card("Fare & Distance Trends", dcc.Graph(figure=fig2, config={'displayModeBar': False}), index=1),
            className="col-span-12 lg:col-span-4"
        ))
    
    elif collection_name == 'dow_stats':
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        df['day_name'] = df['pickup_day'].apply(lambda x: days[x-1] if 1 <= x <= 7 else 'Unknown')
        
        fig1 = create_bar_chart(
            df, 'day_name', 'trip_count', 
            'Weekly Trips',
            labels={'day_name': 'Day', 'trip_count': 'Trips'}
        )
        charts_layout.append(html.Div(
            create_chart_card("Weekly Trip Distribution", dcc.Graph(figure=fig1, config={'displayModeBar': False}), index=0),
            className="col-span-12 lg:col-span-6"
        ))
        
        if 'total_revenue' in df.columns:
            fig2 = create_bar_chart(
                df, 'day_name', 'total_revenue', 
                'Weekly Revenue',
                color=COLORS['success'],
                labels={'day_name': 'Day', 'total_revenue': 'Revenue'}
            )
            charts_layout.append(html.Div(
                create_chart_card("Weekly Revenue", dcc.Graph(figure=fig2, config={'displayModeBar': False}), index=1),
                className="col-span-12 lg:col-span-6"
            ))
            
    elif collection_name == 'monthly_stats':
        df['month_label'] = df['pickup_year'].astype(str) + '-' + df['pickup_month'].astype(str).str.zfill(2)
        
        fig1 = create_dual_axis_chart(
            df, 'month_label', 'trip_count', 'total_revenue',
            'Trips', 'Revenue', 'Monthly Performance'
        )
        charts_layout.append(html.Div(
            create_chart_card("Monthly Performance", dcc.Graph(figure=fig1, config={'displayModeBar': False}), index=0),
            className="col-span-12"
        ))

    elif collection_name == 'daily_stats':
        df['pickup_date'] = pd.to_datetime(df['pickup_date'])
        df_sorted = df.sort_values('pickup_date')
        
        fig1 = create_line_chart(
            df_sorted, 'pickup_date', 'trip_count', 
            'Daily Trips',
            labels={'pickup_date': 'Date', 'trip_count': 'Trips'}
        )
        charts_layout.append(html.Div(
            create_chart_card("Daily Trip Trend", dcc.Graph(figure=fig1, config={'displayModeBar': False}), index=0),
            className="col-span-12"
        ))
        
    elif collection_name == 'payment_stats':
        payment_labels = {1: 'Credit Card', 2: 'Cash', 3: 'No Charge', 4: 'Dispute', 5: 'Unknown'}
        df['payment_name'] = df['payment_type'].map(payment_labels)
        
        fig1 = create_pie_chart(
            df, 'trip_count', 'payment_name', 
            'Payment Distribution'
        )
        charts_layout.append(html.Div(
            create_chart_card("Payment Methods", dcc.Graph(figure=fig1, config={'displayModeBar': False}), index=0),
            className="col-span-12 md:col-span-6"
        ))
        
        if 'avg_tip_percent' in df.columns:
            fig2 = create_bar_chart(
                df, 'payment_name', 'avg_tip_percent', 
                'Tip % by Payment',
                color=COLORS['success'],
                labels={'payment_name': 'Payment Type', 'avg_tip_percent': 'Tip %'}
            )
            charts_layout.append(html.Div(
                create_chart_card("Tipping Behavior", dcc.Graph(figure=fig2, config={'displayModeBar': False}), index=1),
                className="col-span-12 md:col-span-6"
            ))
            
    elif collection_name == 'passenger_dist':
        fig1 = create_bar_chart(
            df, 'passenger_count', 'trip_count', 
            'Passenger Count',
            labels={'passenger_count': 'Passengers', 'trip_count': 'Trips'}
        )
        charts_layout.append(html.Div(
            create_chart_card("Passenger Distribution", dcc.Graph(figure=fig1, config={'displayModeBar': False}), index=0),
            className="col-span-12 md:col-span-6"
        ))
        
        if 'avg_fare' in df.columns:
            fig2 = create_line_chart(
                df, 'passenger_count', 'avg_fare', 
                'Fare by Passengers',
                color=COLORS['success'],
                labels={'passenger_count': 'Passengers', 'avg_fare': 'Avg Fare'}
            )
            charts_layout.append(html.Div(
                create_chart_card("Fare Analysis", dcc.Graph(figure=fig2, config={'displayModeBar': False}), index=1),
                className="col-span-12 md:col-span-6"
            ))
            
    elif collection_name == 'distance_stats':
        fig1 = create_bar_chart(
            df, 'distance_category', 'trip_count', 
            'Distance Distribution',
            labels={'distance_category': 'Distance', 'trip_count': 'Trips'}
        )
        charts_layout.append(html.Div(
            create_chart_card("Trip Distances", dcc.Graph(figure=fig1, config={'displayModeBar': False}), index=0),
            className="col-span-12 md:col-span-6"
        ))
        
        fig2 = create_bar_chart(
            df, 'distance_category', 'avg_fare', 
            'Fare by Distance',
            color=COLORS['success'],
            labels={'distance_category': 'Distance', 'avg_fare': 'Avg Fare'}
        )
        charts_layout.append(html.Div(
            create_chart_card("Cost vs Distance", dcc.Graph(figure=fig2, config={'displayModeBar': False}), index=1),
            className="col-span-12 md:col-span-6"
        ))
        
    elif collection_name == 'cluster_stats':
        fig1 = create_scatter_chart(
            df, 'avg_distance', 'avg_fare', 'trip_count', 'cluster_id',
            'Cluster Analysis',
            labels={'avg_distance': 'Distance', 'avg_fare': 'Fare', 'trip_count': 'Trips'}
        )
        charts_layout.append(html.Div(
            create_chart_card("Cluster Analysis", dcc.Graph(figure=fig1, config={'displayModeBar': False}), index=0),
            className="col-span-12 lg:col-span-8"
        ))
        
        fig2 = create_bar_chart(
            df, 'cluster_id', 'trip_count', 
            'Cluster Size',
            labels={'cluster_id': 'Cluster', 'trip_count': 'Trips'}
        )
        charts_layout.append(html.Div(
            create_chart_card("Cluster Sizes", dcc.Graph(figure=fig2, config={'displayModeBar': False}), index=1),
            className="col-span-12 lg:col-span-4"
        ))
        
    elif collection_name == 'feature_importance':
        df_sorted = df.sort_values('importance', ascending=True)
        fig1 = px.bar(df_sorted, y='feature', x='importance', orientation='h',
                     title=None, labels={'feature': 'Feature', 'importance': 'Importance'})
        fig1.update_traces(marker_color=COLORS['success'], opacity=0.9)
        fig1 = apply_chart_theme(fig1) # Use helper from charts.py but need to import it or redefine
        
        # Re-apply theme locally since we used px directly
        fig1.update_layout(
            font={'family': 'Inter, sans-serif', 'color': COLORS['text']},
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=20, b=20)
        )
        
        charts_layout.append(html.Div(
            create_chart_card("Model Feature Importance", dcc.Graph(figure=fig1, config={'displayModeBar': False}), index=0),
            className="col-span-12"
        ))
        
    elif collection_name == 'ratecode_stats':
        ratecode_labels = {
            1: 'Standard', 2: 'JFK', 3: 'Newark', 
            4: 'Nassau/Westchester', 5: 'Negotiated', 6: 'Group Ride', 99: 'Unknown'
        }
        df['ratecode_name'] = df['RateCodeID'].map(ratecode_labels)
        
        fig1 = create_bar_chart(
            df, 'ratecode_name', 'trip_count', 
            'Rate Code Distribution',
            labels={'ratecode_name': 'Rate Code', 'trip_count': 'Trips'}
        )
        charts_layout.append(html.Div(
            create_chart_card("Rate Code Usage", dcc.Graph(figure=fig1, config={'displayModeBar': False}), index=0),
            className="col-span-12 md:col-span-6"
        ))
        
        fig2 = create_bar_chart(
            df, 'ratecode_name', 'avg_fare', 
            'Fare by Rate Code',
            color=COLORS['success'],
            labels={'ratecode_name': 'Rate Code', 'avg_fare': 'Avg Fare'}
        )
        charts_layout.append(html.Div(
            create_chart_card("Cost by Rate Code", dcc.Graph(figure=fig2, config={'displayModeBar': False}), index=1),
            className="col-span-12 md:col-span-6"
        ))
    
    return html.Div(charts_layout, className="grid-container")

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)