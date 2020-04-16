import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=macbook&_sacat=0"
headers ={"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content,'html.parser')

title1 = soup.find_all(attrs={"s-item__title"})
price1 = soup.find_all(attrs={"s-item__price"})

titles = [x.get_text() for x in title1]
prices = [y.get_text() for y in price1]

#Sort qilsam chiroyli tursa kk csv da
titles = np.array(titles)
prices = np.array(prices)

indices = np.argsort(titles)
titles = titles[indices]
prices = prices[indices]


df = pd.DataFrame({"Narxlar ":prices,"Maxsulotlar ":titles})
df.to_csv("birinchiCrawled_data.csv",index=False)


print("Crawl Natijasi CSV filega saqlandi!")
                
