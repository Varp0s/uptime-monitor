from helpers.file_helpers import read_domains
from database.db import init_db, fetch_data
from plugins.uptime_status import monitor_domains
from dash import Dash, dcc, html
import plotly.graph_objs as go
from dash.dependencies import Output, Input
import threading

init_db()

domains = read_domains('domains.txt')

monitoring_thread = threading.Thread(target=monitor_domains, args=(domains,))
monitoring_thread.daemon = True
monitoring_thread.start()

app = Dash(__name__)

def title():
    return "Uptime Monitor"



app.title = title()
app._favicon = "assets/img/favicon.ico"

app.layout = html.Div([
    html.H1("Uptime Monitor", style={'fontStyle': 'italic'}),
    dcc.Loading(id="loading...", children=[html.Div(id="loading-output")], type="default"),
    dcc.Interval(id='interval-component', interval=1*60000, n_intervals=0),
    dcc.Graph(id='live-graph'),
    html.Footer("© 2024 - Uptime Monitor Powered by Varp0s", style={'textAlign': 'center'}) 
])

@app.callback(
    Output('live-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    df = fetch_data()
    data = []
    
    for domain in df['domain'].unique():
        domain_data = df[df['domain'] == domain]
        trace = go.Scatter(
            x=domain_data['checked_at'],
            y=domain_data['status'],
            mode='lines+markers',
            name=domain
        )
        data.append(trace)
    
    return {'data': data, 'layout': go.Layout(title='Domain Uptime Status')}

if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=1453)