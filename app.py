from dash_extensions.enrich import DashProxy, html
from dash_extensions import BeforeAfter

app = DashProxy()
app.layout = html.Div([
    BeforeAfter(before="/assets/before.jpg", after="/assets/after.jpg", width=256, height=256, defaultProgress=0.1)
])

if __name__ == "__main__":
    app.run_server()