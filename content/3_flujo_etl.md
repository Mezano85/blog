Title: Extraer, Tranformar y Cargar (ETL)... ¿Eso es todo?
Date: 2023-06-19 22:00
Modified: 2023-06-19 22:00
Category: Data Engineering
Slug: flujo_etl
Authors: Francisco G. Mezano
Summary: El proceso de desarrollo de una ETL requiere una comprensión profunda de los requerimientos del negocio, una planificación cuidadosa y una ejecución meticulosa. A lo largo de este artículo, examinaremos las etapas clave y los aspectos esenciales que los data engineers deben considerar!!
Lang: es
Tags: ETL, Flujo

En la era de la información, el procesamiento de datos se ha convertido en una parte esencial.
La Extracción, Transformación y Carga (ETL) es el proceso clave que permite gestionar y analizar datos de manera 
efectiva. En este artículo, exploraremos el proceso de desarrollo de una ETL, desde la identificación de los 
requerimientos hasta la validación de los datos una vez finalizada la carga. Analizaremos las mejores prácticas y 
consideraciones fundamentales que todo data engineer debe tener en cuenta para garantizar el éxito de este proceso.

![Imgur](https://i.imgur.com/cqlPWc5.jpg)

En primer lugar, nos enfocaremos en la importancia de recopilar y comprender los requerimientos del negocio 
antes de iniciar el desarrollo de la ETL. Esto nos permitirá diseñar una solución que se ajuste a las necesidades y 
objetivos específicos de la organización. Además, discutiremos la relevancia de documentar adecuadamente estos 
requerimientos, asegurando una comprensión clara y consistente entre todos los miembros del equipo.

## Requerieminento

Antes de iniciar cualquier actividad es crucial comprender y recopilar los requerimientos del negocio. 
Esto implica una estrecha colaboración entre el Product Owner (PO) y los stakeholders, y una clara comprensión 
de las necesidades y objetivos de la organización.

El PO es el intermediario clave entre el equipo de data y los stakeholders del negocio. Su rol es reunirse 
con los stakeholders para comprender sus necesidades y expectativas, y luego transmitir esos requerimientos 
al equipo de data. El PO debe tener una visión clara de los objetivos del negocio y asegurarse de que los requerimientos 
se traduzcan adecuadamente en el desarrollo de la ETL.

Durante las reuniones con los stakeholders, el PO debe recopilar información relevante sobre los datos disponibles, 
las fuentes de datos, las métricas y KPIs (Key Performance Indicators) requeridos, los formatos de salida deseados, 
la frecuencia de actualización de los datos, entre otros aspectos. Esta comunicación efectiva con los stakeholders 
es esencial para garantizar que el equipo de data tenga una comprensión completa de los requerimientos del negocio.

Una vez que el PO ha recopilado los requerimientos, debe comenzar el proceso de documentación. Esta documentación 
se convierte en un punto de referencia para todo el equipo de data y ayuda a mantener la alineación y el seguimiento 
del progreso del proyecto. Se debe asegurarse de que la documentación incluya detalles sobre las fuentes de datos, 
los sistemas involucrados, las transformaciones requeridas, los formatos de salida y cualquier otra especificación relevante.

## Prueba de concepto

En muchas ocaciones, dependiendo de la complejidad de la integración, es recomendable realizar una prueba de concepto. 
Esta etapa permite validar la viabilidad y eficacia de la solución propuesta, así como identificar posibles desafíos 
y ajustes necesarios antes de su implementación definitiva.

La prueba de concepto involucra seleccionar una muestra representativa de los datos y aplicar transformaciones 
básicas para verificar los resultados. El objetivo es evaluar si las transformaciones y la lógica de negocio se 
aplican correctamente, si los datos se extraen y transforman de manera adecuada, y si los resultados obtenidos 
cumplen con las expectativas del negocio.

Durante esta fase, es importante establecer métricas de éxito y definir criterios claros para evaluar los resultados. 
Esto puede incluir la comparación de los datos transformados con los resultados esperados, la validación de la integridad 
y consistencia de los datos, y la verificación de que los KPIs y métricas relevantes se calculen correctamente.

La prueba de concepto permite identificar posibles problemas y desafíos técnicos antes de la implementación completa. 
Esto brinda la oportunidad de realizar ajustes y mejoras en la solución, como optimizar las consultas, mejorar 
la eficiencia del procesamiento de datos o abordar problemas de calidad de datos... Incluso hechar atras el requerimiento 
y buscar alternativas con los Stakeholders.

Es importante destacar que la prueba de concepto no busca abarcar todos los aspectos y complejidades de la ETL, 
sino validar la viabilidad del enfoque y obtener retroalimentación temprana. Esta etapa puede ser iterativa, 
lo que significa que se pueden realizar múltiples pruebas de concepto hasta lograr la solución óptima.

## Ahora si... la ETL

Una vez que se ha realizado la prueba de concepto con éxito, llega el momento de la implementación de la ETL. 

### E (extract)

La implementación 
de la ETL se inicia con la extracción de los datos de las fuentes identificadas. Esto implica establecer las conexiones 
con las bases de datos, sistemas o fuentes de datos externas y extraer los datos necesarios para el proceso. Dependiendo de 
la complejidad de la extracción, pueden utilizarse diferentes métodos como consultas SQL, APIs o servicios web.

### T (transform)

Una vez que los datos han sido extraídos, se realiza la etapa de transformación. Durante esta fase, se aplican las 
reglas de negocio y las transformaciones definidas en la documentación de la ETL. Esto puede incluir la limpieza de 
datos, la normalización, la agregación, la generación de nuevas variables y cualquier otra manipulación necesaria para 
obtener los datos en el formato requerido.

### L (load)

Finalmente, los datos transformados son cargados en el destino final, que puede ser una base de datos, 
un data warehouse o cualquier otro sistema de almacenamiento utilizado para el análisis y consulta de datos. Durante esta 
etapa, se garantiza la integridad y consistencia de los datos y se realizan las validaciones necesarias para asegurar 
la calidad de los datos cargados.

En cuanto a las herramientas y tecnologías utilizadas en la implementación de una ETL, existen diversas opciones disponibles 
en el mercado. Algunas de las herramientas populares incluyen Apache Spark, Talend, Pentaho Data Integration, 
entre otras. 

## Validación de datos

Una vez que los datos han sido cargados en el destino final durante la implementación de la ETL, sigue una etapa de validación de datos. 
La validación de datos nos permite asegurar la integridad, consistencia de los datos cargados. Ayuda a identificar posibles errores 
o inconsistencias en los datos que podrían afectar la calidad de los análisis y las decisiones tomadas en base a ellos. 

Existen diferentes métodos y técnicas para realizar la validación de datos en una ETL. Lo más comunes es utilizar consultas SQL para 
realizar verificaciones y validaciones en la base de datos. Estas consultas pueden incluir la verificación de la integridad 
referencial, la detección de duplicados, la validación de formatos y cualquier otra regla de validación específica definida 
en los requerimientos del negocio.

Además de las consultas SQL, también se pueden utilizar scripts de validación personalizados. Estos scripts permiten realizar 
comprobaciones más avanzadas y complejas sobre los datos cargados. Pueden involucrar el uso de funciones, condiciones lógicas 
y algoritmos personalizados para validar los datos de acuerdo con las reglas establecidas.

Hay que resaltar que la validación de datos no es un proceso puntual, sino que debe ser realizado de manera continua y periódica. 
Esto implica establecer mecanismos de monitoreo y mantenimiento continuo de los datos cargados, así como la actualización de 
las reglas de validación según sea necesario.

## Ahora finalicemos!!

Una vez finalizada la ejecución de la ETL y validados los datos cargados, es buena practica documentar los resultados obtenidos 
y comunicarlos a los stakeholders.

La documentación de los resultados de la ETL incluye la descripción detallada de los pasos realizados durante el proceso de ETL. Se debe 
registrar la información relevante sobre las fuentes de datos utilizadas, las transformaciones aplicadas, los criterios de validación 
utilizados y cualquier otra consideración importante.

Es ideal mantener un repositorio centralizado de documentación, como un wiki o un sistema de gestión de documentos, donde se pueda acceder 
fácilmente a la información detallada de la ETL. Esto facilita la colaboración entre los miembros del equipo y permite un seguimiento 
efectivo de los resultados y cambios realizados en el proceso de ETL.

Además de la documentación, la comunicación de los resultados es esencial para asegurar que los stakeholders relevantes tengan acceso a la 
información y puedan comprenderla adecuadamente. Esto implica utilizar un lenguaje claro y evitar tecnicismos innecesarios. También 
se pueden utilizar gráficos y visualizaciones para transmitir la información de manera más efectiva y comprensible.



