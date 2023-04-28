
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.remote.errorhandler import StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://twitter.com/login")


subject = "(food OR  plant  OR walk OR watch OR funny OR lovely OR good  ) lang:en  until:2023-04-17"


# Setup the log in
sleep(3)
username = driver.find_element(By.XPATH,"//input[@name='text']")
username.send_keys("EMAil")

next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
next_button.click()

sleep(3)
username = driver.find_element(By.XPATH,"//input[@name='text']")
username.send_keys("PHONE-NUMBER")
next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
next_button.click()
sleep(3)

password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys('PASSWORD')
sleep(3)

log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
log_in.click()

# Search item and fetch it
sleep(5)
search_box = driver.find_element(By.XPATH,"//input[@data-testid='SearchBox_Search_Input']")
search_box.send_keys(subject)
search_box.send_keys(Keys.ENTER)
sleep(3)
driver.find_element_by_link_text('Latest').click()
result = []
twit = driver.find_elements_by_xpath("//div[@data-testid='tweetText']")
sleep(2)
print("------------------------------\n" + str(len(twit)) + "adet twit başarıyla çekildi \n------------------------------")
for i in twit:
    while True :
        try:
            result.append(i.text)
            break
        except StaleElementReferenceException:
            sleep(1)
            continue

counter = 0
son = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    if counter > 10 :
        break
    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
    sleep(2)
    yeni = driver.execute_script("return document.documentElement.scrollHeight")
    if son == yeni :
        break
    son = yeni
    counter += 1
    twit = driver.find_elements_by_xpath("//div[@data-testid='tweetText']")
    sleep(2)
    print("------------------------------\n" + str(len(twit)) + "tweet was successfully scraped \n------------------------------")
    for i in twit:
         while True :
             
             
             try:
                 result.append(i.text)
                 break
             except StaleElementReferenceException:
                  sleep(1)
                  continue

adet = 1
with open("tweets.csv","w",encoding="UTF-8") as file :
    for a in result :
        file.write(f"{adet} - {a}\n")
        adet += 1
print("The tweets have been successfully saved in the tweets.txt file")")
