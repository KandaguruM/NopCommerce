import time

from selenium.webdriver.common.by import By

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select


class test_Registerpage(object):

    def __init__(self, driver):
        self.driver = driver




    Click_registertab_xpath = "(//a[normalize-space()='Register'])[1]"
    gender_male_id = "gender-male"
    Input_firstname_id = "FirstName"
    Input_lastname_id = "LastName"
    dropdown_date_xpath = "(//select[@name='DateOfBirthDay'])[1]"
    dropdown_month_xpath = "(//select[@name='DateOfBirthMonth'])[1]"
    dropdown_year_xpath = "(//select[@name='DateOfBirthYear'])[1]"
    input_email_id = "Email"
    input_company_id = "Company"
    checkbox_newsletter_id = "Newsletter"
    input_password_id = "Password"
    input_confirmpassword_id = "ConfirmPassword"
    button_register_id = "register-button"
    static_register_text_xpath = "(//div[@class='page-body'])[1]//div[@class='result']"


    def test_selectgender(self):
        self.driver.find_element(By.ID, self.gender_male_id).click()

    def test_Enterfirstname(self, firstname):
        self.driver.find_element(By.ID, self.Input_firstname_id).clear()
        self.driver.find_element(By.ID, self.Input_firstname_id).send_keys(firstname)

    def test_Enterlastname(self, lastname):
        self.driver.find_element(By.ID, self.Input_lastname_id).clear()
        self.driver.find_element(By.ID, self.Input_lastname_id).send_keys(lastname)

    def test_dateofbirth(self, date1, month, year):
        date = Select(self.driver.find_element(By.XPATH, self.dropdown_date_xpath))
        date.select_by_visible_text(date1)
        mon = Select(self.driver.find_element(By.XPATH, self.dropdown_month_xpath))
        mon.select_by_visible_text(month)
        yea = Select(self.driver.find_element(By.XPATH, self.dropdown_year_xpath))
        yea.select_by_visible_text(year)

    def test_email(self, email):
        self.driver.find_element(By.ID, self.input_email_id).clear()
        mail = self.driver.find_element(By.ID, self.input_email_id).send_keys(email)

    def test_company(self, companyname1):
        self.driver.find_element(By.ID, self.input_company_id).clear()
        self.driver.find_element(By.ID, self.input_company_id).send_keys(companyname1)

    def test_newsletter(self):
        self.driver.find_element(By.ID, self.checkbox_newsletter_id)

    def test_password(self, password):
        self.driver.find_element(By.ID, self.input_password_id).clear()
        self.driver.find_element(By.ID, self.input_password_id).send_keys(password)

    def test_confirmpassword(self, confirmpassword):
        self.driver.find_element(By.ID, self.input_confirmpassword_id).clear()
        self.driver.find_element(By.ID, self.input_confirmpassword_id).send_keys(confirmpassword)

    def test_clickregisterbutton(self):
        self.driver.find_element(By.ID, self.button_register_id).click()


    def test_Registersuccesstext(self, registertext):
        app_text = self.driver.find_element(By.XPATH, self.static_register_text_xpath).text
        if registertext == app_text:
            print("Register flow completed")
            assert True
        else:
            print("Register flow is not completed please check")
            assert False





