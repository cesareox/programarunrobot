===============================
Avanzando con la programación
===============================

.. admonition:: Preguntas
   :class: hint

   ¿Todos los programas son lo mismo? ¿Cuántos bloques debe tener mi programa? ¿Cómo resuelves un reto que no hayas realizado previamente?

El mundo simulado del robot
---------------------------

Los robots, aunque se mueven en el mundo real, **no ven el mundo
real**. Funcionan en un mundo virtual, **un mundo simulado**. En el
caso de ORL se pueden usar, crear y modificar mundos simulados en base
a unas escenas precargadas (imágenes de fondo). 

ORL tiene de forma predeterminada algunas escenas que puedes cambiar usando el botón "Cambiar
la escena". Estos escenarios dependen del tipo de robot (en nuestro caso
EV3dev). El robot es el mismo, el programa es el mismo, pero puedes
cambiar su mundo simulado. Por ejemplo estos 4:

.. list-table:: 
   :widths: 50 70
   :header-rows: 0

   * - .. image:: /_static/imags/esc-1.webp
     - .. image:: /_static/imags/esc-2.webp
   * - .. image:: /_static/imags/esc-3.webp
     - .. image:: /_static/imags/esc-4.webp

Como ves, un **escenario no es más que una imagen**. Como si fuera un
mapa del mundo simulado en el que se moverá el robot.

Y **sobre ese mundo simulado**, podemos colocar diferentes figuras
geométricas (cuadrado, rectángulo y círculo) para:

#. Añadir obstáculos. El robot detecta obstáculos (necesita un
   sensor), pero no lo puede atravesar.
#. Añadir zonas de color. El robot detecta el color (según los
   sensores que tenga) de las zonas por las que pasa.

Y así, **puedes generar diferentes mundos simulados** para
que tu robot interactúe. El límite está en tu imaginación. En
proyectos STEAM te permite simular el mundo real creando mundos
simulados según tus necesidades. Pero tendrás que hacer una
equivalencia entre el mundo real que quieres simular, y las
herramientas de simulación que te da el software (en este caso figuras
geométricas que o son obstáculos o zonas de color). Además tienes el
límite del escenario (los bordes), que de por sí es un obstáculo.

.. include:: /actividades/S04-A01.inc

Acciones y Sensores
-------------------

En los primeros 5 retos hemos podido ver **algunas de las acciones**
que se permiten con el robot EV3dev:

#. Avanzar y retroceder
#. Girar
#. Hablar

Pero **realmente hay más**, por ejemplo:

#. Parar
#. Reproducir tonos (de duración y frecuencia determinada)
#. Encender diferentes luces del robot

En el **menú acciones** verás qué cosas puedes hacer, según el robot
que escojas.

Por otra parte, tenemos los sensores. Según vimos en :doc:`simulador`, a 
la hora de configurar un robot, podemos configurar qué sensores tenemos
disponibles. Algunos ejemplos los podemos ver en la siguiente imagen:

.. image:: /_static/imags/sensores.webp
   :width: 100%

Hay que **prestar atención** al  valor o acción que 
devuelve el resultado del bloque del sensor. Según la forma del
conector del bloque y su color, se podrán utilizar de una forma u
otra. Depende de cada tipo de robot y sensor.

Ten en cuenta que **no todos los resultados de un sensor** se
pueden utilizar en cualquier lugar. La gran ventaja es que hay
muchísimas posibilidades según el robot que se utilice.

.. admonition:: Ten en cuenta la etapa educativa
   :class: warning

   Es **muy importante** tener en cuenta el nivel educativo de tu
   estudiante. Ojo a no plantearle conceptos demasiado complejos sin
   ir paso a paso.

   Este material debería funcionar sin problemas para mayores de 14
   años, y probable en mayores de 12. Pero nadie como el profesor para
   conocer a su estudiante. Porque una cosa es la edad cronológica y
   otra la edad "cognitiva".
   

Variables y Operaciones
---------------------------------

