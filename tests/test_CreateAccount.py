from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_createAccount(setup,loadData):
    driver = setup
    data = loadData

    # click on Sign in
    driver.find_element(By.LINK_TEXT,"Sign in").click()

    # Enter email address
    driver.find_element(By.CSS_SELECTOR,"[name='email_create']").send_keys(data["email1"])

    # Click on "Create an account"
    driver.find_element(By.XPATH,"//button[@name=\"SubmitCreate\"]").click()

'''
    # Select Title
    driver.find_element(By.XPATH,"//input[@id=\"id_gender1\"]").click()
    driver.find_element(By.NAME,"customer_firstname").send_keys(data["firstName"])
    driver.find_element(By.NAME,"customer_lastname").send_keys(data["lastName"])
    driver.find_element(By.ID,"passwd").send_keys(data["pswd"])

    # Enter your address
    driver.find_element(By.ID,"firstname").send_keys(data["firstName"])
    driver.find_element(By.ID,"lastname").send_keys(data["lastName"])
    driver.find_element(By.ID,"company").send_keys(data["comp"])
    driver.find_element(By.ID,"address1").send_keys(data["add1"])
    driver.find_element(By.ID,"city").send_keys(data["city"])

    # Select State
    Select(driver.find_element(By.NAME,"id_state")).select_by_value("4")

    driver.find_element(By.NAME,"postcode").send_keys(data["postcode"])

    # Select Country
    Select(driver.find_element(By.NAME,"id_country")).select_by_visible_text("United States")

    # Enter Mobile Number
    driver.find_element(By.ID,"phone mobile").send_keys(data["num"])
    driver.find_element(By.XPATH,"//input[@name=\"alias\"]").clear()
    driver.find_element(By.XPATH,"//input[@name=\"alias\"]").send_keys("Home")

    # click Register Button
    driver.find_element(By.NAME,"submitAccount").click()

'''



