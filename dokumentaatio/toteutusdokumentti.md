
## Ohjelman yleisrakenne
 - Yleisrakenne muodostuu 4 eri kerroksesta, UI, data_analyzation, markovchain ja trie. UI tarkoituksena on 
 toimia käyttöliittymänä sovellukselle ja vastaa eri luokkien hyödyntämisestä. Data_analysis kerroksessa löytyy
 data_analysis.py, jonka tehtävänä on lukea ja puhdistaa data.  Markov vastaa itse markov-algoritmin mallin luomisesta. 
 Ja Trie vastaa sovelluksen tietorakennetta. 
 
 ## Saavutetut aika- ja tilavaativuudet (m.m. O-analyysit pseudokoodista)
  - Tietorakenteen, trie-tietorakenne, jonka aikavaativuus on O(W*L) missä W sanojen määrä ja L sanojen keskimääräinen pituus.
  - Trie luokan tilavaativuus on O(n) missä n on kaikkien syötettyhen sanojen kokonaismäärä. Tämä johtuu siitä, että huonoimmassa tapauksessa jokainen syötetty sana voisi olla "unique" sana mikä johtaisi uuden solmun luomiseen jokaiselle sanalle. Jokaiselle solmulle tarvittavan tilan määrä on vakio joten tilankompleksisuus on suoraan verrannollinne syötettyjyen sanojen määrään.  

  - Markov luokassa taas funktion construct_markov_model aikavaativuus on O(n), missä n on syötetyn tekstin pituus. Tämä johtuu siitä, että funktio suorittaa kaksi operaatiota, joiden aikavaativuus on O(n): create_graph_with_ngram- ja generate_text-funktiot. Tilavaativuus on O(m), missä m on trie-puun solmujen kokonaismäärä. Tämä johtuu siitä, että trie-puuhun lisätään solmuja tekstin perusteella.

  - Markov luokassa olevan funktion "Generate text" funktion aikavaativuus on O(n * m), missä n on silmukan ulkopuolisen silmukan iteraatioiden lukumäärä ja m on silmukan sisemmän silmukan iteraatioiden lukumäärä. Sisempi silmukka luo yhden tekstin käymällä läpi trien ja tekemällä satunnaisen valinnan jokaisella solmulla perustuen solmun lapsien painoihin. Tämä vie aikaa O(m). Ulompi silmukka luo 20 tekstiä tällä tavalla, joten kokonaisaikavaativuus on siten O(n * m).

  - Data analyysi luokassa taas Funktion read_from_file aikavaativuus on O(n), missä n on tiedoston rivien kokonaismäärä. Tämä johtuu siitä, että funktio lukee tiedoston rivit ja käy läpi ne clean_text_file-funktiossa. Tilavaativuus on O(m), missä m on käsiteltyjen sanojen kokonaismäärä. Tämä johtuu siitä, että funktio tallentaa kaikki käsiteltyt sanat listaan.

  - Funktion clean_text_file aikavaativuus on O(n), missä n on syötettyjen rivien kokonaismäärä. Tämä johtuu siitä, että funktio käy läpi jokaiset syötetyn tekstin rivit ja käsittelee niitä. Tilavaativuus on O(m), missä m on käsiteltyjen sanojen kokonaismäärä. Tämä johtuu siitä, että funktio tallentaa kaikki käsiteltyt sanat listaan.
  
  
 ## Työn mahdolliset puutteet ja parannusehdotukset
  - Selkeämpi koodi. 
 ## Lähteet
  - https://www.wikiwand.com/en/Markov_chain
  - https://www.wikiwand.com/en/Trie
  - dataset: https://www.kaggle.com/datasets/muhammedfathi/game-of-thrones-book-files
  - ascii art: https://emojicombos.com/game-of-thrones-ascii-art
