from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver=webdriver.Chrome()
driver.get('https://egazette.gov.in/(S(1yyjmaezdld2rzwxfjg2qfs2))/Default.aspx#')
main=driver.current_window_handle
def scrape():
    driver.find_element(By.ID, 'lnk_Extra_All').click()
    wait=WebDriverWait(driver,3)
    element = wait.until(EC.presence_of_element_located((By.ID, "tbl_Gazette")))   
    pdf=element.find_elements(By.XPATH, "//input[@type='image' and @src='images/pdf_icon.png']")
    pdf[0].click()
    print('clicked')
    wait.until(EC.new_window_is_opened([main]))
    window=driver.window_handles
    driver.switch_to.window(window[1])
    print('closing')
    sleep(5)
    driver.close()
    print("tab closed")
    sleep(5)    
scrape()
driver.quit()
    
    
    
