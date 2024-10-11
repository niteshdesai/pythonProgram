import re

pattern=r"^https?\:\//[a-zA-Z0-9]+\.[a-zA-Z]+"

url=input("Enter your url:")

if(re.match(pattern,url)):
    print("valid")
else:
    print("invalid")