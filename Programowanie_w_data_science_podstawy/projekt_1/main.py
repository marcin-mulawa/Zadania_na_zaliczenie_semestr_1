from datetime import datetime
from datetime import timedelta
import glob
import random
import os.path


def read_words_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        words = []
        for line in lines:
            line = line.split(';')
            line[3] = line[3].strip('\n')
            t = datetime.strptime(line[3], '%m/%d/%Y').date()
            words.append({'id':line[0], 'key': line[1], 'value': line[2], 'time': t})
        return words


def choose_file():
    files = []
    for i, el in enumerate(glob.glob('./*.txt')):
        files.append((i, el.strip('.\\')))
    for i, el in files:
        print('{}. {}'.format(i + 1, el))
    num_file = int(input("Wybór (wpisz liczbę): "))
    file = files[num_file - 1][1]
    return file


def learn(words, file):
    for word in words:
        if word['time'] - datetime.now().date() > 7:
            print(word['key'])
            good = word['value']
            ans = input("Wpisz wartośc: ")
            t = datetime.now()
            t = t.strftime("%m/%d/%Y")
            word['time'] = t
            if good == ans:
                print("Dobra odpowiedź")
                word['time'] = timedelta(7)+datetime.now().date()
            else:
                print('Zła odpowiedź')
                word['time'] = datetime.now().date()
    with open(file, 'w') as f:
        add_to_file(f, words)


def menu():
    print("Witaj w programie do nauki słówek!!!\n"
          "Powiedz mi co chcszesz dzisiaj zrobić:\n"
          "3. Uczyć się z istniejącego już pliku.")
    while True:
        try:
            decision = int(input("Wybór (wpisz liczbę): "))
            return decision
        except:
            print("Podaj liczbę!")


def main_loop():
    decision = menu()
    if decision == 1:
        file = input("Podaj nazwę pliku, który chcesz stworzyć") + '.txt'
        create_file(file)
    elif decision == 2:
        print("Wybierz plik do edycji: ")
        file = choose_file()
        edit_file(file)
    elif decision == 3:
        print('Wybierz plik do nauki:')
        file = choose_file()
        learn(file)