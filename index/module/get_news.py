import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import datetime

def get_LETUS_news(login_info):
    # session start
    session = requests.session()

    # action
    url_login = "https://letus.ed.tus.ac.jp/login/index.php"
    response = session.post(url_login, login_info)
    response.raise_for_status()

    url_export = "https://letus.ed.tus.ac.jp/calendar/view.php?view=month"
    response = session.get(url_export)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    date_list = soup.select('.day.text-sm-center.text-md-left.clickable')
    if not date_list:
        return {}

    info_dic = {}
    for date_info in date_list:
        date = datetime.date.fromtimestamp(int(date_info['data-day-timestamp']))
        try:
            info_list = []
            date_info_list = date_info.select_one('.d-none.d-md-block.hidden-phone.text-xs-center').select_one('div').select_one('ul').select('li')
            for i in date_info_list:
                a = i.select_one('a')
                url = a['href']
                title = a['title'].replace(' ', '')
                print(title)
                info_list.append({'url':url,'title':title})
                
            info_dic[date] = info_list
        except:
            pass

    for key in info_dic.keys():
        for i in info_dic[key]:
            res = session.get(i['url'])
            res.raise_for_status()
            try:
                #res_soup = BeautifulSoup(res.text, "html.parser")
                #a = res_soup.select_one('.page-header-headings').select_one('h1').text
                i['class_'] = "イェス"
            except:
                pass

    return info_dic