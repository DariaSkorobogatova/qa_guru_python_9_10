from selene import browser, have, command
from locators.registration_page_loc import RegPageLocators as reg_page, choose_day_of_birth


class MidLevelStepsRegistrationPage:

    def open(self, url):
        browser.open(url)

    def fill_first_name(self, value):
        browser.element(reg_page.first_name_loc).type(value)

    def fill_last_name(self, value):
        browser.element(reg_page.last_name_loc).type(value)

    def fill_email(self, value):
        browser.element(reg_page.email_loc).type(value)

    def choose_gender(self):
        browser.element(reg_page.gender_loc).click()

    def fill_phone_number(self, value):
        browser.element(reg_page.phone_number_loc).type(value)

    def click_birthday(self):
        browser.element(reg_page.date_of_birth_input_loc).click()

    def choose_bd_month(self, value):
        browser.element(reg_page.choose_month_of_birth_loc).type(value)

    def choose_bd_year(self, value):
        browser.element(reg_page.choose_year_of_birth_loc).type(value)

    def choose_bd_day(self, value):
        browser.element(choose_day_of_birth(value)).click()

    def choose_subject(self, value):
        browser.element(reg_page.subject_loc).type(value).press_enter()

    def scroll_hobbies_into_view(self):
        browser.element(reg_page.scroll_to_hobby_loc).perform(command.js.scroll_into_view)

    def choose_hobby(self, value):
        browser.all(reg_page.choose_hobby_loc).element_by(have.exact_text(value)).click()

    def upload_pic(self, path):
        browser.element(reg_page.upload_pic_loc).set_value(path)

    def fill_address(self, value):
        browser.element(reg_page.current_address_loc).type(value)

    def click_state(self):
        browser.element(reg_page.state_loc).click()

    def click_city(self):
        browser.element(reg_page.city_loc).click()

    def choose_state_city(self, value):
        browser.all(reg_page.choose_state_city_loc).element_by(have.exact_text(value)).click()

    def click_submit_bt(self):
        browser.element(reg_page.submit_button_loc).press_enter()

    def check_header(self, value):
        browser.element(reg_page.final_form_header_loc).should(have.text(value))

    def fields_with_user_info(self):
        return browser.element(reg_page.final_form_loc).all(reg_page.fields_with_user_info_loc)

    def close_form(self):
        browser.element(reg_page.close_button_loc).press_enter()
