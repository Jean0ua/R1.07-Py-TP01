def calcul_minute():
    jour = int(input("Veuillez saisir un jour du mois: "))
    heure = int(input("Veuillez saisir une heure dans la journée: "))
    minute = int(input("Veuillez saisir les minutes: "))
    if heure < 24 and minute < 60: 
        m_ecouler = (jour*24*60)+(heure*60)+minute
        print(m_ecouler)
    else:
        print("Veuillez saisir une donnée valide")

calcul_minute()
    
