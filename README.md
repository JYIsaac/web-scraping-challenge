# web-scraping-challenge
Goal
Use BeautifulSoup, Splinter, and Pandas to scrape  various websites for data related to the Mission to Mars and displays the information in a single HTML page.

Process
Scraping

Scraping was first done in a Jupyter notebook. After importing the Splinter, Beautiful Soup, pandas and ChromeDriver, I connected to chromedriver and set up my browser to open each webpage. I scraped the Mars News Website for the title and most recent article and saved it to variables "news_title" and "news_p", respectively. This was accomplished by  BeautifulSoup to parse through the HTML and search for the appropriate elements and classes that contained the information I needed with soup.find_all(). Because the results come back as a list, I indexed the first item and took the text of that.

