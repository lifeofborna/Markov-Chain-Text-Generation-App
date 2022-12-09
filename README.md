# *Tietorakenteet ja algoritmit harjoitustyö: Tekstin generointi sovellus*

Sovelluksen ideana on tekstin generoiminen teksidatasta esim. kirjasta hyödyntämällä markovin ketjua ja trie-tietorakennetta. 

Testikattavuus: ![GHA workflow badge](https://github.com/lifeofborna/Tiralabra/workflows/CI/badge.svg)

## Dokumentaatio
[Vaatimusmäärittely](https://github.com/lifeofborna/Tiralabra/blob/main/dokumentaatio/vaatimusm%C3%A4%C3%A4rittely.md)

[Viikkoraportti 1](https://github.com/lifeofborna/Tiralabra/blob/main/dokumentaatio/Viikkoraportti%201.md)

[Viikkoraportti 2](https://github.com/lifeofborna/Tiralabra/blob/main/dokumentaatio/viikkoraportti2.md)

[Viikkoraportti 3](https://github.com/lifeofborna/Markov-Chain-Text-Generation-App/blob/main/dokumentaatio/viikkoraportti3.md)

[Viikkoraportti 4](https://github.com/lifeofborna/Markov-Chain-Text-Generation-App/blob/main/dokumentaatio/viikkoraportti4.md)

[Viikkoraportti 5](https://github.com/lifeofborna/Markov-Chain-Text-Generation-App/blob/main/dokumentaatio/viikkoraportti5.md)

[Viikkoraportti 6](https://github.com/lifeofborna/Markov-Chain-Text-Generation-App/blob/main/dokumentaatio/viikkoraportti6.md)

[Toteutus dokumentaatio](https://github.com/lifeofborna/Markov-Chain-Text-Generation-App/blob/main/dokumentaatio/toteutusdokumentti.md
)

[Testaus dokumentaatio](https://github.com/lifeofborna/Markov-Chain-Text-Generation-App/blob/main/dokumentaatio/testausdokumentaatio.md
)

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
