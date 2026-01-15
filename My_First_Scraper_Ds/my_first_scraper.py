import requests
import csv
from bs4 import BeautifulSoup

url = "https://storage.googleapis.com/qwasar-public/track-ds/trending_14_06_2022"

# part 0 
def request_github_trending(url):
    page = requests.get(url)
    return page

# part 1
def extract(page):
    soup = BeautifulSoup(page.text,"html.parser")
    html_repos = soup.find_all("article" , {"class" : "Box-row"})
    return html_repos

# part 2
def transform(html_repos):
    N_html_repos = len(html_repos)
    repositories_data = []
    for i in range(N_html_repos) :
        # NAME !!
        NAME_cmpl = html_repos[i].find("h1").text.strip().split("/")
        NAME = str(NAME_cmpl[0].strip())

        # REPOS_NAME !!
        REPOS_NAME = str(NAME_cmpl[1].strip())

        # NBR_STARS !!
        NBR_STARS = html_repos[i].find("div" , {"class" : "f6 color-fg-muted mt-2"}).find("a").text.strip().split()
        NBR_STARS = int(NBR_STARS[0].replace(",",""))

        repositories_data.append({"developer": NAME, "repository_name": REPOS_NAME, "nbr_stars": NBR_STARS})

    return repositories_data

# part 3
def format(repositories_data):
    if not repositories_data or len(repositories_data) == 0:
        return ""

    keys = list(repositories_data[0].keys())
    
    for repo in repositories_data:
        values = [str(repo[key]) for key in keys]
        csv_text += ",".join(values) + "\n"
    return csv_text

#print(format(transform(extract(request_github_trending(url)))))