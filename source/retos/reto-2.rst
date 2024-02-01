=============================
Avanzar y Retroceder
=============================

El problema
===========

Necesito programar un robot que se mueva hacia adelante, se pare 2
segundos y luego retroceda la mitad de lo que ha avanzado. Es decir,
no queremos que llegue a la situación de inicio, sino que se pare a
medio camino.

Nos da igual la velocidad y la distancia, queda a criterio del programador.

.. dropdown:: Solución
   :color: info
   :animate: fade-in

   Aunque es muy sencillo, el algoritmo nos obliga a tener en cuenta
   varios pasos:

   #. Avanzar hacia adelante. Vamos a suponer 50 cm a velocidad 50.
   #. Parar 2 sg. Los valores han de estar en milisegundos, es decir, el valor a poner en el bloque de "parar" o "esperar" será de      2.000
   #. Avanzar hacia atrás, 25 cm (la mitad) a la misma velocidad (50).

   El bloque "esperar" está en el menú de "control" (no es una acción
   propiamente dicha). El programa de bloques es el siguiente:
   
   .. image:: /_static/imags/reto-2.webp

   El escenario de la simulación, en este caso, tampoco influye.
