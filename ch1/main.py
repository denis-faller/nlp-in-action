import re
r = "(hi|hello|hey)[ ]*([a-z]*)"
print(re.match(r, 'Hello Rosa', flags=re.IGNORECASE))
print(re.match(r, "hi ho, hi ho, it's off to work ...", flags=re.IGNORECASE))
print(re.match(r, "hey, what's up", flags=re.IGNORECASE))