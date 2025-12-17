from playwright.sync_api import Page, expect

def test_empty_course_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    title_courses = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    icon_courses = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    title_text_courses = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    description_text_courses = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(title_courses).to_be_visible()
    expect(icon_courses).to_be_visible()
    expect(title_text_courses).to_be_visible()
    expect(description_text_courses).to_be_visible()
