import allure

@allure.step("Opening browser")
def open_browser():
    with allure.step("Get browser"):
        ...

    with allure.step("Start browser"):
        with allure.step("Get browser"):
            ...

@allure.step("Creating course with title '{title_1234}'")
def create_course(title_1234: str):
    ...

@allure.step("Closing browser")
def close_browser():
    ...

def test_feature():
    open_browser()

    create_course(title="Locust")
    create_course(title="Pytest")
    create_course(title="Playwright")
    create_course(title="Phython")

    close_browser()
