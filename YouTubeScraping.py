from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import xlwt, csv, time


def ScrapeComments(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    
    body = driver.find_element(By.TAG_NAME, 'body')
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    while True:
        body.send_keys(Keys.END)
        time.sleep(2)  # Wait for the comments to load
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    
    driver.quit()
    title_div = soup.select_one(
        "#container h1")
    title = title_div.text.strip()
    comments = soup.select("#contents #content #content-text")
    commnt_list = [x.text.strip() for x in comments]
    authors = soup.select("#contents #comment #header #author-text")
    author_thumbnails = soup.select("yt-img-shadow img")
    
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('Sheet1')
    
    for index, comment in enumerate(commnt_list):
            content = [index+1,authors[index].text.strip(), comment]
            sheet.write(content)
    
    # with open('posts/output.xls', 'w', encoding='utf-8', newline='') as file:
    #     file.write(
    #         f"--------------------------------{title}--------------------------------\n\n")
    #     write = csv.writer(file)
    #     headers = ['S.N', 'Username', 'Comments']
    #     write.writerow(headers)
        
    workbook.save('output.xls')
    print(title)


if __name__ == '__main__':
    urls = [
        'https://www.youtube.com/watch?v=TATSAHJKRd8'
    ]
    ScrapeComments(urls[0])
