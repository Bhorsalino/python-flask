from flask import Flask

app = Flask(__name__)


def generate_html(message):
    version_number = '0001'
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
        </html>""".format(message, version_number)
    return html


def greet():
    greeting = 'Welcome to CI/CD'
    return greeting


@app.route('/')
def hello_world():
    html = generate_html(greet())
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
