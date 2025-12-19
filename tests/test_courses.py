from playwright.async_api import Page, expect
import pytest

from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_preview_upload()
    create_course_page.check_visible_create_course_form(title='',description='',estimated_time='',max_score='0', min_score='0')
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image(file='./testdata/files/image.png')
    create_course_page.check_visible_preview_image()

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

