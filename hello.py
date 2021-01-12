from flask import Flask,  render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/CreateVenue')
def CreateClient():
    return render_template('CreateVenue.html')


@app.route('/CreateClient')
def CreateVenue():
    return render_template('CreateClient.html')


@app.route('/CreateEvent')
def CreateEvent():
    return render_template('CreateEvent.html')


if __name__ == '__main__':
    app.run(debug=True)
