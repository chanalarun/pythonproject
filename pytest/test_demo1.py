
from utilities.BaseClass import BaseClass



class TestOne(BaseClass):

    def test_e2e(self):

        self.driver.find_element_by_css_selector('a[href="/angularpractice/shop"]').click()

        products = self.driver.find_elements_by_xpath('//div[@class="card h-100"]')
        for product in products:
            product_nam e =product.find_element_by_xpath("div/h4").text
            if product_name == "Blackberry":
                product.find_element_by_xpath('div/button').click()


        self.driver.find_element_by_xpath('//li[@class="nav-item active"]/a').click()
        # driver.find_element_by_xpath('//a[text()="Blackberry"]')
        # assert product_name == self.driver.find_element_by_xpath('//a[text()="Blackberry"]').text
        self.driver.find_element_by_css_selector('button[class="btn btn-success"]').click()
        self.driver.find_element_by_id("country").send_keys("ind")
        self.time.sleep(5)
        self.driver.find_element_by_xpath('//div[@class="suggestions"]/ul/li/a').click()
        self.driver.find_element_by_css_selector('label[for ="checkbox2"]').click()
        self.driver.find_element_by_css_selector('input[type ="submit"]').click()
        print(self.driver.find_element_by_css_selector(".alert").text)
