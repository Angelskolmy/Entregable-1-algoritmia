# Análisis de algoritmos

Este documento describe los cuatro algoritmos `.psc` de la carpeta y propone dos pruebas manuales para cada uno. Los resultados indicados son los que se esperan de acuerdo con la intención del algoritmo; cuando el código actual produce otro resultado o tiene un riesgo, se señala.

## 1. `CalcEdad.psc` — convertir edad a días

Lee una edad en años, la multiplica por 365 y muestra el resultado aproximado en días. No contempla años bisiestos.

| Prueba | Entrada | Resultado esperado | Resultado / error observado en el código |
|---|---|---|---|
| 1 | `20` | Mostrar `Su edad en dias es de 7300`. | El cálculo es correcto si el programa compila. |
| 2 | `-2` | Rechazar la edad negativa o pedirla de nuevo. | No hay validación: calcula `-730` días. |

**Problema adicional:** el nombre `conVA�oDias` aparece con un carácter de reemplazo (`�`). Puede impedir la compilación según la codificación o el intérprete. Conviene renombrarlo, por ejemplo, `diasPorAnio`. La edad también debería validarse como no negativa.

## 2. `CalculadoraCuentas.psc` — dividir una cuenta con propina

Solicita el monto, el porcentaje de propina y la cantidad de personas; calcula el total con propina y lo divide entre las personas. Permite repetir el cálculo respondiendo `SI`.

| Prueba | Entradas | Resultado esperado | Resultado / error observado en el código |
|---|---|---|---|
| 1 | Iniciar `SI`; monto `100`; propina `10`; personas `2`; continuar `NO`. | Total con propina: 110; mostrar `55` por persona. | El cálculo es correcto. |
| 2 | Iniciar `SI`; monto `-20`, luego `100`; propina `-5`, luego `10`; personas `0`, luego `1`; continuar `NO`. | Rechazar negativos y cero personas; luego mostrar `110` por persona. | Los datos inválidos se vuelven a pedir. Sin embargo, el mensaje dice “más de 1 persona”, pero el código permite exactamente `1`. Si se esperaba obligatoriamente más de una, la condición debe ser `<= 1`. |

**Observación:** la opción de inicio y la de repetición comparan con `SI` en mayúsculas exactas; `si` o `Sí` no inician/continúan el ciclo.

## 3. `CalculadoraPromedio.psc` — calcular el promedio de notas

Pregunta cuántas notas se ingresarán, las guarda en un arreglo y calcula su promedio. También permite repetir la operación.

| Prueba | Entradas | Resultado esperado | Resultado / error observado en el código |
|---|---|---|---|
| 1 | Iniciar `SI`; cantidad `3`; notas `4`, `5`, `3`; continuar `NO`. | Promedio: `4`. | El código suma tres veces `ArchNotas[3]` (3 + 3 + 3), en vez de sumar cada posición; muestra `3`. El acumulador debe usar `ArchNotas[Sumador]`. |
| 2 | Iniciar `SI`; cantidad `0`. | Rechazar la cantidad y volver a pedir un número mayor que cero. | Solo se rechazan cantidades negativas. Con cero se dimensiona un arreglo vacío y luego se intenta dividir entre cero (o se produce un error al dimensionar/acceder, según el intérprete). La validación debe ser `cantidadPonderar <= 0`. |

**Otros problemas:** `ArchNotas` y `Resultado` son enteros, por lo que se pueden perder decimales del promedio. Por ejemplo, el promedio de 4 y 5 debería ser 4.5; use variables reales para notas, acumulador y resultado si se aceptan notas decimales. No se valida un máximo permitido para las notas.

## 4. `saludos.psc` — imprimir un saludo

Muestra el texto `hola mundo` y termina.

| Prueba | Ejecución | Resultado esperado | Resultado / error observado en el código |
|---|---|---|---|
| 1 | Ejecutar el algoritmo. | Mostrar `hola mundo` una vez y finalizar. | No se observa un error lógico; cumple su propósito. |
| 2 | Ejecutarlo de nuevo. | Volver a mostrar `hola mundo` una vez y finalizar. | No conserva estado entre ejecuciones ni requiere entradas; no se identifica otro fallo funcional en este caso. |

## Alcance

Las pruebas son casos manuales derivados de la lectura del código; no se ejecutaron en PSeInt. Por ello, los errores de compilación o el comportamiento exacto ante arreglos de tamaño cero pueden variar según la versión del intérprete.
