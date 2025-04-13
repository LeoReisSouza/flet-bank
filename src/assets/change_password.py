import flet as ft

def change_password(page):
    def go_back(e):
        page.go("/dashboard")
    
    def change_action(e):
        if (current_password.value and 
            new_password.value and 
            confirm_password.value and
            new_password.value == confirm_password.value):
            page.snack_bar = ft.SnackBar(ft.Text("Senha alterada com sucesso!"))
            page.snack_bar.open = True
            page.update()
            page.go("/dashboard")

    current_password = ft.TextField(
        label="Senha atual",
        password=True,
        border_color=ft.colors.GREEN
    )
    new_password = ft.TextField(
        label="Nova senha",
        password=True,
        border_color=ft.colors.GREEN
    )
    confirm_password = ft.TextField(
        label="Confirmar nova senha",
        password=True,
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
                        ft.Text("Alterar Senha", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Icon(ft.icons.PASSWORD, size=50, color=ft.colors.GREEN),
                                current_password,
                                new_password,
                                confirm_password,
                                ft.ElevatedButton(
                                    "Confirmar Alteração",
                                    icon=ft.icons.CHECK_CIRCLE,
                                    on_click=change_action,
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