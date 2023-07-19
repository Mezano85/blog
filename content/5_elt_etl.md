Title: Procesamiento de datos - ELT
Date: 2023-07-18 22:00
Modified: 2023-07-18 22:00
Category: Data Engineering
Slug: elt_etl
Authors: Francisco G. Mezano
Summary: El ELT surgió como una alternativa al ETL, que era el método tradicional de integración de datos. El ETL consiste en extraer, transformar y cargar los datos en un sistema de destino, como un almacén de datos. El ELT consiste en extraer, cargar y transformar los datos, es decir, se invierte el orden de los dos últimos pasos.
Lang: es
Tags: DataOps ETL ELT

El correcto manejo de los datos es fundamental para obtener información valiosa que impulse la toma de decisiones 
y proporcione una ventaja competitiva. En este contexto, los enfoques ETL (Extracción, Transformación y Carga) y 
ELT (Extracción, Carga y Transformación) desempeñan un papel crucial en el procesamiento y la preparación de los datos 
para su análisis.

Anteriormente escribí sobre el [flujo de desarrollo de una ETL](flujo_etl.html), ahora nos enfocaremos un poco en las ELT que se parecen mucho,
de hecho, las siglas tienen el mismo significado solo que en un orden distinto y casos de uso tambien distintos.

![Imgur](https://i.imgur.com/rY6kLEb.png)

El procesamiento de datos se ha convertido en un pilar fundamental para el éxito de las organizaciones. Con la creciente 
cantidad de datos generados cada día, es esencial contar con un enfoque efectivo y ágil para transformar esta vasta cantidad 
de información en conocimientos valiosos y significativos.

## El orden de las siglas altera el proceso

El ELT surgió como una alternativa al ETL, que era el método tradicional de integración de datos. El ETL consiste en extraer, 
transformar y cargar los datos en un sistema de destino, como un data warehouse. El ELT consiste en extraer, cargar y transformar 
los datos, es decir, se invierte el orden de los dos últimos pasos.

El enfoque de ELT surgió como una respuesta a los desafíos y limitaciones que enfrentaban las organizaciones en el procesamiento 
de grandes volúmenes de datos. A medida que el volumen y la variedad de datos aumentaban exponencialmente, las soluciones 
tradicionales de ETL comenzaron a mostrar ciertas limitaciones.

El surgimiento de tecnologías de almacenamiento y procesamiento masivo, como los data lakes y la computación en la nube, 
brindó nuevas oportunidades para manejar grandes volúmenes de datos de manera más eficiente. Esto llevó a un cambio de paradigma 
en el procesamiento de datos, donde la extracción y carga inicial de datos se realizaba directamente en el almacenamiento, 
seguida de la transformación de los datos en un paso posterior.


## Comparativa

Aunque el ELT no reemplaza a ETL, sino que los complementa según el tipo y la cantidad de datos que se quieren integrar. Hagamos una comparativa:

<table style="border-collapse: collapse; width: 100%; font-family: Arial, sans-serif;">
  <tr style="background-color: #f2f2f2;">
    <th style="padding: 8px; text-align: left; border: 1px solid #ddd;">Concepto</th>
    <th style="padding: 8px; text-align: left; border: 1px solid #ddd;">ETL</th>
    <th style="padding: 8px; text-align: left; border: 1px solid #ddd;">ELT</th>
  </tr>
  <tr>
    <td style="padding: 8px; border: 1px solid #ddd;">Etapas</td>
    <td style="padding: 8px; border: 1px solid #ddd;">Extracción, transformación y carga</td>
    <td style="padding: 8px; border: 1px solid #ddd;">Extracción, carga y transformación</td>
  </tr>
  <tr>
    <td style="padding: 8px; border: 1px solid #ddd;">Ventajas</td>
    <td style="padding: 8px; border: 1px solid #ddd;">Mayor control y calidad de los datos, menor dependencia del sistema de destino, mayor compatibilidad con las herramientas de BI</td>
    <td style="padding: 8px; border: 1px solid #ddd;">Mayor flexibilidad y escalabilidad de los datos, menor tiempo y recursos para el proceso, mayor aprovechamiento de la potencia del sistema de destino</td>
  </tr>
  <tr>
    <td style="padding: 8px; border: 1px solid #ddd;">Desventajas</td>
    <td style="padding: 8px; border: 1px solid #ddd;">Mayor tiempo y recursos para el proceso, menor flexibilidad y escalabilidad de los datos, posible pérdida de información al transformar los datos</td>
    <td style="padding: 8px; border: 1px solid #ddd;">Menor control y calidad de los datos, mayor dependencia del sistema de destino, posible deterioro del rendimiento al transformar los datos</td>
  </tr>
  <tr>
    <td style="padding: 8px; border: 1px solid #ddd;">Flexibilidad</td>
    <td style="padding: 8px; border: 1px solid #ddd;">Menor, ya que se requiere definir el esquema y las reglas de transformación antes de cargar los datos</td>
    <td style="padding: 8px; border: 1px solid #ddd;">Mayor, ya que se puede acceder y transformar los datos según la demanda</td>
  </tr>
  <tr>
    <td style="padding: 8px; border: 1px solid #ddd;">Casos de uso</td>
    <td style="padding: 8px; border: 1px solid #ddd;">Datos estructurados y pequeños, almacenes de datos tradicionales, análisis e informes predefinidos</td>
    <td style="padding: 8px; border: 1px solid #ddd;">Datos no estructurados y grandes, almacenes de datos en la nube, análisis e informes ad hoc</td>
  </tr>
</table>


## ¿Cómo que se complementan?

Veamos un caso de uso en el que todo Data Engineer está interesado, un DataLake (Tambien aplicable al DataLakehouse).

Un datalake es un repositorio que almacena datos en su forma original, sin transformar ni estructurar. La capa bronce es 
la capa de entrada, donde se cargan los datos sin procesar desde las fuentes. La capa plata es la capa de procesamiento, 
donde se limpian, validan y enriquecen los datos para mejorar su calidad. La capa oro es la capa de salida, donde se 
transforman y modelan los datos para fines específicos de análisis o inteligencia de negocios.

![Imgur](https://i.imgur.com/CeGGLWO.jpg)

El ELT esta situación, se refiere al proceso de extraer y cargar los datos en la capa bronce, sin aplicar ninguna 
transformación previa. La T se refiere al proceso de transformar los datos en las capas plata y oro, según las necesidades 
de cada caso. Estas transformaciones pueden implicar procesos de ETL, como filtrar, normalizar, agregar, combinar o enriquecer los datos.


