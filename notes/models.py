from django.db import models

class NoteS1(models.Model):
    # Informations Générales
    Dept = models.CharField(max_length=100, null=True, blank=True)
    Matricule = models.CharField(max_length=50, unique=True)
    Prenom = models.CharField(max_length=150, null=True, blank=True)
    Nom = models.CharField(max_length=150, null=True, blank=True)

    # --- UE1 : DPR ---
    NCC_DPR110 = models.FloatField(default=0)
    NSN_DPR110 = models.FloatField(default=0)
    NSR_DPR110 = models.FloatField(default=0)
    Moy_DPR110 = models.FloatField(default=0)
    Capit_DPR110 = models.CharField(default=0)

    NCC_DPR111 = models.FloatField(default=0)
    NSN_DPR111 = models.FloatField(default=0)
    NSR_DPR111 = models.FloatField(default=0)
    Moy_DPR111 = models.FloatField(default=0)
    Capit_DPR111 = models.CharField(default=0)

    NCC_DPR112 = models.FloatField(default=0)
    NSN_DPR112 = models.FloatField(default=0)
    NSR_DPR112 = models.FloatField(default=0)
    Moy_DPR112 = models.FloatField(default=0)
    Capit_DPR112 = models.CharField(default=0)

    MOYENNE_UE1 = models.FloatField(default=0)
    UE1_Valide = models.CharField(max_length=10, null=True, blank=True)

    # --- UE2 : MAI ---
    NCC_MAI110 = models.FloatField(default=0)
    NSN_MAI110 = models.FloatField(default=0)
    NSR_MAI110 = models.FloatField(default=0)
    Moy_MAI110 = models.FloatField(default=0)
    Capit_MAI110 = models.CharField(default=0)

    NCC_MAI111 = models.FloatField(default=0)
    NSN_MAI111 = models.FloatField(default=0)
    NSR_MAI111 = models.FloatField(default=0)
    Moy_MAI111 = models.FloatField(default=0)
    Capit_MAI111 = models.CharField(default=0)

    NCC_MAI112 = models.FloatField(default=0)
    NSN_MAI112 = models.FloatField(default=0)
    NSR_MAI112 = models.FloatField(default=0)
    Moy_MAI112 = models.FloatField(default=0)
    Capit_MAI112 = models.CharField(default=0)

    MOYENNE_UE2 = models.FloatField(default=0)
    UE2_Valide = models.CharField(max_length=10, null=True, blank=True)

    # --- UE3 : DEV ---
    NCC_Dev110 = models.FloatField(default=0)
    NSN_Dev110 = models.FloatField(default=0)
    NSR_Dev110 = models.FloatField(default=0)
    Moy_Dev110 = models.FloatField(default=0)
    Capit_Dev110 = models.CharField(default=0)

    NCC_Dev111 = models.FloatField(default=0)
    NSN_Dev111 = models.FloatField(default=0)
    NSR_Dev111 = models.FloatField(default=0)
    Moy_Dev111 = models.FloatField(default=0)
    Capit_Dev111 = models.CharField(default=0)

    NCC_Dev112 = models.FloatField(default=0)
    NSN_Dev112 = models.FloatField(default=0)
    NSR_Dev112 = models.FloatField(default=0)
    Moy_Dev112 = models.FloatField(default=0)
    Capit_Dev112 = models.CharField(default=0)

    MOYENNE_UE3 = models.FloatField(default=0)
    UE3_Valide = models.CharField(max_length=10, null=True, blank=True)

    # --- UE4 : SYR ---
    NCC_SYR110 = models.FloatField(default=0)
    NSN_SYR110 = models.FloatField(default=0)
    NSR_SYR110 = models.FloatField(default=0)
    Moy_SYR110 = models.FloatField(default=0)
    Capit_SYR110 = models.CharField(default=0)

    NCC_SYR111 = models.FloatField(default=0)
    NSN_SYR111 = models.FloatField(default=0)
    NSR_SYR111 = models.FloatField(default=0)
    Moy_SYR111 = models.FloatField(default=0)
    Capit_SYR111 = models.CharField(default=0)

    MOYENNE_UE4 = models.FloatField(default=0)
    UE4_Valide = models.CharField(max_length=10, null=True, blank=True)

    # --- RÉSULTATS GÉNÉRAUX ---
    Moy_General = models.FloatField(default=0)
    Credit_total = models.FloatField(default=0)
    Decision = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.Matricule} - {self.Nom}"

    class Meta:
        db_table = 'notes_s1'


