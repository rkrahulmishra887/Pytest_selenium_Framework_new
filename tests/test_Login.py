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
    msg= driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div/p").text
    assert "Welcome to your account. Here you can manage all of your personal information and orders." in msg
    assert driver.current_url == "http://automationpractice.com/index.php?controller=my-account"

@pytest.mark.run(order=2)
def test_invalidLogin(setup):
    driver = setup
    #data = loadData
    driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a").click()
    driver.find_element(By.ID, "email").send_keys("rkm1@1")
    driver.find_element(By.ID, "passwd").send_keys("Rahul@1")
    driver.find_element(By.ID, "SubmitLogin").click()
    msg = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div[1]/p").text
    assert "There is 1 error" in msg
    assert driver.current_url == "http://automationpractice.com/index.php?controller=authentication"