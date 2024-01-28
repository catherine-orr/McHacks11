from flask import Flask, render_template

app = Flask(__name__)

def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


hair_color = input("what is your hair color?")
eye_color = input("what color are your eyes")
height = input("how tall are you?")
ethnicity = input("what is your ethnicity?")
