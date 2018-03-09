#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src import InstaBot
from src.usernameGen import usernameGen
from src.bioGen import bioGen
import os

bot = InstaBot()

##### Set Variables #####
######### Signup Form Data #########
bot.username = usernameGen(3, True)
bot.email = bot.username+'@gmail.com'
bot.first_name = bot.username.replace("_", " ").title()
bot.signup_password = 'b@tinlo18'

bot.user_login = bot.username
bot.user_password = 'b@tinlo18'
##### clean Variables #####
bot.clean_vars()
#### Signup or Login####
#check if there is no signup already
if os.path.exists('username.txt'):
    with open('username.txt') as f:
        user_signed = f.readline()
        if len(user_signed) == 0:
            bot.signup()
        else:
            bot.user_login = user_signed
            bot.username = bot.user_login
            bot.login()
else:
    bot.signup()
bio = {'biography': bioGen()}
bot.edit_account(bio)
bot.log_bot()