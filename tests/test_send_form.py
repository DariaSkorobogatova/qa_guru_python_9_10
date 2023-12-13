from selene import have
from pages.registration_page import MidLevelStepsRegistrationPage
from helpers import path


def test_send_form(browser_configs):
    reg_page = MidLevelStepsRegistrationPage()
    reg_page.open('/automation-practice-form')
    reg_page.fill_first_name('Ada')
    reg_page.fill_last_name('Lovelace')
    reg_page.fill_email('lovelace@rumbler.ru')
    reg_page.choose_gender()
    reg_page.fill_phone_number('1112223344')
    reg_page.click_birthday()
    reg_page.choose_bd_month('December')
    reg_page.choose_bd_year('2000')
    reg_page.choose_bd_day(22)
    reg_page.choose_subject('economics')
    reg_page.scroll_hobbies_into_view()
    reg_page.choose_hobby('Reading')
    reg_page.upload_pic(path.to_avatar('flower.png'))
    reg_page.fill_address('Test street, 9-99')
    reg_page.click_state()
    reg_page.choose_state_city('Uttar Pradesh')
    reg_page.click_city()
    reg_page.choose_state_city('Lucknow')
    reg_page.click_submit_bt()
    reg_page.check_header('Thanks for submitting the form')
    reg_page.fields_with_user_info().should(
        have.texts(
            "Ada Lovelace",
            "lovelace@rumbler.ru",
            "Female",
            "1112223344",
            "22 December,2000",
            "Economics",
            "Reading",
            "flower.png",
            "Test street, 9-99",
            "Uttar Pradesh Lucknow",
        )
    )
    reg_page.close_form()


