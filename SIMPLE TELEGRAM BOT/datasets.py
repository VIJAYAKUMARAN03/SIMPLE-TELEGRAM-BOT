

import requests
from bs4 import BeautifulSoup

def awesome_data(data):
  name_selec = []
  link_selec = []

  link = 'https://github.com/awesomedata/awesome-public-datasets'
  req = requests.get(link)
  soup = BeautifulSoup(req.content, 'html.parser')
  html = soup.find_all('a', rel="nofollow")
  for i in range(len(html))[8:]:
    name = (str(html[i]).strip('</a>').split('w">')[0]).lower()
    link = str(html[i]).split('f="')[1].split('" r')[0]
    if (data in name):
      name_selec.append(name)
      link_selec.append(link)
    else:
      name_selec += ''
      link_selec += ''
  lnks=""
  if len(name_selec) > 0:    
    for j in range(len(name_selec)):
      lnks=lnks+(f'\n{link_selec[j]}\n')
  return(lnks)


def data_google(data):
  dataset = data
  dataset_clean = dataset.replace(' ', '+').lower()
  link = f'https://datasetsearch.research.google.com/search?query={dataset_clean}'

  finallink = (f'\n{link}\n')
  return finallink
    
def search_data(dataset):
  link1=awesome_data(dataset)
  link2=data_google(dataset)
  link="Link to access the "+ dataset +" and its related Datasets:\n"+ link1  + link2
  return(link)
#print(search_data('cities'))