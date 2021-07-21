"""Панграмма - это предложение, которое содержит каждую букву алфавита по крайней мере один раз.
Например, предложение "The quick brown fox jumps over the lazy dog" является панграммой, потому что оно использует буквы A-Z по крайней мере один раз
(случай не имеет значения).

Учитывая строку, определите, является ли она панграммой или нет. Верните True, если это так, False, если нет. Игнорируйте цифры и знаки препинания."""


 string

def is_pangram(s):
    a=string.ascii_uppercase
    counter=0
    for val in a:
        if val in s:
            counter +=1
            continue
    if counter == len(a.split()):
        return True
    else:
        return False
