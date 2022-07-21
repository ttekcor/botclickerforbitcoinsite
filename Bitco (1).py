import time
from selenium import webdriver

if __name__ == '__main__':
    while True:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
        Options = webdriver.chrome.options.Options()
        Options.headless = False
        browser = webdriver.Chrome('C:/Users/Housemaster/Desktop/Programming/Python/Work/WebScrapping/chromedriver.exe',
                                   options=Options)
        browser.get('https://freebitco.in/?r=19278965')
        browser.maximize_window()
        time.sleep(2)
        browser.find_element_by_class_name('login_menu_button').click()
        time.sleep(5)
        elem = browser.find_element_by_class_name('pushpad_deny_button')
        if elem.is_displayed() == True:
            elem.click()
        else:
            pass
        browser.find_element_by_id('login_form_btc_address').click()
        elem.send_keys('1MywwRqu6k6G6wvvjdCh33NtmtCurbmrgc')
        time.sleep(1)
        browser.find_element_by_id('login_form_password').click()
        elem.send_keys('S9cUHoyQikBfbK4Q')
        time.sleep(1)
        browser.find_element_by_id('login_button').click()
        time.sleep(4)
        browser.find_element_by_id('play_without_captchas_button').click()
        time.sleep(2)
        browser.find_element_by_id('free_play_form_button').click()
        time.sleep(3)
        browser.quit()
        time.sleep(3610)
