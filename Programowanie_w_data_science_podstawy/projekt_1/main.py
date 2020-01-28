# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
import glob
import random
import os.path
import sys


def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        words = []
        for line in lines:
            line = line.split(';')
            line[2] = line[2].strip('\n')
            t = datetime.strptime(line[2], '%Y-%m-%d').date()
            words.append({'key': line[0], 'value': line[1], 'time': t})
        return words


def read_log():
    with open('log.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        words = []
        first = lines[0].split(';')
        file = first[1].strip('\n')
        print('Data ostatniej powtórki: {}'.format(first[0]))
        print('Plik, z którego ostatnio się uczyłeś: {}'.format(file))
        print('ID\t Data następnej powtórki')
        for line in lines[1:]:
            line = line.split(';')
            line[1] = line[1].strip('\n')
            t = datetime.strptime(line[1], '%Y-%m-%d').date()
            words.append({'key': line[0], 'time': t})
            print('{}\t {}'.format(line[0], line[1]))
        return file,words


def edit_log(words,file):
    with open('log.txt', 'w', encoding='utf-8') as f:
        t = datetime.now()
        t = t.strftime("%Y-%m-%d")
        f.write("{};{}\n".format(t, file))
        for word in words:
            f.write("{};{}\n".format(word['key'], word['time']))
        

def edit_file(file):
    with open(file, 'a', encoding='utf-8') as f:
        add_to_file(f)


def create_file(file):
    if not os.path.exists(file):
        decision = 't'
    else:
        decision = input("Plik istnieje, kontynuować? [t/n]")
    if decision == 't':
        with open(file, 'w', encoding='utf-8') as f:
            add_to_file(f)


def new_words(number):
    words = []
    for i in range(number):
        key = input("Pddaj klucz: ")
        value = input("Podaj wartość: ")
        t = datetime.now()
        t = t.strftime("%Y-%m-%d")
        words.append({'key': key, 'value': value, 'time': t})
    return words


def add_to_file(f, words=None):
    if words is None:
        while True:
            try:
                number = int(input('Podal liczbę słów, które chcesz utworzyć: '))
                break
            except:
                print('Nieprawidłowa liczba')
        words = new_words(number)
    for word in words:
        f.write("{};{};{}\n".format(word['key'], word['value'], word['time']))


def choose_file():
    files = []
    for i, el in enumerate(glob.glob('./*.txt')):
        files.append((i, el.strip('.\\')))
    for i, el in files:
        print('{}. {}'.format(i + 1, el))
    while True:
        num_file = int(input("Wybór (wpisz liczbę): "))
        try:
            file = files[num_file - 1][1]
            return file
        except:
            print("Błedny wybór")



def learning(file, every=False, log=[]):
    t = input('Czy chcesz uczyć się ze szystkich słów znajdujących się w pliku {}, jeśli nie to nauka odbędzie się tylko ze słów, których powtórki należy dokonać [t/n]?'.format(file))
    if t=='t':
        every=True
    words = read_file(file)
    random.shuffle(words)
    for word in words:
        if word['time'] - datetime.now().date() <= timedelta(days=0) or every == True or\
                 word['key'] in [el['key'] for el in log if el['time'] - datetime.now().date() <= timedelta(days=0)]:
            print(word['key'])
            good = word['value']
            ans = input("Wpisz wartośc: ")
            t = datetime.now()
            t = t.strftime("%Y-%m-%d")
            word['time'] = t
            if good == ans:
                print("Dobra odpowiedź")
                tnext = datetime.now() + timedelta(days=7)
                tnext = tnext.strftime("%Y-%m-%d")
                word['time'] = tnext 
            else:
                print('Zła odpowiedź')
                word['time'] = datetime.now().date()
    edit_log(words, file)
    with open(file, 'w', encoding='utf-8') as f:
        add_to_file(f, words)

def menu():
    print("Witaj w programie do nauki słówek!!!\n"
          "Właśnie rozpocząłeś nowwą sesje nauki.\n"
          "Powiedz mi co chcszesz dzisiaj zrobić:\n"
          "1. Stworzyć nowy plik ze słowami do nauki.\n"
          "2. Dolączyć nowe słowa do pliku.\n"
          "3. Uczyć się z istniejącego już pliku.\n"
          "4. Wczytać stan z poprzedniej sesji.\n"
          "5. Wyjdź z programu")
    while True:
        try:
            decision = int(input("Wybór (wpisz liczbę): "))
            return decision
        except:
            print("Podaj liczbę!")


def main_loop():
    while True:
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
            print('wybrano 2')
            learning(file)
        elif decision == 4:
            file, log = read_log()
            learning(file, False, log)
        elif decision == 5:
            sys.exit()


main_loop()
