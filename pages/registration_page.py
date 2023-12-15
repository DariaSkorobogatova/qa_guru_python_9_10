from selene import browser, have, command
from locators.registration_page_loc import RegPageLocators as reg_page, choose_day_of_birth, choose_gender
from model.user_model import User
from helpers import path


class HighLevelStepsRegistrationPage:

    def open(self, url):
        browser.open(url)

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

    def register(self, user: User):
        full_name = user.full_name.split()
        date_of_birth = user.date_of_birth.split()
        day = int(date_of_birth[0])
        month_year = date_of_birth[1].split(',')
        month = month_year[0]
        year = month_year[1]
        state_city = user.city.split()
        state = state_city[0] + ' ' + state_city[1]
        city = state_city[2]
        self.fill_first_name(full_name[0])
        self.fill_last_name(full_name[1])
        self.fill_email(user.email)
        self.choose_gender(user.gender)
        self.fill_phone_number(user.phone_number)
        self.click_birthday()
        self.choose_bd_month(month)
        self.choose_bd_year(year)
        self.choose_bd_day(day)
        self.choose_subject(user.subject)
        self.scroll_hobbies_into_view()
        self.choose_hobby(user.hobby)
        self.upload_pic(path.to_avatar(user.avatar))
        self.fill_address(user.current_address)
        self.click_state()
        self.choose_state_city(state)
        self.click_city()
        self.choose_state_city(city)
        self.click_submit_bt()
        return self

    def should_have_data(self, user: User):
        self.fields_with_user_info().should(have.texts(user.full_name,
                                                       user.email,
                                                       user.gender,
                                                       user.phone_number,
                                                       user.date_of_birth,
                                                       user.subject,
                                                       user.hobby,
                                                       user.avatar,
                                                       user.current_address,
                                                       user.city))
