import random

from consts import u3tier5champs, u2tier5champs, tier5champs, u3tier4champs, u2tier4champs, tier4champs, \
    u3tier3champs, \
    u2tier3champs, tier3champs, u3tier2champs, u2tier2champs, tier2champs, u3tier1champs, u2tier1champs, tier1champs, \
    Brothers, Musicians, Assasins, Supports, Warriors, Mages, Ranged, Tanks, u3lvl9champs, u2lvl9champs, lvl9champs, \
    u3lvl7champs, u2lvl8champs, lvl8champs, u3lvl6champs, u2lvl7champs, lvl7champs, u3lvl5champs, u2lvl6champs, \
    lvl6champs, u3lvl4champs, u2lvl5champs, lvl5champs, u3lvl3champs, u2lvl4champs, lvl4champs, u3lvl2champs, \
    u2lvl3champs, lvl3champs, u2lvl2champs, lvl2champs, u2lvl1champs, lvl1champs, lvlChamps, u1tierchamps, \
    u3tierchamps, u2tierchamps
from fight import find_objects_on_arena, find_tiers_on_arena, count_victory_points
from intro import intro
from levels import get_level
from points import get_points_for_tiers
from utils import get_input

hp = 100
gold = 5
lvl = 1
xp = 0
victory = 0
defeat = 0
shop = ["", "", "", "", "", ""]
bench = ["–", "–", "–", "–", "–", "–", "–", "–", "–"]
arena = ["–"]
enemyarena = [""]
runda = 1


# Funkcje
def shoproll():
    for i in range(1, 6):
        shop[i] = random.choice(lvlChamps[lvl])


def rundalvl1(money, reserve):
    q = ""
    shoproll()
    while q != "T":
        print()
        print(*shop, sep=" | ", end=" |"'\n')
        print("Złoto: ", money)
        print()
        buy = get_input(text="Podaj numery postaci, które chcesz kupić: ").split()
        for i in buy:
            i = int(i)
            if shop[i] == "–":
                print("Zakup nieudany postać zaostała już kupiona."'\n')
            elif money - int(shop[i][-1]) < 0:
                print("Zakup nieduany za mało Złota."'\n')
            else:
                try:
                    n = reserve.index("–")
                except ValueError:
                    n = 0
                reserve[n] = shop[i]
                money -= int(shop[i][-1])
                shop[i] = "–"
                n += 1
        reserve = upgrade(b=reserve)
        print()
        print("Twoja ławka: ", *reserve, sep=" | ", end=" |"'\n')
        print()
        q = str(get_input(text="Przejść Dalej? T/N: "))
    q = ""
    n = 0
    while q != "T":
        champ_on_arena = [int(champ_on_arena) for champ_on_arena in
                          get_input(text="Podaj numer postaci, które chcesz wstawić na arenę: ").split()]
        if champ_on_arena[0] != 0:
            if champ_on_arena[0] != 10:
                for i in champ_on_arena:
                    i -= 1
                    if reserve[i] == "–" and arena[n] == "–":
                        print("Nie udało się wstawić postaci na arenę podane miejsce jest puste.")
                    else:
                        arena[n], reserve[i] = reserve[i], arena[n]
                        n += 1
            else:
                clear = 0
                k = -1
                for i in reserve:
                    if i == "–":
                        clear += 1
                        if clear == len(arena):
                            for j in range(len(arena)):
                                arena[j], reserve[k] = reserve[k], arena[j]
                                k -= 1
                            print("Postacie zostały przeniesione na ławkę.")
                        else:
                            print("Za mało miejsca na ławce.")
        reserve = upgrade(b=reserve)
        print()
        print("Arena : ", *arena, sep=" | ", end=" |"'\n')
        print()
        print("Twoja ławka: ", *reserve, sep=" | ", end=" |"'\n')
        print()
        sell = [int(sell) for sell in get_input(text="Podaj numery postaci, które chcesz sprzedać: ").split()]
        for i in sell:
            if i != 0:
                if bench[i] == "–":
                    print("Sprzedaż nieudana to miejsce jest puste!")
                else:
                    money += int(shop[i][-1])
        q = str(get_input(text="Przejść Dalej? T/N: "))
        if q != "N" and q != "T":
            print("Niewłaściwy argument!!!")
        if q == "N":
            n = 0
    return money, reserve, arena


