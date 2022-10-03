fruitmand = { "appel":3, "banaan":5, "kers":50 }
print( fruitmand.keys() )
# Vul in --> return .keys(): 
print( fruitmand.values() )
# Vul in --> return .values():
print( fruitmand.items() )
# Vul in --> return .items(): 

"""
Wat zijn de gelijkenissen van deze waarden met lijsten? Wat zijn de verschillen?
Hebben beide vierkante haakjes
"""
items = fruitmand.items()
"""
Zijn deze waarden effectief lijsten? Hoe kan je dit testen?
Nee, hebben geen methodes die lijsten hebben.
"""
lijst_items = list(items)
lijst_items.append("hallo")
print(lijst_items)
"""
Indien nee, is het mogelijk om deze waarden naar lijsten om te vormen?

"""