#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time

# In[51]:

def scrape():

    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path)


    # In[17]:


    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(5) # time delay
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[18]:

    
    news_title = soup.find('li', class_='slide')
    article_title = soup.find('li', class_='slide').get_text()
    news_title = news_title.find("div", class_="content_title").get_text()


    # In[19]:


    print(news_title)
    print(article_title)


    # In[39]:


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[40]:


    # featured_image_url = soup.find('a', class_='button fancybox')
    # print(featured_image_url)

    browser.click_link_by_id("full_image")
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    soup.find("img",class_="fancybox-image").get("src")


    # In[41]:


    featured_image_url = soup.find("img",class_="fancybox-image").get("src")
    full_url = "https://www.jpl.nasa.gov" + featured_image_url
    print(full_url)


    # In[42]:


    src="/spaceimages/images/mediumsize/PIA19180_ip.jpg"


    # In[43]:


    import pandas as pd


    # In[47]:


    pf = pd.read_html("https://space-facts.com/mars/")[0]
    pf 


    # In[93]:


    table = pf.to_html()


    # In[83]:


    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[84]:


    resurlt_set = soup.find_all("img",class_="thumb")


    # In[85]:


    resurlt_set[1].get("src")
    resurlt_set[1].get("alt")


    # In[86]:


    titles = []
    pictures = []
    for i in range(4):
        titles.append(resurlt_set[i].get("alt"))
        pictures.append(resurlt_set[i].get("src"))


    # In[87]:


    print(titles)
    print(pictures)


    # In[91]:


    full_pics = [] 
    for p in pictures:
        full_pics.append("https://astrogeology.usgs.gov"+ p)


    # In[92]:


    mars_dic = dict(zip(titles,full_pics))
    mars_dic


    # In[96]:


    everything_dic = {"news_title":news_title,
                    "article_title":article_title,
                    "full_url":full_url,
                    "table":table,
                    "mars_dic":mars_dic
                    }
    
    return everything_dic


# testing the scrape
# result = scrape()

# print(result)




