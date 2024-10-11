import re

pattern=re.compile(r"^[a-zA-Z0-9]+\@[a-zA_Z0-9]+\.[a-zA-Z]+")

url=input("Enter your Email:")

if(pattern.match(url)):
    print("valid")
else:
    print("invalid")