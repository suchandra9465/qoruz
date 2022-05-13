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

bio = driver.driver.find_elements_by_xpath('//div[@data-testid="UserDescription"] > span').text
twt_follwing = driver.find_element_by_css_selector('a[href="/kfc/following"] > span > span').text
twt_follwers = driver.find_element_by_css_selector('a[href="/kfc/followers"] > span > span').text
name = driver.find_elements_by_xpath('//div[@data-testid="UserName"] > div > div > div > div > div >  span > span').text
location = driver.find_elements_by_xpath('//div[@data-testid="UserProfileHeader_Items"] > span > svg > span > span').text
url = page_cards = driver.find_elements_by_xpath('//a[@data-testid="UserUrl"] > svg > span').text
joined_date = driver.find_elements_by_xpath('//a[@data-testid="UserDate"] > svg > span').text
print(twt_follwers,twt_follwing)