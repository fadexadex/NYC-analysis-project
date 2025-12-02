from dash import html, dcc
from dash_iconify import DashIconify

def create_sidebar():
    """
    Create the application sidebar with navigation items.
    """
    nav_items = [
        {'label': 'Hourly Demand', 'value': 'hourly_demand', 'icon': 'lucide:clock'},
        {'label': 'Day Stats', 'value': 'dow_stats', 'icon': 'lucide:calendar'},
        {'label': 'Monthly Trends', 'value': 'monthly_stats', 'icon': 'lucide:bar-chart-2'},
        {'label': 'Daily Stats', 'value': 'daily_stats', 'icon': 'lucide:activity'},
        {'label': 'Payments', 'value': 'payment_stats', 'icon': 'lucide:credit-card'},
        {'label': 'Passengers', 'value': 'passenger_dist', 'icon': 'lucide:users'},
        {'label': 'Distances', 'value': 'distance_stats', 'icon': 'lucide:map'},
        {'label': 'Clusters', 'value': 'cluster_stats', 'icon': 'lucide:pie-chart'},
        {'label': 'Features', 'value': 'feature_importance', 'icon': 'lucide:sliders'},
        {'label': 'Rate Codes', 'value': 'ratecode_stats', 'icon': 'lucide:tag'},
    ]
    
    return html.Div([
        # Sidebar Header
        html.Div([
            html.Div([
                DashIconify(icon="lucide:taxi", width=28, color="#2563EB"),
                html.H3("NYC Taxi", style={'marginLeft': '12px', 'fontSize': '18px', 'fontWeight': '700', 'color': '#0F172A', 'margin': '0 0 0 12px'})
            ], className="d-flex align-items-center mb-4 px-2"),
            
            html.P("ANALYTICS DASHBOARD", style={'fontSize': '11px', 'fontWeight': '600', 'color': '#94A3B8', 'letterSpacing': '1px', 'paddingLeft': '8px', 'marginBottom': '16px'})
        ], className="sidebar-header p-3"),
        
        # Navigation Items
        html.Div([
            html.Div([
                dcc.RadioItems(
                    id='collection-selector',
                    options=[
                        {
                            'label': html.Span([
                                DashIconify(icon=item['icon'], className="nav-icon"),
                                html.Span(item['label'])
                            ], className="d-flex align-items-center"),
                            'value': item['value']
                        } for item in nav_items
                    ],
                    value='hourly_demand',
                    className="nav-menu",
                    labelClassName="nav-item",
                    inputClassName="d-none" # Hide default radio button
                )
            ])
        ], className="flex-grow-1 overflow-auto"),
        
        # Sidebar Footer
        html.Div([
            html.Div([
                html.Div([
                    html.P("Data Source", className="text-xs font-bold text-primary mb-1"),
                    html.Div([
                        DashIconify(icon="simple-icons:mongodb", width=14, className="me-1"),
                        html.Span("MongoDB Atlas", className="text-xs text-secondary")
                    ], className="d-flex align-items-center")
                ], className="bg-blue-50 p-3 rounded-lg border border-blue-100")
            ], className="p-3")
        ])
    ], className="sidebar")