============
El simulador
============

.. admonition:: Preguntas
   :class: hint

   ¿Qué es un simulador? ¿Tengo que usar uno concreto o hay varios? ¿Tengo que instalarlo? ¿Cómo lo uso? ¿Lo puedo usar con el celular? ¿Qué es Open Roberta Lab?

En esta sesión aprenderemos a:

#. Usar un simulador con un programa sencillo 
#. Configurar diferentes Robots
   
¿Cómo se programa un robot?
===========================

Generalmente cada tipo de robot tiene un entorno de desarrollo diferente. Es decir, el fabricante:

#. Entrega un robot (el hardware)
#. Y el software necesario para programarlo (aplicación)

Esta situación es ideal si **sólo cuentas con un tipo de robot** pero
a medida que se disponen de más robots, o como en el caso de Lego EV3
o Wedo, se descatalogan, se convierte en un problema. Esta es una
de las principales razones para **usar un simulador online** 
como OpenRobertaLab (ORL), sirve para diferentes robots y permite
centrarse en el desarrollo software. 

En cualquier caso, una vez que **decidas qué robot vas a usar**,
necesitas:

#. Instalar el software de desarrollo
#. Desarrollar tu programa
#. Y trasladar el programa al robot

El tercer paso, trasladar el programa al robot, **presenta algunas dificultades** para su uso en clase:
 
#. Necesito el robot. Uno por cada estudiante o grupo. Y tiene que funcionar (tener batería y estar operativo).
#. Necesito conectarme con él. Es decir, probar la conexión entre el simulador y el robot, sea con un cable conectado directamente o de forma inalámbrica.

Por estas razones los docentes dejan pasar las oportunidades que el uso de la robótica les da en clase. La **idea de este taller** es avanzar con los pasos 1 y 2, muy sencillos de llevar al aula, antes de preparar la logística del paso 3.

Usando Open Roberta Lab
=======================

Open Roberta en realidad es más que un simulador. `Open Roberta`_ es
una iniciativa del Instituto alemán Fraunhofer para estimular a niños
y jóvenes a programar mediante el uso de robots educativos. Es todo un
entorno de desarrollo multirobot. Algunas de sus ventajas son:

#. Uso de un **navegador web**. No se necesita instalar ningún software de desarrollo específico.
#. Uso de un **estándar de programación**. El software de desarrollo es el mismo para todos los robots. Simplifica el desarrollo de programas.
#. Es **independiente del robot** escogido. Aunque cada programa
   depende del robot escogido, según su configuración hardware, no
   necesitas tener el robot para programar y usas el mismo entorno con
   diferentes robots.

Y además, **es gratis** y de `código abierto`_ .

Open Roberta usa un lenguaje denominado NEPO. NEPO (New Easy
Programming Online) es un **metalenguaje de programación** de código
abierto gratuito que pueden utilizar estudiantes, académicos,
profesores y otras personas interesadas en aprender a programar. Es un
lenguaje de programación **visual, usando bloques, y con una capa de
conexión de hardware** acoplada. El paradigma de programación de NEPO
está inspirado en `Scratch`_  , que fue desarrollado por el Instituto
de Tecnología de Massachusetts. Su uso principal es estimular el
aprendizaje temprano (no programar).

.. include:: /actividades/S02-A01.inc

Primeros Pasos
========================

Un bloque NEPO siempre representa y encapsula una determinada funcionalidad de robot. Un conjunto de funciones de bloques se puede reconocer fácilmente a través de la categoría de bloque asociada, por ejemplo, »sensores«. La programación con NEPO sigue un principio simple. Los bloques están interconectados y serán ejecutados por el robot según el orden que determine el programador. Este principio se denomina "operación secuencial".

Por lo tanto, irás seleccionando bloques y los conectarás entre sí. No
todos los bloques encajan igual, y de esa manera la construcción del
programa implica que escojas un bloque que pueda encajar con otro. De
momento lo más sencillo es un bloque detrás del otro, que te servirá
para hacer tu primer programa.

.. include:: /actividades/S02-A02.inc

Configuración del Robot
=============================

Seleccionar
-----------

Como puedes ver al entrar en el simulador online, **el primer paso**
es seleccionar y configurar el robot que vas a utilizar. ORL tiene soporte para
diferentes tipos de robots:

.. image:: /_static/imags/seleccionar-robot.webp

En este taller **usaremos el robot EV3dev**, porque es muy completo
(tiene varios sensores y actuadores).

Configurar
----------

Una vez escogido el robot, ORL te permite configurarlo y hacerte una
idea de cómo es el robot. Según el tipo
de robot **tendrás más o menos parámetros de configuración**. Y a la hora de desarrollar tu programa, tendrás
disponibles diferentes sensores y acciones. 

.. image:: /_static/imags/conf-robot.webp
   :width: 100%

Cada robot, tendrá su panel de configuración. Estos son tres ejemplos de configuración, donde puedes ver una foto
del robot real y su configuración en ORL:

.. list-table:: 
   :widths: 30 70
   :header-rows: 1

   * - Robot
     - Configuración en ORL
   * - .. image:: /_static/imags/mbot.webp
     - .. image:: /_static/imags/mbot-conf.webp
   * - .. image:: /_static/imags/calliope.webp
     - .. image:: /_static/imags/calliope-conf.webp
   * - .. image:: /_static/imags/ev3.webp
     - .. image:: /_static/imags/ev3-conf.webp

.. include:: /actividades/S02-A03.inc
	     
Una vez seleccionado tu robot, ya podemos profundizar en diferentes
sensores, acciones y otros elementos de programación para resolver
cada reto que te plantees.

.. admonition:: Configuración Física del robot
   :class: warning

   Aunque está fuera del alcance de este taller (por tiempo), esta
   configuracion virtual del robot, tiene un equivalente en la
   configuración física del robot. Es decir, es una simulación de los
   componentes que necesitas en tu robot.

   Si luego vas a trasladar el programa (la simulación) al robot **la
   configuración física y virtual** del robot ha de ser la misma.

.. admonition:: Firmware en un robot
   :class: warning

   Si vas a usar el robot físico, y es de cierta complejidad (por
   ejemplo el robot EV3), para que el programa de ORL funciona y lo
   puedas trasladar, necesitas realizar una instalación de software en
   el robot (lo que se llama firmware).

   De esta manera, tu robot "entenderá" el programa que le envías. Si
   te interesa hacerlo, `no dudes en contactarme`_ . 

----------
	     
.. _`código abierto`: https://github.com/OpenRoberta/openroberta-lab
.. _`Wedo`: https://robotsguide.com/robots/legowedo
.. _`EV3`: https://robotsguide.com/robots/legoev3
.. _`Beebot`: https://www.ro-botica.com/Producto/BEE-BOT/
.. _`Open Roberta`: https://es.wikipedia.org/wiki/Open_Roberta
.. _`Scratch`: https://es.wikipedia.org/wiki/Scratch_(lenguaje_de_programaci%C3%B3n)
.. _`no dudes en contactarme`: https://cesareox.com/info_contacto/contactar
