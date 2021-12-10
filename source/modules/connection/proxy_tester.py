import math
from threading import Thread

import requests

from modules.publication_filter import get_current_time

timeout = 8
good_list = []
THREADS = 8

def verify_list(proxy_list, thread_number):
    global good_list, timeout
    working_list = []
    for prox in proxy_list:
        try:

            proxy_dict = {
                "http": "http://"+prox+"/",
            }

            r = requests.get("http://ipinfo.io/json", proxies=proxy_dict, timeout=timeout)
            site_code = r.json()
            ip = site_code['ip']
            print(get_current_time()+' [PROXY][THREAD:', thread_number,'] Proxy works:', prox)
            working_list.append(prox)
        except Exception as e:
            nihco=";)"
    good_list += working_list


def setup(number_threads, proxy_list):
    thread_amount = float(number_threads)
    amount = int(math.ceil(len(proxy_list)/thread_amount))
    proxy_lists = [proxy_list[x:x+amount] for x in range(0, len(proxy_list), amount)]
    if len(proxy_list) % thread_amount > 0.0:
        proxy_lists[len(proxy_lists)-1].append(proxy_list[len(proxy_list)-1])
    return proxy_lists


def filter_proxies(proxy_list):
    lists = setup(THREADS, proxy_list)
    thread_list = []
    count = 0
    for l in lists:
        thread_list.append(Thread(target=verify_list, args=(l, count)))
        thread_list[len(thread_list)-1].start()
        count += 1

    for x in thread_list:
        x.join()
    return good_list

