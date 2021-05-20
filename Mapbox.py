import plotly.graph_objects as go

token = 'pk.eyJ1IjoianNjaHJvZGVyIiwiYSI6ImNrb3d6bmNoazA5bmsydWxkbHRyNWdkdGgifQ.3FS4CO-7ce5J5GC3nugl-g'

fig = go.Figure(go.Scattermapbox(
    mode = "markers+text+lines",
    lon = [-75, -80, -50, 35], lat = [45, 20, -20 , 10],
    marker = {'size': 20, 'symbol': ["shelter", "campsite", "car", 'commercial']},
    text = ["Bus", "Harbor", "airport",'aaa'],textposition = "bottom right"))

fig.update_layout(
    mapbox = {
        'accesstoken': token,
        'style': "satellite", 'zoom': 0.7},
    showlegend = False)

fig.show()