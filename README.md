# T-picos-Avanzados-de-Programaci-n
Apuntes de clase y programas sobre la materia Tópicos Avanzados de Programación
# UNIDAD 1 – Interfaz Gráfica de Usuario (GUI)
# Interfaz Gráfica de Usuario (GUI)

Una Interfaz Gráfica de Usuario (GUI) es un sistema de interacción entre el usuario y una aplicación que utiliza elementos visuales como ventanas, botones, menús, cuadros de texto e íconos para facilitar la comunicación con el sistema.

A diferencia de una interfaz de línea de comandos (CLI), la GUI permite interacción mediante:

Mouse

Teclado

Pantalla táctil

Eventos visuales

Las GUI están basadas en el modelo dirigido por eventos (event-driven programming).

En Python, existen varias bibliotecas para crear GUI, como:

Tkinter

PyQt

Kivy

Flet

Flet permite crear interfaces modernas usando un modelo reactivo similar a Flutter, pero completamente en Python.

# 1.1 Creación de interfaz gráfica para usuarios

La creación de una GUI implica:

Definir una ventana principal.

Agregar componentes gráficos.

Organizar los elementos en la pantalla.

Asociar eventos a los componentes.

En Flet, la estructura básica es:

```bash
import flet as ft

def main(page: ft.Page):
    page.title = "Mi aplicación"
    page.add(ft.Text("Hola mundo"))

ft.app(target=main)
``` 
Elementos básicos en Flet:

Page → ventana principal

Text → texto

ElevatedButton → botón

TextField → campo de texto

Row y Column → organización de componentes

# 1.2 Tipos de eventos

Un evento es una acción que ocurre dentro del sistema como resultado de la interacción del usuario o del propio programa.

Tipos principales de eventos:

Eventos de clic

Presionar un botón

Eventos de teclado

Escribir texto

Eventos de cambio

Modificación en un campo de texto

Eventos del sistema

Cerrar ventana

Redimensionar

En Flet, los eventos más comunes son:
```bash
on_click

on_change

on_submit

Ejemplo:

def saludar(e):
    print("Botón presionado")

boton = ft.ElevatedButton("Saludar", on_click=saludar)
```
# 1.3 Manejo de eventos

El manejo de eventos consiste en definir qué acción debe ejecutarse cuando ocurre un evento.

Este modelo se conoce como:

Programación dirigida por eventos (Event-Driven Programming)

En este paradigma:

El sistema permanece en espera.

Cuando ocurre un evento, se ejecuta una función asociada.

Ejemplo en Flet:
```bash
def mostrar_texto(e):
    texto.value = "Hola Usuario"
    page.update()

texto = ft.Text("")
boton = ft.ElevatedButton("Mostrar", on_click=mostrar_texto)
```
Aquí:

mostrar_texto es el manejador del evento.
```bash
on_click es el evento.

page.update() refresca la interfaz.
```
# 1.4 Manejo de componentes gráficos de control

Los componentes gráficos de control permiten al usuario interactuar con la aplicación.

En Flet los principales son:

Componente	Función
ElevatedButton	Botón
TextField	Entrada de texto
Checkbox	Selección múltiple
Dropdown	Lista desplegable
Slider	Selección numérica
Switch	Activar/desactivar

Ejemplo práctico:
```bash
def obtener_nombre(e):
    resultado.value = f"Hola {campo.value}"
    page.update()

campo = ft.TextField(label="Ingresa tu nombre")
boton = ft.ElevatedButton("Enviar", on_click=obtener_nombre)
resultado = ft.Text("")
```
# Bibliografía 

Deitel, P., & Deitel, H. (2017). Cómo programar en Java (10.ª ed.). Pearson Educación.

Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2014). Estructuras de datos y algoritmos en Java (6.ª ed.). Wiley.

# Practica 1
Calculadora con Python y Flet

Este repositorio contiene mis primeros apuntes y prácticas de la materia Tópicos Avanzados en Programación.
El objetivo del trabajo fue aprender a instalar Python, utilizar librerías externas y desarrollar una aplicación gráfica utilizando Python y Flet.

