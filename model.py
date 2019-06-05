# This code creates a UI for the user to post their posts on the social media
# Author : Shreya Mitra
# Created : Shreya Mitra
# Date : 05.06.2019
# Version : 1.1


import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))


def create_post(name, content):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values(?, ?)', (name, content))
    con.commit()
    con.close()


def get_posts():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts
