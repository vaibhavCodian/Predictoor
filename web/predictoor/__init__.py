from flask import Flask, url_for, redirect, request, render_template, flash

app = Flask(__name__)


from predictoor import routes