from flask import Flask, request
import json
import os

app = Flask(__name__)


def generate_html(message):
    version_number = "0001"
    html = """
        <html>
        <body>
            <div style='text-align:center;font-size:80px;'>
                <image height="340" width="1200" src="https://user-image.png">
                <br> {0}
                <p>Version Number: {1}</p>
                <br>
            </div>
        </body>
        </html>""".format(
        message, version_number
    )
    return html


def greet():
    greeting = "Welcome to CI/CD"
    return greeting


@app.route("/")
def hello_world():
    html = generate_html(greet())
    return html


@app.route("/", methods=["POST"])
def pubsub_push():
    message = json.loads(request.data.decode("utf-8"))
    info(f"Event display receive message:\n{message}")
    return "OK", 200


def info(msg):
    app.logger.info(msg)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
