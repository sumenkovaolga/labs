

URL = 'http://www.kinopoisk.ru/'
URLMASK_FIND_ACTOR = 'https://www.kinopoisk.ru/index.php?level=7&from=forma&result=adv&m_act%5Bfrom%5D=forma&m_act%5Bwhat%5D=actor&m_act%5Bfind%5D={}'
URLMASK_ACTOR_INFO = 'https://www.kinopoisk.ru/name/{}/'
URLMASK_FILM_INFO = 'https://www.kinopoisk.ru/film/{}/'

HEADERS = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
    'Referer': 'http://www.kinopoisk.ru/',
    # 'Cookie': 'PHPSESSID=39ho8o21mhql4cl80iuvsjtiq5; last_visit=2017-03-31+12%3A54%3A20; mobile=no; noflash=true; _ym_uid=1490954148509454930; _ym_isad=1; _ym_visorc_22663942=b; user_country=ru; loc2=yes',

}
