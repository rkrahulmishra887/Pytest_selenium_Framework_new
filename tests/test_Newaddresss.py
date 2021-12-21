from selenium.webdriver import Keys
from keyboard import press
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.run(order=1)
def test_validLogin(setup,loadData):
    driver = setup
    data = loadData
    driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a").click()
    driver.find_element(By.ID,"email").send_keys(data["email"])
    driver.find_element(By.ID,"passwd").send_keys(data["pswd"])
    driver.find_element(By.ID,"SubmitLogin").click()

    driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div/div/div[1]/ul/li[3]/a/span").click()
    driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div/div[2]/a").click()
    driver.find_element(By.ID, "address1").send_keys("California")
    driver.find_element(By.ID, "city").send_keys("New York")
    driver.find_element(By.ID, "id_state").click()
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/form/div[7]/div/select/option[6]").click()
    driver.find_element(By.ID, "postcode").send_keys("11000")
    driver.find_element(By.ID, "phone").send_keys(data["num2"])
    driver.find_element(By.ID, "phone_mobile").send_keys(data["num3"])
    driver.find_element(By.ID, "alias").clear()
    driver.find_element(By.ID, "alias").send_keys("Office")
    driver.find_element(By.ID, "submitAddress").click()

@pytest.mark.run(order=2)
def test_deleteAddress(setup,loadData):
    driver = setup
    data = loadData
    driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a").click()
    driver.find_element(By.ID, "email").send_keys(data["email"])
    driver.find_element(By.ID, "passwd").send_keys(data["pswd"])
    driver.find_element(By.ID, "SubmitLogin").click()

    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/div[1]/ul/li[3]/a/span").click()
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div[1]/div/div[2]/ul/li[9]/a[2]").click()
    press('enter')



