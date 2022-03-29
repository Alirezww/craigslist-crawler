from urllib.parse import urlparse
from mongo import save_links
from parser import html_parse, parse_page
from mongo import save_page, save_images


def generate_filename(url):
    parsed = urlparse(url)
    return ''.join(['_'.join(parsed.path.split('/'[2:4])), '_', parsed.query.replace('=', '_'), '.html'])


def store_data_to_file(response_obj):
    with open(generate_filename(response_obj.url), 'w') as f:
        f.writelines(response_obj.text)


def store_data_to_mongo(response_obj):
    data = html_parse(response_obj.text)
    if len(data):
        save_links(data)
    return len(data)


def store_data(response_obj, db=True):
    print(response_obj.url)
    if db:
        return store_data_to_mongo(response_obj)
    return store_data_to_file(response_obj)


def store_page(response_obj):
    print(response_obj.url)
    data, images = parse_page(response_obj.text)
    save_page(data)
    save_images({'post_id': data['post_id'], 'images': list(images)})


def store_image(response_obj):
    with open('images.jpg', 'wb') as f:
        f.write(response_obj.content)
