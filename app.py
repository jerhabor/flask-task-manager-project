import os
from flask import Flask
if os.path.exists("env.py"):
    import env


app = Flask(__name__)  # Creating an instance of Flask


@app.route("/")  # Forward slash refers to the default route
def hello():
    return "Hello world ... again!"


if __name__  == "__main__":    # Need to tell app how and where to run our app
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # During development we want to see the actual errors
