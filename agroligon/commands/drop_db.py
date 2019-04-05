import click
from flask.cli import with_appcontext

from agroligon import db


@click.command(name='drop-db')
@with_appcontext
def drop_db():
    db.drop_all()
    db.session.commit()
    print('Database dropped successfully.')
