# MarsMissionScraping
Scrape pages for information on the Mission to Mars and display the data.

It will scrape using Splinter to navigate and BeautifulSoup to gather the following information:

the latest News Title and Paragraph Text from NASA Mars News Site (https://mars.nasa.gov/news/
The JPL Featured Space Image from (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
the latest Mars weather tweet from (https://twitter.com/marswxreport?lang=en)
the table containing facts about the planet including Diameter, Mass, etc. from http://space-facts.com/mars/
high resolution images for each of Mar's hemispheres from https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars


THe data returned will be stored using Mongodb and displayed using Flask template HTML. 

