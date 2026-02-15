from django.shortcuts import render, redirect
from .models import NoteS1, NoteS2, NoteS3, NoteS4  # Assure-toi que c'est bien NoteS1 sans "s"

def index(request):
    if request.method == 'POST':
        matricule = request.POST.get('matricule')
        semestre = request.POST.get('semestre')
        
        if matricule and semestre:
            request.session['matricule'] = matricule
            # view_name deviendra 'releve_s1', 'releve_s2', etc.
            view_name = f'releve_s{semestre}'
            return redirect(view_name)
        else:
            return render(request, 'notes/index.html', {'error': 'Veuillez remplir tous les champs.'})
    
    return render(request, 'notes/index.html')

# --- C'est cette partie qu'il te manque probablement ---

def releve_s1(request):
    matricule = request.session.get('matricule')
    if not matricule:
        return redirect('index')
    try:
        data = NoteS1.objects.get(matricule=matricule)
        return render(request, 'notes/relever_s1.html', {'note': data})
    except NoteS1.DoesNotExist:
        # Message d'erreur si le matricule n'existe pas dans la base
        return render(request, 'notes/index.html', {'error': 'Matricule introuvable.'})

# Pour éviter les crashs si tu testes les autres semestres :
def releve_s2(request):
    matricule = request.session.get('matricule')
    if not matricule:
        return redirect('index')
    try:
        data = NoteS2.objects.get(matricule=matricule)
        return render(request, 'notes/relever_s2.html', {'note': data})
    except NoteS2.DoesNotExist:
        return render(request, 'notes/index.html', {'error': "Cet étudiant n'est pas inscrit à ce semestre"})

def releve_s3(request):
    matricule = request.session.get('matricule')
    if not matricule:
        return redirect('index')
    try:
        data = NoteS3.objects.get(matricule=matricule)
        return render(request, 'notes/relever_s3.html', {'note': data})
    except NoteS3.DoesNotExist:
        return render(request, 'notes/index.html', {'error': "Cet étudiant n'est pas inscrit au S3"})


def releve_s4(request):
    matricule = request.session.get('matricule')
    if not matricule:
        return redirect('index')
    try:
        data = NoteS4.objects.get(matricule=matricule)
        return render(request, 'notes/relever_s4.html', {'note': data})
    except NoteS4.DoesNotExist:
        return render(request, 'notes/index.html', {'error': "Données S4 introuvables"})
