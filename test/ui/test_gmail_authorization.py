import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize(
    "email", ["andrekropes@gmail.com"], indirect=True)
def test_valid_gmail_login(email, google_auth_page, password):
    google_auth_page.navigate_here()
    google_auth_page.fill_email(email)
    google_auth_page.next_email_button.click()
    google_auth_page.fill_password(password)
    google_auth_page.next_password_button.click()
    assert google_auth_page.is_user_authorized(email)


@pytest.mark.parametrize(
    "email",
    (("sdfsf@gmail.com"), ("")))
def test_invalid_missing_gmail_login(google_auth_page, email):
    google_auth_page.navigate_here()
    google_auth_page.fill_email(email)
    google_auth_page.next_email_button.click()
    expect(google_auth_page.email_field_error).to_be_visible()


@pytest.mark.parametrize(
    "password",
    (("sdfsdfsdg"), ("")))
def test_invalid_missing_gmail_password(google_auth_page, password):
    google_auth_page.navigate_here()
    google_auth_page.fill_email("andrekropes@gmail.com")
    google_auth_page.next_email_button.click()
    google_auth_page.fill_password(password)
    google_auth_page.next_password_button.click()
    expect(google_auth_page.password_field_error).to_be_visible()
