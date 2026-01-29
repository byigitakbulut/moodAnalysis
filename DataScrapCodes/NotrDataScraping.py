from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Safari()
urls = ['https://www.imdb.com/title/tt8041270/reviews/?ref_=tt_ov_ql_2',
        'https://www.imdb.com/title/tt10838180/reviews/?ref_=tt_ov_ql_2',
        'https://www.imdb.com/title/tt5108870/reviews/?ref_=tt_ov_ql_2']
notrReviews = []

for url in urls:
    driver.get(url)
    driver.maximize_window()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'ipc-see-more__text')))
    showAll = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/section/div/section/div/div[1]/section[1]/div[3]/div/span[2]/button')
    driver.execute_script('arguments[0].scrollIntoView();', showAll)
    time.sleep(3)
    showAll.click()
    time.sleep(3)
    for count in range(4):
        driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')
        time.sleep(5)
    for review in driver.find_elements(By.CLASS_NAME, 'ipc-html-content-inner-div'):
        notrReviews.append(review.text)
    time.sleep(3)

driver.quit()

df = pd.DataFrame({'Reviews': notrReviews, 'Mood': 'Notr'})
df.to_csv('/Users/yitik/Desktop/Dersler/For Python/moodAnalysis/Datasets/NotrDataset.csv')
