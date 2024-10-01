from selene import browser, have, be
import os


def test_demo_qa():
    browser.open('automation-practice-form/')
    browser.element('#firstName').type('Denis')
    browser.element('#lastName').type('Galdin')
    browser.element('#userEmail').type('testqa_mail@yahoo.com')
    browser.all('#genterWrapper').element_by(have.attribute('value' 'Male')).element('/label').click()
    browser.all('#userNumber-label').type('+79009009000')
    browser.element("#dateOfBirthInput").click()
    browser.element("//div[contains(@class, 'react-datepicker__month')]//div[contains(text(), '27')]").click()
    browser.element("//div[contains(@class, 'react-datepicker__year')]//div[contains(text(), '1997')]").click()
    browser.element("#subjectsInput").type('Endi')
    browser.element("//label[text()='Sports']").click()
    browser.element('element').send_keys(os.path.abspath('picture.png'))
    browser.element('#currentAddress').type('9153 Jerry Dr, Juneau, Alaska 99801, USA')
    browser.element('#state').click()
    browser.all('#state div[id^="react-select-"]').element_by(have.text('Haryana')).click()
    browser.element('#city').click()
    browser.all('#city div[id^="react-select-"]').element_by(have.text('Karnal')).click()
    browser.element('#submit').click()


