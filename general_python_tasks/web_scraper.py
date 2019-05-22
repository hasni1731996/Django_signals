from selenium import webdriver
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome('C:/Users/Muhammad Hassan/Desktop/ChoiceGenie/ChoiceGe/chromedriver.exe')
driver.get("https://news.ycombinator.com/jobs")
def page_scrape(): #"https://news.ycombinator.com/jobs"
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    t_row = soup.findAll("tr", attrs={'class': 'athing'})
    for tr in t_row:
        #print ('ad id..',tr.get('id')) ## Get associated Id with each tr to check its already exists or not
        a_link=tr.find_next("td",attrs={'class' : 'title'})
        comp_link=a_link.find_next("a")
        #print('Location..',comp_link.attrs['href'])  ####Company Location
        comp = comp_link.text
        name_comp = comp.split()
        #print(name_comp[0]) #####Company Name
    if driver.find_element_by_xpath('//*[@id="hnmain"]/tbody/tr[3]/td/table/tbody/tr[95]/td[2]/a').click():
        time.sleep(5)
        driver.get(driver.current_url)
        page_scrape()
page_scrape()
driver.quit()