# --- Modèles pour les autres semestres ---
# Note : Pour S2, S3, etc., tu devras adapter les codes matières (ex: DPR120 au lieu de DPR110)
# si les fichiers Excel changent de structure.


class NoteS2(models.Model):
    Matricule = models.CharField(max_length=50, primary_key=True)
    Prenom = models.CharField(max_length=100, null=True, blank=True)
    Nom = models.CharField(max_length=100, null=True, blank=True)
    Dept = models.CharField(max_length=100, null=True, blank=True)
    
    # UE1 : DPR2
    NCC_DPR210 = models.FloatField(default=0); NSN_DPR210 = models.FloatField(default=0); NSR_DPR210 = models.FloatField(default=0); Moy_DPR210 = models.FloatField(default=0); Capit_PR210 = models.CharField(max_length=10, default='')
    NCC_DPR211 = models.FloatField(default=0); NSN_DPR211 = models.FloatField(default=0); NSR_DPR211 = models.FloatField(default=0); Moy_DPR211 = models.FloatField(default=0); Capit_DPR211 = models.CharField(max_length=10, default='')
    NCC_DPR212 = models.FloatField(default=0); NSN_DPR212 = models.FloatField(default=0); NSR_DPR212 = models.FloatField(default=0); Moy_DPR212 = models.FloatField(default=0); Capit_DPR212 = models.CharField(max_length=10, default='')
    MOYENNE_UE1 = models.FloatField(default=0); UE1_Valide = models.CharField(max_length=10, default='')

    # UE2 : DEV2
    NCC_DEV210 = models.FloatField(default=0); NSN_DEV210 = models.FloatField(default=0); NSR_DEV210 = models.FloatField(default=0); Moy_DEV210 = models.FloatField(default=0); Capit_DEV210 = models.CharField(max_length=10, default='')
    NCC_DEV211 = models.FloatField(default=0); NSN_DEV211 = models.FloatField(default=0); NSR_DEV211 = models.FloatField(default=0); Moy_DEV211 = models.FloatField(default=0); Capit_DEV211 = models.CharField(max_length=10, default='')
    MOYENNE_UE2 = models.FloatField(default=0); UE2_Valide = models.CharField(max_length=10, default='')

    # UE3 : MAI2
    NCC_MAI210 = models.FloatField(default=0); NSN_MAI210 = models.FloatField(default=0); NSR_MAI210 = models.FloatField(default=0); Moy_MAI210 = models.FloatField(default=0); Capit_MAI210 = models.CharField(max_length=10, default='')
    NCC_MAI211 = models.FloatField(default=0); NSN_MAI211 = models.FloatField(default=0); NSR_MAI211 = models.FloatField(default=0); Moy_MAI211 = models.FloatField(default=0); Capit_MAI211 = models.CharField(max_length=10, default='')
    NCC_MAI212 = models.FloatField(default=0); NSN_MAI212 = models.FloatField(default=0); NSR_MAI212 = models.FloatField(default=0); Moy_MAI212 = models.FloatField(default=0); Capit_MAI212 = models.CharField(max_length=10, default='')
    MOYENNE_UE3 = models.FloatField(default=0); UE3_Valide = models.CharField(max_length=10, default='')

    # UE4 : SYR2
    NCC_SYR210 = models.FloatField(default=0); NSN_SYR210 = models.FloatField(default=0); NSR_SYR210 = models.FloatField(default=0); Moy_SYR210 = models.FloatField(default=0); Capit_SYR210 = models.CharField(max_length=10, default='')
    NCC_SYR211 = models.FloatField(default=0); NSN_SYR211 = models.FloatField(default=0); NSR_SYR211 = models.FloatField(default=0); Moy_SYR211 = models.FloatField(default=0); Capit_SYR211 = models.CharField(max_length=10, default='')
    MOYENNE_UE4 = models.FloatField(default=0); UE4_Valide = models.CharField(max_length=10, default='')

    # UE5 : DSI2
    NCC_DSI210 = models.FloatField(default=0); NSN_DSI210 = models.FloatField(default=0); NSR_DSI210 = models.FloatField(default=0); Moy_DSI210 = models.FloatField(default=0); Capit_DSI210 = models.CharField(max_length=10, default='')
    NCC_DSI211 = models.FloatField(default=0); NSN_DSI211 = models.FloatField(default=0); NSR_DSI211 = models.FloatField(default=0); Moy_DSI211 = models.FloatField(default=0); Capit_DSI211 = models.CharField(max_length=10, default='')
    MOYENNE_UE5 = models.FloatField(default=0); UE5_Valide = models.CharField(max_length=10, default='')

    Moy_General = models.FloatField(default=0)
    Credit_total = models.IntegerField(default=0)
    Decision = models.CharField(max_length=50, default='')

    class Meta:
        db_table = 'notes_s2'


