from pyscript import document,display

NonMetals = {"H":("Hydrogen", 1, 1.008), 
             "He":("Helium", 2, 4.0026),
             "C":("Carbon", 6, 12.011),
             "N":("Nitrogen", 7, 14.007),
             "O":("Oxygen", 8, 15.999),
             "F":("Flourine", 9, 18.998),
             "N":("Neon", 10, 20.18),
             "P":("Phosphorus", 15, 30.974),
             "S":("Sulfur", 16, 32.07),
             "Cl":("Chlorine", 17, 35.45),
             "Ar":("Argon", 18, 39.9),
             "Se":("Selenium", 34, 78.97),
             "Br":("Bromine", 35, 79.9),
             "Kr":("Krypton", 36, 83.8),
             "I":("Iodine", 53, 126.9),
             "Xe":("Xenon", 54, 131.29),
             "Rn":("Radon", 86, 86),} # dictionaries of the elements (symbol : (name, atomic number, atomic mass))

def SearchSymbol(e): #function

    ElementSym = document.getElementById("ElementInput").value.capitalize() #getting the value of what the user typed in

    result = NonMetals.get(ElementSym, ('Element not found', "-", "-")) # seeing if what was inputed is in the dictionaries, and when not, element not found will show up

    document.getElementById("Symbol").innerText = ElementSym
    document.getElementById("EName").innerText = result[0]
    document.getElementById("AtomicNo").innerText = result[1]
    document.getElementById("AtomicMass").innerText = result[2] # getting the values then making it appear on the main page
