# Sim Server Log

Skript mis imiteerib serveri tööd kirjutades serveri tegevusi logi faili. 

# Paigaldus
1. Tee PyCharmiga uus projekt läbi versiooni kontrolli (_Version Control_) File -> New Project from Version Control
2. URL reale kleebi Githubi .git link (ja nupule **Clone**)
3. Peale seda võta PyCharmis terminal ning kirjuta ``` pip install -r requirements.txt ```
   * See paigaldab [Faker](https://faker.readthedocs.io/en/master/) mooduli ja mooduli sõltuvused
4. Järgnevaks saad käivitada skripti **run_server.py**

# Töötamine
Käivitades skripti jääb see lõputult tööle kirjutades iga 1-5 sekundi tagant logi faili mingi tegevuse. Samal ajal seda 
ka konosoli näidates. Logi tehakse c:\Temp kausta nimega application.log. Kui logi fail on saavutanud skriptis määratud 
mahu (10kB), siis tehakse sellest eraldi fail mille lõppu lisatakse .1 (application.log.1) ning logi kirjutamist 
jätakatase jälle application.log faili. 

Igakord kui skript uuesti käivitatakse kustutatakse eelnevad logid ära ja alustatakse uuesti logide loomist.
