# Произвести над строкой: nu_zdarova_dimas_chto_po_mateshe следующие операции:
# Test : nu_zdarova_dimas_chto_po_mateshe
Str = input('Input some words divided by _\n')
print("Inputed String is : ", Str, " Length:", len(Str))

# 1. удалить первое слово (вместе с подчеркиванием)
i = 0
while Str[i] != '_':
    Str = Str[i] * 0 + Str[i + 1:]
    i + 1
Str = Str[i + 1] * 0 + Str[i + 1:]
#print("Output (cut):", Str, len(Str))
# 2. поменять местами 5 и 2 слово
count = 0
cntin = 0

word1 = '_'
word2 = '_'
word5 = '_'
word34 = '_'
word6 = '_'
# zdarova_dimas_chto_po_mateshe
for j in Str:
    if j == '_':
        count += 1
    # Чекнуть шоб был индекс Элемента cntin = j
    if count == 0:
        word1 += j
    elif count == 1:
        word2 += j
    elif count == 2 or count == 3:
        word34 += j
    elif count == 4:
        word5 += j
    else:
        word6 += j
#print("Output (Swap):", word1, word5, word34, word2, word6)
Str = word1[1:] + word5[1:] + word34[1:] + word2[1:] + word6[1:]
#print("Output (SwapStr):", Str)
# 3. удалить символ с индексом 2
Str = Str[:2] + Str[3:]
#print("Output (rev):", Str)
# 4. инверсию последнего слова
#for j in Str:
#    if j == '_':
#        count -= 1
#       # print("count:", count)
#    if count != 0:
#        cntin += 1
#print("cntin:", cntin)
#StrInv = Str[cntin::-1]
#print("Output (StrInv):", StrInv)
Srt = Str[:cntin] + Str[cntin::-1]
#print("Output (Inv):", Srt)
# 5. заменить все буквы "о" на "а"
# Str = Str.replace('о', 'а')
# print("Output (switch):", Str)
# Final
print("Output :", Str)
