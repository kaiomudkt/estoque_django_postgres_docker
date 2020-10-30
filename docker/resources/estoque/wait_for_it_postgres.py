import time

import psycopg2 as pg

from time import sleep
from os import environ as env


def connection_database():
    """Establish a connection to PostgreSQL.
    Returns:
        connection object -- object that allows connection to the bank
    """
    return pg.connect(dbname=env['DB_NAME'],
                      user=env['DB_USER'],
                      host=env['DB_HOST'],
                      password=env['DB_PASSWORD'],
                      connect_timeout=env['CONNECT_TIMEOUT'])


def timeout(tic: float, toc: float):
    """
    Check if a timeout occurred according to the past parameters.
    Arguments:
        tic {float} -- start time a timer
        toc {float} -- end time a stopwatch.
    Returns:
        boolean -- Returns true if the timeout was not given,
                    otherwise false will be returned.
    """
    return (toc-tic) > int(env['CONNECT_TIMEOUT'])


def is_server_up(tic: float):
    """Check if the service is running.
    Arguments:
        tic {float} -- start time a stopwatch.
    Raises:
        TimeoutError: Exception issued when the service is not operational before
                    the time specified by the user
    Returns:
        Boolean -- Returns true if PostgreSQL is working, otherwise it will return false
    """
    while True:
        try:
            conn = connection_database()
            conn.close()
            return True
        except BaseException:
            sleep(int(env['CHECK_SERVICE']))
        finally:
            toc = time.time()
            if timeout(tic, toc):
                raise TimeoutError