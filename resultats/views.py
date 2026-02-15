from django.shortcuts import render
from notes.models import NoteS1

def resultat_s1(request):
    matricule = request.GET.get('matricule')
    result = None
    if matricule:
        try:
            result = NotesS1.objects.get(Matricule=matricule)
        except NotesS1.DoesNotExist:
            result = None
    return render(request, 'resultats/relever_s1.html', {'result': result})