import flet as ft

def send_pix(page):
    def go_back(e):
        page.go("/dashboard")
    
    def send_money(e):
        if amount_field.value and pix_key_field.value:
            page.snack_bar = ft.SnackBar(ft.Text("PIX enviado com sucesso!"))
            page.snack_bar.open = True
            page.update()
            page.go("/dashboard")  # Volta após enviar

    amount_field = ft.TextField(
        label="Valor", 
        prefix_text="R$ ", 
        keyboard_type=ft.KeyboardType.NUMBER,
        border_color=ft.colors.GREEN
    )
    pix_key_field = ft.TextField(
        label="Chave PIX",
        border_color=ft.colors.GREEN
    )
    description_field = ft.TextField(
        label="Descrição (opcional)",
        border_color=ft.colors.GREEN
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.ARROW_BACK,
                            on_click=go_back,
                            icon_color=ft.colors.GREEN
                        ),
                        ft.Text("Enviar PIX", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                amount_field,
                                pix_key_field,
                                description_field,
                                ft.ElevatedButton(
                                    "Confirmar Transferência",
                                    icon=ft.icons.CHECK_CIRCLE,
                                    on_click=send_money,
                                    style=ft.ButtonStyle(
                                        bgcolor=ft.colors.GREEN,
                                        color=ft.colors.WHITE,
                                        padding=20,
                                    ),
                                    width=300,
                                ),
                            ],
                            spacing=20,
                        ),
                        padding=20,
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