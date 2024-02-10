from flask import Flask, request, render_template, redirect, url_for, abort, flash, session, g
import os

import pymysql.cursors
from dotenv import load_dotenv

load_dotenv()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        print(os.environ)
        db = g._database = pymysql.connect(
            host=os.environ.get('DB_HOST'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'),
            database=os.environ.get('DB_NAME'),
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    return db

