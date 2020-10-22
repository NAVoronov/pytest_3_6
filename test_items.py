import time

def test_me(browser):	
	browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
	browser.find_element_by_class_name("btn-add-to-basket")
	time.sleep(5)