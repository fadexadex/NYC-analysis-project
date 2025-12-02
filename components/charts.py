import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Modern Color Palette
COLORS = {
    'primary': '#2563EB',      # Blue 600
    'secondary': '#64748B',    # Slate 500
    'success': '#10B981',      # Emerald 500
    'danger': '#EF4444',       # Red 500
    'warning': '#F59E0B',      # Amber 500
    'info': '#06B6D4',         # Cyan 500
    'background': '#FFFFFF',   # White
    'text': '#0F172A',         # Slate 900
    'grid': '#E2E8F0'          # Slate 200
}

def apply_chart_theme(fig):
    """Apply consistent modern theme to all charts"""
    fig.update_layout(
        font={'family': 'Inter, sans-serif', 'color': COLORS['text']},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=40, b=20),
        hoverlabel=dict(
            bgcolor="white",
            font_size=14,
            font_family="Inter, sans-serif",
            bordercolor=COLORS['grid']
        ),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=True,
            linecolor=COLORS['grid'],
            tickfont=dict(color=COLORS['secondary'])
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor=COLORS['grid'],
            gridwidth=0.5,
            zeroline=False,
            showline=False,
            tickfont=dict(color=COLORS['secondary'])
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        # Animation settings
        transition={'duration': 500, 'easing': 'cubic-in-out'},
        hovermode='x unified'
    )
    return fig

def create_bar_chart(df, x, y, title, color=COLORS['primary'], labels=None):
    fig = px.bar(df, x=x, y=y, title=None, labels=labels)
    fig.update_traces(
        marker_color=color,
        marker_line_color='white',
        marker_line_width=1.5,
        opacity=0.9,
        hovertemplate='<b>%{x}</b><br>%{y:,.0f}<extra></extra>'
    )
    return apply_chart_theme(fig)

def create_line_chart(df, x, y, title, color=COLORS['primary'], labels=None):
    fig = px.line(df, x=x, y=y, title=None, labels=labels)
    fig.update_traces(
        line_color=color,
        line_width=3,
        mode='lines+markers',
        marker=dict(size=6, line=dict(width=2, color='white'))
    )
    return apply_chart_theme(fig)

def create_dual_axis_chart(df, x, y1, y2, name1, name2, title):
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(x=df[x], y=df[y1], name=name1,
              marker_color=COLORS['primary'],
              marker_line_color='white',
              marker_line_width=1.5,
              opacity=0.8),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(x=df[x], y=df[y2], name=name2,
                  line=dict(color=COLORS['success'], width=3),
                  mode='lines+markers',
                  marker=dict(size=6, line=dict(width=2, color='white'))),
        secondary_y=True
    )
    
    fig = apply_chart_theme(fig)
    fig.update_layout(title=None, hovermode='x unified')
    return fig

def create_pie_chart(df, values, names, title):
    fig = px.pie(df, values=values, names=names, title=None,
                 color_discrete_sequence=[COLORS['primary'], COLORS['success'], COLORS['warning'], COLORS['info'], COLORS['secondary']])
    
    fig.update_traces(
        textposition='inside',
        textinfo='percent+label',
        marker=dict(line=dict(color='#FFFFFF', width=2)),
        pull=[0.05, 0, 0, 0, 0]
    )
    return apply_chart_theme(fig)

def create_scatter_chart(df, x, y, size, color, title, labels=None):
    fig = px.scatter(df, x=x, y=y, size=size, color=color,
                    title=None, labels=labels,
                    color_continuous_scale=px.colors.sequential.Blues)
    
    fig.update_traces(
        marker=dict(line=dict(width=1, color='white'), opacity=0.8)
    )
    return apply_chart_theme(fig)