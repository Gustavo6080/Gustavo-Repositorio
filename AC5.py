import random

def AC5():
    vida_aven = 100
    atak_aven = random.randint(10, 20)
    defe_aven = random.randint(1,5)
    print("Aventureiro: ", vida_aven, atak_aven, defe_aven)
    vida_mons = random.randint(60, 80)
    atak_mons = random.randint(20, 30)
    print("Monstro: ", vida_mons, atak_mons)

    rodada = 1

    while vida_aven > 0 and vida_mons > 0:
        print("Rodada ", rodada)
        dano_aven= random.randint (1, atak_aven)
        vida_mons -= dano_aven
        print("Aventureiro ataca o Monstro causando", dano_aven)

        vida_mons = vida_aven - random.randint (1, atak_mons)
        if vida_mons <= 0:
            print ("O Monstro morreu! ")
            break

        dano_mons = random.randint(1, atak_mons) - defe_aven
        if dano_mons < 0:
            dano_mons = 0
        vida_aven -= dano_mons
        print("Monstro ataca o Aventureiro causando ", dano_mons )
        if vida_aven <= 0:
            print("O Aventureiro morreu!")
            break

        rodada += 1

    print("Aventureiro vida, Ataque, Defesa ", vida_aven, atak_aven, defe_aven)
    print("Vida do Monstro, Ataque do monstro ", vida_mons, atak_mons)


AC5()