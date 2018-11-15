# MarsMissionScraping
Scrape pages for information on the Mission to Mars and display the data.

It will scrape using Splinter to navigate and BeautifulSoup to gather the following information:

    The latest News Title and Paragraph Text from NASA Mars News Site (https://mars.nasa.gov/news/

    The JPL Featured Space Image from (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)

    The latest Mars weather tweet from (https://twitter.com/marswxreport?lang=en)

    The table containing facts about the planet including Diameter, Mass, etc. from http://space-facts.com/mars/

    High resolution images for each of Mar's hemispheres from https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars


The data returned will be stored using Mongodb and displayed using Flask template HTML. 

Errors are handles with a short message being printed in place of any missing items. If errors occur on more than 3 of the 5 sites used the scrape will not save or display the data, but will redisplay the previous data. If 3 or less errors occur then previous data is disguarded when the new data is saved.

