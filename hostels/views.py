from django.shortcuts import render, get_object_or_404
from .models import Hostel

def landing(request):
    return render(request, 'landing.html')

def search_results(request):
    city = request.GET.get('city', '')
    checkin = request.GET.get('checkin', '')
    checkout = request.GET.get('checkout', '')
    guests = request.GET.get('guests', '')

    hostels = Hostel.objects.filter(city__icontains=city) if city else []

    context = {
        'hostels': hostels,
        'city': city,
        'checkin': checkin,
        'checkout': checkout,
        'guests': guests,
    }
    return render(request, 'results.html', context)

def hostel_detail(request, hostel_id):
    hostel = get_object_or_404(Hostel, pk=hostel_id)
    return render(request, 'hostel_detail.html', {'hostel': hostel})
