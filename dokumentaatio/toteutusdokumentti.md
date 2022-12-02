
## Ohjelman yleisrakenne
 - Yleisrakenne muodostuu 4 eri kerroksesta, UI, data_analyzation, markovchain ja trie. UI tarkoituksena on 
 toimia käyttöliittymänä sovellukselle ja vastaa eri luokkien hyödyntämisestä. Data_analysis kerroksessa löytyy
 data_analysis.py, jonka tehtävänä on lukea ja puhdistaa data.  Markov vastaa itse markov-algoritmin mallin luomisesta. 
 Ja Trie vastaa sovelluksen tietorakenteena. 
 
 ## Saavutetut aika- ja tilavaativuudet (m.m. O-analyysit pseudokoodista)
  - Tietorakenteen, trie-tietorakenne, jonka aikavaativuus on O(W*L) missä W sanojen määrä ja L sanojen keskimääräinen pituus.

 ## Työn mahdolliset puutteet ja parannusehdotukset
  - Aikavaativuutta voisi parantaa kun lasketaan todennäköisyydet siirtymille. 
 ## Lähteet
  - dataset: https://www.kaggle.com/datasets/muhammedfathi/game-of-thrones-book-files
  - ascii art: https://emojicombos.com/game-of-thrones-ascii-art
