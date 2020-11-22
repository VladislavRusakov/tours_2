from random import sample

from stepik_tours.data import tours, departures


def data(request):
    arr = {'tours':tours}

    return arr


def six_tours(request):
    random_tours_ids = sample([i for i in tours.keys()], 6)

    random_tours = {}
    for i, element in enumerate(random_tours_ids):
        random_tours[i] = tours[element]
    content = {'six_tours':random_tours}

    return content


def star_counter(request):

    star_data ={}
    for i in range(1, 17):
        star_data[i] = "★" * int(tours[i]["stars"])
    #  Key - tour_id: value - stars
    star_data = {'star_data':star_data}

    return star_data


def city_cases(request):
    data = {'cases':departures}

    return data