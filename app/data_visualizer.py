import plotly.express as px

# Visualize Stock Data (Line Chart)
def visualize_stock_data(data):
    fig = px.line(data, x='Date', y='Price', title='Stock Prices Over Time')
    return fig.to_html(full_html=False)

# Visualize Global Development Data (Bar Chart)
def visualize_global_development_data(data):
    fig = px.bar(data, x='Region', y='Value', color='Year', title='Global Value by Region')
    return fig.to_html(full_html=False)
'''
# Visualize NASA API Data (Simple Image and Title Display)
def visualize_nasa_data(data):
    fig_html = f"<h3>{data['title'].iloc[0]}</h3><img src='{data['url'].iloc[0]}' alt='NASA Image' style='width:100%; max-width:600px;'>"
    return fig_html
'''
def visualize_nasa_data(data):
    if data is None or data.empty:
        return "<p>No data available for visualization.</p>"

    # Extract the first (and only) row
    date = data['date'].iloc[0]
    title = data['title'].iloc[0]
    explanation = data['explanation'].iloc[0]
    image_url = data['url'].iloc[0]  # Use 'url' or 'hdurl'

    # Build HTML visualization
    visualization_html = f"""
    <div class="nasa-visualization">
        <h3>{title}</h3>
        <p><strong>Date:</strong> {date}</p>
        <img src="{image_url}" alt="{title}" style="max-width:100%; height:auto;">
        <p>{explanation}</p>
    </div>
    """
    return visualization_html


# Visualize Alpha Vantage Data (Line Chart for Stock Prices)
def visualize_alpha_vantage_data(data):
    fig = px.line(data, x='Date', y='Close', title='Alpha Vantage Daily Stock Close Prices')
    return fig.to_html(full_html=False)
