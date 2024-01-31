# 1)


# Masala shartidan berilayotgan parametr str yoki list ekanligini bilmadim
# Shuning uchun 1-funksiya str uchun, 2-funksiya list uchun

def str_in_checker(first:str, second:str) -> bool:
    first = first.split()
    second = second.split()
    for i in first:
        if i not in second:
            return False
    return True

def list_in_checker(first, second) -> bool:
    for i in first:
        if i not in second:
            return False
    return True

print(str_in_checker('salom mening ismim Shomalik', "salom men Farg'ona viloyatida yashayman va mening ismim Shomalik"))
print(str_in_checker('salom mening ismim Shomalik', "salom men Farg'ona viloyatida yashayman va ismim Shomalik"))

print(list_in_checker(['nimadur', 'a'],['a', 'fs', 'nimadur']))
print(list_in_checker(['nimadur', 'a'],['fs', 'nimadur']))

# 2)


def vowel_counter(my_string:str) -> int:
    counter = 0
    for i in my_string:
        if i in 'aeoui':
            counter += 1
    return counter

print(vowel_counter('Hello world!'))


# 3)


# son str yoki int typeda berilishi mumkin 
def zero_counter(argument) -> int:
    counter = 0
    for i in str(argument):
        if i in '0':
            counter += 1 
    return counter

print(zero_counter(1241343412520453004674560459007048567))
print(zero_counter('1241343412520453004674560459007048567'))


# 4)


def vowel_checker(first:str, second:str) -> bool:
    vowels = ''
    if 'a' in second:
        vowels += 'a'
    if 'e' in second:
        vowels += 'e'
    if 'u' in second:
        vowels += 'u'
    if 'i' in second:
        vowels += 'i'
    if 'o' in second:
        vowels += 'o'
    for i in first:
        if i in 'aeoui':
            if i not in vowels:
                return False
    return True

print(vowel_checker('Hello world!', 'There is an example of a string'))
print(vowel_checker('Hello world! u', 'There is an example of a string'))


# 5)


def word_counter(my_string:str) -> int:
    word_counter = 0
    is_word = False
    for i in my_string:
        if i != ' ' and not is_word:
            is_word = True
            word_counter += 1
        elif i == ' ':
            is_word = False
    return word_counter

print(word_counter('  Bu shunchaki misol   so`zlar. Ko`proq joy   tashlangan bo`lsa  ham kod to`g`ri  ishlaydi'))

