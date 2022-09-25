from flask import Flask

app = Flask(__name__)

@app.route('/')
def Homepage():
    return 'Welcome to Homepage'

@app.route('/Careers')
def Careers():
    return 'Welcome to the Careers page'

@app.route('/Mission')
def Mission():
    return 'This is the Mission of the company'

if __name__ == '__main__': 
    app.run(debug=True, host='localhost', port=8000)



