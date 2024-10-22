from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('cover-thumb')
    print('Found<%s> element with that class name!' %(elem.tag_name))
except:
    print('was not able to find an element with that name')