class NoteS3(models.Model):
    Matricule = models.CharField(max_length=50, primary_key=True)
    Prenom = models.CharField(max_length=100, null=True, blank=True)
    Nom = models.CharField(max_length=100, null=True, blank=True)
    Dept = models.CharField(max_length=100, null=True, blank=True)
    
    # UE1 : DPR3 (Personnel)
    NCC_DPR210 = models.FloatField(default=0); NSN_DPR210 = models.FloatField(default=0); NSR_DPR210 = models.FloatField(default=0); Moy_DPR210 = models.FloatField(default=0); Capit_PR210 = models.CharField(max_length=10, default='')
    NCC_DPR211 = models.FloatField(default=0); NSN_DPR211 = models.FloatField(default=0); NSR_DPR211 = models.FloatField(default=0); Moy_DPR211 = models.FloatField(default=0); Capit_DPR211 = models.CharField(max_length=10, default='')
    NCC_DPR212 = models.FloatField(default=0); NSN_DPR212 = models.FloatField(default=0); NSR_DPR212 = models.FloatField(default=0); Moy_DPR212 = models.FloatField(default=0); Capit_DPR212 = models.CharField(max_length=10, default='')
    NCC_DPR213 = models.FloatField(default=0); NSN_DPR213 = models.FloatField(default=0); NSR_DPR213 = models.FloatField(default=0); Moy_DPR213 = models.FloatField(default=0); Capit_DPR213 = models.CharField(max_length=10, default='')
    MOYENNE_UE1 = models.FloatField(default=0); UE1_Valide = models.CharField(max_length=10, default='')

    # UE2 : DAS2 (Science des données)
    NCC_DEV210 = models.FloatField(default=0); NSN_DEV210 = models.FloatField(default=0); NSR_DEV210 = models.FloatField(default=0); Moy_DEV210 = models.FloatField(default=0); Capit_DEV210 = models.CharField(max_length=10, default='')
    NCC_DEV211 = models.FloatField(default=0); NSN_DEV211 = models.FloatField(default=0); NSR_DEV211 = models.FloatField(default=0); Moy_DEV211 = models.FloatField(default=0); Capit_DEV211 = models.CharField(max_length=10, default='')
    MOYENNE_UE2 = models.FloatField(default=0); UE2_Valide = models.CharField(max_length=10, default='')

    # UE3 : MAI2 (Programmation avancée)
    NCC_MAI210 = models.FloatField(default=0); NSN_MAI210 = models.FloatField(default=0); NSR_MAI210 = models.FloatField(default=0); Moy_MAI210 = models.FloatField(default=0); Capit_MAI210 = models.CharField(max_length=10, default='')
    NCC_MAI211 = models.FloatField(default=0); NSN_MAI211 = models.FloatField(default=0); NSR_MAI211 = models.FloatField(default=0); Moy_MAI211 = models.FloatField(default=0); Capit_MAI211 = models.CharField(max_length=10, default='')
    NCC_MAI212 = models.FloatField(default=0); NSN_MAI212 = models.FloatField(default=0); NSR_MAI212 = models.FloatField(default=0); Moy_MAI212 = models.FloatField(default=0); Capit_MAI212 = models.CharField(max_length=10, default='')
    MOYENNE_UE3 = models.FloatField(default=0); UE3_Valide = models.CharField(max_length=10, default='')

    # UE4 : Spécialité 1
    NCC_SYR210 = models.FloatField(default=0); NSN_SYR210 = models.FloatField(default=0); NSR_SYR210 = models.FloatField(default=0); Moy_SYR210 = models.FloatField(default=0); Capit_SYR210 = models.CharField(max_length=10, default='')
    NCC_SYR211 = models.FloatField(default=0); NSN_SYR211 = models.FloatField(default=0); NSR_SYR211 = models.FloatField(default=0); Moy_SYR211 = models.FloatField(default=0); Capit_SYR211 = models.CharField(max_length=10, default='')
    MOYENNE_UE4 = models.FloatField(default=0); UE4_Valide = models.CharField(max_length=10, default='')

    # UE5 : Spécialité 2
    NCC_DSI210 = models.FloatField(default=0); NSN_DSI210 = models.FloatField(default=0); NSR_DSI210 = models.FloatField(default=0); Moy_DSI210 = models.FloatField(default=0); Capit_DSI210 = models.CharField(max_length=10, default='')
    NCC_DSI211 = models.FloatField(default=0); NSN_DSI211 = models.FloatField(default=0); NSR_DSI211 = models.FloatField(default=0); Moy_DSI211 = models.FloatField(default=0); Capit_DSI211 = models.CharField(max_length=10, default='')
    MOYENNE_UE5 = models.FloatField(default=0); UE5_Valide = models.CharField(max_length=10, default='')

    Moy_General = models.FloatField(default=0)
    Credit_total = models.IntegerField(default=0)
    Decision = models.CharField(max_length=50, default='')

    class Meta:
        db_table = 'notes_s3'

