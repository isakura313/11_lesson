import re

to_test = ["example@incom.com",
"gnom@!mail.ru",
"example@privet",
"alsdjaslkdjalksdjkl@",
"@asdasdasd.com",
"brandу@yandex.ru",
"8919654182@com.com",
"sdsda@gmail.c"]

for name in to_test:
    if(re.match(r"[a-z0-9]{2,}@[a-z0-9]{2,}\.[a-z]{2,}", name)):
        print("это почта", name)
