from bs4 import BeautifulSoup
from datetime import datetime


def extract_price(adv):
    cost = adv.find('span', 'item-price')
    return cost


def extract_data(adv):
    return dict(price=extract_price(adv))


def extract_link(li):
    a = li.find('a')
    link = a.attrs.get('href', '')  # a.attrs['href']
    return link


def html_parse(data):
    soup = BeautifulSoup(data, 'html.parser')
    adv_ul = soup.select_one('#search-results')
    adv_list = adv_ul.find_all('li')
    data = list()
    for li in adv_list:
        link = extract_link(li)
        print(link)
        data.append({'link': link, 'flag': False})
    return data


def parse_page(data):
    soup = BeautifulSoup(data, 'html.parser')
    data = dict(title=None, price=None, body=None, post_id=None, datetime=None)

    title = soup.select_one('#titletextonly')
    if title is not None:
        data['title'] = title.text

    price = soup.select_one('.price')
    if price is not None:
        data['price'] = price.text

    body = soup.select_one('#postingbody')
    if body is not None:
        data['body'] = body.text

    post_id = soup.select_one('p.postinginfo:nth-child(1)')
    if post_id is not None:
        data['post_id'] = post_id.text[9:]

    datetime_tag = soup.select_one('.postinginfos > p:nth-child(2) > time:nth-child(1)')
    if datetime_tag is not None:
        data['datetime'] = datetime.strptime(datetime_tag.text, '%Y-%m-%d %H:%M')
    images_link = set()
    for image in soup.find_all('img'):
        images_link.add(image.attrs['src'].replace('50x50c', '600x450'))
    return data, images_link
