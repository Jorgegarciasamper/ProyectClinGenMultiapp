from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import base64
import dash

from app import app
import apps.app2 as app2
import apps.appClinGen as appClinGen
import apps.appIndex as appIndex
import apps.app404 as app404

image_filename = 'assets/img/head.png' # image head
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

header = html.Div(children=[
                html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),height=50),
                html.H1(
                    children="ClinGen", className="header-title"
                ),
                html.P(
                    children="This application relates "
                             "gene to implicated disease",
                    className="header-description",
                ),
                ],className="header" # Aprovechamos el css header para poner la imagen centrada

)

fdivs = [html.H2("Footer")]
for f in range(5):
    fdivs.append(html.P(f'Footer line {f}'))
footer = html.Div(fdivs, className="FOOTER_STYLE")

sidebar = html.Div([
    html.H2("Sidebar"),
    html.Hr(),
    html.P("A simple sidebar layout with navigation links", className="lead"),
    dbc.Nav([
        dbc.NavItem(
            dbc.NavLink("Index", href="/", id="page-Index-link")),
        dbc.NavItem(
            dbc.NavLink("Choose a gen", href="/apps/appClinGen", id="page-1-link")),
        dbc.NavItem(
            dbc.NavLink("Page 2", href="/apps/app2", id="page-2-link")),
    ], vertical=True, pills=True,
    )],
    className="SIDEBAR_STYLE"
)

content = html.Div( className="CONTENT_STYLE")


app.layout = html.Div([
    header,
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
     sidebar, footer, content
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):

    if pathname == '/':
         return appIndex.layout
    elif pathname == '/apps/appClinGen':
         return appClinGen.layout
    elif pathname == '/apps/app2':
         return app2.layout
    else:
        return app404.layout

if __name__ == '__main__':
    app.run_server(debug=True)