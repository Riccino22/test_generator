from flask import Flask
import generate_test as g_test

app = Flask(__name__)

@app.route("/<topic>/<quantity>")
def home(topic, quantity):
    return g_test.generate(topic, quantity)

app.run(debug=True)