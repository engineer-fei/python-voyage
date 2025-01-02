from flask import Blueprint, render_template, request
from datetime import datetime
from .data_fetcher import (
    load_stock_data,
    load_global_development_data,
    fetch_nasa_api_data,
    fetch_alpha_vantage_data
)
from .data_processor import (
    process_stock_data,
    process_global_development_data,
    process_nasa_data,
    process_alpha_vantage_data
)
from .data_visualizer import (
    visualize_stock_data,
    visualize_global_development_data,
    visualize_nasa_data,
    visualize_alpha_vantage_data
)

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    #return render_template('dashboard.html')
    # Toggle between data sources by changing this variable
    #data_source = "alpha_api"  # Options: "stock_file", "global_dev_file", "nasa_api", "alpha_api"
    # Get the data source from the query parameters
    data_source = request.args.get('source', 'stock_file')  # Default to 'stock_file'


    data, visualization_html = None, "<p>No data available.</p>"

    if data_source == "stock_file":
        data = load_stock_data()
        data = process_stock_data(data) if data is not None else None
        visualization_html = visualize_stock_data(data) if data is not None else "<p>Error in visualization.</p>"


    elif data_source == "global_dev_file":
        data = load_global_development_data()
        data = process_global_development_data(data) if data is not None else None
        visualization_html = visualize_global_development_data(data) if data is not None else "<p>Error in visualization.</p>"

    elif data_source == "nasa_api":
        data = fetch_nasa_api_data()
        #print(data) #debug
        data = process_nasa_data(data) if data is not None else None
        visualization_html = visualize_nasa_data(data) if data is not None else "<p>Error in visualization.</p>"

    elif data_source == "alpha_api":
        data = fetch_alpha_vantage_data()
        data = process_alpha_vantage_data(data) if data is not None else None
        visualization_html = visualize_alpha_vantage_data(data) if data is not None else "<p>Error in visualization.</p>"

    else:
        data = None

    if data is not None:
        data_preview = data.head(20).to_html()
    else:
        data_preview = "<p>Error loading data.</p>"
    return render_template('dashboard.html', data_preview=data.head().to_html() if data is not None else "<p>Error loading data.</p>", visualization_html=visualization_html)

    #return render_template('dashboard.html', year=datetime.now().year, data_preview=data.head().to_html() if data is not None else "<p>Error loading data.</p>", visualization_html=visualization_html)
    #return render_template('dashboard.html', year=datetime.now().year, data_preview=data.head().to_html() if data is not None else "<p>Error loading data.</p>")

