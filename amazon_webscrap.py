# Web Scrapping of Amazon Smart Watches

import requests
import pandas as p
from bs4 import BeautifulSoup

response = requests.get("https://www.amazon.in/b/ref=cepc_sbc_atfbau_2?pf_rd_r=J7BE3A9P75ZVQ625VRHW&pf_rd_p=11a61045-3230-41fe-9812-a177c633a897&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-3&pf_rd_t=&pf_rd_i=976419031&node=11599648031")
# print(response)    # <Response [200]>
# print(response.content)

soup = BeautifulSoup(response.content,"html.parser")

# # Smart Watches items from Amazon

watches_items = soup.find_all('span',class_ = 'a-truncate-cut')
watches = []
for i in watches_items[0:10]:
     a = i.get_text()
     print(a)
     watches.append(a)