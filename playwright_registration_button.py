from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    # Заполняем поле email
    registration_form_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_form_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_form_password_input = page.get_by_test_id('registration-form-password-input').locator('input')

    registration_form_email_input.fill("user.name@gmail.com")
    registration_form_username_input.fill("username")
    registration_form_password_input.fill("password")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_enabled()
    page.wait_for_timeout(5000)
