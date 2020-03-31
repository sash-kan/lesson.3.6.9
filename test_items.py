from time import sleep

def test_guest_should_see_add_to_basket_button(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    elements = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert len(elements) > 0, "должна быть кнопка с css-селектором 'button.btn-add-to-basket'"
    sleep(3)
