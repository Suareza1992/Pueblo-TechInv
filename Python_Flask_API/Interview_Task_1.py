from flask import Flask

app = Flask(__name__)

@app.route('/')
def pueblo_message():
    return "Lo mejor lo tiene Pueblo"

if __name__ == "__main__":
    app.run(debug=True)
"""
In the interview, I completely forgot the task said a Python/Flask API app. 
I proceeded to write a simple "print Hello World" code.
"""
