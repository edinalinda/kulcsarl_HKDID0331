#gender input
def get_gender():
    while True:
        gender = input("Nem (m/w): ").lower()
        if gender in ["m", "w"]:
            return gender
        print("Hibás érték! Csak 'm' vagy 'w' adható meg.")
        
        retry = input("Újra próbálod? (y/n): ").lower()
        if retry != "y":
            print("Kilépés...")
            exit()

#altitude input
def get_altitude_value():
    while True:
        value = input("Add meg a magasságot: ")
        try:
            return float(value)
        except ValueError:
            print("Hibás érték! Csak számot adhatsz meg.")
            
            retry = input("Újra próbálod? (y/n): ").lower()
            if retry != "y":
                print("Kilépés...")
                exit()

#altitude unit input
def get_altitude_unit():
    while True:
        unit = input("Mértékegység (m/ft): ").lower()
        if unit in ["m", "ft"]:
            return unit
        print("Hibás érték! Csak 'm' vagy 'ft' adható meg.")
        
        retry = input("Újra próbálod? (y/n): ").lower()
        if retry != "y":
            print("Kilépés...")
            exit()

#convert altitude
def convert_altitude(value, unit):
    """Magasság átváltása méterre."""
    if unit == 'm':
        return value
    elif unit == 'ft':
        return value * 0.3048
    else:
        raise ValueError("A mértékegység csak 'm' vagy 'ft' lehet.")

#hypoxia level
def altitude_to_hypoxia(altitude_m):
    """Magasságból becsült hipoxia-szint (0–10)."""
    if altitude_m < 3000:
        return 1
    elif altitude_m < 6000:
        return 3
    elif altitude_m < 9000:
        return 6
    elif altitude_m < 12000:
        return 8
    else:
        return 10

#performance from hypoxia level
def hypoxia_performance(altitude_m, task_difficulty, hsi_quality):
    """Teljesítmény becslése hipoxia alapján."""
    hypoxia_level = altitude_to_hypoxia(altitude_m)

    base_reaction_time = 350
    reaction_time_penalty = hypoxia_level * 30
    task_penalty = task_difficulty * 15
    hsi_mitigation = hsi_quality * 12

    reaction_time = base_reaction_time + reaction_time_penalty + task_penalty - hsi_mitigation

    error_rate = hypoxia_level * 3.5 + task_difficulty * 2 - hsi_quality * 1.5
    if error_rate < 0:
        error_rate = 0

    return reaction_time, error_rate, hypoxia_level



if __name__ == "__main__":

    gender = get_gender()
    altitude_value = get_altitude_value()
    altitude_unit = get_altitude_unit()

    altitude_m = convert_altitude(altitude_value, altitude_unit)

    task_difficulty = 6
    hsi_quality = 5

    user_rt, user_err, user_hyp = hypoxia_performance(altitude_m, task_difficulty, hsi_quality)

    compare_alt_ft = [12000, 18000, 25000, 30000, 40000]

    print("\n--- Összehasonlítás különböző magasságokon ---")

    for alt_ft in compare_alt_ft:
        alt_m = alt_ft * 0.3048
        rt, err, hyp = hypoxia_performance(alt_m, task_difficulty, hsi_quality)

        print(f"\nMagasság: {alt_ft} ft")
        print(f"Hipoxia szint: {hyp}")
        print(f"Reakcióidő: {round(rt,1)} ms")
        print(f"Hibaarány: {round(err,1)} %")

    
    print("\n--- Te általad megadott magasság eredménye ---")
    print(f"Nem: {'Férfi' if gender == 'm' else 'Nő'}")
    print(f"Magasság méterben: {round(altitude_m,2)} m")
    print(f"Hipoxia szint: {user_hyp}")
    print(f"Reakcióidő: {round(user_rt,1)} ms")
    print(f"Hibaarány: {round(user_err,1)} %")