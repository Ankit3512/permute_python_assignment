from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class Driver:
    options = Options()
    options.add_argument("--incognito")
    options.add_experimental_option("detach", True)
    options.add_argument('headless')

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.policybazaar.com")
    driver.maximize_window()