from flask import Flask, render_template, request, redirect, url_for
from avatartest import avatar_creator

# Route for handling the login page logic
app = Flask(__name__)
@app.route('/avatars', methods=['GET', 'POST'])
def home():
    content = request.json
    avatar_creator(content['skin'], content['hair'], content['top'], content['facial'])
    return json()
