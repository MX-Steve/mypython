py_str="hello world!"
print(py_str.capitalize())
print(py_str.title())
print(py_str.center(50))
print(py_str.center(50,"#"))
print(py_str.ljust(50,"*"))
print(py_str.rjust(50,"*"))
print(py_str.count('l'))
print(py_str.count('lo'))
print(py_str.endswith('!'))
print(py_str.endswith('d!'))
print(py_str.startswith('a'))
print(py_str.islower())
print(py_str.isupper())
print(py_str.isdigit())
print(py_str.isalnum()) # 字母数字吗？
print('  hello\t  '.strip())
print('  hello\t  '.lstrip())
print('  hello\t  '.rstrip())
print(py_str.split())
print(py_str.split('w'))
print('.'.join(['hello','tar','gz']))
print('-'.join(['hello','tar','gz']))
