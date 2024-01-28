from flask import Flask, render_template, request
import os

app = Flask(__name__)

img = os.path.join('index' , 'Image')

@app.route("/")
def home():
    file = os.path.join(img, 'GP.png')
    return render_template('image_render.html', image=file)

if __name__ == '__main__':
    app.run(debug=True)

'''
hair_color = input("what is your hair color?")
eye_color = input("what color are your eyes")
height = input("how tall are you?")
ethnicity = input("what is your ethnicity?")
'''