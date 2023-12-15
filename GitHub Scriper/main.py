from selenium import webdriver

cdp = r"C:\chromedriver-win64.exe"
driver = webdriver.Chrome(executable_path=cdp)
driver.get("https://google.com")
driver.close()
