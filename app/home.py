from flask import Blueprint, render_template, json
import os

home_blueprint = Blueprint('home', __name__, template_folder='templates')


def load_json():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "data", "data-day-1.json")
    data = json.load(open(json_url))
    return data

ROW_PER_PAGE = 40
@home_blueprint.route('/nextpage/<page>')
def next_page(page):
   data = load_json()
   new_page = int(page) + ROW_PER_PAGE
   return render_template("index.html", data=data[int(page)+1:new_page])

@home_blueprint.route('/prevpage/<page>')
def prev_page(page):
   data = load_json()
   new_page = int(page) - ROW_PER_PAGE
   return render_template("index.html", data=data[new_page:(int(page)+1)])

@home_blueprint.route('/')
def index():
   data = load_json()
   return render_template("index.html", data=data[:40])

@home_blueprint.route('/invoice/<id>')
def show(id):
   data = load_json()
   return render_template("show.html", data=data[int(id)])
