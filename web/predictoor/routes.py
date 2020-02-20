from flask import render_template, url_for, flash, redirect, request, abort
from predictoor import app
from predictoor.model_loader import stock_l
from PIL import Image
import secrets
import os

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/stock')
def stock():
    ticker = request.args.get('ticker')
    if ticker:
        data_m, data_p = stock_l(ticker)
        # return data_p
        return render_template('stock.html', data_m=data_m, data_p=data_p)
    else:
        return render_template('stock.html')

@app.route('/pne', methods=['GET'])
def index():
	# Main Page
	return render_template('pneumonia.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():

	# Constants:
	classes = {'TRAIN': ['BACTERIA', 'NORMAL', 'VIRUS'],
	           'VALIDATION': ['BACTERIA', 'NORMAL'],
	           'TEST': ['BACTERIA', 'NORMAL', 'VIRUS']}

	if request.method == 'POST':

		# Get the file from post request
		f = request.files['file']

		# Save the file to ./uploads
		basepath = os.path.dirname(__file__)
		file_path = os.path.join(
			basepath, 'uploads', secure_filename(f.filename))
		f.save(file_path)

		# Make a prediction
		prediction = model_predict(file_path, model)

		predicted_class = classes['TRAIN'][prediction[0]]
		print('We think that is {}.'.format(predicted_class.lower()))

		return str(predicted_class).lower()







