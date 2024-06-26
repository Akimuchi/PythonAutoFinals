from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login substring is not presented in current url"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL_FIELD)
        email_form.send_keys(email)
        password_form = self.browser. \
            find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_FIELD)
        password_form.send_keys(password)
        password_form_confirmation = self.browser. \
            find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_CONFIRMATION_FIELD)
        password_form_confirmation.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
