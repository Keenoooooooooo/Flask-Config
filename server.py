from flask import Flask #--> this imports the flask module 

app = Flask(__name__)
@app.route('/')

def home():
    return "Hello World!"
if __name__ == '__main__':
    app.run()

#note: you may have a hard time executing this code on your localhost.
    #Try manually typing "localhost:5000" in your local browser instead, make sure that the Python file is already running.   
