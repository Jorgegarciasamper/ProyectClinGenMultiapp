from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

from app import app

content = html.Div([
    html.H1('Index'),
    html.Hr(),
    html.P("This is the index page of our application ...", className="lead"),

],className="CONTENT_STYLE")

adbar = html.Div([
    html.H2("Tutorial!!"),
    html.Hr(),
    html.P("I am the tutorial screen I will give you explanations "
           "for the correct operation of the application", className="lead"),

    ],
    className="ADBAR_STYLE"
)
layout = html.Div([adbar, content])