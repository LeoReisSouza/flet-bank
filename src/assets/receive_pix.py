import flet as ft

def receive_pix(page):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.ARROW_BACK,
                            on_click=lambda e: page.go("/dashboard"),
                            icon_color=ft.colors.GREEN
                        ),
                        ft.Text("Receber PIX", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Icon(ft.icons.QR_CODE, size=150, color=ft.colors.GREEN),
                                ft.Text("Chave PIX: 123.456.789-09"),
                                ft.ElevatedButton(
                                    "Copiar Chave",
                                    icon=ft.icons.CONTENT_COPY,
                                    style=ft.ButtonStyle(
                                        bgcolor=ft.colors.GREEN,
                                        color=ft.colors.WHITE,
                                    ),
                                )
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=30,
                    ),
                    width=400,
                )
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
        alignment=ft.alignment.center,
    )