# Sim Server Log

Skript mis imiteerib serveri tööd kirjutades serveri tegevusi logi faili. Lisaks teeb kausta suvalisel hetkel 
mõngingaid teenuste logi faile mida siis ka ära kustutab. 

# Paigaldus
1. Tee PyCharmiga uus projekt läbi versiooni kontrolli (_Version Control_) File -> New Project from Version Control
2. URL reale kleebi Githubi .git link (ja nupule **Clone**)
   * Usalda projekti (Trust Project)
   * Ava endale sobivas aknas
3. Seadista Python Interpreter -> Add New Interpreter -> Add Local Interpreter -> OK
   * Kui küsib kas installida requirements võib lubada, kuid järgmist punkti ära tee ning käivita PyCharm uuesti
4. Peale seda võta PyCharmis terminal (Alt + F12) ning kirjuta ``` pip install -r requirements.txt ```
   * See paigaldab [Faker](https://faker.readthedocs.io/en/master/) mooduli ja mooduli sõltuvused
5. Järgnevaks saad käivitada skripti **run_server.py**

# Töötamine
Käivitades skripti jääb see lõputult tööle kirjutades iga 1-5 sekundi tagant logi faili mingi tegevuse. Samal ajal seda 
ka konosoli näidates. Logi tehakse c:\Temp kausta nimega application.log. Kui logi fail on saavutanud skriptis määratud 
mahu (10kB), siis tehakse sellest eraldi fail mille lõppu lisatakse .1 (application.log.1) ning logi kirjutamist 
jätakatase jälle application.log faili. Kõige vanem logi fail on .9 lõpuga ja kõige uuem .log ehk hetkel kasutatav fail.

Igakord kui skript uuesti käivitatakse kustutatakse eelnevad logid ära ja alustatakse uuesti logide loomist.
