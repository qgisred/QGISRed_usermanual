# Propiedades hidráulicas

Las cuatro primeras herramientas de la barra Tools calculan o actualizan propiedades hidráulicas de las tuberías y nudos de forma masiva: longitud, cota y rugosidad. Funcionan sobre la selección actual o sobre toda la red si no hay selección.

***

## Automatically calculate pipe lengths

**Barra Tools → Automatically calculate pipe lengths**

Recalcula el campo `Length` de cada tubería utilizando la longitud geométrica real medida sobre los vértices del SHP en las unidades del CRS del proyecto.

### Cuándo usarla

* Tras mover vértices o nudos con las herramientas de Edition sin haber actualizado el atributo.
* Después de importar desde un `.inp` cuyas longitudes difieren de la geometría real (coordenadas en escala distinta o proyección diferente).
* Como paso previo a **Check pipe lengths** (Barra Debug) para dejar todos los valores sincronizados antes de la auditoría.

La herramienta sobreescribe el valor de `Length` incondicionalmente en todas las tuberías del ámbito de selección. No pregunta confirmación ni filtra por tolerancia.

> Usa siempre un CRS métrico proyectado (UTM, LCC, etc.). Si el proyecto usa coordenadas geográficas (grados decimales), la longitud calculada estará en grados, no en metros, y será inútil para la simulación.

***

## Interpolate elevation from .asc files…

**Barra Tools → Interpolate elevation from .asc files…**

Asigna la cota (campo `Elevation`) a los nudos, depósitos y embalses del proyecto interpolando su valor desde uno o varios Modelos Digitales del Terreno (MDT) en formato ASC.

\*Selector de archivos MDT: puedes cargar varios archivos ASC para cubrir toda el área de la red.\*

### Formato ASC soportado

```
ncols         500
nrows         400
xllcenter     450000.0
yllcenter     4400000.0
cellsize      5.0
nodata_value  -9999
230.4 231.1 231.8 ...
```

| Cabecera                  | Significado                                                                                         |
| ------------------------- | --------------------------------------------------------------------------------------------------- |
| `ncols` / `nrows`         | Número de columnas y filas de la malla                                                              |
| `xllcenter` / `yllcenter` | Coordenadas del centro de la celda inferior-izquierda (también se acepta `xllcorner` / `yllcorner`) |
| `cellsize`                | Tamaño de celda en las unidades del CRS                                                             |
| `nodata_value`            | Valor que el plugin ignora (celda sin dato)                                                         |

### Proceso de asignación

1. Abre el selector y elige uno o más archivos `.asc`. Puedes combinar varios MDT para cubrir el área completa de la red.
2. QGISRed proyecta la coordenada de cada nudo sobre la malla y obtiene la elevación por interpolación bilineal entre las cuatro celdas vecinas.
3. Solo se actualizan los nudos cuyo `Elevation` actual sea igual al valor por defecto (típicamente 0). Los nudos con cota ya asignada manualmente no se modifican.
4. Los nudos que caen fuera de la extensión de todos los MDT cargados quedan marcados como incidencia en el panel de mensajes.

> El CRS del archivo ASC debe coincidir con el CRS del proyecto. Si no coinciden, las coordenadas no se proyectan y los nudos quedarán fuera de la malla.

***

## Set roughness coefficients (from Material and Date)

**Barra Tools → Set roughness coefficients (from Material and Date)**

Calcula y asigna el coeficiente de rugosidad actual de cada tubería en función de su material, su año de instalación y los parámetros de la **Tabla de materiales** del proyecto.

### Fórmula de cálculo

```
Rugosidad_actual = Rugosidad_inicial + (Año_actual − InstallYear) × Incremento_anual
```

Donde `Rugosidad_inicial` e `Incremento_anual` se obtienen de la fila de la Tabla de materiales que coincide con el campo `Material` de la tubería.

### Requisitos previos

Antes de usar esta herramienta, verifica con la Barra Debug que:

1. Todas las tuberías tienen un `Material` válido (**Check pipe materials**).
2. Todas las tuberías tienen un `InstallYear` correcto (**Check pipe installation dates**).

Si alguno de estos campos está vacío o es inválido para una tubería, su rugosidad no se actualiza y se registra como incidencia.

La rugosidad se escribe en las unidades de la fórmula activa del proyecto:

| Fórmula              | Unidad de rugosidad                         |
| -------------------- | ------------------------------------------- |
| Darcy-Weisbach (D-W) | mm (rugosidad absoluta de pared)            |
| Hazen-Williams (H-W) | Coeficiente C adimensional (típico 100–150) |
| Chezy-Manning (C-M)  | Coeficiente n (típico 0.010–0.020)          |

> La Tabla de materiales almacena la rugosidad inicial en unidades D-W (mm). Si el proyecto usa H-W o C-M, el valor calculado se convierte automáticamente al sistema activo.

***

## Convert roughness coefficients…

**Barra Tools → Convert roughness coefficients…**

Convierte los valores del campo `Roughness` de todas las tuberías entre las tres fórmulas de pérdida de carga. Es necesaria cuando cambias la fórmula hidráulica del proyecto y quieres que los valores existentes mantengan su significado físico.

### Conversiones disponibles

| Origen               | Destino              |
| -------------------- | -------------------- |
| Hazen-Williams (H-W) | Darcy-Weisbach (D-W) |
| Darcy-Weisbach (D-W) | Hazen-Williams (H-W) |
| Chezy-Manning (C-M)  | Darcy-Weisbach (D-W) |
| Darcy-Weisbach (D-W) | Chezy-Manning (C-M)  |

Al cambiar la fórmula hidráulica en **Opciones del proyecto**, QGISRed detecta el cambio y ofrece ejecutar esta herramienta automáticamente. Si rechazas en ese momento, puedes lanzarla manualmente desde aquí.

> La conversión D-W ↔ H-W usa el diámetro y un caudal de referencia para encontrar el C que produce la misma pérdida que la rugosidad D-W a ese caudal. El resultado puede diferir de una calibración directa porque las tres fórmulas no son matemáticamente equivalentes para todos los regímenes de flujo.
