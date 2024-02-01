============================================
Detectando y evitando obstáculos (y colores)
============================================

El problema
===========

Desde el reto anterior (:doc:`reto-6`) ahora queremos que gire si encuentra un obstáculo O si encuentra una zona de color rojo.

.. dropdown:: Solución
   :color: info
   :animate: fade-in
	     
   El algoritmo en este caso es el mismo, lo único que cambia es la condición. Pongo la operación lógica en inglés (OR) para que te des cuenta

   #. Repite indefinidamente
      
      #. Avanzar a una velocidad de 50

      #. Si detecta un obstáculo (a 20cm) *OR* **detecto una zona de color rojo**

	 #. Se para
	 #. Habla y dice el texto
	 #. Gira 100º a la derecha

      #. Sigue con el bucle

   .. image:: /_static/imags/reto-7.webp
      :width: 100%
	      


