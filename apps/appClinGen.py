import dash_table
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from app import app

url_data = 'https://raw.githubusercontent.com/Jorgegarciasamper/ClinGen/master/CSV/Clingen-Gene-Disease-Summary-2021-04-09.csv'
df = pd.read_csv(url_data,delimiter=',',skiprows=(0,1,2,3,5),header=[0])
df_genes_disease = df[['GENE SYMBOL', 'DISEASE LABEL']]


adbar = html.Div([
    html.H2("Gens"),
    html.Hr(),
    html.P("Select the gene to visualize the disease", className="lead"),
    dcc.Dropdown( id='demo-dropdown',
                options=[
                    {'label': gen, 'value': gen}
                    for gen in df_genes_disease['GENE SYMBOL'].unique()
                ],
                value='A2ML1',

                ),

    ],
    className="ADBAR_STYLE"
)

cdivs = [dash_table.DataTable(id='dd-output-container',
                         data=df_genes_disease.to_dict('records'),
                         columns=[{'id': c, 'name': c} for c in df_genes_disease.columns.values],
# Style headers with a dotted underline to indicate a tooltip
    style_header_conditional=[{
        'if': {'column_id': col},#Subrayado la col
        'textDecoration': 'underline',
        'textDecorationStyle': 'dotted',
    } for col in ['GENE SYMBOL', 'DISEASE LABEL']],

    # Overflow into ellipsis
    style_cell={
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'maxWidth': 0,
    },
    tooltip_delay=0,
    tooltip_duration=None
)]


content = html.Div(cdivs, className="CONTENT_STYLE")

layout = html.Div([adbar, content])

@app.callback(
    dash.dependencies.Output('dd-output-container', 'data'),
    [dash.dependencies.Input('demo-dropdown', 'value')])
def update_output(value):
    dfs = df_genes_disease.loc[df_genes_disease['GENE SYMBOL'] == value]
    dfss=dfs.drop_duplicates()



    return dfss.to_dict('records')

