from django.shortcuts import render


def main_view(request):
    return render(request, 'index.html')


def departure_view(request, departure):
    return render(request, 'departure.html')


def tour_view(request, id):
    return render(request, 'tours.html')


def not_found_handler(request, exception):
    return render(request, '404.html')


