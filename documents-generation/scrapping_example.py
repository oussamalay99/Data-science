from bs4 import BeautifulSoup as bs
import requests
import re


URL = "https://www.coover.fr/modeles/creation-entreprise"
source = URL.split("//")[-1].split("/")[0].split(".")[1]


html = requests.get(URL).text
soup = bs(html, "html.parser")
links = soup.select(".wp-block-latest-posts__list a")
target_links = [link.find(string= re.compile("(S|s)tatut")) for link in links]
target_links= [link.find_parent()["href"] for link in target_links if link]

for i,link in enumerate(target_links):
    link_html = requests.get(link).text
    link_url = bs(link_html, "html.parser").find("div", class_="wp-block-file").find("a")["href"]
    ext= link_url.split(".")[-1]

    with open(f"Docs/{source}_{i+1}.{ext}", "wb") as f:
        content = requests.get(link_url).content
        f.write(content)
        f.close()
print("The website has been scraped succesfully!")