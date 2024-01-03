import allure
from pages.registration_page import HighLevelStepsRegistrationPage
from model.user_model import user


def test_send_form(browser_configs):
    reg_page = HighLevelStepsRegistrationPage()
    with allure.step("Open registrations form"):
        reg_page.open('/automation-practice-form')
        reg_page.hide_ad()
    with allure.step("Fill form"):
        reg_page.register(user)
    with allure.step("Check form results"):
        reg_page.should_have_data(user)
        reg_page.close_form()
