============================================
El robot profesor
============================================

El problema
===========

El día a día en el aula, de un profesor, es muy díficil. Entra en su clase y no puede salir hasta que toque el timbre. Se siente como dentro de un espacio rodeado de una línea negra.

A medida que avanza la clase se va encuentrando con alumnos, cada uno con su situación particular. Algunos alumnos están de mal humor, rojos de ira, otros están muy felices y contentos, pero su atención está en otra parte, y lo simulamos con un cuadrado azul. Cada vez que nos encontremos con uno enfadado vamos a decir "Hola, ¿como estás?", si está distraido simplemente le diremos "Presta atención". Y seguimos con nuestra clase tranquilamente.

Hay muchos más alumnos con los que podemos interactuar tranquilamente, y alguno que es un obstáculo. En este caso está totalmente bloqueado y es mejor detectarlo antes de interactuar con él y dejarlo tranquilo. Este mundo simulado lo podemos ver con esta escena predeterminada en ORL:

.. image:: /_static/imags/esc-2.webp

¿Puedes realizar un programa con un robot que refleje el movimiento del profesor mientras va dando su clase?

.. dropdown:: Solución
   :animate: fade-in
   :color: info

   El algoritmo no es tan complicado y es similar a retos anteriores añadiendo una condición de parada:

   #. Avanzo de forma continua
	 
      #. Si encuentro un alumno enfadado
	 
	 #. Digo que "Hola, ¿como estás?"
	 #. Me detengo 1 segundo y sigo avanzando
	    
      #. Si encuentro un alumno contento, pero distraido
	 
	 #. Digo que "Hola!, presta atención"
	 #. Me detengo 1 segundo y sigo avanzando
	    
      #. Si encuentro el limite de la clase (el borde negro) OR Si encuentro un obstáculo
	 
	 #. Giro y sigo avanzando

      He **usado variables** porque así se entiende mejor el programa y puedo ir ajustando los valores. De hecho, en mis simulaciones, según los valores que pongas ahí (por ejemplo una velocidad alta) el robot se sale de la línea negra y tarda en volver a entrar.

      Además he usado **una operación OR para agrupar** las condiciones de giro, que es cuando el color detectado es el negro (el límite) o el alumno bloqueado (el cuadrado azul).

   .. image:: /_static/imags/reto-8.webp
      :width: 100%

   Y además, para este último ejemplo, lo he descargado como un archivo y lo puedes descargar ( :download:`/retos/reto-8.xml`) y luego importar en ORL.
