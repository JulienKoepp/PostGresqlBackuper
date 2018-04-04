#!/usr/bin/python3

import sys
from termcolor import cprint
from lib.advanced_printf import print_no_return as nor_print

def _print_in_color(text, color):
    cprint(text, color, attrs=['bold'], end="", flush=True)

def print_ok():
    nor_print('[')
    _print_in_color('ok', 'green')
    nor_print(']')

def print_error():
    nor_print('[')
    _print_in_color('error', 'red')
    nor_print(']')

def print_error_message(message):
    nor_print("\n")
    print_error()
    nor_print(" ")
    print(message)
