from flask import Flask, session, request, render_template
import surveys

app = Flask(__name__)
app.secret_key = "Vive La France"


@app.route('/')
def 