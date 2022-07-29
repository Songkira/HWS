
# open('파일이름', '모드', encoding='utf8')
# file = open('test.txt', 'w', encoding='utf8')
# file.write('첫번째 관통 프로젝트\n두번째 줄이요!!')

file = open('test.txt', 'r', encoding='utf8')
data = file.read()
print(data)