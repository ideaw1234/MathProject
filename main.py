import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
titles = []
numbers = []
for page_num in range(1, 7):
    url = f"https://news.sanook.com/lotto/archive/page/{page_num}/"
    driver.get(url)
    driver.implicitly_wait(10)
    articles = driver.find_elements(By.XPATH, "/html/body/div[4]/div/div[1]/div/div/div/article")
    for article in articles:
        title_element = article.find_element(By.XPATH,".//div/a/div/h3")
        number_element = article.find_element(By.XPATH,".//div/a/div/ul/li[4]/strong")
        title_text = title_element.text
        number_text = number_element.text
        titles.append(title_text)
        numbers.append(number_text)

driver.quit()
data = {
    "Title": titles,
    "Number": numbers
}
df = pd.DataFrame(data)

csv_file_path = "articles_data.csv"
df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')

print(f"Data has been written to {csv_file_path}")
