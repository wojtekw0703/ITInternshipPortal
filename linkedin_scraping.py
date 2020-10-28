import requests
from bs4 import BeautifulSoup

linkedin_url_list = "https://www.linkedin.com/jobs/search/?geoId=92000000&keywords=internship&location=Na%20całym%20świecie"
link_indeed = requests.get(linkedin_url_list)
site = BeautifulSoup(link_indeed.text, 'html.parser')

def find_job_titles():
    jobs_a = site.find_all(name='a', attrs={'data-control-id': 'disabled ember-view job-card-container__link job-card-list__title'})
    scraped_job_titles = []
    for job in jobs_a:
        job_attrs = job.attrs
        scraped_job_titles.append(job_attrs['title'])
    return scraped_job_titles

print(find_job_titles)
