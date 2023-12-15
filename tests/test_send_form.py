from selene import have
from pages.registration_page import HighLevelStepsRegistrationPage
from model.user_model import user


def test_send_form(browser_configs):
    reg_page = HighLevelStepsRegistrationPage()
    reg_page.open('/automation-practice-form')
    reg_page.register(user)
    reg_page.should_have_data(user)
    reg_page.close_form()
