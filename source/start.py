from modules.olx_handler import getPublications
from modules.proxy_getter import findWorkingProxy

good_proxy = findWorkingProxy()

min_sum = '500'
max_sum = '1000'

getPublications(min_sum, max_sum, good_proxy)






