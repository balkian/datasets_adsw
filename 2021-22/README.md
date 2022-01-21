Esta carpeta contiene:

* `metadata.tsv`, datos de películas extraídos del dataset de Kaggle, eliminando algunas columnas y transformando otras para tener una estructura más limpia.
* `cast.tsv`, un fichero con el elenco de cada película. La primera columna es el id de la película.

Los valores están separados por tabuladores para facilitar el procesamiento.
Para cada fichero tsv tiene también el código asociado que se usó para generarlo.

Para facilitar las pruebas, hay varios ficheros de tamaño más reducido:
* `metadata_top100.tsv`. Datos de las 100 películas más populares
* `cast_bacon.tsv` Cast de películas en las que aparece Kevin Bacon

También está el fichero `metadata_sorted.csv`, que contiene las películas ordenadas por orden de popularidad, para facilitar la tarea de crear versiones reducidas del dataset.


# Source

The original dataset can be found on Kaggle (https://www.kaggle.com/rounakbanik/the-movies-dataset) under the CC0 Public Domain license
