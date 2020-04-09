import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_button_add_to_basket(browser):
    try:
        browser.get(link)
        time.sleep(30)
        browser.find_element_by_css_selector("button.btn.btn-lg")
        found = True
    except:
        found = False
    assert found, "Button 'Add to basket' is not find on page"
