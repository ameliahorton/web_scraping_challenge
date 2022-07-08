# Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import time

from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    news_title, news_text = nasa_text(browser)
    jpl_image = jpl(browser)
    html_table = facts(browser)
    cerberus_url, schiaparelli_url, syrtis_url, vm_url = hemispheres(browser)

    mars_info = {'news_title': news_title,
    'news_text': news_text,
    'jpl_image': jpl_image,
    'facts': html_table,
    'cerberus_url': cerberus_url,
    'schiaparelli_url': schiaparelli_url,
    'syrtis_major_url': syrtis_url,
    'valles_mariners_url': vm_url
    }
    return mars_info

def nasa_text(browser):
    nasa_url = 'https://redplanetscience.com/'
    browser.visit(nasa_url)
    time.sleep(1)
    html = browser.html

    nasa_soup = bs(html, "html.parser")

    news_title = nasa_soup.find_all('div', class_='content_title')[0].text
    news_text = nasa_soup.find_all('div', class_='article_teaser_body')[0].text
    return news_title, news_text

def jpl(browser):
    # jpl space image
    jpl_url = 'https://spaceimages-mars.com/'
    browser.visit(jpl_url)
    full_image_button = browser.find_by_tag('button')[1]
    full_image_button.click()
    time.sleep(1)
    html = browser.html

    jpl_soup = bs(html, 'html.parser')
    featured_image_url = jpl_url+jpl_soup.find('img', class_='fancybox-image').get('src')

    return featured_image_url

def facts(browser):
    # Mars facts url and table
    mars_facts_url = 'https://galaxyfacts-mars.com'
    fact_table = pd.read_html(mars_facts_url)
    mars_fact_df = fact_table[1]
    html_table = mars_fact_df.to_html()

    return html_table

def hemispheres(browser):
    # mars hemispheres
    cer_url = 'https://marshemispheres.com/'
    browser.visit(cer_url)
    cer_link = browser.find_by_tag('h3')[0]
    cer_link.click()
    time.sleep(1)
    html = browser.html
    cer_soup = bs(html, 'html.parser')
    cerberus_url = cer_url+cer_soup.find('img', class_='wide-image').get('src')

    sch_url = 'https://marshemispheres.com/'
    browser.visit(sch_url)
    sch_link = browser.find_by_tag('h3')[1]
    sch_link.click()
    time.sleep(1)
    html = browser.html
    sch_soup = bs(html, 'html.parser')
    schiaparelli_url = sch_url+sch_soup.find('img', class_='wide-image').get('src')

    syr_url = 'https://marshemispheres.com/'
    browser.visit(syr_url)
    syr_link = browser.find_by_tag('h3')[2]
    syr_link.click()
    time.sleep(1)
    html = browser.html
    syr_soup = bs(html, 'html.parser')
    syrtis_url = syr_url+syr_soup.find('img', class_='wide-image').get('src')

    vm_url = 'https://marshemispheres.com/'
    browser.visit(vm_url)
    vm_link = browser.find_by_tag('h3')[3]
    vm_link.click()
    time.sleep(1)
    html = browser.html
    vm_soup = bs(html, 'html.parser')
    vm_url = vm_url+vm_soup.find('img', class_='wide-image').get('src')

    return cerberus_url, schiaparelli_url, syrtis_url, vm_url
    
    browser.quit()


if __name__=='__main__':
    mars_info = scrape()
    print (mars_info)

    