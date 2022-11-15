from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route("/")

def homePage():
    name = "Rodrigo Barbosa"
    details = readDetails('static/description.txt')
    return render_template('base.html', name=name, aboutMe=details)



# Function to read in details for page
@app.route("/")
def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]


@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    if request.method == 'POST':
        name=request.form['name']
    return render_template('form.html', name=name)



# @app.route("/hi/<name>")
# def hello_world2(name="nobody"):

#     information = {'name': 'chris',
#                    'job': 'student'
#                    }
#     return render_template('hello.html', myVar=name)


# @app.route("/test/<name>")
# def test(name="nobody"):

#     return render_template('test.html', result=name)