def get_round(money, reserve):
    if len(arena) < lvl:
        arena.append("–")
    q = ""
    shoproll()
    while q != "T":
        print()
        print(*shop, sep=" | ", end=" |"'\n')
        print("Złoto: ", money)
        print()
        buy = [int(buy) for buy in get_input(text="Podaj numery postaci, które chcesz kupić: ").split()]
        for i in buy:
            if i != 0:
                if shop[i] == "–":
                    print("Zakup nieudany postać zaostała już kupiona."'\n')
                elif money - int(shop[i][-1]) < 0:
                    print("Zakup nieduany za mało Złota."'\n')
                else:
                    try:
                        n = reserve.index("–")
                    except ValueError:
                        n = 0
                    reserve[n] = shop[i]
                    money -= int(shop[i][-1])
                    shop[i] = "–"
                    n += 1
        reserve = upgrade(b=reserve)
        print()
        print("Twoja ławka: ", *bench, sep=" | ", end=" |"'\n')
        print()
        q = str(get_input(text="Przejść Dalej? T/N: "))
    q = ""
    try:
        n = arena.index("–")
    except ValueError:
        n = -1
    while q != "T":
        champ_on_arena = [int(champ_on_arena) for champ_on_arena in
                          get_input(text="Podaj numer postaci, które chcesz wstawić na arenę: ").split()]
        if champ_on_arena[0] != 0:
            if champ_on_arena[0] != 10:
                for i in champ_on_arena:
                    i -= 1
                    if reserve[i] == "–" and arena[n] == "–":
                        print("Nie udało się wstawić postaci na arenę podane miejsce jest puste.")
                    else:
                        arena[n], reserve[i] = reserve[i], arena[n]
                        n -= 1
            else:
                clear = 0
                k = -1
                for i in reserve:
                    if i == "–":
                        clear += 1
                        if clear == len(arena):
                            for j in range(len(arena)):
                                arena[j], reserve[k] = reserve[k], arena[j]
                                k -= 1
                            print("Postacie zostały przeniesione na ławkę.")
        reserve = upgrade(b=bench)
        print()
        print("Arena : ", *arena, sep=" | ", end=" |"'\n')
        print()
        print("Twoja ławka: ", *reserve, sep=" | ", end=" |"'\n')
        print()
        sell = [int(sell) for sell in get_input(text="Podaj numery postaci, które chcesz sprzedać: ").split()]
        for i in sell:
            if i != 0:
                if reserve[i - 1] == "–":
                    print("Sprzedaż nieudana to miejsce jest puste!")
                else:
                    money += int(reserve[i - 1][-1])
                    reserve[i - 1] = "–"
        q = str(get_input(text="Przejść Dalej? T/N: "))
        if q != "N" and q != "T":
            print("Niewłaściwy argument!!!")
        if q == "N":
            n = 0
    return money, reserve, arena


