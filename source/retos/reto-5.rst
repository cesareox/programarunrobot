===============================
Cuadrados dentro de un cuadrado
===============================

El problema
===========

Un reto más avanzado para trabajar el recorrido de un robot, creando
figuras geométricas (cuadrados) conectados entre sí.

Queremos programar un robot que, activando su rastro, genere la figura
descrita en la siguiente imagen. Son 2 cuadrados de 15 cm de lado,
dentro de un cuadrado más grande, de 45 cm de lado.

.. image:: /_static/imags/reto-5.webp

El robot deberá volver al punto de partida y, al llegar, dirá "terminé
mi recorrido".

.. dropdown:: Solución
   :color: info
   :animate: fade-in

   Vemos que hay varios movimientos que se repiten. Recuerda que
   puedes copiar/pegar bloques o conjuntos de bloques, de forma
   sencilla.

   El algoritmo lo podriamos diseñar en dos fases, una más genérica y
   otra más concreta:

   #. Avanzar
   #. Crear el primer cuadrado
   #. Avanzar
   #. Crear el segundo cuadrado
   #. Avanzar
   #. Parar y decir "terminé mi recorrido"

   Y para concretar el algoritmo necesitamos concretar cuánto avanza y cómo se crear un cuadrado (revisa :doc:`reto-4`).

   Aquí puedes ver una propuesta de solución.:
      
   .. image:: /_static/imags/reto-5-sol.webp

   El escenario de la simulación, en este caso, tampoco influye. Pero
   probando con uno sencillo, verás que muchas veces la simulación no
   se corresponde con la realidad.

   .. image:: /_static/imags/reto-5-sol2.webp

