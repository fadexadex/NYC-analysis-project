from dash import html
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

def create_stat_card(title, value, icon, color, trend=None, trend_value=None, index=0):
    """
    Create a modernized statistic card with animations and trend indicators.
    
    Args:
        title (str): Card title
        value (str): Main value to display
        icon (str): Iconify icon name
        color (str): Color hex code or CSS variable
        trend (str, optional): 'up' or 'down'
        trend_value (str, optional): Percentage or value change
        index (int): Index for staggered animation delay
    """
    
    # Determine trend color and icon
    trend_color = "text-success" if trend == "up" else "text-danger" if trend == "down" else "text-secondary"
    trend_icon = "heroicons:arrow-trending-up" if trend == "up" else "heroicons:arrow-trending-down" if trend == "down" else "heroicons:minus"
    
    # Calculate delay class based on index
    delay_class = f"delay-{min((index + 1) * 100, 500)}"
    
    return html.Div([
        html.Div([
            # Icon Container
            html.Div([
                DashIconify(icon=icon, width=20, color="white")
            ], style={
                'backgroundColor': color,
                'boxShadow': f'0 4px 10px {color}40'
            }, className="stat-icon-wrapper-small"),
            
            # Content
            html.Div([
                html.H4(title, className="stat-label-small"),
                html.H2(value, className="stat-value-small animate-count-up"),
                
                # Trend Indicator
                html.Div([
                    DashIconify(icon=trend_icon, width=14, className=f"me-1 {trend_color}"),
                    html.Span(trend_value, className=f"text-xs font-medium {trend_color}"),
                    html.Span(" vs last month", className="text-[10px] text-secondary ms-1")
                ], className="d-flex align-items-center mt-1") if trend else None
                
            ], className="stat-content")
            
        ], className="d-flex flex-column h-100")
    ], className=f"stat-card animate-fade-in-up {delay_class}")

def create_chart_card(title, chart_component, index=0, header_action=None):
    """
    Create a card container for charts with standard styling.
    """
    delay_class = f"delay-{min((index + 1) * 100, 500)}"
    
    return html.Div([
        html.Div([
            html.H3(title, className="chart-title"),
            header_action if header_action else None
        ], className="chart-header"),
        
        html.Div(chart_component, className="chart-body")
    ], className=f"chart-card animate-scale-up {delay_class}")