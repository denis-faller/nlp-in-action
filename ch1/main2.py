import re
r = r'''[^a-z]*([y]o|[h']?ello|ok|hey|(good[ ])?(morn[gin']{0,3}|afternoon|even[gin']{0,3}))[\s,;:]{1,3}([a-z]{1,20})'''
re_greeting = re.compile(r, flags=re.IGNORECASE)
print(re_greeting.match('Hello Rosa'))
print(re_greeting.match('Hello Rosa').groups())
print(re_greeting.match("Good morning Rosa"))
print(re_greeting.match("Good Manning Rosa"))
print(re_greeting.match('Good evening Rosa Parks').groups())
print(re_greeting.match("Good Morn'n Rosa"))
print(re_greeting.match("yo Rosa"))
print(re_greeting.match('Good evening Rosa Parks').groups())