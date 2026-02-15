from django.db import models

class NoteS1(models.Model):
    matricule = models.CharField(max_length=50, primary_key=True)
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    
    # DPR1 : Développement Personnel
    ncc_dpr110 = models.FloatField(default=0) # Français Devoir
    nsn_dpr110 = models.FloatField(default=0) # Français Examen
    nsr_dpr110 = models.FloatField(default=0) # Français Rattrapage
    moy_dpr110 = models.FloatField(default=0)
    capit_dpr110 = models.CharField(max_length=10)

    ncc_dpr111 = models.FloatField(default=0) # Anglais
    nsn_dpr111 = models.FloatField(default=0)
    nsr_dpr111 = models.FloatField(default=0)
    moy_dpr111 = models.FloatField(default=0)
    capit_dpr111 = models.CharField(max_length=10)

    ncc_dpr112 = models.FloatField(default=0) # PPP
    nsn_dpr112 = models.FloatField(default=0)
    nsr_dpr112 = models.FloatField(default=0)
    moy_dpr112 = models.FloatField(default=0)
    capit_dpr112 = models.CharField(max_length=10)

    moyenne_ue1 = models.FloatField(default=0)
    ue1_valide = models.CharField(max_length=10)

    # MAI1 : Outils Mathématiques
    ncc_mai110 = models.FloatField(default=0) # Algèbre
    nsn_mai110 = models.FloatField(default=0)
    nsr_mai110 = models.FloatField(default=0)
    moy_mai110 = models.FloatField(default=0)
    capit_mai110 = models.CharField(max_length=10)

    ncc_mai111 = models.FloatField(default=0) # Analyse
    nsn_mai111 = models.FloatField(default=0)
    nsr_mai111 = models.FloatField(default=0)
    moy_mai111 = models.FloatField(default=0)
    capit_mai111 = models.CharField(max_length=10)

    ncc_mai112 = models.FloatField(default=0) # Pix
    nsn_mai112 = models.FloatField(default=0)
    nsr_mai112 = models.FloatField(default=0)
    moy_mai112 = models.FloatField(default=0)
    capit_mai112 = models.CharField(max_length=10)

    moyenne_ue2 = models.FloatField(default=0)
    ue2_valide = models.CharField(max_length=10)

    # DEV1 : Programmation
    ncc_dev110 = models.FloatField(default=0) # C++
    nsn_dev110 = models.FloatField(default=0)
    nsr_dev110 = models.FloatField(default=0)
    moy_dev110 = models.FloatField(default=0)
    capit_dev110 = models.CharField(max_length=10)

    ncc_dev111 = models.FloatField(default=0) # BDD
    nsn_dev111 = models.FloatField(default=0)
    nsr_dev111 = models.FloatField(default=0)
    moy_dev111 = models.FloatField(default=0)
    capit_dev111 = models.CharField(max_length=10)

    ncc_dev112 = models.FloatField(default=0) # Web
    nsn_dev112 = models.FloatField(default=0)
    nsr_dev112 = models.FloatField(default=0)
    moy_dev112 = models.FloatField(default=0)
    capit_dev112 = models.CharField(max_length=10)

    moyenne_ue3 = models.FloatField(default=0)
    ue3_valide = models.CharField(max_length=10)

    # Architecture / BDD Intro
    ncc_syr110 = models.FloatField(default=0)
    nsn_syr110 = models.FloatField(default=0)
    nsr_syr110 = models.FloatField(default=0)
    moy_syr110 = models.FloatField(default=0)
    capit_syr110 = models.CharField(max_length=10)

    # Systèmes / Réseaux Intro
    ncc_syr111 = models.FloatField(default=0)
    nsn_syr111 = models.FloatField(default=0)
    nsr_syr111 = models.FloatField(default=0)
    moy_syr111 = models.FloatField(default=0)
    capit_syr111 = models.CharField(max_length=10)

    # Moyenne de l'Unité d'Enseignement
    moyenne_ue4 = models.FloatField(default=0)
    ue4_valide = models.CharField(max_length=10)

    # Totaux
    moy_general = models.FloatField(default=0)
    credit_total = models.IntegerField(default=0)
    decision = models.CharField(max_length=50)

    class Meta:
        db_table = 'notes_s1' # Nom exact de votre table MySQL


