import pytest
from util import config
from selenium import webdriver

driver = None

@pytest.fixture()
def setup():
    global driver
    driver = webdriver.Chrome(config.chrome_path)
    driver.maximize_window()
    driver.get(config.base_url)
    return driver

@pytest.fixture()
def loadData():
    return {"email":"rkm123@pat.com","firstName":"Rahul","lastName":"Mishra","pswd":"Rahul@123",
            "email1":"rkm12@nag.com","comp":"Nagarro","add1":"Kadamkuan","city":"patna",
            "postcode":"70000","num":"9768754328","num2":"9876543210","num3":"8293765432",
            "pdt":"Printed dress"}

@pytest.fixture()
def teardown():
    yield
    driver.quit()