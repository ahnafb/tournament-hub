from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["UPLOAD_FOLDER"] = "./static/profile_pics"

SECRET_KEY = "AHNAF"

MONGODB_CONNECTION_STRING = "mongodb+srv://ahnafb:nanaf2730@cluster0.qzd2yiy.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGODB_CONNECTION_STRING)
db = client.dbsparta_plus_week4

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)