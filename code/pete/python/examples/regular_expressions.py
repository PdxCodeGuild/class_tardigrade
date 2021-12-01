# [0-9]{3}-[0-9]{3}-[0-9]{4}\b
import re
print(re.match('a', 'abcdef'))    # match
print(re.match('c', 'abcdef'))    # no match
print(re.search('c', 'abcdef'))   # match
print(re.search('^c', 'abcdef'))  # no match
print(re.search('^a', 'abcdef'))  # match
match_object = re.match('a', 'abcdef') # you can do more with the object that re.match returns

phone_numbers="""
123-456-7890
1234-56-7890
987-765-3219
123-123-12345"""

validated_phone_numbers = re.findall(r'[0-9]{3}-[0-9]{3}-[0-9]{4}\b', phone_numbers)
print(validated_phone_numbers)

email_addresses = """pete@pdxcodeguild.com
sheri@pdxcodeguild.com
realperson@truemail.xyz.banana
pete-at-pdxcodeguild.com
pete@pdxcodeguild.net
@pdxcodeguild.com
pETe@pdxcodeguild.com
pete@pdxcodeguildcom"""

email_regex = re.compile(r'[A-z]+@[a-z]+\.[a-z]{3}$', re.M)
validated_email_addresses = email_regex.findall(email_addresses)
print(validated_email_addresses)