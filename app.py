import json
from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import numpy as np
import functions.func as func
from flask import jsonify
_data = pd.read_csv('data_hcm.csv')
gia = 0
dien_tich = 0
vi_tri = ''
A1 = np.array([1, 1.1, 1.5, 2, 2.5])
A2 = np.array([1, 1.3, 1.2, 2.5, 2])
A3 = np.array([1, 1.5, 1.5, 1.5, 1.5])
A4 = np.array([1, 1.5, 1.5, 0.5, 0.8])

# Khởi tạo flask app
app = Flask(__name__)

# Khai báo các route 1 cho API
@app.route('/')
def index():
    return render_template("form.html")


@app.route("/predict", methods=['GET'])
def predict():
    return render_template("predict.html")

@app.route('/form', methods=['POST'])
def process():
	if request.method == 'POST':
		name = request.form['name']
		owner = request.form['owner']
		phone = request.form['phone']
		email = request.form['email']
		category_id = request.form['category_id']
		area_from = int(request.form['area_from'])
		area_to = int(request.form['area_to'])
		price_from = int(request.form['price_from'])
		price_to = int(request.form['price_to'])
		city_id = request.form['city_id']
		district_id = request.form['district_id']
		family = request.form['family']
		age = int(request.form['age'])
		top = []
		if (age < 35):
			top = func.main(data = _data, price_from = price_from, price_to = price_to,
						area_from = area_from, area_to = area_to, provinceName = 'Hồ Chí Minh',
						districtName = district_id, weight_vector_col1 = A1)
		elif (age <50):
			top = func.main(data = _data, price_from = price_from, price_to = price_to,
						area_from = area_from, area_to = area_to, provinceName = 'Hồ Chí Minh',
						districtName = district_id, weight_vector_col1 = A2)
		elif (age <65):
			top = func.main(data = _data, price_from = price_from, price_to = price_to,
						area_from = area_from, area_to = area_to, provinceName = 'Hồ Chí Minh',
						districtName = district_id, weight_vector_col1 = A3)
		elif (age <80):
			top = func.main(data = _data, price_from = price_from, price_to = price_to,
						area_from = area_from, area_to = area_to, provinceName = 'Hồ Chí Minh',
						districtName = district_id, weight_vector_col1 = A4)
		results = []
		for i in range(len(top)):
			z = int(top[i])

			if len(_data[_data["index"] == z]):
				item = {
					"title": _data[_data["index"] == z]['title'].values[0],
					"description": _data[_data['index'] ==z ]['description'].values[0],
					"address": _data[_data['index'] ==z ]['address'].values[0],
					"Price": _data[_data['index'] ==z ]['fPrice'].values[0],
					"Area": _data[_data['index'] == z]['fArea'].values[0],
					"Room": _data[_data['index'] == z]['bedRoom'].values[0],
					"range_school":_data[_data['index'] == z]['range_school'].values[0],
					"range_tt": _data[_data['index'] == z]['range_tt'].values[0],
					"districtName": _data[_data['index'] == z]['districtName'].values[0],
					"provinceName": _data[_data['index'] == z]['provinceName'].values[0]
				}
				results.append(item)
		#print(results)
		return render_template("predict.html", results = results)
	return render_template("form.html")


if __name__ == "__main__":
	print("App run!")
	# Load model
	app.run( debug= False , threaded=False)