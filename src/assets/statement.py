import flet as ft
from datetime import datetime

def statement(page):
    def go_back(e):
        page.go("/dashboard")

    transactions = [
        {"date": datetime(2024, 11, 15), "description": "Transferência PIX", "amount": -150.00, "icon": ft.icons.PAYMENTS},
        {"date": datetime(2024, 11, 14), "description": "Depósito", "amount": 500.00, "icon": ft.icons.ACCOUNT_BALANCE_WALLET},
        {"date": datetime(2024, 11, 10), "description": "Pagamento boleto", "amount": -89.90, "icon": ft.icons.RECEIPT},
        {"date": datetime(2024, 11, 5), "description": "Transferência recebida", "amount": 200.00, "icon": ft.icons.QR_CODE},
    ]

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
                        ft.Text("Extrato", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Últimas movimentações", size=18, weight=ft.FontWeight.BOLD),
                                *[
                                    ft.ListTile(
                                        leading=ft.Icon(t["icon"], color=ft.colors.GREEN),
                                        title=ft.Text(t["description"]),
                                        subtitle=ft.Text(t["date"].strftime("%d/%m/%Y %H:%M")),
                                        trailing=ft.Text(
                                            f"R$ {t['amount']:+.2f}",
                                            color=ft.colors.GREEN if t["amount"] > 0 else ft.colors.RED,
                                            weight=ft.FontWeight.BOLD
                                        ),
                                    ) for t in transactions
                                ],
                                ft.ElevatedButton(
                                    "Ver extrato completo",
                                    icon=ft.icons.HISTORY,
                                    style=ft.ButtonStyle(
                                        bgcolor=ft.colors.GREEN,
                                        color=ft.colors.WHITE,
                                    ),
                                ),
                            ],
                            spacing=10,
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