"""
Modeling of service requests at a gas station.
Grigorev A., Batenev P., Zhambaeva D.
"""

import rulocal as ru
import random


def azs_read():
    """ Read azs.txt and return list of dict-s with automats. """
    lst_azs = []
    with open('azs.txt', 'r') as f_in:
        azs = f_in.readlines()
        for line in azs:
            lst = line.split()
            dic = {}
            dic['num'] = int(lst[0])
            dic['max_tern'] = int(lst[1])
            dic['mark'] = set()
            for num in range(2, len(lst)):
                dic['mark'].add(lst[num])
            dic['tern'] = 0
            lst_azs.append(dic)
    return lst_azs


def marks_read():
    """ Form dict of marks. """
    lst_marks = {}
    with open('azs.txt', 'r') as f_in:
        azs = f_in.readlines()
        for line in azs:
            lst = line.split()
            for num in range(2, len(lst)):
                lst_marks[lst[num]] = 0
    return lst_marks


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


def duration(litr):
    """ How long will the car refuel. """
    if litr % 10 == 0:
        number = random.randint(-1, 1)
        time = litr // 10 + number
        if time == 0:
            time = 1
        return time
    else:
        number = random.randint(-1, 1)
        time = litr // 10 + 1 + number
        if time == 0:
            time = 1
        return time


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
    for automat in list_azs:
        print(ru.AZS_INF.format(automat['num'],
                                automat['max_tern'],
                                automat['mark'],
                                automat['tern']*'*'))


def azs_choice(list_azs, ben):
    """ Choice automat and return it's number """
    min_tern = float('inf')
    for i in list_azs:
        if ben in i['mark'] and i['max_tern'] > i['tern']:
            min_tern = min(min_tern, i['tern'])

    for i in list_azs:
        if ben in i['mark'] and i['tern'] == min_tern and i['max_tern'] > i['tern']:
            return i['num']


def main():
    """ Main function. """
    orders = oder_read()
    orders2 = oder_read()
    azs = azs_read()
    count = 0
    min_before = 0
    go_out = 0
    deportations = [i for i in range(1440)]
    marks = marks_read()
    price = {'АИ-80': 39.2, 'АИ-92': 41, 'АИ-95': 43.9, 'АИ-98': 44.8}

    for minutes in range(1440):
        time = min_hour(minutes)
        time_dur = duration(orders[count]['liters'])

        num_automat = azs_choice(azs, orders[count]['mark'])
        if time == orders[count]['time'] and not(num_automat is None):

            print(ru.NEW_CLIENT.format(time, orders[count]['mark'],
                                       orders[count]['liters'],
                                       time_dur,
                                       num_automat))
            marks[orders[count]['mark']] += orders[count]['liters']

            orders2[count]['num_azs'] = num_automat
            orders2[count]['dur'] = time_dur
            deportations[minutes + time_dur] = orders2[count]

            azs[num_automat-1]['tern'] += 1
            azs_print(azs)

            min_before += 1
            count += 1

        elif min_hour(min_before) == orders[count]['time'] and not(num_automat is None):

            print(ru.NEW_CLIENT.format(min_hour(min_before),
                                       orders[count]['mark'],
                                       orders[count]['liters'],
                                       time_dur,
                                       num_automat))
            marks[orders[count]['mark']] += orders[count]['liters']

            orders2[count]['num_azs'] = num_automat
            orders2[count]['dur'] = time_dur
            deportations[minutes + time_dur] = orders2[count]

            azs[num_automat - 1]['tern'] += 1
            azs_print(azs)

            count += 1
        elif num_automat is None:
            go_out += 1
            print(ru.CLIENT_GO_OUT.format(time, orders[count]['mark'],
                                          orders[count]['liters'],
                                          time_dur))
        else:
            min_before += 1

        if type(deportations[minutes]) is not int and time == min_hour(minutes):

            dep_mark = deportations[minutes]['mark']
            dep_litres = deportations[minutes]['liters']
            dep_dur = deportations[minutes]['dur']
            no_dep_time = deportations[minutes]['time']

            print(ru.CLIENT_LEAVE.format(time, no_dep_time,
                                         dep_mark,
                                         dep_litres,
                                         dep_dur))

            for i in azs:
                if i['num'] == deportations[minutes]['num_azs']:
                    i['tern'] -= 1

            azs_print(azs)

    print('')
    print(ru.LITERS)
    print(str(marks).replace('{','').replace('}','').replace('\'',''))
    _sum = 0
    for key in marks:
        _sum += marks[key]*price[key]
    print(ru.SUM_RESULT, _sum)
    print(ru.GO_OUT_RESULT, go_out)


if __name__ == '__main__':
    main()
