leeftijd = int(input('Geef je leeftijd: '))
print('Bij de volgende vraag ja of nee invullen')
paspoort = str(input('Nederlands paspoort: '))
if leeftijd > 18 and paspoort == 'ja':
    print('Gefeliciteerd, je mag stemmen!')
else:
    print('Helaas, je mag niet stemmen.')