#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("", )
say_my_name("", "White")
say_my_name("",)
try:
        say_my_name(12, "White")
except Exception as e:
        print(e)
