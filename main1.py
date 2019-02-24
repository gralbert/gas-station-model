"""
Modeling of service requests at a gas station.
Grigorev A., Batenev P., Zhambaeva D.
"""

import rulocal as ru


def azs_read():
    """ Read azs.txt and return list of dict-s with automats. """
    # TODO
    # Должна возвращать список словарей такого плана: [{'max_tern': , 'marks': , 'tern': }, {'max_tern': , ....}.. ]


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
    # TODO
    # Уже готова


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
    # TODO


def azs_choice(list_azs):
    """ Choice automat and return it's number """
    # TODO
    # Получает на вход list_azs и, в зависимсти от марки безина и очерди, возвращает номер автомата, куда встант машина.


def main():
    """ Main function. """
    list_orders = oder_read()
    list_azs = azs_read()
    dict_leaves = {}

    for minutes in range(1440):

        time = min_hour(minutes)

        if time in list_orders[minutes]:
            print(ru.NEW_CLIENT.format(time, list_orders[minutes][time], azs_choice(list_azs)))
            dict_leaves[str(time_leaving(time))] = time_leaving

        azs_print(list_azs)

        if time in dict_leaves:
            azs_print(list_azs)

        print(ru.CLIENT_LEAVE.format(time_leaving()))
    print(list_orders)


if __name__ == '__main__':
    main()
