================================
Detectando y evitando obstáculos
================================

El problema
===========

Vamos a simular un robot que se va a mover continuamente en su mundo
simulado. Se va a ir moviendo de tal manera que cuando encuentre un
obstáculo, para y gira 100 grados a la derecha para esquivarlo. Y
sigue avanzando a una velocidad de 50.

Verás que el robot no parará nunca y simplemente recorrerá todo el
escenario detectando obstáculos (los bordes son obstáculos también) y esquivándolos. Como si tuviera un **propósito propio** (recuerda la definición de un robot - :doc:`/sesiones/robots`). 

Además, cada vez que encuentre un obstáculo, dirá **Encontré un obstáculo. Giro y avanzo**. Para ver qué escribe en la pantalla tendrás que activar la vista de robot.

.. dropdown:: Solución
   :color: info
   :animate: fade-in
	     
   Ya se van complicando un poquito los retos. En este caso se incluyen instrucciones de los tres tipos, y además tienes que obtener valores de los sensores e incluirlos en las condiciones de las instrucciones. En este caso el algoritmo será el siguiente:

   #. Repite indefinidamente
      
   #. Avanzar a una velocidad de 50

   #. Si detecta un obstáculo (a 20cm):

      #. Se para
      #. Habla y dice el texto
      #. Gira 100º a la derecha

   #. Sigue con el bucle

   .. image:: /_static/imags/reto-6.webp
      :width: 100%

   Usé también una variable (*giro*) aunque no es imprescindible. Eso
   te permite, de forma sencilla ver como se comporta sin en vez de
   girar 100º, gira 125º. Haz la prueba.
	      


