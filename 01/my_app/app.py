from flask import Flask

app = Flask(__name__, instance_path="/home/devhouse/lab/flask-cookbook/01/my_app/instance", instance_relative_config=True)


@app.route("/")
def hello_world():
    return "<img src='/static/images/logo.png'>my_app: Hello to the World of Flask!"


if __name__ == "__main__":
    app.config.from_pyfile("config.cfg", silent=False)
    app.run()
