"""
Author: Sean Sabour
Description: A simple way to return the pg_dump results.
"""
import sys
import subprocess

def dump(url):
    """
    Runs pg_dump on remote machine
    """
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)

def dump_file_name(url, timestamp=None):
    db_name = url.split("/")[-1]
    db_name = db_name.split("?")[0]
    if timestamp:
        return f"{db_name}-{timestamp}.sql"
    else:
        return f"{db_name}.sql"
