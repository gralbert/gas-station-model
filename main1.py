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
    time = litr // 10
    if litr % 10 == 0:
        number = random.randint(-1, 1)
        time = litr // 10
        return time
    else:
        number = random.randint(-1, 1)
        time = litr // 10 + 1
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
    for i in list_azs:
        if ben in i['mark'] and i['max_tern'] >= i['tern']:
            i['tern'] += 1
            return i['num']


def main():
    """ Main function. """
    orders = oder_read()
    azs = azs_read()
    dict_leaves = {}
    count = 0
    min_before = 0
    go_out = 0

    for minutes in range(1440):

        time = min_hour(minutes)
        # while time != list_orders[0]['time'] and count != len(list_orders):

        # отслежка прибытия (с учётом одновременного)

        time_dur = duration(orders[count]['liters'])
        #print(orders[count]['liters'])
        #print(orders[count]['mark'])
        num_automat = azs_choice(azs, orders[count]['mark'])
        if time == orders[count]['time'] and not(num_automat is None):


            print(ru.NEW_CLIENT.format(time, orders[count]['mark'],
                                       orders[count]['liters'],
                                       time_dur,
                                       num_automat))

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

            azs[num_automat - 1]['tern'] += 1
            azs_print(azs)

            count += 1

        elif not(num_automat is None):
            min_before += 1
        else:
            go_out +=1



        #if time in dict_leaves:
            #azs_print(azs)

        #print(ru.CLIENT_LEAVE.format(time_leaving()))
    #print(orders)

if __name__ == '__main__':
    main()