class NoteS2(models.Model):
    matricule = models.CharField(max_length=50, primary_key=True)
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    
    # DPR2
    ncc_dpr210 = models.FloatField(default=0)
    nsn_dpr210 = models.FloatField(default=0)
    nsr_dpr210 = models.FloatField(default=0)
    moy_dpr210 = models.FloatField(default=0)
    capit_pr210 = models.CharField(max_length=10) # Nom colonne SQL exact

    ncc_dpr211 = models.FloatField(default=0)
    nsn_dpr211 = models.FloatField(default=0)
    nsr_dpr211 = models.FloatField(default=0)
    moy_dpr211 = models.FloatField(default=0)
    capit_dpr211 = models.CharField(max_length=10)

    ncc_dpr212 = models.FloatField(default=0)
    nsn_dpr212 = models.FloatField(default=0)
    nsr_dpr212 = models.FloatField(default=0)
    moy_dpr212 = models.FloatField(default=0)
    capit_dpr212 = models.CharField(max_length=10)
    moyenne_ue1 = models.FloatField(default=0)
    ue1_valide = models.CharField(max_length=10)

    # DEV2
    ncc_dev210 = models.FloatField(default=0)
    nsn_dev210 = models.FloatField(default=0)
    nsr_dev210 = models.FloatField(default=0)
    moy_dev210 = models.FloatField(default=0)
    capit_dev210 = models.CharField(max_length=10)

    ncc_dev211 = models.FloatField(default=0)
    nsn_dev211 = models.FloatField(default=0)
    nsr_dev211 = models.FloatField(default=0)
    moy_dev211 = models.FloatField(default=0)
    capit_dev211 = models.CharField(max_length=10)
    moyenne_ue2 = models.FloatField(default=0)
    ue2_valide = models.CharField(max_length=10)

    # MAI2
    ncc_mai210 = models.FloatField(default=0)
    nsn_mai210 = models.FloatField(default=0)
    nsr_mai210 = models.FloatField(default=0)
    moy_mai210 = models.FloatField(default=0)
    capit_mai210 = models.CharField(max_length=10)

    ncc_mai211 = models.FloatField(default=0)
    nsn_mai211 = models.FloatField(default=0)
    nsr_mai211 = models.FloatField(default=0)
    moy_mai211 = models.FloatField(default=0)
    capit_mai211 = models.CharField(max_length=10)

    ncc_mai212 = models.FloatField(default=0)
    nsn_mai212 = models.FloatField(default=0)
    nsr_mai212 = models.FloatField(default=0)
    moy_mai212 = models.FloatField(default=0)
    capit_mai212 = models.CharField(max_length=10)
    moyenne_ue3 = models.FloatField(default=0)
    ue3_valide = models.CharField(max_length=10)

    # SYR2
    ncc_syr210 = models.FloatField(default=0)
    nsn_syr210 = models.FloatField(default=0)
    nsr_syr210 = models.FloatField(default=0)
    moy_syr210 = models.FloatField(default=0)
    capit_syr210 = models.CharField(max_length=10)

    ncc_syr211 = models.FloatField(default=0)
    nsn_syr211 = models.FloatField(default=0)
    nsr_syr211 = models.FloatField(default=0)
    moy_syr211 = models.FloatField(default=0)
    capit_syr211 = models.CharField(max_length=10)
    moyenne_ue4 = models.FloatField(default=0)
    ue4_valide = models.CharField(max_length=10)

    # DSI2 (Module spécialité)
    ncc_dsi210 = models.FloatField(default=0)
    nsn_dsi210 = models.FloatField(default=0)
    nsr_dsi210 = models.FloatField(default=0)
    moy_dsi210 = models.FloatField(default=0)
    capit_dsi210 = models.CharField(max_length=10)

    ncc_dsi211 = models.FloatField(default=0)
    nsn_dsi211 = models.FloatField(default=0)
    nsr_dsi211 = models.FloatField(default=0)
    moy_dsi211 = models.FloatField(default=0)
    capit_dsi211 = models.CharField(max_length=10)
    moyenne_ue5 = models.FloatField(default=0)
    ue5_valide = models.CharField(max_length=10)

    # Totaux
    moy_general = models.FloatField(default=0)
    credit_total = models.IntegerField(default=0)
    decision = models.CharField(max_length=50)

    class Meta:
        db_table = 'notes_s2'

