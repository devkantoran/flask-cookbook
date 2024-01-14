from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello to the World of Flask!"


# Alternatively comment below code and use flask run --debug
# if __name__ == "__main__":
#     app.run(debug=True)


if __name__ == "__main__":
    # app.config.from_object("configuration.BaseConfig")
    # app.config.from_object("configuration.ProductionConfig")
    # app.config.from_object("configuration.StagingConfig")
    app.config.from_object("configuration.DevelopmentConfig")
    print("SECRET_KEY:", app.config["SECRET_KEY"])
    print("DEBUG:", app.config["DEBUG"])
    print("TESTING:", app.config["TESTING"])
    print("NEW_CONFIG_VARIABLE:", app.config["NEW_CONFIG_VARIABLE"])
    app.run()




