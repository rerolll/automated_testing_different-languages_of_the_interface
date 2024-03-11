import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default=None,
        help="Choose language",
    )
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox",
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None

    user_language = request.config.getoption("language")

    if user_language is None:
        raise pytest.UsageError("--language should be")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")

        options = ChromeOptions()
        options.add_experimental_option(
            "prefs", {"intl.accept_languages": user_language}
        )

        service = ChromeService(
            executable_path=ChromeDriverManager().install()
        )
        browser = webdriver.Chrome(service=service, options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")

        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)

        browser = webdriver.Firefox(
            service=FirefoxService(
                executable_path=GeckoDriverManager().install()
            ),
            options=options,
        )
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()
