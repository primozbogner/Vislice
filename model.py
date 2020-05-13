import random

STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo.upper()
        self.crke = [] if crke is None else [crka.upper() for crka in crke]

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def poraz(self):
        return self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK

    def zmaga(self):
        return set(self.geslo) == set(self.pravilne_crke())

    def pravilni_del_gesla(self):
        pravilni_del = ''
        for znak in self.geslo:
            pravilni_del += znak if znak in self.crke else '_'
        return pravilni_del
        
    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()

        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
            if crka in self.geslo:
                if self.zmaga():
                    return ZMAGA
                else:
                    return PRAVILNA_CRKA

            else:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA

bazen_besed = []
for beseda in open('besede.txt', encoding="utf-8"):
    bazen_besed.append(beseda.strip().upper())

def nova_igra():
    beseda = random.choice(bazen_besed)
    return Igra(beseda)
