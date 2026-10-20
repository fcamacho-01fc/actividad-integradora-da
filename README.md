# Proyecto Integrador: Gestión de Granja de Gallinas

## Objetivo

Este proyecto tiene como objetivo construir una aplicación de consola en Python para apoyar la gestión básica de una granja de gallinas ponedoras.

Durante el desarrollo del proyecto se integran conceptos vistos en el curso, como:

- funciones
- módulos
- listas
- diccionarios
- ciclos
- archivos JSON
- fechas
- manejo de errores con `try/except`

La aplicación permite trabajar con información de producción, ventas, clientes e inventario.

---

## Estructura del proyecto

```text
integradora/
    main.py
    menu.py
    produccion.py
    ventas.py
    clientes.py
    inventario.py
    datos/
        produccion.json
        ventas.json
        clientes.json
        inventario.json
```

---

## Archivos principales

### `main.py`

Es el punto de entrada del programa.

Su responsabilidad principal es mostrar el menú general y dirigir al usuario al módulo correspondiente.

---

### `menu.py`

Contiene el menú principal del sistema.

Permite acceder a las secciones de:

- producción
- ventas
- clientes
- inventario

---

### `produccion.py`

Gestiona los registros de producción de huevo.

Cada registro puede almacenar información como:

- ID
- fecha
- cantidad producida

Los datos se guardan en:

```text
datos/produccion.json
```

---

### `ventas.py`

Gestiona las ventas de huevo.

Cada venta puede almacenar:

- ID
- fecha
- cliente
- cantidad
- precio por huevo

Los datos se guardan en:

```text
datos/ventas.json
```

---

### `clientes.py`

Gestiona la información de los clientes.

Cada cliente puede incluir:

- ID
- nombre
- teléfono

Los datos se guardan en:

```text
datos/clientes.json
```

---

### `inventario.py`

Gestiona el inventario disponible.

El inventario se obtiene utilizando la información histórica de producción y ventas.

Si el archivo de inventario todavía no existe, el sistema puede reconstruirlo utilizando:

```text
datos/produccion.json
datos/ventas.json
```

El resultado se guarda en:

```text
datos/inventario.json
```

---

## Carpeta `datos`

La carpeta `datos` contiene los archivos JSON utilizados por el programa para conservar información entre ejecuciones.

Esto permite que los datos no se pierdan al cerrar la aplicación.

---

## Ejecución

Desde la carpeta principal del proyecto se puede ejecutar:

```bash
python main.py
```

También es posible ejecutar algunos módulos directamente para revisar su funcionamiento.

Por ejemplo:

```bash
python ventas.py
```

---

## Idea general del proyecto

Cada módulo tiene una responsabilidad específica.

```text
main.py
    coordina el sistema

produccion.py
    gestiona producción

ventas.py
    gestiona ventas

clientes.py
    gestiona clientes

inventario.py
    procesa producción y ventas para obtener existencias
```

El objetivo principal del proyecto es practicar cómo dividir un problema real en módulos pequeños y organizados utilizando Python.
