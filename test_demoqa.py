from selene import browser, have, command
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
    browser.element('element').perform(command.js.drop_file(os.path.abspath('C:\Desktop\картинки')))

    browser.element('#currentAddress').type('9153 Jerry Dr, Juneau, Alaska 99801, USA')
    browser.element('#state').click()
    browser.all('#state div[id^="react-select-"]').element_by(have.text('Haryana')).click()
    browser.element('#city').click()
    browser.all('#city div[id^="react-select-"]').element_by(have.text('Panipat')).click()
    browser.element('#submit').click()

    browser.element('//td[contains(text(),"Student Name")]/../td[2]').should(have.exact_text('Denis Galdin'))
    browser.element('//td[contains(text(),"Student Email")]/../td[2]').should(have.exact_text('testqa_mail@uahoo.com'))
    browser.element('//td[contains(text(),"Gender")]/../td[2]').should(have.exact_text('Male'))
    browser.element('//td[contains(text(),"Mobile")]/../td[2]').should(have.exact_text('+79009009000'))
    browser.element('//td[contains(text(),"Date of Birth")]/../td[2]').should(have.exact_text('27 January,1997'))
    browser.element('//td[contains(text(),"Subject")]/../td[2]').should(have.exact_text('Endi'))
    browser.element('//td[contains(text(),"Hobbies")]/../td[2]').should(have.exact_text('Sports'))
    browser.element('//td[contains(text(),"Picture")]/../td[2]').should(have.exact_text('pic.jpg'))
    browser.element('//td[contains(text(),"Address")]/../td[2]').should(
        have.exact_text('9153 Jerry Dr, Juneau, Alaska 99801, USA'))
    browser.element('//td[contains(text(),"State and City")]/../td[2]').should(have.exact_text('Haryana Papinat'))
