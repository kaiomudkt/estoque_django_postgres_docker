#!/usr/bin/env python

import os
import time
import wait_for_it_postgres

from dotenv import load_dotenv
from subprocess import run as ps


def load_environment(env_file_path: str):
    """Load variables into the environment.
    Arguments:
        env_file_path {str} -- environment variable file path
    """
    envPath = os.path.join(os.path.dirname(
        os.path.dirname(__file__)), env_file_path)
    load_dotenv(envPath)


def makemigrations():
    """Responsible for make migrations."""
    ps(['python', '/opt/app/estoque/manage.py', 'makemigrations'])
    
def migrate():
    """Responsible for applying migrations."""

    ps(['python', '/opt/app/estoque/manage.py', 'migrate'])


def create_super_user():
    """Create the root user."""
    ps(['python', '/opt/app/estoque/manage.py',
        'createsuperuser', '--noinput'])


def check_postgres_server():
    """Responsible for checking the functioning of the PostgreSQL server."""
    tic = time.time()
    is_start_postgres = wait_for_it_postgres.is_server_up(tic=tic)
    return is_start_postgres


def run_server():
    """Run the entrypoint command."""
    print(os.environ['CMD_ENTRYPOINT'])
    cmd_entrypoint = os.environ['CMD_ENTRYPOINT']
    ps(cmd_entrypoint.split())


try:
    load_environment('/opt/estoque/.env/')
    if check_postgres_server():
        print("Executing - job - makemigrations")
        makemigrations()
        print("Executing - job - migrate")
        migrate()
        print("Executing - job - create_super_user")
        create_super_user()
        print("Executing server")
        run_server()
    else:
        raise Exception('Error establishing connection')
except TimeoutError:
    raise Exception('Timeout')
