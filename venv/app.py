from flask import Flask, render_template, request
from RQ import add_job, check_results, check_status, cancel_job, print_all_jobs
from SimpleToken import id2token

app = Flask(__name__)

number = -1
id = "10000"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/handle_data', methods=['POST'])
def handle_data():
    global number
    global id
    result = request.form
    for key, value in result.items():
        if key == 'number':
            number = value
    id = int(id) + 1
    id = str(id)
    new_id = add_job(int(number), id)

    print(new_id)
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def get_results():
    forms = request.form
    for key, value in forms.items():
        if key == 'id':
            id = value
    result = check_results(id)
    return render_template('results.html', value=result)


@app.route('/check_single', methods=['POST'])
def check_single():
    forms = request.form
    for key, value in forms.items():
        if key == 'id':
            id = value
    result = check_status(id)
    return render_template('index.html', value=result)


@app.route('/cancel', methods=['POST'])
def cancel():
    forms = request.form
    for key, value in forms.items():
        if key == 'id':
            id = value
    result = cancel_job(id)
    return render_template('index.html', value=result)

@app.route('/home')
def home():
    return render_template('index.html')


app.run('127.0.0.1', debug=True)