# ==========================================
#                SEMESTRE 4
# ==========================================
class NoteS4(models.Model):
    Matricule = models.CharField(max_length=50, primary_key=True)
    Prenom = models.CharField(max_length=100, null=True, blank=True)
    Nom = models.CharField(max_length=100, null=True, blank=True)
    Dept = models.CharField(max_length=100, null=True, blank=True)
    
    # UE1 : DPR41
    NCC_DPR110 = models.FloatField(default=0); NSN_DPR110 = models.FloatField(default=0); NSR_DPR110 = models.FloatField(default=0); Moy_DPR110 = models.FloatField(default=0); Capit_DPR110 = models.CharField(max_length=10, default='')
    NCC_DPR111 = models.FloatField(default=0); NSN_DPR111 = models.FloatField(default=0); NSR_DPR111 = models.FloatField(default=0); Moy_DPR111 = models.FloatField(default=0); Capit_DPR111 = models.CharField(max_length=10, default='')
    NCC_DPR112 = models.FloatField(default=0); NSN_DPR112 = models.FloatField(default=0); NSR_DPR112 = models.FloatField(default=0); Moy_DPR112 = models.FloatField(default=0); Capit_DPR112 = models.CharField(max_length=10, default='')
    MOYENNE_UE1 = models.FloatField(default=0); UE1_Valide = models.CharField(max_length=10, default='')

    # UE2 : PAV41
    NCC_MAI110 = models.FloatField(default=0); NSN_MAI110 = models.FloatField(default=0); NSR_MAI110 = models.FloatField(default=0); Moy_MAI110 = models.FloatField(default=0); Capit_MAI110 = models.CharField(max_length=10, default='')
    NCC_MAI111 = models.FloatField(default=0); NSN_MAI111 = models.FloatField(default=0); NSR_MAI111 = models.FloatField(default=0); Moy_MAI111 = models.FloatField(default=0); Capit_MAI111 = models.CharField(max_length=10, default='')
    NCC_MAI112 = models.FloatField(default=0); NSN_MAI112 = models.FloatField(default=0); NSR_MAI112 = models.FloatField(default=0); Moy_MAI112 = models.FloatField(default=0); Capit_MAI112 = models.CharField(max_length=10, default='')
    MOYENNE_UE2 = models.FloatField(default=0); UE2_Valide = models.CharField(max_length=10, default='')

    # UE3 : Spécialité
    NCC_Dev110 = models.FloatField(default=0); NSN_Dev110 = models.FloatField(default=0); NSR_Dev110 = models.FloatField(default=0); Moy_Dev110 = models.FloatField(default=0); Capit_Dev110 = models.CharField(max_length=10, default='')
    NCC_Dev111 = models.FloatField(default=0); NSN_Dev111 = models.FloatField(default=0); NSR_Dev111 = models.FloatField(default=0); Moy_Dev111 = models.FloatField(default=0); Capit_Dev111 = models.CharField(max_length=10, default='')
    NCC_Dev112 = models.FloatField(default=0); NSN_Dev112 = models.FloatField(default=0); NSR_Dev112 = models.FloatField(default=0); Moy_Dev112 = models.FloatField(default=0); Capit_Dev112 = models.CharField(max_length=10, default='')
    MOYENNE_UE3 = models.FloatField(default=0); UE3_Valide = models.CharField(max_length=10, default='')

    # UE4 : STG41 (Stage)
    NCC_STG112 = models.FloatField(default=0); NSN_STG112 = models.FloatField(default=0); NSR_STG112 = models.FloatField(default=0); Moy_STG112 = models.FloatField(default=0); Capit_STG112 = models.CharField(max_length=10, default='')
    MOYENNE_UE4 = models.FloatField(default=0); UE4_Valide = models.CharField(max_length=10, default='')

    Moy_General = models.FloatField(default=0)
    Credit_total = models.IntegerField(default=0)
    Decision = models.CharField(max_length=50, default='')

    class Meta:
        db_table = 'notes_s4'


