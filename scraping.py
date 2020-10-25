import requests
from bs4 import BeautifulSoup

url = "https://pl.indeed.com/praca?as_and=staż+it&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch"
link = requests.get(url)
site = BeautifulSoup(link.text, 'html.parser')
jobs_a = site.find_all(name='a', attrs={'data-tn-element': 'jobTitle'})
scraped_job_titles = []
for job in jobs_a:
    job_attrs = job.attrs
    scraped_job_titles.append(job_attrs['title'])
print(scraped_job_titles)

scraped_company_names = []

company_span = site.find_all('span', attrs={'class': 'company'})

for span in company_span:
    scraped_company_names.append(span.text.strip())
print(scraped_company_names)

scraped_job_locations = []
loc_div = site.find_all('div', attrs={'class': 'recJobLoc'})

for loc in loc_div:
    loc_attrs = loc.attrs
    scraped_job_locations.append(loc_attrs['data-rc-loc'])
print(scraped_job_locations)
