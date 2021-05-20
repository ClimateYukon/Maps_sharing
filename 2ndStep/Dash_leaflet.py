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
    ], style={'width': '100%', 'height': '100vh', 'margin': "auto", "display": "block"}, id="map"),
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



# from : https://lyz-code.github.io/blue-book/coding/python/dash_leaflet/


'''Check that out :
import dash_leaflet as dl
import gpxpy

icon = {
    "iconUrl": "https://leafletjs.com/examples/custom-icons/leaf-green.png",
    "shadowUrl": "https://leafletjs.com/examples/custom-icons/leaf-shadow.png",
    "iconSize": [38, 95],  # size of the icon
    "shadowSize": [50, 64],  # size of the shadow
    "iconAnchor": [
        22,
        94,
    ],  # point of the icon which will correspond to marker's location
    "shadowAnchor": [4, 62],  # the same for the shadow
    "popupAnchor": [
        -3,
        -76,
    ],  # point from which the popup should open relative to the iconAnchor
}


def get_data():
    gpx_file = open("data.gpx", "r")
    gpx = gpxpy.parse(gpx_file)
    markers = []
    for waypoint in gpx.waypoints:
        markers.append(
            dl.Marker(
                title=waypoint.name,
                position=(waypoint.latitude, waypoint.longitude),
                icon=icon,
                children=[
                    dl.Tooltip(waypoint.name),
                    dl.Popup(waypoint.name),
                ],
            )
        )
    cluster = dl.MarkerClusterGroup(id="markers", children=markers)
    return cluster


app = dash.Dash(__name__)
app.layout = html.Div(
    dl.Map(
        [
            dl.TileLayer(),
            get_data(),
        ],
        zoom=7,
        center=(40.0884, -3.68042),
    ),
    style={
        "height": "100vh",
    },
)'''