class NoteS3(models.Model):
    matricule = models.CharField(db_column='Matricule', max_length=50, primary_key=True)
    prenom = models.CharField(db_column='Prenom', max_length=100)
    nom = models.CharField(db_column='Nom', max_length=100)
    dept = models.CharField(db_column='Dept', max_length=100) # Votre PHP indique 'pt'
    
    # UE 1 : DPR (Utilise les colonnes DPR210 à DPR213 d'après votre PHP)
    ncc_fr = models.FloatField(db_column='NCC_DPR210', default=0)
    nsn_fr = models.FloatField(db_column='NSN_DPR210', default=0)
    nsr_fr = models.FloatField(db_column='NSR_DPR210', default=0)
    moy_fr = models.FloatField(db_column='Moy_DPR210', default=0)
    capit_fr = models.CharField(db_column='Capit_PR210', max_length=10)

    ncc_an = models.FloatField(db_column='NCC_DPR211', default=0)
    nsn_an = models.FloatField(db_column='NSN_DPR211', default=0)
    nsr_an = models.FloatField(db_column='NSR_DPR211', default=0)
    moy_an = models.FloatField(db_column='Moy_DPR211', default=0)
    capit_an = models.CharField(db_column='Capit_DPR211', max_length=10)

    ncc_ppp = models.FloatField(db_column='NCC_DPR212', default=0)
    nsn_ppp = models.FloatField(db_column='NSN_DPR212', default=0)
    nsr_ppp = models.FloatField(db_column='NSR_DPR212', default=0)
    moy_ppp = models.FloatField(db_column='Moy_DPR212', default=0)
    capit_ppp = models.CharField(db_column='Capit_DPR212', max_length=10)

    ncc_ges = models.FloatField(db_column='NCC_DPR213', default=0)
    nsn_ges = models.FloatField(db_column='NSN_DPR213', default=0)
    nsr_ges = models.FloatField(db_column='NSR_DPR213', default=0)
    moy_ges = models.FloatField(db_column='Moy_DPR213', default=0)
    capit_ges = models.CharField(db_column='Capit_DPR213', max_length=10)
    
    moyenne_ue1 = models.FloatField(db_column='MOYENNE_UE1', default=0)
    ue1_valide = models.CharField(db_column='UE1_Valide', max_length=10)

    # UE 2 : DEV (Python et Langage Web)
    ncc_py = models.FloatField(db_column='NCC_DEV210', default=0)
    nsn_py = models.FloatField(db_column='NSN_DEV210', default=0)
    nsr_py = models.FloatField(db_column='NSR_DEV210', default=0)
    moy_py = models.FloatField(db_column='Moy_DEV210', default=0)
    capit_py = models.CharField(db_column='Capit_DEV210', max_length=10)

    ncc_lw = models.FloatField(db_column='NCC_DEV211', default=0)
    nsn_lw = models.FloatField(db_column='NSN_DEV211', default=0)
    nsr_lw = models.FloatField(db_column='NSR_DEV211', default=0)
    moy_lw = models.FloatField(db_column='Moy_DEV211', default=0)
    capit_lw = models.CharField(db_column='Capit_DEV211', max_length=10)
    
    moyenne_ue2 = models.FloatField(db_column='MOYENNE_UE2', default=0)
    ue2_valide = models.CharField(db_column='UE2_Valide', max_length=10)

    # UE 3 : MAI (Algèbre, Probabilités, Pix)
    ncc_al = models.FloatField(db_column='NCC_MAI210', default=0)
    nsn_al = models.FloatField(db_column='NSN_MAI210', default=0)
    nsr_al = models.FloatField(db_column='NSR_MAI210', default=0)
    moy_al = models.FloatField(db_column='Moy_MAI210', default=0)
    capit_al = models.CharField(db_column='Capit_MAI210', max_length=10)

    ncc_pr = models.FloatField(db_column='NCC_MAI211', default=0)
    nsn_pr = models.FloatField(db_column='NSN_MAI211', default=0)
    nsr_pr = models.FloatField(db_column='NSR_MAI211', default=0)
    moy_pr = models.FloatField(db_column='Moy_MAI211', default=0)
    capit_pr = models.CharField(db_column='Capit_MAI211', max_length=10)

    ncc_pix = models.FloatField(db_column='NCC_MAI212', default=0)
    nsn_pix = models.FloatField(db_column='NSN_MAI212', default=0)
    nsr_pix = models.FloatField(db_column='NSR_MAI212', default=0)
    moy_pix = models.FloatField(db_column='Moy_MAI212', default=0)
    capit_pix = models.CharField(db_column='Capit_MAI212', max_length=10)
    
    moyenne_ue3 = models.FloatField(db_column='MOYENNE_UE3', default=0)
    ue3_valide = models.CharField(db_column='UE3_Valide', max_length=10)

    # UE 4 : SYR
    ncc_sl = models.FloatField(db_column='NCC_SYR210', default=0)
    nsn_sl = models.FloatField(db_column='NSN_SYR210', default=0)
    nsr_sl = models.FloatField(db_column='NSR_SYR210', default=0)
    moy_sl = models.FloatField(db_column='Moy_SYR210', default=0)
    capit_sl = models.CharField(db_column='Capit_SYR210', max_length=10)

    ncc_se = models.FloatField(db_column='NCC_SYR211', default=0)
    nsn_se = models.FloatField(db_column='NSN_SYR211', default=0)
    nsr_se = models.FloatField(db_column='NSR_SYR211', default=0)
    moy_se = models.FloatField(db_column='Moy_SYR211', default=0)
    capit_se = models.CharField(db_column='Capit_SYR211', max_length=10)
    
    moyenne_ue4 = models.FloatField(db_column='MOYENNE_UE4', default=0)
    ue4_valide = models.CharField(db_column='UE4_Valide', max_length=10)

    # UE 5 : DSI
    ncc_sp = models.FloatField(db_column='NCC_DSI210', default=0)
    nsn_sp = models.FloatField(db_column='NSN_DSI210', default=0)
    nsr_sp = models.FloatField(db_column='NSR_DSI210', default=0)
    moy_sp = models.FloatField(db_column='Moy_DSI210', default=0)
    capit_sp = models.CharField(db_column='Capit_DSI210', max_length=10)

    ncc_pri = models.FloatField(db_column='NCC_DSI211', default=0)
    nsn_pri = models.FloatField(db_column='NSN_DSI211', default=0)
    nsr_pri = models.FloatField(db_column='NSR_DSI211', default=0)
    moy_pri = models.FloatField(db_column='Moy_DSI211', default=0)
    capit_pri = models.CharField(db_column='Capit_DSI211', max_length=10)
    
    moyenne_ue5 = models.FloatField(db_column='MOYENNE_UE5', default=0)
    ue5_valide = models.CharField(db_column='UE5_Valide', max_length=10)

    # Résumé
    moy_general = models.FloatField(db_column='Moy_General', default=0)
    credit_total = models.IntegerField(db_column='Credit_total', default=0)
    decision = models.CharField(db_column='Decision', max_length=50)

    class Meta:
        db_table = 'notes_s3' # Nom de la table dans MySQL
        managed = False      # TRÈS IMPORTANT : Django ne touchera pas à la structure


