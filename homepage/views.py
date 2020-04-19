from django.shortcuts import render, get_object_or_404
from .models import Notes

# View for /homepagedemo/
def index(request):
    try:
        # Selecting the latest note
        latestnote = Notes.objects.latest('create_time')
    except(KeyError, Notes.DoesNotExist):
        latestnote = "No notes yet! Go a head and compose your first note!"
        return render(request, 'homepage/homepagedemo.html', {'latestnote': latestnote})
    else:
        # Passing selected note to bedisplayed on basic HTML page
        return render(request, 'homepage/homepagedemo.html', {'latestnote': latestnote})

# View for # /homepagedemo/addnotes/
def add(request):
    # Saving newly added notes from the homepage 
    newnote = request.POST.get("newnote")
    n = Notes(diary_notes = newnote)
    n.save()
    return render(request, 'homepage/homepagedemo.html', {'latestnote': n})    