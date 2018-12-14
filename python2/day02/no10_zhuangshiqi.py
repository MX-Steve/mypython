#!/usr/bin/env python3
"zhuang shi qi"
def set_color(func):
    def color():
        return "\033[31;1m%s\033[0m" % func()
    return color

@set_color
def greet():
    return " How are you ?"

if __name__ == '__main__':
    print(greet)
    print(greet())