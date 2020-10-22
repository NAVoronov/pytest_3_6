import time

def test_me(browser):	
	browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
	btn = browser.find_element_by_class_name("btn-add-to-basket")
	assert btn.get_attribute("class") == "btn btn-lg btn-primary btn-add-to-basket"
	time.sleep(5)
