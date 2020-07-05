from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

def appendToFile(data):
	with open('db.txt', mode='a') as db:
		email = data['email']
		subject = data['subject']
		msg = data['msg']
		file = db.write(f'\n{email}\t {subject}\t {msg}')

def appendToCSV(data):
	with open('db.csv', mode='a', newline='') as csvfile:
		email = data['email']
		subject = data['subject']
		msg = data['msg']	
		csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, msg])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			appendToCSV(data)
			return redirect('/thankyou.html')
		except:
			return 'something went wrong - didn\' save to db'
	else:
		return 'Missed\'er bud'



# @app.route('/<username>/<int:post_id>')
# def user(username=None, post_id=None):
#     return render_template('index.html', name=username, id=post_id)