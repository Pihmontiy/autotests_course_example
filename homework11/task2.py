# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

driver = webdriver.Chrome()
sbis_site = 'https://fix-online.sbis.ru/'
user_login = 'Lynch'
user_pass = 'Qq123123'
try:
    print('Открыть сайт')
    driver.get(sbis_site)
    sleep(1)
    print('Проверить адрес сайта')
    assert driver.current_url == 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/', "Неверный адрес сайта"

    print('Ввести логин')
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    sleep(1)

    print('Ввести пароль')
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_pass, Keys.ENTER)
    sleep(5)

    print('Проверить загрузку после авторизации')
    accordeon = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-Accordion__container')
    assert accordeon.is_displayed(), 'Не загрузился боковой аккордеон'

    print('Переход в реестр Контакты')
    acc_cont_btn = driver.find_element(By.XPATH, '//span[text()="Контакты"]')
    assert acc_cont_btn.is_displayed(), 'Кнопка аккордеона Контакты - не отображается'
    acc_cont_btn.click()
    sleep(1)
    acc_cont_btn_sub = driver.find_element(By.XPATH, '//*[@data-qa="NavigationPanels-SubMenu__head"]')
    assert acc_cont_btn_sub.is_displayed()
    acc_cont_btn_sub.click()
    assert driver.current_url == "https://fix-online.sbis.ru/page/dialogs"
    sleep(1)

    print("Создаем окно диалога")
    new_diag_btn = driver.find_element(By.XPATH, '//*[@data-name="sabyPage-addButton"]')
    assert new_diag_btn.is_displayed(), 'Кнопка создание диалога не отображается'
    new_diag_btn.click()
    sleep(3)

    print('Открываем окно выбора адресата')
    pvp_panel = driver.find_element(By.XPATH, '//div[@class="controls-StackTemplate-content"]')
    assert pvp_panel.is_displayed(), 'Панель выбора адресата не отображается'
    search_input = driver.find_element(By.XPATH, "//div[contains(@class,'popup')]//input")
    assert search_input.is_displayed(), 'Поле поиска не отображается'
    search_input.send_keys('Линч Дэвид')
    sleep(2)

    print('Вводим имя адресата, выбираем для отправки')
    search_result = driver.find_element(By.XPATH, '//div/*[@class="msg-addressee-item"]//span[@title="Линч Дэвид"]')
    search_result.click()
    sleep(1)

    print('Вводим тестовое сообщение')
    msg_panel = driver.find_element(By.XPATH, '//div[@class="msg-addressee-manager ws-flexbox"]')
    assert msg_panel.is_displayed(), 'Панель сообщения не появилась'
    msg_input = driver.find_element(By.XPATH, '//div[@data-qa="textEditor_slate_Field"]')
    assert msg_input.is_displayed(), 'Строка ввода сообщение не отображается'

    print('Отправляем тестовое сообщение')
    msg_input.send_keys('Тестовый текст', Keys.CONTROL, Keys.ENTER)

    
    my_msg = driver.find_element(By.CLASS_NAME, '.msg-entity-text')
    assert my_msg.text == 'Тестовый текст'
    sleep(5)

finally:
    driver.quit()