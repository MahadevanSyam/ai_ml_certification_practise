from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Hello , this is our Flask Website";

if __name__=='__main__':
    app.run(debug=False)