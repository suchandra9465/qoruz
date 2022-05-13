# import requests
# from bs4 import BeautifulSoup

# url = "https://twitter.com/kfc"

# pageContent = requests.get(url)

# # htmlContent = pageContent.content

# soup = BeautifulSoup(pageContent.content, 'html.parser')


# # print(soup.prettify())

# # title = soup.title
# follow_box = soup.find('div',{'class':'css-1dbjc4n'})
# print(follow_box)

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

driver = webdriver.Firefox(executable_path='./geckodriver', options=options)
driver.implicitly_wait(10)

driver.get('https://twitter.com/kfc')

twt_follwing = driver.find_element_by_css_selector('a[href="/kfc/following"] > span > span').text
twt_follwers = driver.find_element_by_css_selector('a[href="/kfc/followers"] > span > span').text

print(twt_follwers,twt_follwing)