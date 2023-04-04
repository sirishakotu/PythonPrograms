# imports
import requests
import pandas as p
from bs4 import BeautifulSoup

response = requests.get("https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.brand%255B%255D%3DPanasonic&p%5B%5D=facets.brand%255B%255D%3DIFB&p%5B%5D=facets.brand%255B%255D%3DCARRIER&p%5B%5D=facets.brand%255B%255D%3DHitachi&p%5B%5D=facets.brand%255B%255D%3DDaikin&param=675&otracker=clp_creative_card_2_3.creativeCard.CREATIVE_CARD_tvs-and-appliances-new-clp-store_NARD2OPRN57P&fm=neo%2Fmerchandising&iid=M_a6c3dea0-1924-4f0c-ad1a-674c83507fb9_3.NARD2OPRN57P&ppt=clp&ppn=tvs-and-appliances-new-clp-store&ssid=d59zgkdg7k0000001676347091885")
# print(response)  ### response should be 200 for success
soup = BeautifulSoup(response.content,'html.parser')

# Items names details,here am taking AC item from Flipkart

names_items = soup.find_all('div',class_ = "_4rR01T")
name_items= []
for i in names_items[0:10]:
    a=i.get_text()
    # print(a) ## We can know line by line the name of item 
    name_items.append(a)

# Prices of AC items

price_items = soup.find_all('div',class_ = '_30jeq3 _1_WHN1')
price = []
for i in price_items[0:10]:
    a = i.get_text()
    # print(a)
    price.append(a)

# Ratings of AC items

ratings_items = soup.find_all('div',class_ = '_3LWZlK')
ratings = []
for i in ratings_items[0:10]:
    a = i.get_text()
    # print(a)
    ratings.append(a)

# Images of AC items

image_items = soup.find_all('img',class_ = '_396cs4')
images = []
for i in image_items[0:10]:
    a = i['src']  #  Every image link is in source code
    # print(a)
    images.append(a)

# Links of AC items

link_items = soup.find_all('a',class_ = '_1fQZEK')
links = []
for i in link_items[0:10]:
    a = "http://www.flipkart.com" + i['href']
    # print(a)
    links.append(a)

# Storing everything in File Format

df = p.DataFrame()

df['AC Names'] = name_items
df['AC Prices'] = price
df['AC Ratings'] = ratings
df['AC Images'] = images
df['AC Links'] = links

# Converting to File using 'to_csv
df.to_csv('AC_Data.csv')




