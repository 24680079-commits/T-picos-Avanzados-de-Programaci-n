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