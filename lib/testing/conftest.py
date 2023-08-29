# tests/conftest.py

import pytest
import sqlite3

@pytest.fixture
def db_connection():
    connection = sqlite3.connect(':memory:')
    yield connection
    connection.close()

@pytest.fixture
def db_cursor(db_connection):
    return db_connection.cursor()