En la práctica, la programación tiene muchos conceptos en los que
habría que profundizar. Pero en un contexto de iniciación, además de
lo que ya hemos visto es bueno profundizar en dos conceptos
importantes: las variables y las operaciones.
Son dos aspectos importantes en cualquier lenguaje de programación y permiten resolver problemas más complejos. Veremos los aspectos más básicos y es un buen momento para iniciarse en su uso.

Variables y Valores
-------------------

Una variable es **un identificador de un valor**, un dato concreto. Y recuerda que un valor puede ser un número, un texto, un valor lógico (booleano). Es lo que llamamos el tipo del dato. Tres ejemplos:

#. 5 es un valor, y su tipo de datos es número
#. "Hola, soy un robot" es un valor y su tipo de dato es texto. Es una cadena de texto, y lo sabemos porque lo ponemos entre comillas
#. Verdadero es un valor y su tipo de datos es booleano (lógico). Es
   un valor "especial" y sólo existen dos valores de ese tipo: Verdadero o Falso.

Una variable es como una caja en la que ponemos un valor. A esa
variable le ponemos un nombre, que lo llamamos identificador, y
siempre que pongamos el nombre (de la caja), es lo mismo que poner el valor. Es el equivalente a
las variables que usamos en matemáticas. Por ejemplo

.. image:: /_static/imags/variables.webp
   :width: 100%
	   
En este caso hemos usado una **instrucción de asignación** (un bloque especial), donde asignamos un valor a esa variable (*Giro*). Siempre que se use como *Giro* lo va a sustituir
por el valor (número) que le hemos asignado (en este caso 100). 

En el caso de ORL las variables del programa se añaden (y se asignan) al principio, dentro del bloque "Inicio del
programa". Pueden ser útiles en muchos casos, generalmente para simplificar el uso del programa. Por ejemplo:

#. Para no repetir siempre un mismo valor
#. Para configurar un valor al principio y cambiar el comportamiento del programa
#. Para modificar el valor a lo largo del problema, según las necesidades del programa

Operaciones
~~~~~~~~~~~

Y tanto los valores, como las variables, se utilizan en expresiones
usando diferentes tipos de operaciones. Estas expresiones son operaciones sobre valores, los operandos, que dan como resultado un valor. Es el equivalente a una fórmula matemática. Estos son los tres grupos de operaciones más habituales:

#. las **aritméticas**: las habituales de sumar, restar, etc. Su resultado es numérico. Sirven para crear expresiones aritméticas.
#. las **de comparación**: mayor, menor, igual a. Su resultado es un valor lógico (Verdadero/Falso). Sirven para crear expresiones lógicas.
#. las **lógicas**. Su resultado es un valor lógico
   
Las operaciones lógicas (AND / OR) permiten obtener expresiones
lógicas que son resultado de varias operaciones, es decir, es un
cálculo especial de valores verdadero/falso. Generalmente construímos
expresiones (*fórmulas*) usando diferentes operaciones. Veamos el
siguiente ejemplo:
	   
.. image:: /_static/imags/operadores.webp
   :width: 100%

#. Se obtiene un valor del sensor de colores y **se compara** con un valor especial
   (un color). El resultado será Verdadero (el color que se obtiene
   del sensor es rojo) o Falso (no lo es).
#. Se obtiene la distancia a un obstáculo, desde el sensor de
   ultrasonidos y se compara con el valor 20 (cm). Si el valor es
   menor, el resultado es Verdadero.
#. Se realiza la **operación lógica O** (OR) que será Verdadero si uno de los dos es verdadero.
#. **El resultado** (verdadero o falso) se usa dentro de una instrucción que acepta este tipo de valor (técnicamente se llaman valores lógicos o booleanos).

Aprender a Programar (Practicar)
----------------------------------------------

Pero bueno, **demasiada teoría en esta sesión**. Vamos a ponerlo en
práctica en estos dos retos similares, donde solo cambia la condición
de detección. Con esto, estaremos listos para el reto final.

#. :doc:`/retos/reto-6`
#. :doc:`/retos/reto-7`
