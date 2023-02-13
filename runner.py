from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

servy = Service('./chromedriver')
driver = webdriver.Chrome(service=servy)
path = 'https://learn.zybooks.com/signin'
driver.get(path)

zy_login_email = driver.find_element(By.ID, "ember8")
zy_login_pw = driver.find_element(By.ID, "ember10")
zy_submit_btn = driver.find_element(By.ID, "ember6")

zy_login_email.send_keys("enter ur own username silly")

zy_login_pw.send_keys("enter ur own password silly")

zy_login_pw.send_keys(Keys.ENTER)

zy_341_section_access_btn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "ember21")))
zy_341_section_access_btn.click()


zy_assignment_tab_btn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"ember101\"]/div[2]/button[3]")))
zy_assignment_tab_btn.click()

zy_assignment_1_menu_click = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"ember101\"]/div[1]/div[3]/div/div[1]/h3")))
zy_assignment_1_menu_click.click()

zy_assignment_1_menu_click_assignment_pt_1 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "ember148")))
zy_assignment_1_menu_click_assignment_pt_1.click()



input()
