def file_size(filename): #количество символов с учётом пробела
   with open(filename) as f:
      return len(f.read())

print(file_size('/Users/kirillpetruska/Documents/python/laboratorna №4/laba4.txt'), ": количество символов с учётом пробела")

file = open("/Users/kirillpetruska/Documents/python/laboratorna №4/laba4.txt", "r+")
countsimbol = 0 #количество символов без учёта пробела
for simbol in file.read():
    if simbol != " ":
        countsimbol = countsimbol + 1
print(countsimbol, ": количество символов без учёта пробела")
file.close()

file = open("/Users/kirillpetruska/Documents/python/laboratorna №4/laba4.txt", "r+")
count = 0 
for word in file.read().split(): #количество слов в тексте 
    count = count + 1
print(count, ": количество слов в тексте")
file.close()

with open("/Users/kirillpetruska/Documents/python/laboratorna №4/laba4.txt", "r") as file: #количество слов что встречаются только 1 раз
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Уникальных слов: {len(uniques)}")
    file.close()

#15 ВАРИАНТ - ЗАДАНИЕ 3
love = ["обійми", "радість", "любов", "щастя", "Полюбила", "поцілунки", "відчуття", "градус", "балкон", "романтика", "пустий", "пляшка", "відносини", "близькість", "рефлексія", "божевілля", "притома", "зусилля", "адекватність", "втрата", "забуття", "нещастя", "серце", "крок", "життя", "секрет", "відвертість", "щирість", "люди", "найпрекрасніше"]
file = open("/Users/kirillpetruska/Documents/python/laboratorna №4/laba4.txt", "r+", encoding="utf-8")
count = 0 #количество появления слов в тексте
for simbol in file.read().split():
    for word in love:
       if simbol == word:
           count = count + 1
print(count, ": количество появления слов которые характеризуют романтический чувства в тексте ")
file.close() 
