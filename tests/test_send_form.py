from selene import browser, by, have, be
import os


def test_send_form(browser_configs):
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Ada')
    browser.element('#lastName').type('Lovelace')
    browser.element('#userEmail').type('lovelace@rumbler.ru')
    browser.element('//div[@id="genterWrapper"]/div[2]/div[2]').click()
    browser.element('#userNumber').type('1112223344')
    browser.element('#dateOfBirthInput').click()
    browser.element('[value="11"]').click()
    browser.element('[value="2000"]').click()
    browser.element('[aria-label*="22nd"]').click()
    browser.element('#subjectsInput').type('economics')
    browser.element('#react-select-2-option-0').click()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('../pictures/flower.png'))
    browser.element('#currentAddress').type('Test street, 9-99')
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Lucknow').press_enter()
    browser.element('#submit').press_enter()
    # Почему press_enter() на кнопке submit срабатывает, а click() - нет?
    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.all('.table>tbody>tr>td:nth-of-type(even)').should(have.texts(
        'Ada Lovelace',
        'lovelace@rumbler.ru',
        'Female',
        '1112223344',
        '22 December,2000',
        'Economics',
        'Sports, Reading, Music',
        'flower.png',
        'Test street, 9-99',
        'Uttar Pradesh Lucknow'
    ))
    browser.element('#closeLargeModal').press_enter()