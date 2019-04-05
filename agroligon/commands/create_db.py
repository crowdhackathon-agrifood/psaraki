import click
from flask.cli import with_appcontext

from agroligon import db


@click.command(name='create-db')
@with_appcontext
def create_db():
    db.create_all()
    db.session.commit()
    print('Database created successfully.')
