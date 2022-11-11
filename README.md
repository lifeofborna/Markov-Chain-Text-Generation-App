# *Tietorakenteet ja algoritmit harjoitustyö: Tekstin generointi sovellus*

Sovelluksen ideana on tekstin generoiminen teksidatasta esim. kirjasta hyödyntämällä markovin ketjua ja trie-tietorakennetta. 


## Dokumentaatio
[Vaatimusmäärittely](https://github.com/lifeofborna/Tiralabra/blob/main/dokumentaatio/vaatimusm%C3%A4%C3%A4rittely.md)

[Viikkoraportti 1](https://github.com/lifeofborna/Tiralabra/blob/main/dokumentaatio/Viikkoraportti%201.md)

## Asennus

1. Tarvittavien riippuvuuksien asentaminen:
>**poetry install**

2. Sovelluksen käynnistäminen tapahtuu seuraavasti:
>**poetry run invoke start**


## Komentorivitoiminnot

### Sovelluksen käynnistys:
>**poetry run invoke start**

### Sovelluksen testien suoritus
>**poetry run invoke test**

### Testikattavuuden suoritus
> **poetry run invoke coverage-report** 
> 
Raportti löytyy htmlcov hakemistosta.

### Pylint tarkistukset suoritetaan:
> **poetry run invoke lint**
