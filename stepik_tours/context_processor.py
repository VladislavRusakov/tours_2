from random import sample

from .data import tours

def Data(request):
    arr = {'tours':tours}
    return arr


def SixTours(request):
    random_tours_ids = sample([i for i in tours.keys()], 6)

    random_tours = {}
    for i, element in enumerate(random_tours_ids):
        random_tours[i] = tours[element]
    content = {'six_tours':random_tours}

    return content
