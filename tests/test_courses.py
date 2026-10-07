import pytest
from playwright.sync_api import expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course#/courses")

    courses_title = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    there_is_no_results_alert = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(there_is_no_results_alert).to_be_visible()
    expect(there_is_no_results_alert).to_have_text("There is no results")

    icon_alert = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(icon_alert).to_be_visible()

    results_from_the_load_test_pipeline_will_be_displayed_here_alert = chromium_page_with_state.get_by_test_id(
        "courses-list-empty-view-description-text")
    expect(results_from_the_load_test_pipeline_will_be_displayed_here_alert).to_be_visible()
    expect(results_from_the_load_test_pipeline_will_be_displayed_here_alert).to_have_text(
        "Results from the load test pipeline will be displayed here")
