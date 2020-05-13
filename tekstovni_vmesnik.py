import model, izris_stanja

def izpis_igre(igra):
    return (
        f"Uganjene del gesla: {igra.pravilni_del_gesla()}\n"+
        f"Neuspeli poskusi: {igra.nepravilni_ugibi()}\n" +
        f"{izris_stanja.izris(igra)}\n"
    )
      
def izpis_zmage(igra):
    return (
        "Čestitam, uganil si geslo {}.\n".format(igra.geslo) +
        "Uspelo ti je v {} poskusih.\n".format(len(igra.crke)) +
        """
          \u263A/
         /|
         / \\
"""
    )

def izpis_poraza(igra):
    return (
        "Porabil si vse poskuse.\n" +
        "Pravilno geslo je bilo {}.\n".format(igra.geslo) +
        f"{izris_stanja.izris(igra)}\n"
    )

def zahtevaj_vnos():
    crka = input('Vnesi črko: ')
    if crka not in 'aAbBcCčČdDeEfFgGhHiIjJkKlLmMnNoOpPrRsSšŠtTuUvVzZžŽ':
        print('Prosim vnesi veljaven znak.')
        return zahtevaj_vnos()
    else:
        return crka

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        poskus = zahtevaj_vnos()
        stanje = igra.ugibaj(poskus)
        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break
    ponovna_igra = input('Ali želite ponovno igrati (DA/NE)? ')
    if ponovna_igra in 'DAda1':
        return pozeni_vmesnik()

pozeni_vmesnik()