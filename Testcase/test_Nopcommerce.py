import time
from selenium.webdriver.common.by import By
from Utilities.test_necessarylogic import randomemail
from Utilities import excel
from Pageobject.test_Registerpage import test_Registerpage
from Testcase.conftest import setup

site = "https://demo.nopcommerce.com"

file = "C:/Users/ADMIN/Downloads/Nop Commerce Testcase.xlsx"
sheetname = "REGISTER"
column = 11


class test_Register(object):
    # User data
    firstname = "guru"
    lastname = "M"
    date = 30
    Month = "September"
    Year = 1995
    Email = randomemail()
    Company = " Commerce"
    Password = "guru1022"
    Confirmpassword = "guru1022"

    # Webapplication text for validation
    Register_successtext = "Your registration completed"

    wait_time = 1

    def test_setup(self):
        self.driver = setup()
        self.driver.get(site)
        self.driver.maximize_window()
        self.rp = test_Registerpage(self.driver)
        self.driver.find_element(By.XPATH, self.rp.Click_registertab_xpath).click()
        time.sleep(self.wait_time)
        excel.Write_data(file, sheetname, 18, column, "pass")

        # Select Gender male gender
        gender = self.rp.test_selectgender()
        # Below code will write the result automatically in the test case.
        excel.Write_data(file, sheetname, 20, column, "pass")

        # enter firstname
        self.rp.test_Enterfirstname(self.firstname)
        time.sleep(self.wait_time)
        # Below code will write the result automatically in the test case.
        excel.Write_data(file, sheetname, 21, column, "pass")

        # enter last name
        self.rp.test_Enterlastname(self.lastname)
        time.sleep(self.wait_time)
        # Below code will write the result automatically in the test case.
        excel.Write_data(file, sheetname, 22, column, "pass")

        # enter date of birth
        self.rp.test_dateofbirth(str(self.date), self.Month, str(self.Year))
        time.sleep(self.wait_time)
        # Below code will write the result automatically in the test case.
        excel.Write_data(file, sheetname, 23, column, "pass")

        # enter email
        self.rp.test_email(self.Email)
        time.sleep(self.wait_time)
        # Below code will write the result automatically in the test case.
        excel.Write_data(file, sheetname, 24, column, "pass")

        # enter company name
        self.rp.test_company(self.Company)
        time.sleep(self.wait_time)
        # Below code will write the result automatically in the test case.
        excel.Write_data(file, sheetname, 25, column, "pass")

        # enter password
        self.rp.test_password(self.Password)
        time.sleep(self.wait_time)
        # Below code will write the result automatically in the test case.
        excel.Write_data(file, sheetname, 28, column, "pass")

        # enter Confirm password
        self.rp.test_confirmpassword(self.Confirmpassword)
        time.sleep(self.wait_time)
        # Below code will write the result automatically in the test case.
        excel.Write_data(file, sheetname, 29, column, "pass")

        # click Registration button
        self.rp.test_clickregisterbutton()
        time.sleep(self.wait_time)
        # Below code will write the result automatically in the test case.
        excel.Write_data(file, sheetname, 30, column, "pass")

        # Validate register success text
        self.rp.test_Registersuccesstext(self.Register_successtext)


c = test_Register()
c.test_setup()
