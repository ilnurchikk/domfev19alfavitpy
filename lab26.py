print("Это приложение позволяет познакомится с русским алфавитом .")
for i in range(ord('а'), ord('я')+1):
        print(chr(i), end='. ')

start = input("\n Если хотите работать с приложение алфавит нажмите:start \n если хотите выйти наберите несколько букв:")
if start =="start":
        while True:
            try:
                a = input(('\n Введите букву: '))
                if a == "а":
                    print('аист')
                elif a == "б":
                    print('баран')
                elif a == "в":
                    print('ворона')
                elif a == "г":
                    print('гиена')
                elif a == "д":
                    print('дом')
                elif a == "е":
                    print('ель')
                elif a == "ё":
                    print('ёж')
                elif a == "ж":
                    print('жук')
                elif a == "з":
                    print('зонт')
                elif a == "и":
                    print('икра')
                elif a == "й":
                    print('йогурт')
                elif a == "к":
                    print('конь')
                elif a == "л":
                    print('лошадь')
                elif a == "м":
                    print('молоко')
                elif a == "н":
                    print('носорог')
                elif a == "о":
                    print('олень')
                elif a == "п":
                    print('питон')
                elif a == "р":
                    print('река')
                elif a == "с":
                    print('сорока')
                elif a == "л":
                    print('лошадь')
                elif a == "м":
                    print('молоко')
                elif a == "н":
                    print('носорог')
                elif a == "о":
                    print('олень')
                elif a == "п":
                    print('питон')
                elif a == "р":
                    print('река')
                elif a == "с":
                    print('сорока')
                elif a == "т":
                    print('тетрадь')
                elif a == "у":
                    print('утка')
                elif a == "ф":
                    print('филин')
                elif a == "х":
                    print('хлеб')
                elif a == "ц":
                    print('цапля')
                elif a == "ч":
                    print('черепаха')
                elif a == "ш":
                    print('шоколад')
                elif a == "щ":
                    print('щука')
                elif a == "х":
                    print('хлеб')
                elif a == "ъ":
                    print('с ъ есть')
                elif a == "ы":
                    print('рыс ь ')
                elif a == "ь":
                    print('мол ь ')
                elif a == "э":
                    print('экватор')
                elif a == "ю":
                    print('юла')
                elif a == "я":
                    print('яблоко')
                else:
                    print("выход")
                    break
            except ValueError:
                print("вы должны ввести буквы")
