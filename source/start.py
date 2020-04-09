from modules.olx_handler import get_publications
from modules.proxy_getter import find_working_proxy
from modules.publication_filter import get_date, sort_by_time

#good_proxy = find_working_proxy()

min_sum = '500'
max_sum = '1000'

#get_publications(min_sum, max_sum, good_proxy)


#debug testing
text="Оперативная память Samsung DDR3L 1600 8GB Intel/AMD для ноутбука Ноутбуки и аксессуары » " \
     "Запчасти для ноутбуков OLX Доставка 550 грн. Кирово Сегодня 10:09"

sort_by_time(text)
#end

