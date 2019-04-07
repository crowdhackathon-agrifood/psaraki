from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint('home', __name__)


@blueprint.route('/')
def index():
    return render_template('index.html')


@blueprint.route('/search')
def search():
    return render_template('search.html')


@blueprint.route('/producer')
@login_required
def producer():
    return render_template('producer.html')


@blueprint.route('/producer_registration')
def producer_registration():
    return render_template('producer_registration.html')


@blueprint.route('/consumer')
@login_required
def consumer():
    return render_template('consumer.html')


@blueprint.route('/payment')
@login_required
def payment():
    return render_template('payment.html')


@blueprint.route('/products')
@login_required
def products():
    return render_template('products.html')
