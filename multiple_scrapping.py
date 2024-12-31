# code
#Importing Important Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

link = 'https://books.toscrape.com/catalogue/page-1.html'

#Sending a request to the website(link)
res = requests.get(link)

#Creating a soup using BeautifulSoup
soup = BeautifulSoup(res.text,'html.parser')

Multiple_Pages = []
#tqdm used for better representation.
for page in tqdm(range(1,51)):
  	#using a for loop as there are 50 pages then creating a link using page-1,page-2...page-50
    link = 'https://books.toscrape.com/catalogue/page-'+str(page)+'.html'
    res = requests.get(link)
    soap = BeautifulSoup(res.text,'html.parser')
    #same code as in scraping for 1 page
    for sp in soap.find_all('li',class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3'):
       
        book_link   = "https://books.toscrape.com/catalogue/" + sp.find_all('a')[-1].get('href')

        title       = sp.find_all('a')[-1].get('title')

        img_link    = "https://books.toscrape.com/" + sp.find('img').get('src')[3:]

        book_rating = (sp.find('p').get('class')[-1])

        price       = sp.find('p',class_='price_color').text[1:]

        stock       =  sp.find('p',class_ = 'instock availability').text.strip()

        Multiple_Pages.append([title,book_rating,price,stock,book_link,img_link])

 

#Creating a Dataframe
Multiple_Pages_df = pd.DataFrame(data=Multiple_Pages)
Multiple_Pages_df = Multiple_Pages_df.rename(columns={0: 'Title', 1: 'Rating',2:'Price',3:'Stock Available',4:'Book Link',5:'Image Link'})
df_1 = Multiple_Pages_df


#Saving the Dataframe in a csv file

Multiple_Pages_df.to_csv('All Books.csv',index=False)