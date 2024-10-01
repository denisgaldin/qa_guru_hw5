from selene import browser, have
import os

def test_demo_qa():
    browser.open('automation-practice-form/')
    browser.element('#firstName').type('Denis')
    browser.element('#lastName').type('Galdin')
    browser.element('#userEmail').type('testqa_mail@yahoo.com')
    browser.element('[value="Male"]').click()
    browser.element('#userNumber').type('+79009009000')
    browser.element("#dateOfBirthInput").click()
    browser.element("//div[contains(@class, 'react-datepicker__month')]//div[contains(text(), '27')]").click()
    browser.element("//div[contains(@class, 'react-datepicker__year')]//div[contains(text(), '1997')]").click()
    browser.element("#subjectsInput").type('Endi')
    browser.element("//label[text()='Sports']").click()
    browser.element('#uploadFile').upload_file(os.path.abspath('C:\\Desktop\\картинки\\pic.jpg'))
    browser.element('#currentAddress').type('9153 Jerry Dr, Juneau, Alaska 99801, USA')
    browser.element('#state').click()
    browser.all('#state div[id^="react-select-"]').element('Haryana').click()
    browser.element('#city').click()
    browser.all('#city div[id^="react-select-"]').element('Panipat').click()
    browser.element('#submit').click()

    browser.all('//tr//td[2]').should(have.exact_texts('Denis Galdin', 'testqa_mail@yahoo.com', 'Male', '79009009000',
                                                       '27 January 1997', 'Endi', 'Sports', 'pic.jpg',
                                                       '9153 Jerry Dr, Juneau, Alaska 99801, USA', 'Haryana Panipat'))