from config import config
import string
import random
import requests
import json


def random_string():
    return ''.join(random.choice(string.lowercase) for x in range(10))


def logout(browser):
    browser.visit('{0}{1}'.format(config['DM_FRONTEND_URL'], '/logout'))


def login(browser, email, password):
    logout(browser)
    browser.visit('{0}{1}'.format(config['DM_FRONTEND_URL'], '/login'))
    browser.fill('email_address', email)
    browser.fill('password', password)
    click_button('Log in', browser)


def click_button(text, browser):
    button = browser.find_by_value(text).first
    button.click()


def save_and_continue(browser):
    click_button('Save and continue', browser)


def click_link(link_text, browser):
    browser.click_link_by_text(link_text)


def visit_page(page, browser):
    browser.visit('{0}{1}'.format(config['DM_FRONTEND_URL'], page))


def enter_title(title, browser):
    browser.fill('title', title)


def create_brief(title, browser):
    visit_page('/', browser)
    click_link('Find an individual specialist', browser)
    click_button('Create brief', browser)
    enter_title(title, browser)
    click_button('Save and continue', browser)


def delete_brief(title):
    headers = {'Authorization': 'Bearer {}'.format(config['DM_DATA_API_AUTH_TOKEN']),
               'Content-type': 'application/json'}
    get_briefs = requests.get('{}/briefs?per_page=1000'.format(config['DM_DATA_API_URL']), headers=headers)
    print title
    if (get_briefs.status_code == 200):
        print get_briefs.json()['briefs']
        briefs = [b for b in get_briefs.json()['briefs'] if b['title'] == title]
        if briefs:
            requests.delete('{}/briefs/{}'.format(config['DM_DATA_API_URL'], briefs[0]['id']), headers=headers,
                            data=json.dumps({'updated_by': ''}))
