#!/usr/bin/env python3

import http.cookiejar
import os
import urllib.parse

USERNAME_ENVNAME = 'HACKER_ORG_USERNAME'
PASSWORD_ENVNAME = 'HACKER_ORG_PASSWORD'

BASE_CHALLENGE_URL = 'http://www.hacker.org/challenge/chal.php'

username = None
password = None

def init_username_password():
    global username, password
    
    if USERNAME_ENVNAME in os.environ:
        username = os.environ[USERNAME_ENVNAME]
    else:
        username = input('username: ')
    
    if PASSWORD_ENVNAME in os.environ:
        password = os.environ[PASSWORD_ENVNAME]
    else:
        password = input('password: ')

def configure_cookies():
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    urllib.request.install_opener(opener)

def build_challenge_url(problem_id, answer=None):
    query = {'id': problem_id, 'name': username, 'password': password}
    if answer:
        query['answer'] = answer
        query['go'] = 'Submit'
    
    parameters = urllib.parse.urlencode(query)
    return '{base_challenge_url}?{parameters}'.format(base_challenge_url=BASE_CHALLENGE_URL, parameters=parameters)


init_username_password()
configure_cookies()
