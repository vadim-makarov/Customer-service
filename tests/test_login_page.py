# class TestLoginPage:
#     def test_should_be_login_url(self, browser):
#         page = LoginPage(browser, LOGIN_LINK)
#         page.open()
#         page.should_be_login_url()
#
#     def test_should_be_login_form(self, browser):
#         page = LoginPage(browser, LOGIN_LINK)
#         page.open()
#         page.should_be_login_form_name()
#
#     def test_should_be_registration_form(self, browser):
#         page = LoginPage(browser, LOGIN_LINK)
#         page.open()
#         page.should_be_register_link()
#
#     def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
#         page = MainPage(browser, HOME_LINK)
#         page.open()
#         page.go_to_basket()
#         page = BasketPage(browser, basket_link, timeout=0)
#         page.open()
#         page.basket_is_empty()
#         page.basket_is_empty_text()
