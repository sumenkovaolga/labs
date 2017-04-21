from urllib.parse import quote_plus
import requests
from bs4 import BeautifulSoup
import re
import random
import time

from config import *


def test():
    img_dat = download_image('https://st.kp.yandex.net/images/film_iphone/iphone360_575180.jpg')
    print(len(img_dat))


def test2():
    actor_id = get_actor_id_by_name('Джонни Депп')
    film_ids_list = get_film_ids_list_by_actor_id(actor_id)
    get_film_info_by_id(random.choice(film_ids_list))
    pass


def get_actor_id_by_name(actor_name):
    esc_actor_name = quote_plus(actor_name)
    url = URLMASK_FIND_ACTOR.format(esc_actor_name)
    print(url)
    html_text = requests.get(url, params='', headers=HEADERS, timeout=60).text

    soup = BeautifulSoup(html_text, "lxml")

    pattern = re.compile(r'Скорее всего, вы ищете:')
    el = soup.find(text=pattern).parent.parent
    actor_id = el.a['data-id']
    print('actor_id: {}'.format(actor_id))
    return actor_id


def get_film_ids_list_by_actor_id(actor_id):
    url = URLMASK_ACTOR_INFO.format(actor_id)
    print(url)
    time.sleep(1)
    html_text = requests.get(url, params='', headers=HEADERS, timeout=60).text


    pattern = re.compile(r'<span class=\"name\"><a href=\"/film/(\d+)/\"')

    film_ids_list = []
    for m in pattern.finditer(html_text):
        # print('%02d-%02d: %s' % (m.start(), m.end(), html_text[m.start(): m.end()]))
        film_ids_list.append(m.group(1))

    print('films count: {}'.format(len(film_ids_list)))
    return film_ids_list


def get_film_info_by_id(film_id):
    url = URLMASK_FILM_INFO.format(film_id)
    print(url)
    time.sleep(1)
    html_text = requests.get(url, params='', headers=HEADERS, timeout=60).text

    soup = BeautifulSoup(html_text, "lxml")

    ret_dict = {
        'film_href': url,
        'film_name': soup.find("meta", {'name': "mrc__share_title"})['content']
    }

    element = soup.find("meta", {'name': "mrc__share_description"})
    if element and element.has_attr('content'):
        ret_dict['film_descr'] = element['content']
    else:
        ret_dict['film_descr'] = 'Описание фильма отсутствует.'

    ret_dict['film_poster'] = soup.find('a', {'class':"popupBigImage"}).img['src']

    print('film name: {}'.format(ret_dict['film_name']))
    print('film descr: {}'.format(ret_dict['film_descr']))
    print('film poster: {}'.format(ret_dict['film_poster']))

    return ret_dict


def download_image(url):
    r = requests.get(url, stream=True)
    data = b''
    if r.status_code == 200:
        for chunk in r.iter_content(1024):
            data += chunk
    return data


if __name__ == '__main__':
    test()


