def atack(atacker, defender):
    if atacker.who == "Aggressor" or defender.who == "Aggressor":
        defender.hp -= atacker.damage/defender.defence
        atacker.hp -= defender.damage/atacker.defence
    if atacker.who == "Egoist" and defender.who == "Egoist":
        defender.hp -= atacker.damage/defender.defence
        atacker.hp -= defender.damage/atacker.defence
    if atacker.who == "Egoist" and defender.who == "Altruist":
        if atacker.hp <= 50:
            atacker.hp, defender.hp = atacker.hp+0.33*defender.hp, defender.hp*0.67
        else:
            defender.hp -= atacker.damage/defender.defence
            atacker.hp -= defender.damage/atacker.defence
    if atacker.who == "Altruist" and defender.who == "Altruist":
        atacker.hp, defender.hp = (atacker.hp + defender.hp)/2, (atacker.hp + defender.hp)/2
    if atacker.who == "Altruist" and defender.who == "Egoist":
        if defender.hp <= 50:
            atacker.hp, defender.hp = atacker.hp*0.67, defender.hp+0.33*atacker.hp
    return None
