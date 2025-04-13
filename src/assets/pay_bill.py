import flet as ft

def pay_bill(page):
    def go_back(e):
        page.go("/dashboard")
    
    def pay_action(e):
        if barcode_field.value:
            page.snack_bar = ft.SnackBar(ft.Text("Boleto pago com sucesso!"))
            page.snack_bar.open = True
            page.update()
            page.go("/dashboard")

    barcode_field = ft.TextField(
        label="Código de barras",
        border_color=ft.colors.GREEN
    )
    amount_field = ft.TextField(
        label="Valor",
        prefix_text="R$ ",
        border_color=ft.colors.GREEN,
        read_only=True
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
                        ft.Text("Pagar Boleto", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Icon(ft.icons.RECEIPT_LONG, size=50, color=ft.colors.GREEN),
                                barcode_field,
                                amount_field,
                                ft.ElevatedButton(
                                    "Pagar Boleto",
                                    icon=ft.icons.PAYMENT,
                                    on_click=pay_action,
                                    style=ft.ButtonStyle(
                                        bgcolor=ft.colors.GREEN,
                                        color=ft.colors.WHITE,
                                        padding=20,
                                    ),
                                    width=300,
                                ),
                            ],
                            spacing=20,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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