from flask import Blueprint, render_template

blueprint = Blueprint('home', __name__)


@blueprint.route('/')
def index():
    return render_template('index.html')


@blueprint.route('/search')
def search():
    return render_template('search.html')


@blueprint.route('/producer')
def producer():
    return render_template('producer.html')


@blueprint.route('/consumer')
def consumer():
    return render_template('consumer.html')


@blueprint.route('/payment')
def payment():
    return render_template('payment.html')
