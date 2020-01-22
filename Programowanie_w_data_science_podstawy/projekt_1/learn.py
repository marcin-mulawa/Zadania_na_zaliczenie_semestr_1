from datetime import datetime
from datetime import  timedelta
import glob
import random
import os.path


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
        print('Data ostatniej powtórki: {}'.format(lines[0]))
        print('ID\t Data następnej powtórki')
        for line in lines[1:]:
            line = line.split(';')
            line[1] = line[1].strip('\n')
            t = datetime.strptime(line[1], '%m/%d/%Y')
            words.append({'key': line[0], 'time': t})
            print('line[0]\t line[1]')
        return words
read_file('kolory.txt')
#read_log()