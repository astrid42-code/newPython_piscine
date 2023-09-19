import time
import datetime

months = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec',
}

seconds = time.time() # seconds est un float



other_seconds = '{:.2e}'.format(time.time())
myDate = datetime.datetime.today()
month = myDate.month

print("Seconds since January 1, 1970:", seconds, "or", other_seconds,
      "in scientific notation")
print(months[month], myDate.day, myDate.year)

# pour affichage des secondes : partir de la fin et tous les 3 chiffres, mettre un sep=','
# ou
# diviser et modulo le nb de chiffres par 3 (attention, ne concerne que les chiffres à gauche du point) ;
# le modulo me dit ou mettre la 1ere virgule
# ensuite tous les 3 chiffres je mets une virgule avec un sep
# OU : TROUVER LA FONCTION QUI FAIT LE BON AFFICHAGE directement???

# Attention : Le sujet demande un script (à mettre / faire ici???)
