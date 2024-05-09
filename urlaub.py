## First Baby Steps in Python :-)
## Berechung der Urlaubstage

def urlaubstage():
    basis_urlaub = 26
    unter18_urlaub = 30
    urlaub = 0    
    
    while True:
        try:
            alter = int(input("Bitte Alter eingeben: "))
            if alter < 0:
                raise ValueError("Das Alter kann nicht negativ sein.")
            break
        except ValueError:
            print("Bitte geben Sie eine gültige Zahl für das Alter ein.")

    while True:
        gdb50_input = input("GdB 50 % oder höher? (ja/nein): ").lower()
        if gdb50_input in ['ja', 'nein']:
            gdb50 = gdb50_input == 'ja'
            break
        else:
            print("Bitte geben Sie entweder 'ja' oder 'nein' ein.")

    while True:
        mehrals10_input = input("Länger als 10 Jahre im Betrieb? (ja/nein): ").lower()
        if mehrals10_input in ['ja', 'nein']:
            mehrals10 = mehrals10_input == 'ja'
            break
        else:
            print("Bitte geben Sie entweder 'ja' oder 'nein' ein.")

    if alter < 18:
        urlaub = unter18_urlaub
        if gdb50:
            urlaub += 5
        if mehrals10:
            urlaub += 2
    else:
        urlaub = basis_urlaub
        if gdb50:
            urlaub += 5
        if mehrals10:
            urlaub += 2

    print(f"Die Urlaubstage betragen: {urlaub} Tage")    

urlaubstage()
