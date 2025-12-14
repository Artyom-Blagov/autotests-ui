from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Заполняем поле email
    login_form_email_input = page.get_by_test_id('login-form-email-input').locator('input')
    login_form_email_input.fill("user.name@gmail.com")

    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).not_to_be_disabled()

    page.wait_for_timeout(5000)
