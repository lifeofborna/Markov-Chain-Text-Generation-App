## Harjoitustyön toimivuutta ollaan testattu laitoksen tietokoneella ja mm virtuaalityöasemassa. 

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
