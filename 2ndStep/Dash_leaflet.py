import dash_html_components as html
import dash_leaflet as dl
import dash_leaflet.express as dlx
import dash
import geojson
from geojson import Feature, Point, FeatureCollection
from dash.dependencies import Output, Input
from dash_extensions.javascript import arrow_function
app = dash.Dash()

with open(r"C:\Users\julien_schroder\Desktop\JM_FinaleMaps_Repo\Points4326.geojson") as f:
    points = geojson.load(f)
with open(r"C:\Users\julien_schroder\Desktop\JM_FinaleMaps_Repo\Routes4326.geojson") as g:
    routes = geojson.load(g)


dRoutes = FeatureCollection([f for f in routes['features']])
dPoints = FeatureCollection([f for f in points['features']])

biosfera = dlx.geojson_to_geobuf(dlx.dicts_to_geojson([dict(lat=29.015, lon=-118.271)]))
app.layout = html.Div([
    dl.Map(center=[39, -98], zoom=4, children=[
        dl.TileLayer(),
        dl.GeoJSON(data=dPoints,id='capitals',cluster=True),  # in-memory geojson (slowest option)
        dl.GeoJSON(data=dRoutes,id='states'),  # in-memory geobuf (smaller payload than geojson)
    ], style={'width': '100%', 'height': '50vh', 'margin': "auto", "display": "block"}, id="map"),
    html.Div(id="state"), html.Div(id="capital")
])


@app.callback(Output("capital", "children"), [Input("capitals", "click_feature")])
def capital_click(feature):
    if feature is not None:
        return f"You clicked {feature['properties']['Name']}"


@app.callback(Output("state", "children"), [Input("states", "hover_feature")])
def state_hover(feature):
    if feature is not None:
        return f"{feature['properties']['Name']}"



if __name__ == '__main__':
    app.run_server()
