import random

slova = ['честь', 'справедливость', 'сдержанность', 'стиль', 'жизнерадостность', 'юмор', 'взгляд', 'преданность',
         'милосердие', 'величие', 'рассвет', 'закат', 'звездопад', 'петрикор', 'тишина', 'улыбка', 'смех', 'крешендо',
         'натюрморт', 'пейзаж', 'портрет', 'вдохновение', 'ноты', 'пианино', 'скрипка', 'легкость', 'нежность']
slovo = slova[random.randrange(5)]
len_slovo = len(slovo)
health = 5
test = False
used_letters = ""
secret_slovo = []
j = 0
for i in range(len(slovo)):
    secret_slovo += '*'
while len_slovo != 0 and health != 0:
    test = False
    while True:
        letter = input("Guess a letter:\n")
        if letter in used_letters or len(letter) > 1:
            print("No more than one letter or your letter already used!")
        else:
            used_letters += letter
            break
    count = 0
    for i in slovo:
        if letter in i:
            len_slovo -= 1
            test = True
            secret_slovo[count] = letter
        count += 1

    if not test:
        health -= 1
        j += 1
        print("Missed, mistake " + str(j) + ' out of 5.')
    else:
        print("Hit!")
        print(''.join(secret_slovo))

if len_slovo == 0:
    print("You won :)", slovo.upper())
else:
    print("You lost :(")
