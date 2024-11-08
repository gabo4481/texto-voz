# texto-voz
# Convertidor de Texto a Voz con Dear PyGui y pyttsx3

Este proyecto es una aplicación gráfica en Python que permite cargar un archivo de texto y convertir su contenido en voz utilizando `pyttsx3`. La interfaz gráfica está construida con `Dear PyGui`.

## Características

- Cargar y visualizar el contenido de archivos de texto `.txt`.
- Seleccionar una voz, ajustar la velocidad y el volumen de la conversión.
- Convertir texto a voz y guardarlo como archivo `.mp3`.
- Probar la voz seleccionada antes de realizar la conversión final.
- Mostrar cantidad de letras y caracteres.

## Requisitos

- Python 3.8 o superior
- `Dear PyGui`
- `pyttsx3`

## Instalación

1. Clona el repositorio o descarga los archivos.
2. Instala los paquetes necesarios ejecutando el siguiente comando:

    ```bash
    pip install dearpygui pyttsx3
    ```
3. (Alternativa opcional) tambien puedes instalar los archivo `.whl`.

## Uso

1. Ejecuta el archivo principal del proyecto (por ejemplo, `app.py`) con el siguiente comando:

    ```bash
    python app.py
    ```

2. En la ventana de la aplicación, selecciona **Cargar texto** para cargar un archivo `.txt` y visualizar su contenido.

3. Configura las opciones de conversión:
   - **Velocidad**: Ajusta la velocidad de lectura.
   - **Volumen**: Ajusta el volumen de la voz.
   - **Voz**: Selecciona una de las voces disponibles en tu sistema.

4. Presiona **Probar Voz** para escuchar una muestra con las configuraciones actuales.

5. Cuando estés listo, presiona **Convertir** para generar el archivo de audio `output_file.mp3` con el contenido del texto cargado.

## Estructura del Código

- **Funciones Principales**:
  - `leer_archivo`: Carga y muestra el contenido de un archivo de texto.
  - `texto_voz`: Convierte el contenido de texto a voz y guarda el resultado en un archivo `.mp3`.
  - `prueba_voz`: Permite escuchar una prueba de la voz seleccionada con las configuraciones actuales.

- **Interfaz Gráfica**:
  - Utiliza `Dear PyGui` para crear una ventana con botones, controles deslizantes, y un cuadro de texto para mostrar el contenido del archivo.

## Notas

- La aplicación guarda el archivo de audio generado como `output_file.mp3` en el directorio actual.
- Asegúrate de tener voces instaladas en tu sistema para que `pyttsx3` funcione correctamente.

