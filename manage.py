#!/usr/bin/env python
import os

from flask.ext.script import Command, Manager, Server, Option, prompt_bool, prompt_choices
from jumper import app
import nose

# Load our configuration onto our application object
_conf = os.getenv("APP_CONFIG", "DevelopmentConfig")
_conf = "config." + _conf
app.config.from_object(_conf)

manager = Manager(app)


@manager.shell
def make_shell_context():
    return dict(app=app)

manager.add_command(
    "runserver",

    Server(
        use_debugger=app.config['DEBUG'],
        use_reloader=app.config['DEBUG'],
        host=app.config['LISTEN_HOST'],
        port=app.config['LISTEN_PORT']
    )
)

@manager.command
def test():
    from subprocess import call
    call(["nosetests", "-v",
          "--with-coverage", "--cover-package=api", "--cover-branches",
          "--cover-erase", "--cover-html", "--cover-html-dir=cover"])


if __name__ == '__main__':
    manager.run()