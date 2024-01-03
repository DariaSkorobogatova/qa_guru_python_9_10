from selene import browser, have, command
from locators.registration_page_loc import (
    RegPageLocators as reg_page,
    choose_day_of_birth,
    choose_gender,
)
from model.user_model import User
from helpers import path


class HighLevelStepsRegistrationPage:
    def open(self, url):
        browser.open(url)

    def hide_ad(self):
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    def fill_first_name(self, value):
        browser.element(reg_page.first_name_loc).type(value)

    def fill_last_name(self, value):
        browser.element(reg_page.last_name_loc).type(value)

    def fill_email(self, value):
        browser.element(reg_page.email_loc).type(value)

    def choose_gender(self, value):
        browser.element(choose_gender(value)).click()

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
        browser.element(reg_page.scroll_to_hobby_loc).perform(
            command.js.scroll_into_view
        )

    def choose_hobby(self, value):
        browser.all(reg_page.choose_hobby_loc).element_by(
            have.exact_text(value)
        ).click()

    def upload_pic(self, path):
        browser.element(reg_page.upload_pic_loc).set_value(path)

    def fill_address(self, value):
        browser.element(reg_page.current_address_loc).type(value)

    def click_state(self):
        browser.element(reg_page.state_loc).click()

    def click_city(self):
        browser.element(reg_page.city_loc).click()

    def choose_state_city(self, value):
        browser.all(reg_page.choose_state_city_loc).element_by(
            have.exact_text(value)
        ).click()

    def click_submit_bt(self):
        browser.element(reg_page.submit_button_loc).press_enter()

    def check_header(self, value):
        browser.element(reg_page.final_form_header_loc).should(have.text(value))

    def fields_with_user_info(self):
        return browser.element(reg_page.final_form_loc).all(
            reg_page.fields_with_user_info_loc
        )

    def close_form(self):
        browser.element(reg_page.close_button_loc).press_enter()

    def register(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.choose_gender(user.gender)
        self.fill_phone_number(user.phone_number)
        self.click_birthday()
        self.choose_bd_month(user.bd_month)
        self.choose_bd_year(user.bd_year)
        self.choose_bd_day(user.bd_day)
        self.choose_subject(user.subject)
        self.scroll_hobbies_into_view()
        self.choose_hobby(user.hobby)
        self.upload_pic(path.to_avatar(user.avatar))
        self.fill_address(user.current_address)
        self.click_state()
        self.choose_state_city(user.state)
        self.click_city()
        self.choose_state_city(user.city)
        self.click_submit_bt()
        return self

    def should_have_data(self, user: User):
        self.fields_with_user_info().should(
            have.texts(
                f"{user.first_name} {user.last_name}",
                user.email,
                user.gender,
                user.phone_number,
                f"{user.bd_day} {user.bd_month},{user.bd_year}",
                user.subject,
                user.hobby,
                user.avatar,
                user.current_address,
                f"{user.state} {user.city}",
            )
        )
