# Verificación de Atributos

Las cuatro herramientas del segundo grupo de la barra Debug auditan los **datos alfanuméricos** de las tuberías para detectar errores de transcripción, valores incoherentes o campos vacíos que impedirían una simulación correcta o el cálculo de rugosidades por envejecimiento.

Todas operan sobre la selección actual o sobre toda la red si no hay selección previa.

---

## Check pipe lengths

**Barra Debug → Check pipe lengths**

Compara la **longitud almacenada en el atributo `Length`** de cada tubería con la **longitud geométrica real** calculada a partir de los vértices del SHP.

### Diálogo de tolerancia

Al activar la herramienta se abre un diálogo donde defines:

| Campo | Descripción |
|-------|-------------|
| **Tolerancia (%)** | Diferencia porcentual máxima aceptable entre longitud de atributo y longitud geométrica |
| **Actualizar longitudes** | Si está marcado, reemplaza el valor del atributo con la longitud geométrica en todas las tuberías que superen la tolerancia |

### Cuándo aparecen diferencias

- Tuberías importadas desde un `.inp` donde `Length` fue calculado con una escala diferente.
- Tuberías cuya geometría se modificó (vértices movidos) sin actualizar el atributo.
- Redes en CRS proyectados vs. geográficos: si las coordenadas del `.inp` son en grados y se usan como metros, las longitudes son incorrectas.

> QGISRed calcula la longitud geométrica siempre en las unidades del CRS del proyecto. Si el proyecto usa coordenadas geográficas (grados), las longitudes serán incorrectas. Usa siempre un CRS métrico proyectado.

---

## Check diameters

**Barra Debug → Check diameters**

Revisa los diámetros de todas las tuberías seleccionadas (o de toda la red) y señala aquellos que estén fuera del rango habitual o que sean cero.

### Qué detecta

- Tuberías con diámetro **cero o negativo** (error de importación o edición manual).
- Tuberías con diámetros estadísticamente atípicos respecto al resto del modelo (valores extremadamente altos o bajos).
- Tuberías sin diámetro asignado (campo vacío).

### Resultado

Los elementos con diámetros problemáticos se seleccionan en el mapa y se muestra un resumen en el panel de mensajes. No modifica automáticamente ningún valor: la corrección debe hacerse manualmente desde el diálogo de propiedades o la tabla de atributos.

---

## Check pipe materials

**Barra Debug → Check pipe materials**

Comprueba que el valor del campo `Material` de cada tubería esté definido en la **Tabla de materiales del proyecto** (Barra Project → Tabla de materiales).

### Qué detecta

- Tuberías con material vacío o nulo.
- Tuberías con un código de material que no existe en la tabla del proyecto (por ejemplo, un código heredado de otro sistema GIS).
- Tuberías con el valor `UNKNOWN` (valor por defecto cuando no se conoce el material).

### Por qué es importante

El material es imprescindible para la herramienta **Asignar rugosidades** (Barra Tools), que calcula la rugosidad por envejecimiento a partir del material y la fecha de instalación. Si el material no es válido, la rugosidad no se puede calcular.

---

## Check pipe installation dates

**Barra Debug → Check pipe installation dates**

Verifica el campo `InstallYear` de las tuberías, que almacena el año de instalación en formato numérico (`YYYY`).

### Qué detecta

| Problema | Descripción |
|----------|-------------|
| **Fecha vacía** | Campo `InstallYear` nulo o cero |
| **Fecha futura** | Año superior al año actual |
| **Formato incorrecto** | Valores no numéricos o fuera del rango razonable (antes de 1800 o después del año actual) |

### Por qué es importante

La fecha de instalación, combinada con el material, permite calcular la **rugosidad actual** de cada tubería mediante la fórmula de envejecimiento:

```
Rugosidad = Rugosidad_inicial + (Año_actual − InstallYear) × Incremento_anual
```

Si la fecha es incorrecta, la rugosidad calculada será errónea y la simulación hidráulica producirá resultados alejados de la realidad.