def enemy():
    if runda == 1:
        enemyarena[0] = random.choice(lvl1champs)

    elif runda == 2:
        enemyarena.append(random.choice(u2lvl1champs))

    elif runda == 3:
        for i in range(len(enemyarena)):
            enemyarena[i] = random.choice(lvl2champs)

    elif runda == 4:
        enemyarena[1] = random.choice(u2lvl2champs)

    elif runda == 5:
        enemyarena.append(random.choice(u3lvl2champs))

    elif runda == 6:
        for i in range(len(enemyarena)):
            enemyarena[i] = random.choice(lvl3champs)

    elif runda == 7:
        enemyarena[1] = random.choice(u2lvl3champs)

    elif runda == 8:
        enemyarena[2] = random.choice(u2lvl3champs)

    elif runda == 9:
        enemyarena.append(random.choice(u3lvl2champs))

    elif runda == 10:
        for i in range(len(enemyarena)):
            enemyarena[i] = random.choice(lvl4champs)

    elif runda == 11:

        for i in range(0, 2):
            enemyarena[i] = random.choice(u2lvl4champs)

    elif runda == 12:
        enemyarena[2] = random.choice(u2lvl4champs)

    elif runda == 13:
        enemyarena.append(random.choice(u3lvl3champs))

    elif runda == 14:
        for i in range(len(enemyarena)):
            enemyarena[i] = random.choice(lvl5champs)

    elif runda == 15:
        for i in range(0, 2):
            enemyarena[i] = random.choice(u2lvl5champs)

    elif runda == 16:
        enemyarena[2] = random.choice(u2lvl5champs)

    elif runda == 17:
        enemyarena[3] = random.choice(u2lvl5champs)

    elif runda == 18:
        enemyarena.append(random.choice(u3lvl4champs))

    elif runda == 19:
        for i in range(len(enemyarena)):
            enemyarena[i] = random.choice(lvl6champs)

    elif runda == 20:
        enemyarena[0] = random.choice(u2lvl6champs)

    elif runda == 21:
        enemyarena[1] = random.choice(u2lvl6champs)

    elif runda == 22:
        enemyarena[2] = random.choice(u2lvl6champs)

    elif runda == 23:
        enemyarena.append(random.choice(u3lvl5champs))

    elif runda == 24:
        for i in range(len(enemyarena)):
            enemyarena[i] = random.choice(lvl7champs)

    elif runda == 25:
        enemyarena[0] = random.choice(u2lvl7champs)

    elif runda == 26:
        enemyarena[1] = random.choice(u2lvl7champs)

    elif runda == 27:
        enemyarena[2] = random.choice(u2lvl7champs)

    elif runda == 28:
        enemyarena[3] = random.choice(u2lvl7champs)

    elif runda == 29:
        enemyarena.append(random.choice(u3lvl6champs))

    elif runda == 30:
        for i in range(len(enemyarena)):
            enemyarena[i] = random.choice(lvl8champs)

    elif runda == 31:
        enemyarena[0] = random.choice(u2lvl8champs)

    elif runda == 32:
        enemyarena[1] = random.choice(u2lvl8champs)

    elif runda == 33:
        enemyarena[2] = random.choice(u2lvl8champs)

    elif runda == 34:
        enemyarena[3] = random.choice(u2lvl8champs)

    elif runda == 35:
        enemyarena.append(random.choice(u3lvl7champs))

    elif runda == 36:
        for i in range(len(enemyarena)):
            enemyarena[i] = random.choice(lvl9champs)

    elif runda == 37:
        for i in range(0, 2):
            enemyarena[i] = random.choice(u2lvl9champs)

    elif runda == 38:
        for i in range(2, 4):
            enemyarena[i] = random.choice(u2lvl9champs)

    elif runda == 39:
        for i in range(4, 6):
            enemyarena[i] = random.choice(u2lvl9champs)

    elif runda == 40:
        for i in range(0, 2):
            enemyarena[i] = random.choice(u3lvl9champs)


def upgrade(b):
    for j in range(2):
        upg = 1
        b.sort()
        for i in range(len(b)):
            if b[i] == "–":
                break
            elif b[i] == b[i + 1]:
                upg += 1
            else:
                upg = 1
            if upg == 3:
                for t2 in u2tierchamps:
                    if t2 == b[i]:
                        for at2 in u3tierchamps:
                            if at2[:-6] == t2[:-6]:
                                t2 = at2
                                if b[i][-5] == "2":
                                    b[i - 1] = t2
                                    b[i] = "–"
                                    b[i + 1] = "–"
                                else:
                                    continue
                for t1 in u1tierchamps:
                    if t1 == b[i]:
                        for at1 in u2tierchamps:
                            if at1[:-6] == t1[:-6]:
                                t1 = at1
                                if b[i][-5] == "1":
                                    b[i - 1] = t1
                                    b[i] = "–"
                                    b[i + 1] = "–"
                                else:
                                    continue
    return b


data = get_points_for_tiers()


