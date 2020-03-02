from flask import render_template, url_for, flash, redirect, request, abort
from predictoor import app
from predictoor.model_loader import stock_l, pne
from PIL import Image
import numpy as np
from werkzeug.utils import secure_filename
import secrets
import os

# for Pnemonia
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
# .....


app.config["IMAGE_UPLOADS"] = "/home/vaibhav/Documents/code_To_learn/predictoor_/Predictoor/web/predictoor/static/images"

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
        return render_template('stock.html', ticker=ticker)

@app.route('/pne', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		if request.files:
			im = request.files["image"]
			if im.filename == '':
				print("Must Have A File Name")
				return redirect(request.url)

			filename = secure_filename(im.filename)
			im.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
			
			# print(pne(app.config["IMAGE_UPLOADS"]+"/"+filename))
			# print(image)

			path = app.config["IMAGE_UPLOADS"]+"/"+filename
			print(path)

			# model -> pred
			model = load_model('model_vgg19.h5')
			img = image.load_img(path, target_size=(224, 224))
			x = image.img_to_array(img)
			x = np.expand_dims(x, axis=0)
			img_data = preprocess_input(x)
			classes = model.predict(img_data)
			pred = "no pnemonia"
			if classes[0][0] == 0.0:
				pred = "Pnemonia"
			# print("Classes :", classes)
			# return redirect(request.url)
			return pred
	# Main Page
	return render_template('pneumonia.html')




