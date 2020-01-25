from time import sleep
from selenium import webdriver


driver = webdriver.Chrome(executable_path=r"G:/Shah/Django_Selenium/crawl/chromedriver.exe") # The Path to your webdriver

main_url = "http://127.0.0.1:8000/" # our localhost 
driver.get(main_url)

sleep(5)

search_input = driver.find_element_by_xpath("//input[@name='q']")
search_btn = driver.find_element_by_xpath("//button[@type='submit']")

search_input.send_keys("")
search_btn.click()

all_the_li = driver.find_elements_by_xpath("//li")

full_link = []
rates_list = []

for li in all_the_li:
    inner_text = li.text
    full_link.append(inner_text)
    splitted_text = inner_text.split(",")
    rate = splitted_text[1]
    rates_list.append(int(rate))

rates_list.sort() # ascending

for rate in rates_list:
    for link in full_link:
        splitted_text = link.split(",")
        second_rate = int(splitted_text[1])
        if rate == second_rate:
            print(link)
        
    
sleep(2)
driver.close()
driver.quit()