def fight(health, win, loss, money, a, ea):
    avp = 0
    eavp = 0

    atanks = find_objects_on_arena(arena=a, objects=Tanks)
    aranged = find_objects_on_arena(arena=a, objects=Ranged)
    amages = find_objects_on_arena(arena=a, objects=Mages)
    awarriors = find_objects_on_arena(arena=a, objects=Warriors)
    asupports = find_objects_on_arena(arena=a, objects=Supports)
    aassasins = find_objects_on_arena(arena=a, objects=Assasins)
    amusicians = find_objects_on_arena(arena=a, objects=Musicians)
    abrothers = find_objects_on_arena(arena=a, objects=Brothers)
    a1tier = find_tiers_on_arena(arena=a, objects=tier1champs)
    a1tier2 = find_tiers_on_arena(arena=a, objects=u2tier1champs)
    a1tier3 = find_tiers_on_arena(arena=a, objects=u3tier1champs)
    a2tier = find_tiers_on_arena(arena=a, objects=tier2champs)
    a2tier2 = find_tiers_on_arena(arena=a, objects=u2tier2champs)
    a2tier3 = find_tiers_on_arena(arena=a, objects=u3tier2champs)
    a3tier = find_tiers_on_arena(arena=a, objects=tier3champs)
    a3tier2 = find_tiers_on_arena(arena=a, objects=u2tier3champs)
    a3tier3 = find_tiers_on_arena(arena=a, objects=u3tier3champs)
    a4tier = find_tiers_on_arena(arena=a, objects=tier4champs)
    a4tier2 = find_tiers_on_arena(arena=a, objects=u2tier4champs)
    a4tier3 = find_tiers_on_arena(arena=a, objects=u3tier4champs)
    a5tier = find_tiers_on_arena(arena=a, objects=tier5champs)
    a5tier2 = find_tiers_on_arena(arena=a, objects=u2tier5champs)
    a5tier3 = find_tiers_on_arena(arena=a, objects=u3tier5champs)

    eatanks = find_objects_on_arena(arena=ea, objects=Tanks)
    earanged = find_objects_on_arena(arena=ea, objects=Ranged)
    eamages = find_objects_on_arena(arena=ea, objects=Mages)
    eawarriors = find_objects_on_arena(arena=ea, objects=Warriors)
    easupports = find_objects_on_arena(arena=ea, objects=Supports)
    eaassasins = find_objects_on_arena(arena=ea, objects=Assasins)
    eamusicians = find_objects_on_arena(arena=ea, objects=Musicians)
    eabrothers = find_objects_on_arena(arena=ea, objects=Brothers)
    ea1tier = find_tiers_on_arena(arena=ea, objects=tier1champs)
    ea1tier2 = find_tiers_on_arena(arena=ea, objects=u2tier1champs)
    ea1tier3 = find_tiers_on_arena(arena=ea, objects=u3tier1champs)
    ea2tier = find_tiers_on_arena(arena=ea, objects=tier2champs)
    ea2tier2 = find_tiers_on_arena(arena=ea, objects=u2tier2champs)
    ea2tier3 = find_tiers_on_arena(arena=ea, objects=u3tier2champs)
    ea3tier = find_tiers_on_arena(arena=ea, objects=tier3champs)
    ea3tier2 = find_tiers_on_arena(arena=ea, objects=u2tier3champs)
    ea3tier3 = find_tiers_on_arena(arena=ea, objects=u3tier3champs)
    ea4tier = find_tiers_on_arena(arena=ea, objects=tier4champs)
    ea4tier2 = find_tiers_on_arena(arena=ea, objects=u2tier4champs)
    ea4tier3 = find_tiers_on_arena(arena=ea, objects=u3tier4champs)
    ea5tier = find_tiers_on_arena(arena=ea, objects=tier5champs)
    ea5tier2 = find_tiers_on_arena(arena=ea, objects=u2tier5champs)
    ea5tier3 = find_tiers_on_arena(arena=ea, objects=u3tier5champs)

    avp += count_victory_points(objects=atanks)
    avp += count_victory_points(objects=aranged)
    avp += count_victory_points(objects=amages)
    avp += count_victory_points(objects=awarriors)
    avp += count_victory_points(objects=asupports)
    avp += count_victory_points(objects=aassasins)

    if abrothers == 2:
        avp += 4
    elif abrothers == 1:
        avp -= 2
    # tiers
    avp += int(data['a1tier'][a1tier])
    avp += int(data['a1tier2'][a1tier2])
    avp += int(data['a1tier3'][a1tier3])
    avp += int(data['a2tier'][a2tier])
    avp += int(data['a2tier2'][a2tier2])
    avp += int(data['a2tier3'][a2tier3])
    avp += int(data['a3tier'][a3tier])
    avp += int(data['a3tier2'][a3tier2])
    avp += int(data['a3tier3'][a3tier3])
    avp += int(data['a4tier'][a4tier])
    avp += int(data['a4tier2'][a4tier2])
    avp += int(data['a4tier3'][a4tier3])
    avp += int(data['a5tier'][a5tier])
    avp += int(data['a5tier2'][a5tier2])
    avp += int(data['a5tier3'][a5tier3])
    eavp += int(data['ea1tier'][ea1tier])
    eavp += int(data['ea1tier2'][ea1tier2])
    eavp += int(data['ea1tier3'][ea1tier3])
    eavp += int(data['ea2tier'][ea2tier])
    eavp += int(data['ea2tier2'][ea2tier2])
    eavp += int(data['ea2tier3'][ea2tier3])
    eavp += int(data['ea3tier'][ea3tier])
    eavp += int(data['ea3tier2'][ea3tier2])
    eavp += int(data['ea3tier3'][ea3tier3])
    eavp += int(data['ea4tier'][ea4tier])
    eavp += int(data['ea4tier2'][ea4tier2])
    eavp += int(data['ea4tier3'][ea4tier3])
    eavp += int(data['ea5tier'][ea5tier])
    eavp += int(data['ea5tier2'][ea5tier2])
    eavp += int(data['ea5tier3'][ea5tier3])
    # percent upgrades
    if amusicians == 2:
        avp += avp // 4
    elif amusicians == 1:
        avp += avp // 10

    eavp += count_victory_points(objects=eatanks)
    eavp += count_victory_points(objects=earanged)
    eavp += count_victory_points(objects=eamages)
    eavp += count_victory_points(objects=eawarriors)
    eavp += count_victory_points(objects=easupports)
    eavp += count_victory_points(objects=eaassasins)
    if eabrothers == 2:
        eavp += 4
    elif eabrothers == 1:
        eavp -= 2
    # tiers

    # percent upgrades
    if eamusicians == 2:
        eavp += eavp // 4
    elif eamusicians == 1:
        eavp += eavp // 10

    if avp >= eavp:
        print("Wygrana")
        win += 1
        money += 8
    else:
        print("Przegrana")
        health -= 10
        loss += 1
        money += 4
    return health, win, loss, money


