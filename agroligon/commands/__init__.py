from agroligon.commands.create_db import create_db
from agroligon.commands.drop_db import drop_db


def init_commands(app):
    # Register 'flask create-db' command
    app.cli.add_command(create_db)

    # Register 'flask drop-db' command
    app.cli.add_command(drop_db)
