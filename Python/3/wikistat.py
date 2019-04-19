# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import re
import os


def get_link_list(html_doc):

    '''    html_doc = ''
    if not path:
        path = '.'
    try:
        with open(path + file_name, 'r') as f:
            html_doc = f.read()
    except:
        return []
    '''
    soup = BeautifulSoup(html_doc, 'lxml')
    link_list = soup.find_all('a', href=True)
    return_list = []
    #link_list = soup.find_all(re.compile('<a href=("\/wiki\/(\D)+?")(\D)*<\/a>'))
    for current_link in link_list:
        if re.match(r'^\/wiki\/(\D)*$', current_link['href']):
            return_list.append(current_link['href'].split('/wiki/')[1])
    return list(set(return_list))

def find_end(link, end, decide_list, step_list, files):
    if len(step_list) > 10:
        return

    link_list = files.setdefault(link, {'links': []})
    if end in link_list['links']:
        decide_list.append(tuple(step_list))
        return
    for current_link in link_list['links']:
        if current_link not in step_list:
            stop_link = False
            for current_decide in decide_list:
                if current_link in current_decide:
                    stop_link = True
                    break
            if stop_link:
                continue

            step_list.append(current_link)
            find_end(current_link, end, decide_list, step_list, files)
            step_list.remove(current_link)


def fill_files_html(path, files):
    for key in files:
        with open(path + key, 'r') as f:
            files[key] = {'html': f.read()}
            files[key]['links'] = get_link_list(files[key]['html'])

# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_tree(start, end, path):
    link_re = re.compile(r"(?<=/wiki/)[\w()]+")  # Искать ссылки можно как угодно, не обязательно через re
    files = dict.fromkeys(os.listdir(path))  # Словарь вида {"filename1": None, "filename2": None, ...}
    fill_files_html(path, files)
    link_list = files[start]['links']
    decide_list = []
    decide_len = 0
    for current_link in link_list:
        stop_link = False
        for current_decide in decide_list:
            if current_link in current_decide:
                stop_link = True
                break
        if stop_link:
            continue
        step_list = [start]
        find_end(current_link, end, decide_list, step_list, files)
        if len(decide_list) > decide_len:
            decide_len = len(decide_list)
            print (decide_list)
    # TODO Проставить всем ключам в files правильного родителя в значение, начиная от start

    return files

def calculate_brige(filed_dict, purpose, bridge):
    pass


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_bridge(start, end, path):
    files = build_tree(start, end, path)
    all_bridge = []
    calculate_brige(files, end, all_bridge)
    bridge = []
    # TODO Добавить нужные страницы в bridge
    return bridge


def parse(start, end, path):
    """
    Если не получается найти список страниц bridge, через ссылки на которых можно добраться от start до end, то,
    по крайней мере, известны сами start и end, и можно распарсить хотя бы их: bridge = [end, start]. Оценка за тест,
    в этом случае, будет сильно снижена, но на минимальный проходной балл наберется, и тест будет пройден.
    Чтобы получить максимальный балл, придется искать все страницы. Удачи!
    """

    bridge = build_bridge(start, end, path)  # Искать список страниц можно как угодно, даже так: bridge = [end, start]

    # Когда есть список страниц, из них нужно вытащить данные и вернуть их
    out = {}
    for file in bridge:
        with open("{}{}".format(path, file)) as data:
            soup = BeautifulSoup(data, "lxml")

        body = soup.find(id="bodyContent")

        # TODO посчитать реальные значения
        imgs = 5  # Количество картинок (img) с шириной (width) не меньше 200
        headers = 10  # Количество заголовков, первая буква текста внутри которого: E, T или C
        linkslen = 15  # Длина максимальной последовательности ссылок, между которыми нет других тегов
        lists = 20  # Количество списков, не вложенных в другие списки

        out[file] = [imgs, headers, linkslen, lists]

    return out
