from selenium.webdriver.common.by import By

def test_Search(setup,loadData):
    driver = setup
    data = loadData

    # Enter Product Name on Search Bar
    driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys(data["pdt"])
    # Click Search Button
    driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()

    msg= driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div[2]/h1/span[2]").text
    assert "5 results have been found." in msg
    assert driver.current_url == "http://automationpractice.com/index.php?controller=search&orderby=position&orderway=desc&search_query=Printed+dress&submit_search="

