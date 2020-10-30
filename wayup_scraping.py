import requests
from bs4 import BeautifulSoup

page_to_search = requests.get("https://www.wayup.com/s/internships/it/")
soup = BeautifulSoup(page_to_search.content, 'html.parser')
job_titles = soup.find_all("h3")

list_of_job_titles = [k.text for k in job_titles]
print(list_of_job_titles)



html_page = requests.get('https://www.wayup.com/s/internships/it/').text
soup = BeautifulSoup(html_page, "lxml")
for link in soup.findAll('a'):
    print(link.get('href'))
