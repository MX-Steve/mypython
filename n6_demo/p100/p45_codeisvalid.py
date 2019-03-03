import os
import keyword
import string

first_letter=string.ascii_letters+'_'
others=first_letter+string.digits

def isvalid(word):
  if keyword.iskeyword(word):
    return word+"is key word"

  if word[0] not in first_letter:
    return word +"must start letter or _"

  for ind,w in enumerate(word[1:]):
    if w not in others:
      return "%s在%s位置出现不合法字符"%(word,(ind+1))
  return "%s is valid"%word

if __name__ == "__main__":
  word=input("请输入验证码：")
  result=isvalid(word)
  print(result)
