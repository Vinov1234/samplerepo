from selenium import webdriver
browser = webdriver.Firefox()
print(type(browser))
selenium.Webdrivr.firefox.Webdriver.Webdirver
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('cover-thumb')
    print('found<%s> element with that class name!'%(elem.tag_name))
except:
    print('was not able to find an element with that name')
