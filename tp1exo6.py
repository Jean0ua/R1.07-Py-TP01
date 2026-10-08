def jour_associer():
        minute_ecoule = int(input("Veuillez saisir le nombre de mionutes écouler depuis le débur de l'année: "))
        heure = minute_ecoule//60
        jour = heure // 24
        heure -= jour*24
        minute_ecoule -= jour*24*60 + heure*60

        print("Le jour associé a ce nombre de minutes est",jour,"jours",heure,"h",minute_ecoule,"min")

jour_associer()
