from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import Notes
from litmus.models import Profile

# View for /homepagedemo/user_id/
def index(request, user_id):
    try:
        # Selecting the latest note
        all_notes = Notes.objects.filter(user_profile = user_id)
        all_notes = list(all_notes)
        #if len(all_notes) == 0:
        #    return redirect('litmus/homepagedemo/errors/400/')
        all_notes.sort(key = lambda x : datetime.strptime(str(x.create_time), '%Y-%m-%d %H:%M:%S.%f%z'), reverse = True)
        latestnote = all_notes[0].diary_notes
        print(latestnote)
    except(KeyError, Notes.DoesNotExist):
        latestnote = 'No notes yet! Go ahead and create your first note !'
        return render(request, 'homepage/homepagedemo.html', 
                     {'latestnote': latestnote,
                      'user_id' : user_id})
    else:
        # Passing selected note tobe displayed on basic HTML page
        return render(request, 'homepage/homepagedemo.html', 
                     {'latestnote': latestnote,
                      'user_id' : user_id})

# View for # /homepagedemo/user_id/addnotes/
def add(request, user_id):
    # Saving newly added notes from the homepage 
    newnote = request.POST.get("newnote")
    print(newnote)
    #if newnote == "":
        #return redirect(errors, error_code = 400)
        #return render(request, 'homepage/homepageerror.html', 
        #            {'error_message' : error_message,})
    #else:
    user_profile = get_object_or_404(Profile, pk = user_id)
    n = Notes()
    n.user_profile = user_profile
    n.diary_notes = newnote
    n.save()
    latestnote = n.diary_notes
    return redirect('/litmus/homepagedemo/' + str(user_id) + '/')

# Error messages
def errors(request, error_code):
    print("Hey here\n\n")
    return render(request, 'homepage/homepageerror.html', 
                 {'error_code' : error_code,})   
  