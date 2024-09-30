from selene import browser, have, be

browser.element('#firstName').type('Denis')
browser.element('#lastName').type('Galdin')
browser.element('#userEmail').type('testqa_mail@yahoo.com')
browser.all('#genterWrapper').element_by(have.attribute('value' 'Male')).element('/label').click()
browser.all('#userNumber-label').type('+79009009000')