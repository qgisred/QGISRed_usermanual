# Rugosidades

La barra Tools ofrece dos herramientas complementarias para gestionar el coeficiente de rugosidad de las tuberías: una que lo calcula por envejecimiento a partir del material y la fecha de instalación, y otra que lo convierte entre las tres fórmulas de pérdida de carga que soporta EPANET.

---

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
1. Todas las tuberías tienen un `Material` válido (herramienta **Check pipe materials**).
2. Todas las tuberías tienen un `InstallYear` correcto (herramienta **Check pipe installation dates**).

Si alguno de estos campos está vacío o es inválido, la rugosidad de esa tubería no se actualiza y se registra como incidencia.

### Comportamiento

Opera sobre la selección actual o sobre todas las tuberías si no hay selección. Sobreescribe el campo `Roughness` con el valor calculado. La fórmula usada para la rugosidad (D-W, H-W o C-M) es la configurada en **Opciones del proyecto → Hidráulica**.

| Fórmula | Unidad de rugosidad |
|---------|---------------------|
| Darcy-Weisbach (D-W) | mm (rugosidad absoluta de pared) |
| Hazen-Williams (H-W) | Coeficiente C adimensional (típico 100–150) |
| Chezy-Manning (C-M) | Coeficiente n (típico 0.010–0.020) |

> La Tabla de materiales almacena la rugosidad inicial en las unidades de la fórmula D-W (mm). Si el proyecto usa H-W o C-M, el valor calculado se convierte automáticamente al sistema activo.

---

## Convert roughness coefficients…

**Barra Tools → Convert roughness coefficients…**

Convierte los valores del campo `Roughness` de todas las tuberías entre las tres fórmulas de pérdida de carga. Es necesaria cuando cambias la fórmula hidráulica del proyecto (en **Opciones del proyecto → Hidráulica**) y quieres que los valores existentes mantengan su significado físico.

### Conversiones disponibles

| Origen | Destino | Método |
|--------|---------|--------|
| Hazen-Williams (H-W) | Darcy-Weisbach (D-W) | Equivalencia por caudal de referencia |
| Darcy-Weisbach (D-W) | Hazen-Williams (H-W) | Equivalencia por caudal de referencia |
| Chezy-Manning (C-M) | Darcy-Weisbach (D-W) | Relación entre n y rugosidad absoluta |
| Darcy-Weisbach (D-W) | Chezy-Manning (C-M) | Relación entre rugosidad absoluta y n |

### Cuándo usarla

Al cambiar la fórmula hidráulica en **Opciones del proyecto**, QGISRed detecta el cambio y ofrece automáticamente ejecutar esta herramienta. Si rechazas la conversión automática en ese momento, puedes lanzarla manualmente desde aquí.

> La conversión es una aproximación: las tres fórmulas no son matemáticamente equivalentes para todos los regímenes de flujo. La conversión D-W ↔ H-W usa el diámetro y un caudal de referencia para encontrar el C de H-W que produce la misma pérdida que la rugosidad D-W a ese caudal. El resultado puede diferir ligeramente de una calibración directa.
