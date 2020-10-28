import requests
from bs4 import BeautifulSoup

indeed_url_list = "https://pl.indeed.com/praca?as_and=staż+it&as_phr=&as_any=&as_not=&as_" \
                  "ttl=&as_cmp=&jt=all&st=&salary=&radius=25&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch"
link_indeed = requests.get(indeed_url_list)
site = BeautifulSoup(link_indeed.text, 'html.parser')

def find_job_titles():
    jobs_a = site.find_all(name='a', attrs={'data-tn-element': 'jobTitle'})
    scraped_job_titles = []
    for job in jobs_a:
        job_attrs = job.attrs
        scraped_job_titles.append(job_attrs['title'])
    return scraped_job_titles

def find_company_name():
    scraped_company_names = []
    company_span = site.find_all('span', attrs={'class': 'company'})
    for span in company_span:
        scraped_company_names.append(span.text.strip())
    return scraped_company_names

def find_job_location():
    scraped_job_locations = []
    loc_div = site.find_all('div', attrs={'class': 'recJobLoc'})
    for loc in loc_div:
        loc_attrs = loc.attrs
        scraped_job_locations.append(loc_attrs['data-rc-loc'])
    return scraped_job_locations

def find_job_url(soup):
    job_urls = []
    for link in soup.find_all('h2', {'class': 'title'}):
        partial_url = link.a.get('href')
        complete_url = 'https://pl.indeed.com/praca' + partial_url
        job_urls.append(complete_url)
    return job_urls

def find_job_id(soup):
    job_id_list = []
    for job in soup.find_all('h2', {'class': 'title'}):
        job_id = job.a.get('id')
        job_id_list.append(job_id)
    return job_id_list

list_of_titles = find_job_titles()
list_of_company = find_company_name()
list_of_locations = find_job_location()
list_of_urls = find_job_url(site)
list_of_id = find_job_id(site)
import requests
from bs4 import BeautifulSoup

indeed_url_list = "https://pl.indeed.com/praca?as_and=staż+it&as_phr=&as_any=&as_not=&as_" \
                  "ttl=&as_cmp=&jt=all&st=&salary=&radius=25&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch"
link_indeed = requests.get(indeed_url_list)
site = BeautifulSoup(link_indeed.text, 'html.parser')

def find_job_titles():
    jobs_a = site.find_all(name='a', attrs={'data-tn-element': 'jobTitle'})
    scraped_job_titles = []
    for job in jobs_a:
        job_attrs = job.attrs
        scraped_job_titles.append(job_attrs['title'])
    return scraped_job_titles

def find_company_name():
    scraped_company_names = []
    company_span = site.find_all('span', attrs={'class': 'company'})
    for span in company_span:
        scraped_company_names.append(span.text.strip())
    return scraped_company_names

def find_job_location():
    scraped_job_locations = []
    loc_div = site.find_all('div', attrs={'class': 'recJobLoc'})
    for loc in loc_div:
        loc_attrs = loc.attrs
        scraped_job_locations.append(loc_attrs['data-rc-loc'])
    return scraped_job_locations

def find_job_url(soup):
    job_urls = []
    for link in soup.find_all('h2', {'class': 'title'}):
        partial_url = link.a.get('href')
        complete_url = 'https://pl.indeed.com/praca' + partial_url
        job_urls.append(complete_url)
    return job_urls

def find_job_id(soup):
    job_id_list = []
    for job in soup.find_all('h2', {'class': 'title'}):
        job_id = job.a.get('id')
        job_id_list.append(job_id)
    return job_id_list

list_of_titles = find_job_titles()
list_of_company = find_company_name()
list_of_locations = find_job_location()
list_of_urls = find_job_url(site)
list_of_id = find_job_id(site)
import requests
from bs4 import BeautifulSoup

indeed_url_list = "https://pl.indeed.com/praca?as_and=staż+it&as_phr=&as_any=&as_not=&as_" \
                  "ttl=&as_cmp=&jt=all&st=&salary=&radius=25&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch"
link_indeed = requests.get(indeed_url_list)
site = BeautifulSoup(link_indeed.text, 'html.parser')

def find_job_titles():
    jobs_a = site.find_all(name='a', attrs={'data-tn-element': 'jobTitle'})
    scraped_job_titles = []
    for job in jobs_a:
        job_attrs = job.attrs
        scraped_job_titles.append(job_attrs['title'])
    return scraped_job_titles

def find_company_name():
    scraped_company_names = []
    company_span = site.find_all('span', attrs={'class': 'company'})
    for span in company_span:
        scraped_company_names.append(span.text.strip())
    return scraped_company_names

def find_job_location():
    scraped_job_locations = []
    loc_div = site.find_all('div', attrs={'class': 'recJobLoc'})
    for loc in loc_div:
        loc_attrs = loc.attrs
        scraped_job_locations.append(loc_attrs['data-rc-loc'])
    return scraped_job_locations

def find_job_url(soup):
    job_urls = []
    for link in soup.find_all('h2', {'class': 'title'}):
        partial_url = link.a.get('href')
        complete_url = 'https://pl.indeed.com/praca' + partial_url
        job_urls.append(complete_url)
    return job_urls

def find_job_id(soup):
    job_id_list = []
    for job in soup.find_all('h2', {'class': 'title'}):
        job_id = job.a.get('id')
        job_id_list.append(job_id)
    return job_id_list

list_of_titles = find_job_titles()
list_of_company = find_company_name()
list_of_locations = find_job_location()
list_of_urls = find_job_url(site)
list_of_id = find_job_id(site)
import requests
from bs4 import BeautifulSoup

indeed_url_list = "https://pl.indeed.com/praca?as_and=staż+it&as_phr=&as_any=&as_not=&as_" \
                  "ttl=&as_cmp=&jt=all&st=&salary=&radius=25&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch"
link_indeed = requests.get(indeed_url_list)
site = BeautifulSoup(link_indeed.text, 'html.parser')

def find_job_titles():
    jobs_a = site.find_all(name='a', attrs={'data-tn-element': 'jobTitle'})
    scraped_job_titles = []
    for job in jobs_a:
        job_attrs = job.attrs
        scraped_job_titles.append(job_attrs['title'])
    return scraped_job_titles

def find_company_name():
    scraped_company_names = []
    company_span = site.find_all('span', attrs={'class': 'company'})
    for span in company_span:
        scraped_company_names.append(span.text.strip())
    return scraped_company_names

def find_job_location():
    scraped_job_locations = []
    loc_div = site.find_all('div', attrs={'class': 'recJobLoc'})
    for loc in loc_div:
        loc_attrs = loc.attrs
        scraped_job_locations.append(loc_attrs['data-rc-loc'])
    return scraped_job_locations

def find_job_url(soup):
    job_urls = []
    for link in soup.find_all('h2', {'class': 'title'}):
        partial_url = link.a.get('href')
        complete_url = 'https://pl.indeed.com/praca' + partial_url
        job_urls.append(complete_url)
    return job_urls

def find_job_id(soup):
    job_id_list = []
    for job in soup.find_all('h2', {'class': 'title'}):
        job_id = job.a.get('id')
        job_id_list.append(job_id)
    return job_id_list

list_of_titles = find_job_titles()
list_of_company = find_company_name()
list_of_locations = find_job_location()
list_of_urls = find_job_url(site)
list_of_id = find_job_id(site)
