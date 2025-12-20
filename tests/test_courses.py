import pytest

from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):

    #Проверки на странице Create Course
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(title='',description='',estimated_time='',max_score='0', min_score='0')
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    #Действия по созданию курса
    create_course_page.upload_preview_image(file='./testdata/files/image.png')
    create_course_page.check_visible_image_upload_view()
    create_course_page.fill_create_course_form(
        title = "Playwright",
        estimated_time = "2 weeks",
        description = "Playwright",
        max_score = "100",
        min_score = "10",
    )
    create_course_page.click_create_course_button()

    #Редирект на Courses
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index = 0,
        title = "Playwright",
        max_score="100",
        min_score="10",
        estimated_time = "2 weeks",
    )

@pytest.mark.courses
@pytest.mark.regression
def test_empty_course_list(courses_list_page: CoursesListPage):
    courses_list_page.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
    )
    courses_list_page.navbar.check_visible('username')
    courses_list_page.sidebar.check_visible()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_empty_view()







'''def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user@gmail.com')
        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')
        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path='browser-state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        title_courses = page.get_by_test_id('courses-list-toolbar-title-text')
        icon_courses = page.get_by_test_id('courses-list-empty-view-icon')
        title_text_courses = page.get_by_test_id('courses-list-empty-view-title-text')
        description_text_courses = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(title_courses).to_be_visible()
        expect(icon_courses).to_be_visible()
        expect(title_text_courses).to_be_visible()
        expect(description_text_courses).to_be_visible()'''

