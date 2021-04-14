import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash

app = dash.Dash()
server = app.server
app.config.suppress_callback_exceptions = True

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
    dbc.themes.BOOTSTRAP,
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)