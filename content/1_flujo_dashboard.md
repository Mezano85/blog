Title: ¿Cuál es el flujo para la elaboración de un dashboard?
Date: 2023-06-10 22:00
Modified: 2023-06-10 22:00
Category: Analytics
Slug: flujo_dashboard
Authors: Francisco G. Mezano
Summary: Este artículo explica los pasos para crear un dashboard que responda a las necesidades del stakeholder. El primer paso es definir el requerimiento, el segundo es diseñar el dashboard, el tercero es construir el pipeline de datos, el cuarto es construir y diseñar el dashboard y el quinto es productificar el pipeline y el dashboard. También describe los roles del Data Analyst y el Data Engineer en el proceso.
Lang: es
Tags: Dashboard, Flujo


Cuando se trata de analizar datos y comunicar resultados, es importante contar con visualizaciones claras y 
dashboards que transmitan la información de manera efectiva.

En este artículo abordaré el cómo es un flujo adecuado para la elaboración de un dashboard. Suele suceder que
el usuario final imagine un dashboard ideal que incluso podría haber trabajado en Excel y que mantiene
manualmente, pero cuando llega la hora de producirlo, no alcanzamos el resultado esperado... o, si lo logramos,
puede ser después de varias idas y vueltas que provocan que el tiempo de producción se alargue.

