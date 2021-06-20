import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver


user_id = input("github user id")
url = "https://github.com/"+user_id
r = requests.get(url)
soup = bs(r.content, "html.parser")
profile_pic = soup.find("img", {"alt" : "Avatar"})['src']
print(profile_pic)
driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get(profile_pic)