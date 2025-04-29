from dash import Dash, html, dcc, page_container
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Breast Cancer Dashboard"

app.layout = dbc.Container([
    html.H1("Breast Cancer Classifier Dashboard", className="text-center my-4"),
    dcc.Tabs([
        dcc.Tab(label='🏠 Home', value='/'),
        dcc.Tab(label='📊 Feature Importance', value='/feature-importance'),
        dcc.Tab(label='🔍 Survival Predictor', value='/predict')
    ], id='tabs', value='/', persistence=True),
    page_container
], fluid=True)

if __name__ == "__main__":
    app.run_server(debug=True)