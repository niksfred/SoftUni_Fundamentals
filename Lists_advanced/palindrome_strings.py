word_list = input().split()
searched_palindrome = input()

palindrome_list = []
for word in word_list:
    if word == "".join(reversed(word)):
        palindrome_list.append(word)

count = palindrome_list.count(searched_palindrome)

print(palindrome_list)
print(f"Found palindrome {count} times")
