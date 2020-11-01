import requests
from bs4 import BeautifulSoup

page_to_search = requests.get("https://www.wayup.com/s/internships/it/")
soup = BeautifulSoup(page_to_search.content, 'html.parser')
job_url = []

def find_job_title():
    job_titles = soup.find_all("h3")
    list_of_job_titles = [k.text for k in job_titles]
    return list_of_job_titles

def find_company_name():
    company_name = soup.find_all("h4")
    list_of_company_names = [k.text for k in company_name]
    list_of_company_names.pop(0)
    list_of_company_names.pop(0)
    return list_of_company_names

def find_job_url():
    href_list = []
    html_page = requests.get('https://www.wayup.com/s/internships/it/').text
    soup = BeautifulSoup(html_page, "lxml")
    for link in soup.findAll('a'):
        href_list.append(link.get('href'))
    href_list = href_list[27:]
    return href_list

ultimate_title_list = find_job_title()
ultimate_compname_list = find_company_name()
ultimate_jurl_list = find_job_url()
