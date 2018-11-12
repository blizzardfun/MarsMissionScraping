from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# Initialize browser
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    # ### NASA Mars News scraping
    #--------------------------------------------------
    browser = init_browser()       # Initialize browser
    # Visit NASA Mars News Site  collect the latest News Title and Paragraph Text
    url="https://mars.nasa.gov/news/"
    browser.visit(url)
    html=browser.html
        # Scrape page into soup
    soup=bs(html,"html.parser")
    # get the most recent news title and teaser
    latest_news = soup.find('li', class_="slide")
    news_title = latest_news.find('div', class_="content_title").text
    news_p=latest_news.find('div', class_="article_teaser_body").text
    #news_date=latest_news.find('div', class_="list_date").text

    # ### JPL Mars Space Images
    #---------------------------------------------------
    # Visit JPL Mars Space Images  Use splinter to navigate the site and find the image url for the current Featured Mars Image
    base_url="https://www.jpl.nasa.gov"
    images_url="/spaceimages/?search=&category=Mars/"
    url=base_url + images_url
    browser.visit(url)
        # click past first and 2nd page
    browser.click_link_by_partial_text('FULL IMAGE')
    browser.click_link_by_partial_text('more info')
    html=browser.html
    # Scrape page into soup 
    soup=bs(html,"html.parser")
    # find the figure
    figure=soup.find('figure',class_='lede')
    rel_image=figure.find('a')['href']
    # get the full url
    featured_image_url=base_url + rel_image
    #print(featured_image_url)

    # ### Mars Weather
    #--------------------------------------------------------------
    # Visit Mars Weather twitter account  scrape the latest Mars weather tweet from the page
    url="https://twitter.com/marswxreport?lang=en"
    # Scrape page into soup
    browser.visit(url)
    html=browser.html
    soup=bs(html,"html.parser")
    #save the weather data
    mars_weather = soup.find('p', class_="TweetTextSize").text

    # ### Mars Facts
    #---------------------------------------------------------------------
    # Visit Mars Facts webpage  use Pandas to scrape the table of facts about the planet( Diameter, Mass, etc)  
    url="http://space-facts.com/mars/"
        # Scrape page into pandas
    tables = pd.read_html(url)
    df=tables[0]
    # save the table as html  
    html_table = df.to_html()

    # ### Mars Hemispheres
    #----------------------------------------------------------------
    # Visit USGS Astrogeology site  obtain high resolution images for each of Mar's hemispheres.
    base_url="https://astrogeology.usgs.gov"
    image_url="/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    url=base_url + image_url
    # Scrape page into soup
    browser.visit(url)
    hemisphere_image_urls=[]

    # Cerberus Hemisphere
    browser.click_link_by_partial_text('Cerberus Hemisphere')
    html=browser.html
    soup=bs(html,"html.parser")
    #find the image and make the full url
    rel_image=soup.find('img',class_="wide-image")['src']
    image_url=base_url + rel_image
    #print(image_url)
    image_title=soup.find('h2', class_="title").text
    #print(image_title)
    #save in dictionary and add to image list
    image_dict={"title":image_title, "img_url":image_url}
    hemisphere_image_urls.append(image_dict)

    # Schiaparelli Hemisphere
    browser.back()
    browser.click_link_by_partial_text('Schiaparelli Hemisphere')
    html=browser.html
    soup=bs(html,"html.parser")
    #find the image and make the full url
    rel_image=soup.find('img',class_="wide-image")['src']
    image_url=base_url + rel_image
    #print(image_url)
    image_title=soup.find('h2', class_="title").text
    #print(image_title)
    #save in dictionary and add to image list
    image_dict={"title":image_title, "img_url":image_url}
    hemisphere_image_urls.append(image_dict)


    # Syrtis Major Hemisphere
    browser.back()
    browser.click_link_by_partial_text('Syrtis Major Hemisphere')
    html=browser.html
    soup=bs(html,"html.parser")
    #find the image and make the full url
    rel_image=soup.find('img',class_="wide-image")['src']
    image_url=base_url + rel_image
    #print(image_url)
    image_title=soup.find('h2', class_="title").text
    #print(image_title)
    #save in dictionary and add to image list
    image_dict={"title":image_title, "img_url":image_url}
    hemisphere_image_urls.append(image_dict)

    # Valles Marineris Hemisphere
    browser.back()
    browser.click_link_by_partial_text('Valles Marineris Hemisphere')
    html=browser.html
    soup=bs(html,"html.parser")
    #find the image and make the full url
    rel_image=soup.find('img',class_="wide-image")['src']
    image_url=base_url + rel_image
    #print(image_url)
    image_title=soup.find('h2', class_="title").text
    #print(image_title)
    image_dict={"title":image_title, "img_url":image_url}
    hemisphere_image_urls.append(image_dict)
    #print(hemisphere_image_urls)
    browser.quit()

    mars_dict={"NASA title":news_title,
                "NASA news":news_p,
                "JPL featured url":featured_image_url,
                "Weather":mars_weather,
                "Mars facts":html_table,
                "Hemisphere urls":hemisphere_image_urls}
    return mars_dict
