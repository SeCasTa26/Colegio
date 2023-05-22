import os

from dotenv import load_dotenv
from flask_mysqldb import MySQL

from app import app

load_dotenv()  # take environment variables from .env.

# Mysql Settings
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER') or 'root'
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD') or ''
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST') or 'localhost' # localhost
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB') or 'flaskcrud'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_PORT'] = 3307

# MySQL Connection
mysql = MySQL(app)
