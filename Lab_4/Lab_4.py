Str = input("Input two words divided by space")
print("Inputed String is : ", Str, " Length:", len(Str))
flag, word1, word2 = 0, '', ''
for i in Str:
    if i == ' ':
        flag = 1
    if flag == 0:
        word1 += i
    else:
        word2 += i
l1 = word2[2]
l2 = word1[1]
word1 = word1[:1] + l1 + word1[2:]
word2 = word2[1:2] + l2 + word2[3:]
print('Output:', word2, word1, l1, l2)
