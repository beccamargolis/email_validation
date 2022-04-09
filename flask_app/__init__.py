from flask import Flask, session

app = Flask(__name__)

app.secret_key = "I like to bake banana muffins with walnuts on Sundays."