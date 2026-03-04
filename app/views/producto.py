import flet as ft
from app.styles.estilos import Buttons, Card, Colors, Textos, Inputs
from app.components.popup import show_popup

def producto_view(page: ft.Page):

    titulo = ft.Text("Registro de Productos", style=Textos.H1)
    subtitulo = ft.Text("Ingrese los datos del producto", style=Textos.H2)
    
    nombre = ft.TextField(
        label="Nombre del Producto",
        **Inputs.INPUT_PRIMARY
    )
    
    precio = ft.TextField(
        label="Precio",
        **Inputs.INPUT_PRIMARY
    )
    
    cantidad = ft.TextField(
        label="Cantidad",
        **Inputs.INPUT_PRIMARY
    )
    
    async def calcular_total(e):
        try:
            precio_valor = float(precio.value if precio.value else 0)
            cantidad_valor = int(cantidad.value if cantidad.value else 0)
            total = precio_valor * cantidad_valor
            
            nombre_producto = nombre.value if nombre.value else "Sin nombre"
            mensaje = (
                f"Producto: {nombre_producto}\n\n"
                f"Precio: ${precio_valor}\n"
                f"Cantidad: {cantidad_valor}\n"
                f"──────────────\n"
                f"TOTAL: ${total}"
            )
            
            await show_popup(
                page,
                "RESULTADO",
                mensaje,
                bgcolor=Colors.SUCCESS,
                txtcolor=Colors.WHITE
            )
            
        except ValueError:
            await show_popup(
                page,
                "ERROR",
                "Por favor ingrese valores numéricos válidos\n"
                "en precio y cantidad",
                bgcolor=Colors.DANGER,
                txtcolor=Colors.WHITE
            )
        
        page.update()
    
    async def limpiar_campos(e):
        nombre.value = ""
        precio.value = ""
        cantidad.value = ""
        page.update()
        
        await show_popup(
            page,
            "",
            "Todos los campos han sido vaciados",
            bgcolor=Colors.PRIMARY,
            txtcolor=Colors.WHITE
        )
    
    btn_calcular = ft.Button(
        "Calcular Total",
        style=Buttons.BUTTON_PRIMARY,
        on_click=calcular_total
    )
    
    btn_limpiar = ft.Button(
        "Limpiar",
        style=Buttons.BUTTON_SUCCESS,
        on_click=limpiar_campos
    )
    
    columna = ft.Column(
        controls=[
            titulo,
            subtitulo,
            ft.Divider(height=10, color=Colors.BORDER),
            nombre,
            precio,
            cantidad,
            ft.Row(
                controls=[btn_calcular, btn_limpiar],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER
            ),
        ],
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    
    card = ft.Container(
        content=columna,
        **Card.TARJETA,
    )
    
    return ft.Container(
        padding=10,
        alignment=ft.Alignment(0, 0),
        content=card,
    )