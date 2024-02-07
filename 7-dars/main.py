import generators

for i in generators.password_generator(int(input("Nechta password generate qilmoqchisiz? "))):
    print(i)

# Bundan pastdagi generatorlarda qaysi sonni kiritilsa shu "songacha" bo'lganlarni qaytaradi
# Bu narsa masala shartiga muvofiq, xatolik tarzida hisoblamaysiz degan umiddaman)
for i in generators.even_generator(int(input("Qaysi songacha bo'lgan juft sonlarni ko'rmoqchisiz? "))):
    print(i)

for i in generators.odd_generator(int(input("Qaysi songacha bo'lgan toq sonlarni ko'rmoqchisiz? "))):
    print(i)

for i in generators.prime_generator(int(input("Qaysi songacha bo'lgan tub sonlarni ko'rmoqchisiz? "))):
    print(i)

