from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Заполняем поле email
    login_form_email_input = page.get_by_test_id('login-form-email-input').locator('input')
    login_form_email_input.focus()
    for char in 'user.name@gmail.com':
        page.keyboard.type(char, delay=10)
    page.keyboard.press("ControlOrMeta+A")



    # Задержка для наглядности выполнения теста (не рекомендуется использовать в реальных автотестах)
    page.wait_for_timeout(5000)