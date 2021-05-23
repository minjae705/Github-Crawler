import requests
from bs4 import BeautifulSoup

def user_repos_parser(url):
    URL = "https://github.com"+url
    print(URL)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    watchers = repo_watchers(soup,url)
    stargazers = repo_stargazers(soup,url)
    forks = repo_forks(soup,url)
    user_repos_results={
#        "watchers": watchers,
        "stargazers":stargazers,
        "forks" :forks
    }
    return user_repos_results


def repo_watchers(soup,url):
    watchers_text  = url+"/watchers"
    watchers = soup.find('a', href=watchers_text)
    if watchers == None:
        watchers = 0
    else:
        watchers = int(watchers.text)
    return watchers

def repo_stargazers(soup,url):
    stargazers_text  = url+"/stargazers"
    stargazers = soup.find('a', href=stargazers_text)
    stargazers = stargazers.text
    stargazers = stargazers.replace('\n','')    
    stargazers = stargazers.replace(' ','')
    return stargazers

def repo_forks(soup,url):
    forks_text  = url+"/network/members"
    forks = soup.find('a', href=forks_text)
    forks = forks.text
    forks = forks.replace('\n','')
    forks = forks.replace(' ','')
    return forks

def repo_info(url):
    user_repos_results = user_repos_parser(url)
    return user_repos_results

myrepos = []

for i in myrepos:
    print(i, repo_info(i))
