#Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Test_ProductCount:
    def test_valid_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() #ekranı büyütür
        sleep(5)
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("standard_user")
        sleep(5)
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(5)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(5)
        listOfProducts = driver.find_elements(By.CLASS_NAME,"inventory_item")
        testResult = len(listOfProducts) == 6
        print(len(listOfProducts))
        print(f"Test Sonucu: {testResult}")


testClass = Test_ProductCount()
testClass.test_valid_login()



