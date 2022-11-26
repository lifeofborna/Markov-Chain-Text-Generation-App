# Testausdokumentti
Sovellusta on luota erillaisia unittestejä jolla testataan yksikkötestejä. Integraatio testejä on myös luotu 
esim markov luokkien testamiisessa joudutaan käyttämään trie luokkaa. 

## Yksikkö ja integraatiotestaus
Tällä hetkellä testejä on luotu kaikille olennaisille luokille esim markov/trie/data_analysis. Varmistetaan, että data on puhdasta eikä sisällä esimerkiksi ei haluttuja merkkejä. Testataan graafin luominen luo oikean graafin. Testaus myös
tarkistaa että todennäköisyydet ovat oikein laskettuja myös graafissa. Testit myös varmistavat, että 
sovellus luo tekstiä oikealla lähtökohdalla. 

## Testauskattavuus
Kattaa tällä hetkellä kaikki olennaiset luokat sovelluksessa. 
![Kuva](https://github.com/lifeofborna/Markov-Chain-Text-Generation-App/blob/main/dokumentaatio/kuvat/coveragerep.png)