class NoteS4(models.Model):
    matricule = models.CharField(db_column='Matricule', max_length=50, primary_key=True)
    prenom = models.CharField(db_column='Prenom', max_length=100)
    nom = models.CharField(db_column='Nom', max_length=100)
    dept = models.CharField(db_column='Dept', max_length=100)
    
    # UE 1 : DPR41 (DPR110 à 112 d'après votre PHP)
    ncc_fr = models.FloatField(db_column='NCC_DPR110', default=0)
    nsn_fr = models.FloatField(db_column='NSN_DPR110', default=0)
    nsr_fr = models.FloatField(db_column='NSR_DPR110', default=0)
    moy_fr = models.FloatField(db_column='Moy_DPR110', default=0)
    capit_fr = models.CharField(db_column='Capit_DPR110', max_length=10)

    ncc_an = models.FloatField(db_column='NCC_DPR111', default=0)
    nsn_an = models.FloatField(db_column='NSN_DPR111', default=0)
    nsr_an = models.FloatField(db_column='NSR_DPR111', default=0)
    moy_an = models.FloatField(db_column='Moy_DPR111', default=0)
    capit_an = models.CharField(db_column='Capit_DPR111', max_length=10)

    ncc_ppp = models.FloatField(db_column='NCC_DPR112', default=0)
    nsn_ppp = models.FloatField(db_column='NSN_DPR112', default=0)
    nsr_ppp = models.FloatField(db_column='NSR_DPR112', default=0)
    moy_ppp = models.FloatField(db_column='Moy_DPR112', default=0)
    capit_ppp = models.CharField(db_column='Capit_DPR112', max_length=10)
    
    moyenne_ue1 = models.FloatField(db_column='MOYENNE_UE1', default=0)
    ue1_valide = models.CharField(db_column='UE1_Valide', max_length=10)

    # UE 2 : PAV41 (Utilise MAI110 à 112 d'après votre PHP)
    ncc_al = models.FloatField(db_column='NCC_MAI110', default=0)
    nsn_al = models.FloatField(db_column='NSN_MAI110', default=0)
    nsr_al = models.FloatField(db_column='NSR_MAI110', default=0)
    moy_al = models.FloatField(db_column='Moy_MAI110', default=0)
    capit_al = models.CharField(db_column='Capit_MAI110', max_length=10)

    ncc_ana = models.FloatField(db_column='NCC_MAI111', default=0)
    nsn_ana = models.FloatField(db_column='NSN_MAI111', default=0)
    nsr_ana = models.FloatField(db_column='NSR_MAI111', default=0)
    moy_ana = models.FloatField(db_column='Moy_MAI111', default=0)
    capit_ana = models.CharField(db_column='Capit_MAI111', max_length=10)

    ncc_pix = models.FloatField(db_column='NCC_MAI112', default=0)
    nsn_pix = models.FloatField(db_column='NSN_MAI112', default=0)
    nsr_pix = models.FloatField(db_column='NSR_MAI112', default=0)
    moy_pix = models.FloatField(db_column='Moy_MAI112', default=0)
    capit_pix = models.CharField(db_column='Capit_MAI112', max_length=10)
    
    moyenne_ue2 = models.FloatField(db_column='MOYENNE_UE2', default=0)
    ue2_valide = models.CharField(db_column='UE2_Valide', max_length=10)

    # UE 3 : Module de Spécialité (Utilise Dev110 à 112 d'après votre PHP)
    ncc_cpp = models.FloatField(db_column='NCC_Dev110', default=0)
    nsn_cpp = models.FloatField(db_column='NSN_Dev110', default=0)
    nsr_cpp = models.FloatField(db_column='NSR_Dev110', default=0)
    moy_cpp = models.FloatField(db_column='Moy_Dev110', default=0)
    capit_cpp = models.CharField(db_column='Capit_Dev110', max_length=10)

    ncc_bd = models.FloatField(db_column='NCC_Dev111', default=0)
    nsn_bd = models.FloatField(db_column='NSN_Dev111', default=0)
    nsr_bd = models.FloatField(db_column='NSR_Dev111', default=0)
    moy_bd = models.FloatField(db_column='Moy_Dev111', default=0)
    capit_bd = models.CharField(db_column='Capit_Dev111', max_length=10)

    ncc_tw = models.FloatField(db_column='NCC_Dev112', default=0)
    nsn_tw = models.FloatField(db_column='NSN_Dev112', default=0)
    nsr_tw = models.FloatField(db_column='NSR_Dev112', default=0)
    moy_tw = models.FloatField(db_column='Moy_Dev112', default=0)
    capit_tw = models.CharField(db_column='Capit_Dev112', max_length=10)
    
    moyenne_ue3 = models.FloatField(db_column='MOYENNE_UE3', default=0)
    ue3_valide = models.CharField(db_column='UE3_Valide', max_length=10)

    # UE 4 : Stage (STG112)
    ncc_stg = models.FloatField(db_column='NCC_STG112', default=0)
    nsn_stg = models.FloatField(db_column='NSN_STG112', default=0)
    nsr_stg = models.FloatField(db_column='NSR_STG112', default=0)
    moy_stg = models.FloatField(db_column='Moy_STG112', default=0)
    capit_stg = models.CharField(db_column='Capit_STG112', max_length=10)
    
    moyenne_ue4 = models.FloatField(db_column='MOYENNE_UE4', default=0)
    ue4_valide = models.CharField(db_column='UE4_Valide', max_length=10)

    # Totaux
    moy_general = models.FloatField(db_column='Moy_General', default=0)
    credit_total = models.IntegerField(db_column='Credit_total', default=0)
    decision = models.CharField(db_column='Decision', max_length=50)

    class Meta:
        db_table = 'notes_s4'
        managed = False