# intro()
# while runda < 40:
#     while hp > 0:
#         if lvl == 1:
#             print("Punkty życia: ", hp)
#             print("Runda: ", runda)
#             gold, bench, arena = rundalvl1(money=gold, reserve=bench)
#             enemy()
#             hp, victory, defeat, gold = fight(health=hp, win=victory, loss=defeat, money=gold, a=arena, ea=enemyarena)
#             xp += 4
#             lvl = get_level(experience_points=xp, level=lvl)
#             runda += 1
#             print("Wygrane walki: ", victory)
#             print("Przegrane walki: ", defeat)
#             print("Twój Poziom: ", lvl)
#         if lvl == 2 or lvl == 3 or lvl == 4 or lvl == 5 or lvl == 6 or lvl == 7 or lvl == 8 or lvl == 9:
#             print("Punkty życia: ", hp)
#             print("Runda: ", runda)
#             gold, bench, arena = get_round(money=gold, reserve=bench)
#             enemy()
#             hp, victory, defeat, gold = fight(health=hp, win=victory, loss=defeat, money=gold, a=arena, ea=enemyarena)
#             xp += 4
#             lvl = get_level(experience_points=xp, level=lvl)
#             runda += 1
#             print("Wygrane walki: ", victory)
#             print("Przegrane walki: ", defeat)
# print(arena)
# print(enemyarena)


# while hp > 0:
#     if lvl == 1:
#         rundalvl1(gold, lvl)
