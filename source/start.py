from modules.olx_handler import get_publications
from modules.proxy_getter import find_working_proxy

good_proxy = find_working_proxy()

min_sum = '500'
max_sum = '1000'
salo = get_publications(min_sum, max_sum, good_proxy)

