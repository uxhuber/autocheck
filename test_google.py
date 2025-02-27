from selenium import webdriver

def test_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys("Hello World")
    search_box.submit()
    assert "Hello World" in driver.title
    driver.quit()
    print("Test passed!")