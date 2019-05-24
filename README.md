# Clasificador de libros basado mediante lenguaje natural

Este proyecto ha sido realizado por _Adrián Álvarez_ para la asignatura de _Inteligencia Artificial Avanzada_ impartida por la _Universidad de La Laguna_ durante el curso 2018/2019.

```
 ├── lib                    # Directorio que contiene los módulos ejecutables del programa.
     ├── categories.txt     # En este fichero se escriben las categorías de las que se desea
     ├─                     # obtener el nombre de los títulos.
     ├── scraper.py         # Módulo que se encarga de rascar los títulos de goodreads.
     ├── files_to_arff.py   # Módulo que se encarga de fusionar los corpus obtenidos y de
                            # transformarlos a un formato compatible para la lectura en weka.

 ├── outputs                # Directorio en el que se almacenan todos los corpus obtenidos a
                            # partir del módulo scraper.py

 ├── arff_files             # Directorio que contiene ficheros arff obtenidos con el programa,
                            # para ver los resultados de la clasificación en weka.
```
