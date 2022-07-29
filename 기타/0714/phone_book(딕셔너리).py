# key-value 쌍으로 저장
# {key:value, key:value, .....}
menu = {"월요일":"제육", "화요일":"갈비탕", "수요일":"피자", "목요일":"치킨"}
phone_num = {"제육":"123-4567"}

print(menu)
print(menu["월요일"])
menu["월요일"] = "해장국"
print(menu)