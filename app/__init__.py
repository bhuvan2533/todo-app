"""Setup at app startup"""
from flask import Flask
import psycopg2

app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrpqvpmbg5e4khp9dv0-a.oregon-postgres.render.com",
        database="todo_app_uwfh",
        user="todo_app_uwfh_user",
        password="FLcly76oNvivzBdAl06umgxq3oJvvPNo")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
