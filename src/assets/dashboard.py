import flet as ft

def dashboard(page):
    def navigate_to(e, route):
        page.go(route)

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("LeoBank", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Olá, Leonardo", size=24, weight=ft.FontWeight.BOLD),
                                ft.Text("Saldo disponível", size=16),
                                ft.Text("R$ 5.284,90", size=36, weight=ft.FontWeight.BOLD),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=20,
                    ),
                    width=400,
                ),
                ft.GridView(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.PAYMENTS,
                            icon_color=ft.colors.GREEN,
                            icon_size=36,
                            tooltip="Enviar PIX",
                            on_click=lambda e: navigate_to(e, "/send_pix"),
                        ),
                        ft.IconButton(
                            icon=ft.icons.QR_CODE,
                            icon_color=ft.colors.GREEN,
                            icon_size=36,
                            tooltip="Receber PIX",
                            on_click=lambda e: navigate_to(e, "/receive_pix"),
                        ),
                        ft.IconButton(
                            icon=ft.icons.RECEIPT,
                            icon_color=ft.colors.GREEN,
                            icon_size=36,
                            tooltip="Pagar Boleto",
                            on_click=lambda e: navigate_to(e, "/pay_bill"),
                        ),
                        ft.IconButton(
                            icon=ft.icons.ACCOUNT_CIRCLE,
                            icon_color=ft.colors.GREEN,
                            icon_size=36,
                            tooltip="Meus Dados",
                            on_click=lambda e: navigate_to(e, "/user_profile"),
                        ),
                    ],
                    runs_count=4,
                    max_extent=100,
                ),
                ft.ListTile(
                    title=ft.Text("Extrato"),
                    leading=ft.Icon(ft.icons.LIST_ALT, color=ft.colors.GREEN),
                    on_click=lambda e: navigate_to(e, "/statement"),
                ),
                ft.ListTile(
                    title=ft.Text("Alterar Senha"),
                    leading=ft.Icon(ft.icons.PASSWORD, color=ft.colors.GREEN),
                    on_click=lambda e: navigate_to(e, "/change_password"),
                ),
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
        padding=20,
    )