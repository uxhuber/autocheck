from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def close_modals(driver):
    try:
        # Закрываем модальное окно (если оно есть)
        modal_close_button = driver.find_element(By.CSS_SELECTOR, "[data-qa='onboarding-modal-button-skip']")
        modal_close_button.click()
        time.sleep(1)
    except Exception as e:
        print(f"Модальное окно не найдено или уже закрыто: {e}")


def search_vacancies(driver, keyword, city, experience):
    # Заполнение поля поиска
    search_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "text"))
    )
    search_field.send_keys(keyword)
    search_field.submit()
    time.sleep(2)

    
    try:
       
        city_filter = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{city}']"))
        )
        driver.execute_script("arguments[0].click();", city_filter)  # Используем JS для клика
        time.sleep(2)

        
        experience_filter = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{experience}']"))
        )
        driver.execute_script("arguments[0].click();", experience_filter)  # Используем JS для клика
        time.sleep(2)

        print("Фильтры применены успешно.")
    except Exception as e:
        print(f"Ошибка при применении фильтров: {e}")

# проверка результатов
def check_results(driver, keyword):
    try:
        results = driver.find_elements(By.CSS_SELECTOR, ".serp-item__title")
        if len(results) > 0:
            print(f"Найдено {len(results)} вакансий по запросу '{keyword}'.")
        else:
            print("Ошибка: Нет результатов поиска.")
    except Exception as e:
        print(f"Ошибка при проверке результатов: {e}")


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://hh.ru")

    try:
        # Закрытие модалок
        close_modals(driver)

        # Поиск вакансий тестировщика
        print("Тест 1: Поиск вакансий...")
        search_vacancies(driver, "тестировщик", "Москва", "От 1 года до 3 лет")
        check_results(driver, "тестировщик")

    except Exception as e:
        print(f"Ошибка во время выполнения теста: {e}")

    finally:
        driver.quit()