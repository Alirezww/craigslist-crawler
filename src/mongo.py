from pymongo import MongoClient
import logging
client = MongoClient()
db = client['crawler']
links_collection = db.links
advertisements_collection = db.advertisements
images_collection = db.images

logger = logging.getLogger(__name__)


def save_links(data):
    return links_collection.insert_many(data)


def get_links():
    return links_collection.find({'flag': False})


def get_images_link():
    return images_collection.find()


def save_page(data):
    return advertisements_collection.insert_one(data)


def save_images(images):
    return images_collection.insert_one(images)


def set_flag(link_id):
    links_collection.find_one_and_update(
        {"_id": link_id}, {"$set": {'flag': True}}
    )