El proyecto final consiste en una calculadora, basada en un código proporcionado por el profesor, al cual se le realizaron varias mejoras funcionales y visuales.

⸻
# Sistema Operativo
![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=white)


# Entorno de Desarrollo
	•	Visual Studio Code
	•	Lenguaje: Python
	•	Librería: Flet

Para trabajar el proyecto utilicé Visual Studio Code, ya que permite ejecutar archivos Python de forma sencilla usando el botón Run, lo cual facilita el desarrollo de aplicaciones con interfaz gráfica.

⸻

# Instalación de Python en macOS

Para poder desarrollar el proyecto fue necesario instalar Python.

Pasos realizados:
	1.	Ingresé al sitio oficial de Python:
https://www.python.org

	2.	Entré a la sección Downloads.
  
	3.	Descargué la versión recomendada para macOS.
  
	4.	Ejecuté el instalador y seguí los pasos indicados.
  
	5.	Finalicé la instalación.

<img width="1792" height="1120" alt="Captura de pantalla 2026-02-09 a la(s) 18 05 27" src="https://github.com/user-attachments/assets/f1b01b59-0c13-4e99-a11f-151ff2f299a0" />

Verificación de la instalación

Para verificar que Python se instaló correctamente:
	1.	Abrí la Terminal.
  
	2.	Ejecuté el comando:
  
  python3 --version
  
  <img width="824" height="507" alt="Captura de pantalla 2026-02-09 a la(s) 18 06 05" src="https://github.com/user-attachments/assets/7dde36dc-8357-40a0-a3fd-c14c6e0c99b0" />

  
  # Instalación de Flet

Flet es la librería utilizada para crear la interfaz gráfica de la calculadora.

