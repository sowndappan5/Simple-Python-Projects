import requests 
import xml.etree.ElementTree as ET 

# URL of the news RSS feed (updated URL)
RSS_FEED_URL = "http://www.example.com/rss/news.xml"  # Change this to the new RSS feed URL

def fetchRSS(): 
    ''' 
    Utility function to fetch the RSS feed 
    '''
    # Create an HTTP request response object 
    response = requests.get(RSS_FEED_URL) 

    # Return the content of the response 
    return response.content 

def parseRSSFeed(rss): 
    ''' 
    Utility function to parse the XML format of the RSS feed 
    '''
    # Create an ElementTree root object 
    root = ET.fromstring(rss) 

    # Initialize an empty list for news items 
    news_items = [] 

    # Iterate through news items 
    for item in root.findall('./channel/item'): 
        news = {} 

        # Iterate through child elements of each item 
        for child in item: 

            # Special handling for namespace object content:media 
            if child.tag == '{http://search.yahoo.com/mrss/}content': 
                news['media'] = child.attrib['url'] 
            else: 
                news[child.tag] = child.text.encode('utf8') 
        news_items.append(news) 

    # Return the list of news items 
    return news_items 

def getTopStories(): 
    ''' 
    Main function to generate and return news items 
    '''
    # Load the RSS feed 
    rss = fetchRSS() 

    # Parse the XML 
    news_items = parseRSSFeed(rss) 
    return news_items 