def int_func(word):
    latin_alp = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(latin_alp) else False

words = input('Input wrods with Latin with spaces: ').split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')
