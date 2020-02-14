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
        data = stock_l(ticker)
        return render_template('stock.html', data=data)
    else:
        return render_template('stock.html')







