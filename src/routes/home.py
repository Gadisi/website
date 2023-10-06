import random
import sqlite3
from flask import Blueprint, render_template

home_route = Blueprint('home', __name__)


@home_route.get('/')
async def get_home():
    image_filenames = ['images/gallery/image_1.jpg', 'images/gallery/image_2.jpg', 'images/gallery/image_3.jpg',
                       'images/gallery/image_4.jpg']
    image_filename = random.choice(image_filenames)
    return render_template('index.html', image_filenames=image_filenames, image_filename=image_filename)


@home_route.get('/admin/login')
async def login():
    return render_template('auth.html')


@home_route.get('/admin')
async def admin():
    conn = sqlite3.connect('projects.db')
    cursor = conn.cursor()
    return render_template('admin/admin.html')
