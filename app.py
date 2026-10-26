from flash import Flask

app = Flash(__name__)

@app.route("/")
def hello_world():
    return "Hello World"