Pasos:
	1.	Abrí la Terminal.
  
	2.	Ejecuté el siguiente comando:

  ![PHOTO-2026-01-30-10-15-22](https://github.com/user-attachments/assets/5a672325-a73d-4cfe-af75-24f786b58097)

  
  3.	Esperé a que la instalación finalizara correctamente.

![a5508e60-117a-4ff1-986d-90c083f5ef96](https://github.com/user-attachments/assets/8d0ea77c-077d-4446-97f2-30284565bbfe)

  ▶️ Ejecución del Proyecto en Visual Studio Code

El programa se ejecuta directamente desde Visual Studio Code.

Pasos:
	1.	Abrí Visual Studio Code.
	2.	Abrí la carpeta del proyecto.
	3.	Abrí el archivo .py.
	4.	Presioné el botón Run.

Al ejecutar el archivo, Flet genera automáticamente el entorno gráfico, mostrando la ventana de la calculadora.

<img width="1792" height="1120" alt="Captura de pantalla 2026-02-09 a la(s) 18 09 02" src="https://github.com/user-attachments/assets/6ff1b265-f3e0-4724-a30a-90221c3108cf" />

# Proyecto: Calculadora con Flet

Como práctica,  código base para crear una calculadora usando Flet.
Este código incluía:
	•	Configuración básica de la ventana.
	•	Un display para mostrar números.
	•	Botones organizados en un GridView.
  
<img width="1792" height="1120" alt="Captura de pantalla 2026-02-09 a la(s) 18 13 13" src="https://github.com/user-attachments/assets/1da637e8-e058-4827-9e12-40d759b7a1a3" />

# Modificaciones y Mejoras Realizadas

A partir del código proporcionado por el profesor, realicé las siguientes modificaciones y mejoras:

⸻

# Agregado de botones numéricos con eventos

Se agregaron más botones numéricos a la calculadora.
Cada botón utiliza el evento on_click para detectar cuándo es presionado.

Para identificar qué botón se presionó, se utilizó la propiedad data, la cual envía el valor del botón a la función de evento.

<img width="1792" height="1120" alt="Captura de pantalla 2026-02-09 a la(s) 18 15 14" src="https://github.com/user-attachments/assets/b7e1a746-0b92-403e-a978-c7d68d121836" />

 Escritura dinámica en el display

Se implementó una función que actualiza el display de la calculadora:

	•	Si el display contiene "0", el valor se reemplaza.
	•	Si ya contiene números, el nuevo número se concatena.

Esto permite simular el funcionamiento real de una calculadora.

⸻

 Botón AC (All Clear)

Se agregó un botón AC, el cual borra completamente el contenido del display y lo regresa al valor "0".

Este botón mejora la funcionalidad de la calculadora y permite reiniciar la operación.

 Botón DEL (Borrar un solo dígito)

Además del botón AC, se implementó un botón DEL, el cual permite borrar los números uno por uno.

Funcionamiento:
	•	Si el display tiene más de un carácter, se elimina el último.
	•	Si solo queda un número, el display vuelve a "0".

Esta mejora hace que la calculadora sea más intuitiva y funcional.

Ajustes de tamaño y diseño

Se realizaron ajustes para evitar que la calculadora creciera demasiado:
	•	Se eliminó el uso de expand=True.
	•	Se definió un tamaño fijo para la ventana y el grid.
	•	Se evitó el uso de scroll, manteniendo todos los botones visibles.

Esto mejora la experiencia del usuario.

<img width="306" height="431" alt="Captura de pantalla 2026-02-09 a la(s) 18 19 27" src="https://github.com/user-attachments/assets/e931fcbc-6b07-415f-9d05-1f7ff40d00f9" />

Conclusión

Este proyecto permitió aprender:
	•	Cómo instalar Python y librerías en macOS.
	•	Cómo ejecutar proyectos en Visual Studio Code.
	•	Cómo crear interfaces gráficas con Flet.
	•	Cómo manejar eventos con on_click.
	•	Cómo mejorar un código base agregando nuevas funcionalidades.

Este trabajo representa mis primeras prácticas dentro de la materia Tópicos Avanzados en Programación.

```bash
import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora TAP - Eventos"
    page.window_width = 250
    page.window_height = 380
    page.window_resizable = False
    page.padding = 15

    # TEXTO DEL DISPLAY
    texto_display = ft.Text(value="0", size=28)

    # EVENTO PARA BOTONES NUMÉRICOS
    def boton_click(e):
        if texto_display.value == "0":
            texto_display.value = e.control.data
        else:
            texto_display.value += e.control.data
        page.update()

    # EVENTO PARA BORRAR UN SOLO NÚMERO (DEL)
    def borrar_uno(e):
        if len(texto_display.value) > 1:
            texto_display.value = texto_display.value[:-1]
        else:
            texto_display.value = "0"
        page.update()

    # DISPLAY
    display = ft.Container(
        content=texto_display,
        bgcolor=ft.Colors.BLACK12,
        border_radius=8,
        alignment=ft.alignment.Alignment(1, 0),
        padding=10,
        height=60,
    )

    # GRID DE BOTONES (TAMAÑO CONTROLADO)
    grid = ft.GridView(
        runs_count=3,
        spacing=8,
        run_spacing=8,
        width=210,
        height=220,
    )

    # FUNCIÓN PARA CREAR BOTONES
    def crear_boton(texto, color, evento, data=None):
        return ft.Container(
            content=ft.Text(texto, color="white"),
            alignment=ft.alignment.Alignment(0, 0),
            height=50,
            bgcolor=color,
            border_radius=8,
            on_click=evento,
            data=data,
        )

    # BOTONES NUMÉRICOS
    for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        grid.controls.append(
            crear_boton(num, ft.Colors.PRIMARY, boton_click, num)
        )

    # BOTÓN DEL (BORRA UNO)
    grid.controls.append(
        crear_boton("DEL", ft.Colors.SECONDARY, borrar_uno)
    )

    # BOTÓN AC (BORRA TODO)
    grid.controls.append(
        crear_boton(
            "AC",
            ft.Colors.ERROR,
            lambda e: (
                setattr(texto_display, "value", "0"),
                page.update()
            ),
        )
    )

    page.add(display, grid)

ft.app(target=main)
```


# Practica 2 
En esta practica creamos el evento que permita enviar el dato del número al display, 

# Implementación del Evento para Enviar el Número al Display

En esta práctica, el profesor nos proporcionó un código base que únicamente contenía la estructura visual de la calculadora, es decir:

Ventana configurada

Sección del display

Sección de botones numéricos

Sección de operaciones

Organización con Column, Row y Container

Sin embargo, el código original era estático, ya que los botones no realizaban ninguna acción al presionarse.

 Diferencia entre el código del profesor y mi versión
 Código del profesor:

Solo estructura visual.

Los botones eran Container sin evento.

El display mostraba un texto fijo "DISPLAY".

No existía interacción.

Mi versión:

Convertí el display en un objeto dinámico.

Agregué un evento on_click a cada botón.

Utilicé la propiedad data para identificar qué número fue presionado.

Implementé una función que actualiza el display en tiempo real.

# Lógica Implementada
1. Creación de un display dinámico

En lugar de usar un texto fijo, creé una variable llamada:

```bash
texto_display = ft.Text("0", size=20)
```

Esto permite modificar el valor del display durante la ejecución del programa.

2. Creación del evento boton_click

Definí una función que se ejecuta cada vez que se presiona un botón numérico:

```bash
def boton_click(e):
    if texto_display.value == "0":
        texto_display.value = e.control.data
    else:
        texto_display.value += e.control.data
    page.update()
```

 Explicación de la lógica del evento
✔ Parámetro e

El parámetro e representa el evento generado al hacer clic en el botón.

✔ e.control.data

Cada botón tiene una propiedad data que contiene el número correspondiente.

Ejemplo:

```bash
data="1",
on_click=boton_click
```

Cuando se presiona el botón "1", el evento envía el valor "1" a la función.

✔ Condición principal

```bash
if texto_display.value == "0":
```

Si el display contiene solo "0", significa que aún no se ha ingresado ningún número.

En ese caso:

Se reemplaza el "0" por el número presionado.

✔ Concatenación de números

```bash
else:
    texto_display.value += e.control.data
```

Si ya hay un número en pantalla:

El nuevo número se concatena al final.

Esto permite formar números de varias cifras.

Ejemplo:

Si el display tiene "2" y presiono "5",

El resultado será "25".

✔ Actualización de la interfaz

```bash
page.update()
```

Esta instrucción es fundamental, ya que:

Refresca la interfaz gráfica.

Permite que el cambio en el display sea visible inmediatamente.

Sin esta línea, el valor cambiaría internamente, pero no se mostraría en pantalla.

# Modificación en los Botones

En el código original, los botones solo tenían diseño visual.

Yo agregué dos propiedades importantes:

```bash
data="1",
on_click=boton_click
```

data → almacena el valor del botón.

on_click → conecta el botón con la función que maneja el evento.

Esto transforma los botones de elementos estáticos a elementos interactivos.

# Resultado Final

Con estas modificaciones logré:

Que cada botón numérico envíe su valor al display.

Que el display construya números dinámicamente.

Que la interfaz responda a eventos.

Convertir una maqueta estática en una aplicación funcional.

# Conclusión

En esta práctica comprendí cómo funcionan los eventos en Flet y cómo se pueden utilizar para crear interacción en una aplicación gráfica.

Aprendí que:

Los eventos permiten comunicación entre la interfaz y la lógica del programa.

La propiedad data es útil para identificar qué botón fue presionado.

page.update() es necesario para reflejar cambios en la interfaz.

Esta modificación marcó el paso de una aplicación estática a una aplicación interactiva.

# codigo final 
```bash
import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Estática - TAP"
    page.window_width = 280
    page.window_height = 450
    page.window_resizable = False
    page.padding = 15

    # --- 1. SECCIÓN DISPLAY (ROJO) ---
    texto_display = ft.Text("0", size=20)

    def boton_click(e):
        if texto_display.value == "0":
            texto_display.value = e.control.data
        else:
            texto_display.value += e.control.data
        page.update()

    seccion_display = ft.Container(
        content=texto_display,
        bgcolor=ft.Colors.BLACK12,
        height=70,
        alignment=ft.alignment.Alignment(0, 0),
        border=ft.border.all(1, ft.Colors.RED)
    )

    # --- 2. SECCIÓN BOTONES NUMÉRICOS (AZUL) ---
    seccion_numeros = ft.Column(
        controls=[

            # Fila 1
            ft.Row(
                controls=[
                    ft.Container(
                        expand=1,
                        height=50,
                        bgcolor="blue",
                        border=ft.border.all(1, "white"),
                        alignment=ft.alignment.Alignment(0, 0),
                        content=ft.Text("1", color="white"),
                        data="1",
                        on_click=boton_click
                    ),
                    ft.Container(
                        expand=1,
                        height=50,
                        bgcolor="blue",
                        border=ft.border.all(1, "white"),
                        alignment=ft.alignment.Alignment(0, 0),
                        content=ft.Text("2", color="white"),
                        data="2",
                        on_click=boton_click
                    ),
                    ft.Container(
                        expand=1,
                        height=50,
                        bgcolor="blue",
                        border=ft.border.all(1, "white"),
                        alignment=ft.alignment.Alignment(0, 0),
                        content=ft.Text("3", color="white"),
                        data="3",
                        on_click=boton_click
                    ),
                ]
            ),

            # Fila 2
            ft.Row(
                controls=[
                    ft.Container(
                        expand=1,
                        height=50,
                        bgcolor="blue",
                        border=ft.border.all(1, "white"),
                        alignment=ft.alignment.Alignment(0, 0),
                        content=ft.Text("4", color="white"),
                        data="4",
                        on_click=boton_click
                    ),
                    ft.Container(
                        expand=1,
                        height=50,
                        bgcolor="blue",
                        border=ft.border.all(1, "white"),
                        alignment=ft.alignment.Alignment(0, 0),
                        content=ft.Text("5", color="white"),
                        data="5",
                        on_click=boton_click
                    ),
                    ft.Container(
                        expand=1,
                        height=50,
                        bgcolor="blue",
                        border=ft.border.all(1, "white"),
                        alignment=ft.alignment.Alignment(0, 0),
                        content=ft.Text("6", color="white"),
                        data="6",
                        on_click=boton_click
                    ),
                ]
            ),

            # Fila 3
            ft.Row(
                controls=[
                    ft.Container(
                        expand=1,
                        height=50,
                        bgcolor="blue",
                        border=ft.border.all(1, "white"),
                        alignment=ft.alignment.Alignment(0, 0),
                        content=ft.Text("7", color="white"),
                        data="7",
                        on_click=boton_click
                    ),
                    ft.Container(
                        expand=1,
                        height=50,
                        bgcolor="blue",
                        border=ft.border.all(1, "white"),
                        alignment=ft.alignment.Alignment(0, 0),
                        content=ft.Text("8", color="white"),
                        data="8",
                        on_click=boton_click
                    ),
                    ft.Container(
                        expand=1,
                        height=50,
                        bgcolor="blue",
                        border=ft.border.all(1, "white"),
                        alignment=ft.alignment.Alignment(0, 0),
                        content=ft.Text("9", color="white"),
                        data="9",
                        on_click=boton_click
                    ),
                ]
            ),
        ],
        spacing=10
    )

    # --- 3. SECCIÓN OPERACIONES (VERDE) ---
    seccion_operaciones = ft.Row(
        controls=[
            ft.Container(expand=1, height=60, bgcolor="green", border=ft.border.all(1, "white")),
            ft.Container(expand=1, height=60, bgcolor="green", border=ft.border.all(1, "white")),
            ft.Container(expand=1, height=60, bgcolor="green", border=ft.border.all(1, "white")),
        ]
    )

    # --- CONSTRUCCIÓN FINAL ---
    page.add(
        ft.Column(
            controls=[
                seccion_display,
                ft.Text("Números:", size=12),
                seccion_numeros,
                ft.Divider(),
                ft.Text("Operaciones:", size=12),
                seccion_operaciones
            ],
            spacing=15
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
```
<img width="797" height="644" alt="Captura de pantalla 2026-02-14 a la(s) 21 59 25" src="https://github.com/user-attachments/assets/8ce50622-1fd4-4a22-bbc7-32025764d8fb" />

