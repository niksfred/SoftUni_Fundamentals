n = int(input())

word_dic = {}
for i in range(0,n):
    key = input()
    synonim = input()
    if not key in word_dic:
        word_dic[key] = [synonim]
    else:
        word_dic.get(key).append(synonim)
    
for word, value in word_dic.items():
    print(f"{word} - {', '.join(word_dic.get(word))}")
