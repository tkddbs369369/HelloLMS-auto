from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://e-cyber.catholic.ac.kr")


while True:


    try:
        attend_div = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div#attend_div[style*='display:show']"))
        )
        for i in range(100,1001):
            pin_input = attend_div.find_element(By.ID, "pin")
            pin_input.clear()
            pin_input.send_keys(i)


            # 클릭
            attend_btn = attend_div.find_element(By.ID, "attendBtn")
            attend_btn.click()
            print(i,'로 시도')

            try: #번호 불일치시
                alert = WebDriverWait(driver, 1).until(EC.alert_is_present())
                alert_text = alert.text
                print(f"경고 : {alert_text}")
                alert.accept()

            except:
                pass
            pass
    except:
        pass


input()
driver.quit()