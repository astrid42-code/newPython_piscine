import time, datetime

months = {
    1 : 'Jan',
    2 : 'Feb',
    3 : 'Mar',
    4 : 'Apr',
    5 : 'May',
    6 : 'Jun',
    7 : 'Jul',
}


seconds = time.time()
len_s = len(seconds)


other_seconds = '{:.2e}'.format(time.time())
myDate = datetime.datetime.today()
month = myDate.month


print("Seconds since January 1, 1970:", seconds, "or", other_seconds, "in sientific notation")
print(months[month], myDate.day, myDate.year)


# partir de la fin et tous les 3 chiffres, mettre un sep=','
# ou
# diviser et modulo le nb de chiffres par 3 ;
# le modulo me dit ou mettre la 1ere virgule
# ensuite ous les 3 chiffres je mets une virgule avec un sep 