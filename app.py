from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

start_time = time.time()

driver=webdriver.Chrome()
from selenium.webdriver.chrome.options import Options


driver.get('https://egazette.gov.in/(S(1yyjmaezdld2rzwxfjg2qfs2))/Default.aspx#')
main=driver.current_window_handle
def scrape(listu):
    driver.find_element(By.ID, 'lnk_Extra_All').click()
    wait=WebDriverWait(driver,10)
    element = wait.until(EC.presence_of_element_located((By.ID, "tbl_Gazette")))   
    target_rows=[]
    target_rows.append(element.find_element(By.XPATH, ".//tr[td[9]/span[text()='{str}']]".format(str=listu[0])))
    print(target_rows)
    for i in range(len(target_rows)):
        print(i)
        time.sleep(5)
        try:
            target_rows[i].find_element(By.XPATH, "//input[@type='image' and @src='images/pdf_icon.png']").click()
        except:
            print('stfu')
            return 'stfu'
        print('clicked')
        wait.until(EC.new_window_is_opened([main]))
        window=driver.window_handles
        driver.switch_to.window(window[1])
        print(driver.current_url)
        print('****************')
        print('closing')
        driver.close()
        print("tab closed")
        driver.switch_to.window(main)
        

        
        
scrape(['CG-AS-E-22102024-258127'])
driver.quit()
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

print(elapsed_time)    
    
    
