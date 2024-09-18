from django.shortcuts import render, get_object_or_404, redirect
from .models import NightClub


# List all nightclubs
def club_list(request):
    clubs = NightClub.objects.all()
    return render(request, 'nightclubs/club_list.html', {'clubs': clubs})


# View nightclub details
def club_detail(request, nightclubID):
    club = get_object_or_404(NightClub, nightclubID=nightclubID)
    return render(request, 'nightclubs/club_detail.html', {'club': club})


# Create a new nightclub
def create_club(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        ageReq = request.POST['ageReq']
        categories = request.POST['categories']
        dressCode = request.POST['dressCode']
        daysActive = request.POST['daysActive']

        # Create a new nightclub
        NightClub.createNightclub(
            name=name,
            address=address,
            ageReq=ageReq,
            categories=categories,
            dressCode=dressCode,
            daysActive=daysActive
        )
        return redirect('club_list')
    return render(request, 'nightclubs/create_club.html')


# Update nightclub hours
def update_club_hours(request, nightclubID):
    club = get_object_or_404(NightClub, nightclubID=nightclubID)
    if request.method == 'POST':
        new_hours = request.POST['hours']
        club.updateHours(new_hours)
        return redirect('club_detail', nightclubID=club.nightclubID)
    return render(request, 'nightclubs/update_hours.html', {'club': club})


# Delete a nightclub
def delete_club(request, nightclubID):
    club = get_object_or_404(NightClub, nightclubID=nightclubID)
    if request.method == 'POST':
        club.deleteNightclub()
        return redirect('club_list')
    return render(request, 'nightclubs/delete_club.html', {'club': club})
