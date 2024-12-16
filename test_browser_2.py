import logging
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Создаем обработник для записи в файл
file_handler = logging.FileHandler('test.logo', mode='w')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Создаем обработник для вывода в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

# Добавляем обработчики к логгеру
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Тестовые сообщения
logger.debug("This is a harmless debug Message")
logger.info("This is just an information")
logger.warning("It is a Warning. Please make changes")
logger.error("You are trying to divide by zero")
logger.critical("Internet is down")

@pytest.fixture(scope="module")# Определяем фикстуру для браузера с областью действия "module"
def browser():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))#созд экземпляр браузера Chrome
    yield browser#морозимся и возвр браузер
    browser.quit()#все закр после теста

from pages.sbis_contacts import SbisContactsPage
class TestSbisContactsPage:
    def test_region_navigation(self, browser):
        logger.info('ZAPUSK TESTA ')
        page = SbisContactsPage(browser)

        page.open()
        current_url_44reg = page.get_current_url()
        assert current_url_44reg == 'https://sbis.ru/contacts/44-kostromskaya-oblast?tab=clients'
        time.sleep(5)
        page.click_anchor_to_region()
        logger.info(' TEST ')
        time.sleep(3)
        page.select_region(43)
        time.sleep(3)
        current_url_41reg = page.get_current_url()
        assert current_url_41reg == 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'

        logger.info('TEST IS END AND WERY WELL')