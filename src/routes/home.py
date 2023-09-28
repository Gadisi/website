import random

from flask import Blueprint, render_template


home_route = Blueprint('home', __name__)


@home_route.get('/')
async def get_home():
    image_filenames = ['images/gallery/image_1.jpg', 'images/gallery/image_2.jpg', 'images/gallery/image_3.jpg', 'images/gallery/image_4.jpg']
    image_filename = random.choice(image_filenames)
    return render_template('index.html', image_filenames=image_filenames, image_filename=image_filename)


