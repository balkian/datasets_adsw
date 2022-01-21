Esta carpeta contiene datos de películas y su elenco. Los archivos principales son:

* `metadata.tsv`. Datos de películas extraídos del dataset de Kaggle, eliminando algunas columnas y transformando otras para tener una estructura más limpia.
* `cast.tsv`. El elenco de cada película. La primera columna es el id de la película, el resto de columnas son nombres de cada actor.

Los valores están separados por tabuladores para facilitar el procesamiento.
Como los ficheros son grandes y difíciles de visualizar en GitHub, se añade un ejemplo de ambos más adelante.
Cada fichero tsv tiene también el código asociado que se usó para generarlo.

Para facilitar las pruebas, hay varios ficheros de tamaño más reducido:
* `metadata_top100.tsv`. Datos de las 100 películas más populares
* `cast_bacon.tsv` Cast de películas en las que aparece Kevin Bacon

También está el fichero `metadata_sorted.csv`, que contiene las películas ordenadas por orden de popularidad, para facilitar la tarea de crear versiones reducidas del dataset.

# Ejemplo metadata


|popularity|vote_average|vote_countid|imdb_id|original_title|budget|genres|homepage|original_language|overview|release_date|revenue|runtime|spoken_languages|tagline|title|adult|
|----------|------------|------------|-------|--------------|------|------|--------|-----------------|--------|------------|-------|-------|----------------|-------|-----|-----|
|21.946943|7.7||tt0114709|Toy Story|30000000|Animation,Comedy,Family|http://toystory.disney.com/toy-story|en|Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.|1995-10-30|373554033|81.0|en||Toy Story|False|
|17.015539|6.9||tt0113497|Jumanji|65000000|Adventure,Fantasy,Family||en|When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who's been trapped inside the game for 26 years -- into their living room. Alan's only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.|1995-12-15|262797249|104.0|en,fr|Roll the dice and unleash the excitement!|Jumanji|False|

# Ejemplo de cast

```
862	Tom Hanks	Tim Allen	Don Rickles	Jim Varney	Wallace Shawn	John Ratzenberger	Annie Potts	John Morris	Erik von Detten	Laurie Metcalf	R. Lee Ermey	Sarah Freeman	Penn Jillette
8844	Robin Williams	Jonathan Hyde	Kirsten Dunst	Bradley Pierce	Bonnie Hunt	Bebe Neuwirth	David Alan Grier	Patricia Clarkson	Adam Hann-Byrd	Laura Bell Bundy	James Handy	Gillian Barber	Brandon Obray	Cyrus Thiedeke	Gary Joseph Thorup	Leonard Zola	Lloyd Berry	Malcolm Stewart	Annabel Kershaw	Darryl Henriques	Robyn Driscoll	Peter Bryant	Sarah Gilson	Florica Vlad	June Lion	Brenda Lockmuller
...
```




# Source

The original dataset can be found on Kaggle (https://www.kaggle.com/rounakbanik/the-movies-dataset) under the CC0 Public Domain license