![Imgur](https://i.imgur.com/0kkY7ey.jpg)

En el proceso, explicaré quién está involucrado en cada parte del proceso, ya que también suele haber
confusiones entre los responsables. En este caso, hablaré sobre los roles de dos personas importantes en la
elaboración de un dashboard: el **Data Analyst** y el **Data Engineer**.

Antes de iniciar con el flujo, quiero aclarar que si hay una persona responsable de inicio a fin del 
proceso, no hará todas las actividades, pero es responsable de que el resultado final sea el esperado 
y de llevar la coordinación con el resto del equipo para lograrlo. El responsable es el Data Analyst.


## Paso 1: ¿Qué preguntas queremos responder?

El primer paso es la definición del requerimiento por parte del stakeholder. En esta etapa, el stakeholder 
debe expresar claramente **las preguntas o problemas que desea resolver a través del dashboard**. Algunas 
pautas que pueden ayudar en este proceso son:

* Identificar el objetivo principal: El stakeholder debe definir el propósito principal del dashboard, es decir, 
qué información desea obtener o qué decisiones desea respaldar a través de su uso.

* Determinar las métricas clave: Es importante que el stakeholder identifique las métricas o indicadores clave que 
son relevantes para su objetivo. Estas métricas deben ser cuantificables y medibles.

* Establecer el público objetivo: El stakeholder debe especificar quiénes serán los principales usuarios del dashboard 
y qué tipo de información necesitan para tomar decisiones informadas.

* Definir el alcance y la granularidad: El stakeholder debe indicar qué datos deben incluirse en el dashboard y 
el nivel de detalle necesario. Esto implica determinar si se requiere información a nivel general, por área específica, 
por periodo de tiempo, entre otros aspectos.

* Establecer el formato y la estructura: El stakeholder puede proporcionar orientación sobre el diseño general del dashboard, 
quiero hacer una aclaración importante, solo es una orientación, no implica necesariamente que será el diseño
adecuado, el experto en las visualizaciones, la disposición de los elementos y la organización de la información
es el Data Analyst, pero siempre se debe escuchar la opinión del Stakeholder para tener una mejor idea de lo que se requiere. 

A esta altura, es probable que el usuario tenga un reporte, generalmente en Excel que es como se comienza 
con el analisis de información si no tienes un perfil tecnológico. Es importante aclarar que cada herramienta de 
BI tiene funcionalidades y carencias que generalmente no permitirán llegar al mismo resultado, sin embargo
siempre se tendrán alternativas visuales que lograrán responder las preguntas incluso en varias ocasiones de
una mejor manera.

El diálogo abierto y la colaboración entre el stakeholder y el analista de datos son fundamentales en esta etapa para garantizar 
que las necesidades y expectativas del stakeholder se comprendan completamente. Una vez que se ha definido 
claramente el requerimiento del dashboard, se puede avanzar al siguiente paso del proceso.

## Paso 2: Diseño

El Data Analyst inicia con la elaboración de un bosquejo o diseño preliminar. Esto implica tener en cuenta las 
restricciones y características específicas de la herramienta de visualización utilizada en la empresa, 
ya que cada herramienta tiene su propia sintaxis, capacidades y limitaciones.

El Data Analyst se encarga de definir cómo se presentarán los datos en el dashboard, qué tipos de visualizaciones 
se utilizarán, cómo se organizarán los diferentes elementos y qué interacciones o filtros estarán disponibles 
para el usuario. Este proceso requiere una comprensión profunda de las necesidades del stakeholder expresadas en 
el paso anterior y de cómo los datos pueden transmitir la información de manera clara y efectiva.

Además de diseñar la apariencia visual del dashboard, el Data Analyst también identifica los datos necesarios 
para su creación. Puede tener experiencia en la extracción, transformación y carga de datos (ETL) de manera básica 
y utilizar esta habilidad para preparar los datos requeridos. Sin embargo, es importante destacar que la 
responsabilidad principal de la productificación del flujo de datos recae en el Data Engineer.

De nuevo, la comunicación con el Stakeholder es importante, ayudará mucho tener una opinion del usuario final
sobre el diseño preliminar, es posible que salgan un par de ideas que logren una mejor versión.

## Paso 3: Pipeline de datos

Este paso es responsabilidad del Data Engineer, en algunas ocasiones, cuando el dashboard no es complejo
de elaborar y los datos se tienen ya disponibles para reportar en un datawarehouse podría no ser necesario 
pero lo integreré acá porque es frecuente necesitarlo.

En esta etapa, el Data Analyst colabora estrechamente con el Data Engineer para asegurarse de que los datos 
necesarios estén disponibles en el formato adecuado. El Data Analyst puede comunicar al Data Engineer 
los requisitos de datos específicos, como las fuentes de datos, la estructura de datos, las transformaciones 
necesarias y cualquier otro aspecto relevante para la construcción del dashboard.

El Data Engineer analiza las fuentes de datos disponibles y evalúa su calidad y relevancia para el dashboard. 
Puede ser necesario trabajar con diferentes sistemas, bases de datos o servicios para obtener los datos necesarios.

Una vez que se identifican las fuentes de datos, el Data Engineer diseña la estructura y las transformaciones 
necesarias para preparar los datos. Esto implica la limpieza de datos, la eliminación de duplicados, 
la normalización de formatos y la realización de cálculos o agregaciones específicas según sea necesario.

Además, se debe tener en cuenta la escalabilidad y el rendimiento del pipeline de datos. Esto implica optimizar 
las consultas y los procesos de carga de datos para garantizar tiempos de respuesta rápidos y eficientes, 
especialmente cuando se manejan grandes volúmenes de datos. Aquí puede implementar técnicas de particionamiento 
o indexación para mejorar el rendimiento de las consultas.

Una vez que el Data Engineer termine, el Data analyst tendrá la fuente de datos lista para poner manos a la obra.

## Paso 4: Construcción

Una vez que el Data Engineer ha establecido el pipeline de datos y los datos necesarios están disponibles, 
el Data Analyst puede proceder a la construcción y diseño del dashboard. 

En esta etapa, se seleccionan los gráficos y visualizaciones adecuados para representar los datos de manera 
clara y comprensible. Se eligen entre una variedad de opciones, como gráficos de barras, circulares, de líneas, 
mapas y tablas, dependiendo de la naturaleza de los datos y los objetivos del dashboard.

Se define la disposición y estructura del dashboard, organizando los componentes visuales de manera coherente 
y fácil de entender. Se decide la ubicación de los gráficos, las leyendas, los filtros interactivos y cualquier 
otro elemento necesario para la interacción y exploración de datos.

Además, el Data Analyst se asegura de que el diseño del dashboard siga buenas prácticas de visualización de datos. 
Esto implica utilizar colores adecuados, evitar la saturación visual, proporcionar etiquetas claras y legibles, 
y mantener una jerarquía visual coherente para facilitar la comprensión de la información.

Es importante destacar que el proceso de construcción y diseño del dashboard debe ser iterativo.
El Data Analyst debe compartir versiones preliminares del dashboard con el stakeholder y otros usuarios 
clave para recibir comentarios y realizar ajustes. Esto garantiza que el dashboard final cumpla con las expectativas 
y los requisitos establecidos inicialmente.

## Paso 5: Productificación

Una vez que el dashboard ha sido elaborado y se ha finalizado su diseño, es el momento de llevar a cabo la
productificación tanto del dashboard como del pipeline de datos. Existen dos enfoques principales para considerar en esta etapa:

* Productificación del Pipeline de Datos antes de la Elaboración del Dashboard (Productificación desde el paso 3):
En este enfoque, se prioriza la productificación del pipeline de datos antes de iniciar la elaboración del dashboard. 
Esto implica diseñar y desarrollar un flujo de datos confiable y automatizado que recolecte, transforme y proporcione 
los datos necesarios para el dashboard. Al productificar el pipeline de datos antes, se garantiza la disponibilidad 
y la actualización continua de los datos requeridos, lo que permite al Data Analyst trabajar con información en 
tiempo real durante la creación del dashboard. Esto evita retrasos o ajustes posteriores en el pipeline y agiliza 
el proceso de elaboración del dashboard. Por contra, si durante la construcción del dasboard se requieren ajustes en el 
pipeline puede implicar trabajos adicionales.

* Productificación del Pipeline de Datos después de la Elaboración del Dashboard (Productificación en el paso 5, junto con el dashboard)):
En este enfoque, se enfoca en completar la elaboración del dashboard antes de productificar el pipeline de datos. 
Durante la creación del dashboard, pueden surgir cambios o ajustes en los requisitos o en la forma en que se presentan 
los datos. Una vez que el dashboard ha sido finalizado, se procede a productificar el pipeline de datos, 
asegurando que el flujo de datos esté completamente alineado con las necesidades específicas del dashboard. 
Esto implica optimizar y automatizar el flujo de datos para garantizar su confiabilidad y disponibilidad continua.

Es importante destacar que la decisión sobre cuándo productificar el pipeline de datos dependerá de factores como 
la complejidad de los datos, la posibilidad de cambios durante la creación del dashboard y los recursos disponibles. 
La comunicación y la colaboración entre el Data Analyst y el Data Engineer son fundamentales para determinar el enfoque 
más adecuado en cada caso.

Una vez que tanto el dashboard como el pipeline de datos han sido productificados, hemos llegado al final del proceso. 
El dashboard estará listo para ser utilizado por los usuarios finales.





