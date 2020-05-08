from selenium import webdriver
browser=webdriver.firefox()
browser.get("url")

elem=browser.find_element_by_css_selector("selector path")
elem.click()

elems=browser.find_elements_by_css_selector('p')
len(elems)

searchElem=browser.find_elements_by_css_selector('.search-field')
searchElem.send_keys('text_to_be_searched')
searchElem.submit()
browser.back()
browser.forward()
browser.refresh()
browser.quit()