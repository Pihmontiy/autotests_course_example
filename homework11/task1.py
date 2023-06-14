# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
sbis_contact = 'https://sbis.ru/contacts'
sbis_contact_title = 'СБИС Контакты'
tensor_site = 'https://tensor.ru/'
tensor_about = 'https://tensor.ru/about'

try:
    driver.get(sbis_site)
    sleep(1)
    print('Проверить адрес сайта и заголовок страницы')
    assert driver.current_url == sbis_site, 'Неверный адрес сайта'
    assert driver.title == sbis_title, 'Неверный заголовок сайта'

    print('Проверить отображение четырех вкладок')
    tabs = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
    assert len(tabs) == 4

    print('Проверить текст, атрибут и видимость кнопки Контакты')
    cont_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item [href="/contacts"]')

    print('Перейти на страницу Контакты')
    assert cont_btn.is_displayed(), 'Элемент не отображается'
    cont_btn.click()

    print('Проверить адрес сайта и заголовок страницы')
    sleep(1)
    assert sbis_contact in driver.current_url, 'Неверный адрес страницы'
    assert sbis_contact_title in driver.title, 'Неверный заголовок сайта'

    print('Кликнуть на баннер "Тензор"')
    tens_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__border-left a[href="https://tensor.ru/"]')
    sleep(1)
    assert tens_btn.is_displayed(), 'Баннера тензор нет'
    tens_btn.click()
    sleep(3)
    driver.switch_to.window(driver.window_handles[1])

    print('Проверить адрес сайта')
    assert driver.current_url == tensor_site
    print('Найти новость Сила в людях')
    news = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]')
    detail_btn = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
    news.location_once_scrolled_into_view
    assert news.is_displayed(), 'Новости Сила в людях - нет'
    assert detail_btn.is_displayed(), 'Кнопка "Подробнее" в новости не отображается'
    detail_btn.click()

    print('Проверить адрес сайта')
    sleep(1)
    assert driver.current_url == tensor_about, 'Неверный адрес'

finally:
    driver.quit()
