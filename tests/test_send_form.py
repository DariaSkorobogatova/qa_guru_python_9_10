from selene import browser, have, command
import allure
import os
import tests


def test_send_form(browser_configs):
    with allure.step("Open registrations form"):
        browser.open("/automation-practice-form")

    with allure.step("Fill form"):
        browser.element("#firstName").type("Ada")
        browser.element("#lastName").type("Lovelace")
        browser.element("#userEmail").type("lovelace@rumbler.ru")
        browser.element("[name=gender][value=Female]+label").click()
        browser.element("#userNumber").type("1112223344")
        browser.element("#dateOfBirthInput").click()
        browser.element('.react-datepicker__month-select').type('December')
        browser.element('.react-datepicker__year-select').type('2000')
        browser.element(f'.react-datepicker__day--0{22}').click()
        browser.element("#subjectsInput").type("economics").press_enter()
        browser.element("[for=hobbies-checkbox-2]").perform(command.js.scroll_into_view)
        browser.all('.custom-checkbox').element_by(have.exact_text('Reading')).click()
        browser.element("#uploadPicture").set_value(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), "../resourses/flower.png")
            )
        )
        browser.element("#currentAddress").type("Test street, 9-99")
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Uttar Pradesh')).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Lucknow')).click()
        browser.element("#submit").press_enter()
        browser.element(".modal-header").should(have.text("Thanks for submitting the form"))

    with allure.step("Check form results"):
        browser.element(".table").all("td:nth-of-type(even)").should(
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
        browser.element("#closeLargeModal").press_enter()
