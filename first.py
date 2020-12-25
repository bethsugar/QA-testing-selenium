from selenium import webdriver
import time



driver = webdriver.Chrome(executable_path=r"C:\driver dech\chromedriver.exe")

driver.get('https://www.facebook.com/')
time.sleep(5)

email_field = driver.find_element_by_id("email")
email_field.send_keys("demoguy@gmail.com")

pss_field = driver.find_element_by_id("pass")
pss_field.send_keys("miabuela en patineta")
time.sleep(3)

loggin_button = driver.find_element_by_xpath('//*[@id="u_0_b"]')
loggin_button.click()

body = driver.find_element_by_tag_name('body')
all_text = body.text

if "Recuperar cuenta" not in all_text:
    raise BaseException("The 'Recuperar cuenta' text is not found.")
else: 
    print("Test Pass")

time.sleep(10)

driver.quit()