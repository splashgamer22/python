from microbit import *

# Pierre (rock)
pierre = Image("99999:"
               "90009:"
               "90009:"
               "90009:"
               "99999:")

# Feuille (paper)
feuille = Image("99999:"
                "90009:"
                "90909:"
                "90009:"
                "99999:")

# Ciseaux (scissors)
ciseaux = Image("99009:"
                "99090:"
                "00900:"
                "99090:"
                "99009:")

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(ciseaux)
        sleep(500)

    elif button_a.is_pressed():
        display.show(pierre)
        sleep(500)

    elif button_b.is_pressed():
        display.show(feuille)
        sleep(500)

    display.clear(100)
    sleep(100)

