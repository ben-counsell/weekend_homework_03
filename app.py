from flask import Flask
from controllers.controller import book_blueprint

app = Flask(__name__)
app.register_blueprint(book_blueprint)