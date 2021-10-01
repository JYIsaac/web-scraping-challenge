from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import time


def scrape():
#Set up splinger
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # Open browser to Mars News Site
    browser.visit('https://redplanetscience.com/')

    time.sleep(1)

    #Parse through html
    html = browser.html
    soup = bs(html, 'html.parser')

    # Search for news titles
    title_results = soup.find_all('div', class_='content_title')

    # Search for paragraph text under news titles
    p_results = soup.find_all('div', class_='article_teaser_body')

    # Extract first title and paragraph, and assign to variables
    news_title = title_results[0].text
    news_p = p_results[0].text

    print(news_title)
    print(news_p)

    # Open browser to JPL Featured Image
    browser.visit('https://spaceimages-mars.com/')

    time.sleep(1)

    html = browser.html
    soup = bs(html, 'html.parser')

    # Search for image source
    results = soup.find_all('img', class_='headerimage')
    relative_img_path = results[0]['src']
    featured_img_url = 'https://www.jpl.nasa.gov' + str(relative_img_path)

    print(featured_img_url)

    # Open browser to Astrogeology site
    browser.visit('https://galaxyfacts-mars.com/')

    time.sleep(1)

    html = browser.html
    soup = bs(html, 'html.parser')


    # Use Pandas to scrape data
    tables = pd.read_html('https://galaxyfacts-mars.com/')

    # Take second table for Mars facts
    df = tables[1]

    # Rename columns and set index
    df.columns=['description', 'value']
    df

    # Convert table to html
    mars_facts_table = [df.to_html(classes='data table table-borderless', index=False, header=False, border=0)]
    mars_facts_table

    # Open browswer to site
    browser.visit('https://marshemispheres.com/')

    time.sleep(1)

    #Search for hemispehere titles
    html = browser.html
    soup = bs(html, 'html.parser')

    titles = []

    # Search for the names of all 4 hemispeheres
    results = soup.find_all('div', class_="collapsible results")
    hemispheres = results[0].find_all('h3')

    #For loop through the results and get text and put into empty list
    for name in hemispheres:
        titles.append(name.text)

    titles

    # Search for thumbnail links
    thumbnail_results = results[0].find_all('a')
    thumbnail_links = []

    for thumbnail in thumbnail_results:
                
    # If the thumbnail element has an image...
        if (thumbnail.img):
                    
            # then grab the attached link
            thumbnail_url = 'https://marshemispheres.com/' + thumbnail['href']
                    
            # Append list with links
            thumbnail_links.append(thumbnail_url)

    img_url = []

    for url in thumbnail_links:
                
        # Click through each thumbanil link
        browser.visit(url)
            
        html = browser.html
        soup = bs(html, 'html.parser')
            
        # Scrape each page for the relative image path
        results = soup.find_all('img', class_='wide-image')
        relative_img_path = results[0]['src']
            
        # Combine the reltaive image path to get the full url
        img_link = 'https://marshemispheres.com/' + relative_img_path
            
        # Add full image links to a list
        img_url.append(img_link)

        

    # Zip together the list of hemisphere names and hemisphere image links
    mars_hemisphere_zip = zip(titles, img_url)

    hemisphere_image_urls = []

    # Iterate through the zipped object
    for title, img in mars_hemisphere_zip:
            
        mars_hemisphere_dict = {}
            
        # Add hemisphere title to dictionary
        mars_hemisphere_dict['title'] = title
            
        # Add image url to dictionary
        mars_hemisphere_dict['img_url'] = img
            
        # Append the list with dictionaries
        hemisphere_image_urls.append(mars_hemisphere_dict)

        # print(img)

            
    #Store data in dictionary
    mars_data = {
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image": featured_img_url,
        "mars_facts": mars_facts_table,
        "hemispheres": hemisphere_image_urls
            }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data




      