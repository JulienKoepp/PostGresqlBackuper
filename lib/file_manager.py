#!/usr/bin/python3

import os

def read_all_lines(filename):
    file_handler = open(filename)

    all_lines = []

    for line in file_handler:
        all_lines.append(line)
    file_handler.close()

    return all_lines

def write_all_lines(lines, filename):
    file_handler = open(filename, "w")
    for line in lines:
        file_handler.write(line+"\n")
    file_handler.close()

def folder_exists(folder_name):
    return os.path.exists(folder_name)

def file_exists(file_name):
    return folder_exists(file_name)

def file_is_empty(filename):
    return os.stat(filename).st_size == 0

def write_string(string, filename):
    file_handler = open(filename, "w")
    file_handler.write(string)
    file_handler.close()

def force_write_string(string, filename):
    file_handler = open(filename, "w+")
    file_handler.write(string)
    file_handler.close()

def read_string(filename):
    return read_all_lines(filename)
