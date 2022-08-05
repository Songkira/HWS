logs = ["dig1 8 1 51","let1 art can","dig2 3 6","let2 own kit dig", "let3 art zero"]

digits=[]
letters=[]
for log in logs:
    if log.split()[1].isalpha():
        letters.append(log)
    else:
        digits.append(log)

letters.sort(key=lambda x:(x.split()[1:], x.split()[0]))
print(letters + digits)