class NoteS5(models.Model):
    Matricule = models.CharField(max_length=50, primary_key=True)
    Prenom = models.CharField(max_length=100, null=True, blank=True)
    Nom = models.CharField(max_length=100, null=True, blank=True)
    Dept = models.CharField(max_length=100, null=True, blank=True)
    
    # UE1 : DPR1
    NCC_DPR510 = models.FloatField(default=0); NSN_DPR510 = models.FloatField(default=0); NSR_DPR510 = models.FloatField(default=0); Moy_DPR510 = models.FloatField(default=0); Capit_DPR510 = models.CharField(max_length=10, default='')
    NCC_DPR511 = models.FloatField(default=0); NSN_DPR511 = models.FloatField(default=0); NSR_DPR511 = models.FloatField(default=0); Moy_DPR511 = models.FloatField(default=0); Capit_DPR511 = models.CharField(max_length=10, default='')
    NCC_DPR512 = models.FloatField(default=0); NSN_DPR512 = models.FloatField(default=0); NSR_DPR512 = models.FloatField(default=0); Moy_DPR512 = models.FloatField(default=0); Capit_DPR512 = models.CharField(max_length=10, default='')
    MOYENNE_UE1 = models.FloatField(default=0); UE1_Valide = models.CharField(max_length=10, default='')

    # UE2 : MAI1 (Big Data)
    NCC_BWC510 = models.FloatField(default=0); NSN_BWC510 = models.FloatField(default=0); NSR_BWC510 = models.FloatField(default=0); Moy_BWC510 = models.FloatField(default=0); Capit_BWC510 = models.CharField(max_length=10, default='')
    NCC_BWC511 = models.FloatField(default=0); NSN_BWC511 = models.FloatField(default=0); NSR_BWC511 = models.FloatField(default=0); Moy_BWC511 = models.FloatField(default=0); Capit_BWC511 = models.CharField(max_length=10, default='')
    NCC_BWC512 = models.FloatField(default=0); NSN_BWC512 = models.FloatField(default=0); NSR_BWC512 = models.FloatField(default=0); Moy_BWC512 = models.FloatField(default=0); Capit_BWC512 = models.CharField(max_length=10, default='')
    MOYENNE_UE2 = models.FloatField(default=0); UE2_Valide = models.CharField(max_length=10, default='')

    # UE3 : DEV1
    NCC_DSI510 = models.FloatField(default=0); NSN_DSI510 = models.FloatField(default=0); NSR_DSI510 = models.FloatField(default=0); Moy_DSI510 = models.FloatField(default=0); Capit_DSI510 = models.CharField(max_length=10, default='')
    NCC_DSI511 = models.FloatField(default=0); NSN_DSI511 = models.FloatField(default=0); NSR_DSI511 = models.FloatField(default=0); Moy_DSI511 = models.FloatField(default=0); Capit_DSI511 = models.CharField(max_length=10, default='')
    NCC_DSI512 = models.FloatField(default=0); NSN_DSI512 = models.FloatField(default=0); NSR_DSI512 = models.FloatField(default=0); Moy_DSI512 = models.FloatField(default=0); Capit_DSI512 = models.CharField(max_length=10, default='')
    MOYENNE_UE3 = models.FloatField(default=0); UE3_Valide = models.CharField(max_length=10, default='')

    # UE4 : SYR1 (Module spécialité)
    NCC_DSI520 = models.FloatField(default=0); NSN_DSI520 = models.FloatField(default=0); NSR_DSI520 = models.FloatField(default=0); Moy_DSI520 = models.FloatField(default=0); Capit_DSI520 = models.CharField(max_length=10, default='')
    NCC_DSI521 = models.FloatField(default=0); NSN_DSI521 = models.FloatField(default=0); NSR_DSI521 = models.FloatField(default=0); Moy_DSI521 = models.FloatField(default=0); Capit_DSI521 = models.CharField(max_length=10, default='')
    MOYENNE_UE4 = models.FloatField(default=0); UE4_Valide = models.CharField(max_length=10, default='')

    Moy_General = models.FloatField(default=0)
    Credit_total = models.IntegerField(default=0)
    Decision = models.CharField(max_length=50, default='')

    class Meta:
        db_table = 'notes_s5'