from modules.olx_handler import get_publications
from modules.proxy_getter import find_working_proxy
from modules.publication_filter import get_date, filter_by_time, filter_by_words

good_proxy = find_working_proxy()

min_sum = '500'
max_sum = '1000'

get_publications(min_sum, max_sum, good_proxy)


#debug testing

#end

