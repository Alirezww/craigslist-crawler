import requests
from store import store_data, store_page, store_image
from mongo import get_links, set_flag, get_images_link


def start_crawl(url):
    crawl = True
    page = 0
    while crawl:
        response = requests.get(url.format(page * 120))
        page += 1
        crawl = store_data(response)
    print(f'{page - 1} pages found..')


def get_one_single_page(link):
    response = requests.get(link)
    if response.ok:
        store_page(response)
        return True
    return False


def crawl_pages():
    links = get_links()
    for link in links:
        result = get_one_single_page(link['link'])
        if result:
            set_flag(link['_id'])


def download_one_image(image_link):
    response = requests.get(image_link)
    if response.ok:
        store_image(response)
    print("done")


def download_images():
    post_images = get_images_link()
    for post_image in post_images:
        for image_link in post_image['images']:
            download_one_image(image_link)


if __name__ == '__main__':
    target = 'https://seoul.craigslist.org/search/apa?s={}'
    # crawl_pages()
    # start_crawl(target)
    # download_images()
