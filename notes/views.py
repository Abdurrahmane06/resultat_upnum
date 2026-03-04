from django.shortcuts import render, get_object_or_404
# IMPORTANT : On importe TOUS les modèles nécessaires
from .models import NoteS1, NoteS2, NoteS3, NoteS4, NoteS5

def index(request):
    return render(request, 'notes/index.html')

# Cette fonction gère le dictionnaire des modèles pour éviter les "if/elif" à répétition
def get_model_by_semester(semestre):
    mapping = {
        '1': NoteS1,
        '2': NoteS2,
        '3': NoteS3,
        '4': NoteS4,
        '5': NoteS5,
    }
    return mapping.get(str(semestre))

def consulter_resultats(request):
    if request.method == 'POST':
        matricule = request.POST.get('matricule')
        semestre = request.POST.get('semestre')

        model = get_model_by_semester(semestre)
        
        if model:
            # On cherche l'étudiant
            resultat = model.objects.filter(Matricule=matricule).first()
            
            if resultat:
                # On renvoie vers le bon template
                template_name = f'notes/relever_s{semestre}.html'
                return render(request, template_name, {'note': resultat})
            else:
                return render(request, 'notes/index.html', {
                    'error': f"Matricule {matricule} introuvable pour le semestre {semestre}."
                })
        
    return render(request, 'notes/index.html')

# AJOUT DE CETTE FONCTION : C'est elle qui manque à tes URLs !
def releve_generique(request, semestre, matricule):
    # Nettoyage du paramètre semestre (ex: transformer 's5' en '5')
    s_num = semestre.lower().replace('s', '')
    
    model = get_model_by_semester(s_num)
    
    if not model:
        return render(request, '404.html', status=404)

    note = get_object_or_404(model, Matricule=matricule)
    return render(request, f'notes/relever_s{s_num}.html', {'note': note})
    
    
# import pandas as pd
# import os
# from django.shortcuts import render
# from django.conf import settings

# # 1. Vue pour la page d'accueil (Recherche)
# def index(request):
#     """Affiche la page de recherche initiale."""
#     return render(request, 'notes/index.html')

# # 2. Vue pour traiter la recherche et afficher les résultats
# def consulter_resultats(request):
#     """Lit le fichier Excel correspondant au semestre et cherche le matricule."""
#     if request.method == 'POST':
#         matricule = request.POST.get('matricule')
#         semestre = request.POST.get('semestre')  # Doit être '3' ou '4'

#         # Définir le chemin du fichier Excel selon le semestre choisi
#         # Exemple: projet_notes/data/S3_results.xlsx
#         file_name = f"notes_s{semestre}.xlsx"
#         file_path = os.path.join(settings.BASE_DIR, 'data', file_name)

#         # Vérifier si le dossier 'data' et le fichier existent
#         if not os.path.exists(file_path):
#             return render(request, 'notes/index.html', {
#                 'error': f"Le fichier de données pour le semestre {semestre} est introuvable."
#             })

#         try:
#             # Lire le fichier Excel avec pandas
#             df = pd.read_excel(file_path)

#             # Filtrer par matricule (conversion en string pour éviter les erreurs de type)
#             # Assurez-vous que la colonne dans Excel s'appelle exactement 'matricule'
#             resultat = df[df['Matricule'].astype(str) == str(matricule)]

#             if not resultat.empty:
#                 # Transformer la ligne trouvée en dictionnaire pour le template
#                 note_dict = resultat.iloc[0].to_dict()
                
#                 # Choisir le template correspondant au semestre
#                 template_name = f'notes/relever_s{semestre}.html'
                
#                 return render(request, template_name, {'note': note_dict})
#             else:
#                 return render(request, 'notes/index.html', {
#                     'error': f"Aucun résultat trouvé pour le matricule {matricule} au semestre {semestre}."
#                 })

#         except Exception as e:
#             return render(request, 'notes/index.html', {
#                 'error': f"Erreur lors de la lecture du fichier Excel : {e}"
#             })

#     # Si accès direct via l'URL sans POST, redirection vers l'index
#     return render(request, 'notes/index.html')









# from django.shortcuts import render, redirect
# from .models import NoteS1, NoteS2, NoteS3, NoteS4  # Assure-toi que c'est bien NoteS1 sans "s"

# def index(request):
#     if request.method == 'POST':
#         matricule = request.POST.get('matricule')
#         semestre = request.POST.get('semestre')
        
#         if matricule and semestre:
#             request.session['matricule'] = matricule
#             # view_name deviendra 'releve_s1', 'releve_s2', etc.
#             view_name = f'releve_s{semestre}'
#             return redirect(view_name)
#         else:
#             return render(request, 'notes/index.html', {'error': 'Veuillez remplir tous les champs.'})
    
#     return render(request, 'notes/index.html')

# # --- C'est cette partie qu'il te manque probablement ---

# def releve_s1(request):
#     matricule = request.session.get('matricule')
#     if not matricule:
#         return redirect('index')
#     try:
#         data = NoteS1.objects.get(matricule=matricule)
#         return render(request, 'notes/relever_s1.html', {'note': data})
#     except NoteS1.DoesNotExist:
#         # Message d'erreur si le matricule n'existe pas dans la base
#         return render(request, 'notes/index.html', {'error': 'Matricule introuvable.'})

# # Pour éviter les crashs si tu testes les autres semestres :
# def releve_s2(request):
#     matricule = request.session.get('matricule')
#     if not matricule:
#         return redirect('index')
#     try:
#         data = NoteS2.objects.get(matricule=matricule)
#         return render(request, 'notes/relever_s2.html', {'note': data})
#     except NoteS2.DoesNotExist:
#         return render(request, 'notes/index.html', {'error': "Cet étudiant n'est pas inscrit à ce semestre"})

# def releve_s3(request):
#     matricule = request.session.get('matricule')
#     if not matricule:
#         return redirect('index')
#     try:
#         data = NoteS3.objects.get(matricule=matricule)
#         return render(request, 'notes/relever_s3.html', {'note': data})
#     except NoteS3.DoesNotExist:
#         return render(request, 'notes/index.html', {'error': "Cet étudiant n'est pas inscrit au S3"})


# def releve_s4(request):
#     matricule = request.session.get('matricule')
#     if not matricule:
#         return redirect('index')
#     try:
#         data = NoteS4.objects.get(matricule=matricule)
#         return render(request, 'notes/relever_s4.html', {'note': data})
#     except NoteS4.DoesNotExist:
#         return render(request, 'notes/index.html', {'error': "Données S4 introuvables"})
