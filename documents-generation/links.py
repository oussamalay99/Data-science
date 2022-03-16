# Importing the necessary libraries
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession

# Intitialize a session that will be used to make requests
s = HTMLSession()

# The URL that contains the results of a google research
URL = "https://www.google.com/search?q=mod%C3%A8les+de+statuts+d%27entreprise"

# This function return the content of a webpage 
def getData(url):
    html = s.get(url).text
    soup= bs(html, "lxml")
    return soup

# This function returns the link of the following page of results if it exists
def getNextPage(soup):
    page = soup.select_one("#pnnext")
    if page:
        return "https://www.google.com" + page["href"]
    return None

# This function select the links displayed in the page of results and store them in file links.txt
def add_links(soup):
    links = soup.select(".yuRUbf > a")
    doc_links = [link["href"] for link in links]
    with open("links.txt", "a") as f:
        for link in doc_links:
            f.write(link + "\n")
        print("Documents have been stored successfully!")

# Now all we need to do is iterate over all the results, add the links to our file and move to the next page till the end
while URL:
    print(f"scraping the URL: {URL} ...")
    soup = getData(URL)
    add_links(soup)
    URL = getNextPage(soup)
print("the websites have been scraped successfully!")