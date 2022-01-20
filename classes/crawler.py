from bs4 import BeautifulSoup
from selenium import webdriver
''' -- BeautifulSoup -- '''
url = "https://www.google.com/"
soup = BeautifulSoup(url, 'html.parser')


''' -- Selenium WebDriver -- '''
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path="path/to/chromedriver.exe", chrome_options=options)
driver.get("example.html")
# do something here...
driver.close()