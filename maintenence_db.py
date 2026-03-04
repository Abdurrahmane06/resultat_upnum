import os
import django
import pandas as pd
from django.db import models

# 1. CONFIGURATION
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resultats.settings')
django.setup()

from notes.models import NoteS1, NoteS2, NoteS3, NoteS4, NoteS5

def clean_value(val, field_obj):
    """
    Nettoie la valeur en fonction du type de champ Django.
    """
    s_val = str(val).strip().replace(',', '.')
    
    # Si c'est un champ numérique (Float, Decimal, Integer)
    if isinstance(field_obj, (models.FloatField, models.DecimalField, models.IntegerField)):
        try:
            if s_val == '' or s_val.lower() == 'nan':
                return 0.0
            return float(s_val)
        except ValueError:
            return 0.0
            
    # Pour les champs texte (Charfield, TextField)
    else:
        # On enlève le .0 que Pandas ajoute aux entiers (comme les matricules)
        if s_val.endswith('.0'):
            return s_val[:-2]
        return '' if s_val.lower() == 'nan' else s_val

configurations = [
    (NoteS1, 'data/notes_s1.xlsx'),
    (NoteS2, 'data/notes_s2.xlsx'),
    (NoteS3, 'data/notes_s3.xlsx'),
    (NoteS4, 'data/notes_s4.xlsx'),
    (NoteS5, 'data/notes_s5.xlsx'),
]

for modele, chemin in configurations:
    if os.path.exists(chemin):
        print(f"⏳ Traitement de {chemin}...")
        
        # On lit tout en string pour garder le contrôle total
        df = pd.read_excel(chemin, dtype=str).fillna('')
        
        # On crée un dictionnaire des champs du modèle pour connaître leur type
        champs_dict = {f.name: f for f in modele._meta.get_fields() if f.name != 'id'}
        
        objets = []
        for _, row in df.iterrows():
            row_dict = row.to_dict()
            data = {}
            
            for k, v in row_dict.items():
                if k in champs_dict:
                    # On passe l'objet du champ pour savoir si c'est un nombre ou du texte
                    data[k] = clean_value(v, champs_dict[k])
            
            if data:
                objets.append(modele(**data))
        
        # Nettoyage et insertion
        modele.objects.all().delete()
        modele.objects.bulk_create(objets)
        print(f"✅ Import de {modele.__name__} ({len(objets)} lignes) réussi.")
    else:
        print(f"❌ Fichier introuvable : {chemin}")