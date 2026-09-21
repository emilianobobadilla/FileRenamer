# FileRenamer

FileRenamer es una herramienta de línea de comandos desarrollada en Python para renombrar archivos de una carpeta de forma rápida y controlada.

Permite definir el nombre base de los archivos, el número inicial y la cantidad de dígitos utilizados para la numeración.

## Características

- Renombrado automático de archivos dentro de una carpeta.
- Nombre base personalizable.
- Número inicial configurable.
- Cantidad de dígitos configurable.
- Validación de los datos proporcionados por el usuario.
- Comprobación de que la configuración de numeración sea compatible con la cantidad de archivos.
- Detección de conflictos con nombres de archivos existentes.
- Detención del proceso ante un conflicto para evitar sobrescribir archivos.
- Interfaz mediante línea de comandos.

## Uso

El programa se ejecuta desde la línea de comandos:

```bash
python src/main.py --folder "ruta/a/la/carpeta" --name "Archivo" --start 1 --digits 3
```

Por ejemplo:

```bash
python src/main.py --folder "C:\Users\Usuario\Desktop\Fotos" --name "Foto" --start 1 --digits 3
```

Con esta configuración, los archivos se renombran siguiendo una numeración como:

```text
Foto_001
Foto_002
Foto_003
...
```

## Argumentos

|Argumento| Descripción|
|---|---|
|`--folder`| Carpeta que contiene los archivos que se desean renombrar.|
|`--name`| Nombre base que tendrán los archivos.|
|`--start`| Número desde el que comenzará la numeración.|
|`--digits`| Cantidad de dígitos utilizada para la numeración.|

Para consultar los argumentos disponibles:

```bash
python src/main.py --help
```

## Requisitos

- Python 3.x
- No requiere paquetes externos.

El proyecto utiliza únicamente módulos incluidos en la biblioteca estándar de Python.

## Funcionamiento

Antes de comenzar la renombración, el programa valida los datos proporcionados y comprueba que la configuración de numeración sea compatible con la cantidad de archivos que se van a procesar.

Si durante la renombración se detecta que un nombre generado ya existe, el proceso se detiene para evitar sobrescribir archivos existentes.