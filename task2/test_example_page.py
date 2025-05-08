import pytest
from example_page import ExamplePage


def test_example_page_title_and_link(page):
    example_page = ExamplePage(page, "https://example.com")
    example_page.open()

    # Проверка заголовка
    example_page.should_have_valid_header()

    # Проверка наличия ссылки
    example_page.should_have_more_information_link()

    # Клик по ссылке и проверка URL
    example_page.click_more_information_link()
    example_page.should_have_correct_url_after_click()
