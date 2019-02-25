"""
Modeling of service requests at a gas station.
Grigorev A., Batenev P., Zhambaeva D.
"""

import rulocal as ru
import random

def azs_read():
    """ Read azs.txt and return list of dict-s with automats. """
    # Должна возвращать список словарей такого плана: [{'max_tern': , 'marks': , 'tern': }, {'max_tern': , ....}.. ]
    lst = {}
    with open('azs.txt', 'r') as f_in:
        text = f_in.readlines()
        text = [line.strip() for line in text]
        for i in range(len(text)):
            lst_1 = {}
            line = text[i]
            line = line.split()
            [lst_1['max_tern']] = line[1]
            lst_2 = []
            for j in range(2, len(line)):
                h = line[j]
                lst_2.append(h)
            lst_1.update({'marks': lst_2})
            lst[line[0]] = lst_1
    return lst


def oder_read():
    """ Read input.txt and return list of dict-s with clients. """
    lst_clients = []
    with open('input.txt') as f:
        clients = f.readlines()
        for line in clients:
            str = line.split()
            d = {}
            d['time'] = str[0]
            d['liters'] = int(str[1])
            d['mark'] = str[2]
            lst_clients.append(d)
    return lst_clients


def duration():
    """ How long will the car refuel. """
    litr = int(input())
    time = litr // 10
    if litr % 10 == 0:
        time = litr // 10
        print(time)
    else:
        time = litr // 10 + 1
        print(time)
    number = random.randint(-1, 1)
    t = time + number
    return t


def min_hour(minutes):
    """ Minutes to hours. """
    hours = (minutes % 1440) // 60
    mins = (minutes % 1440) % 60
    time = "%s:%s" % (str(hours).zfill(2), str(mins).zfill(2))
    return time


def time_leaving(hours, duration):
    """ Hours to minutes and returns information about leaving. """
    r = int(duration())
    hour = int(hours[0:2])
    minut = int(hours[3:6])
    minutes = hour * 60 + minut + r
    return min_hour(minutes)


def azs_print(list_azs):
    """ Prints information about each automat. """


def azs_choice(list_azs, ben):
    """ Choice automat and return it's number """
    # Получает на вход list_azs, марку бензина и, в зависимсти от марки безина и очерди, возвращает номер автомата, куда встант машина.
    queue = {1: 0, 2: 0, 3: 0}

    # это для примера, в таком формате подаются переменные на вход
    '''list_azs = [{'max_tern': 3, 'mark': 'АИ-80', 'tern': 1},
                {'max_tern': 2, 'mark': 'АИ-92', 'tern': 2},
                {'max_tern': 4, 'mark': ['АИ-92', 'АИ-95', 'АИ-98'], 'tern': 3}]
    ben = 'АИ-92' '''

    for i in list_azs:
        t = i['tern']
        if i['mark'] == ben and i['max_tern'] >= queue[t]:
            queue[t] += 1
            return i['tern']
        if i['mark'] == ['АИ-92', 'АИ-95', 'АИ-98']:
            lst = ['АИ-92', 'АИ-95', 'АИ-98']
            for j in lst:
                if j == ben and i['max_tern'] >= queue[t]:
                    queue[t] += 1
                    return i['tern']
    # Стоит учесть, что если свободных мест не будет, то функция возвратит None.
    # Ну или можно прописать через else, что нужно возвратить в таком случае


def main():
    """ Main function. """
    orders = oder_read()
    azs = azs_read()
    dict_leaves = {}
    count = 0
    min_before = 0

    for minutes in range(1440):

        time = min_hour(minutes)
        time_dur = duration()
        # while time != list_orders[0]['time'] and count != len(list_orders):

        # отслежка прибытия (с учётом одновременного)
        if time == orders[count]['time']:
            print(ru.NEW_CLIENT.format(time, orders[count]['mark'],
                                       orders[count]['liters'],
                                       time_dur, azs_choice(azs)))
            min_before += 1
            count += 1
        elif min_hour(min_before) == orders[count]['time']:
            print(ru.NEW_CLIENT.format(min_hour(min_before),
                                       orders[count]['mark'],
                                       orders[count]['liters'],
                                       time_dur, azs_choice(azs)))
            count += 1
        else:
            min_before += 1


        azs_print(azs)

        if time in dict_leaves:
            azs_print(azs)

        print(ru.CLIENT_LEAVE.format(time_leaving()))
    print(orders)

if __name__ == '__main__':
    main()
