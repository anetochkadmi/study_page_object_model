from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"

def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    
    page.should_be_login_link()
    page.go_to_login_page()
    
    login_page = LoginPage(browser, link)
    login_page.should_be_login_page()
    # login_page.should_be_login_form()
    # login_page.should_be_register_form()
    # login_page.should_be_login_url()