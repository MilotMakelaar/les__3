cijferICOR = 7
cijferPROG = 8
cijferCSN = 7
gemiddelde = ((cijferICOR + cijferPROG + cijferCSN)/3)
beloning = ((cijferICOR * 30) + (cijferPROG * 30) + (cijferCSN * 30))
line1 = int(gemiddelde)
line2 = int(beloning)
overzicht = "Mijn cijfers (gemiddeld een {} leveren een beloning van {} op!".format(line1, line2)
print(overzicht)