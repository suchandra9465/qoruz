import requests
from bs4 import BeautifulSoup

url = "https://twitter.com/kfc"

pageContent = requests.get(url)

# htmlContent = pageContent.content

soup = BeautifulSoup(pageContent.content, 'html.parser')

# print(soup.prettify())

# title = soup.title
follow_box = soup.find('div',{'class':'css-1dbjc4n r-1mf7evn'})
print(follow_box)
# followers = follow_box.find('a').find('span',{'class':'ProfileNav-value'})
# print("Number of followers: {} ".format(followers.get('data-count')))