import flet as ft

def user_profile(page):
    def go_back(e):
        page.go("/dashboard")
    
    def edit_profile(e):
        page.snack_bar = ft.SnackBar(ft.Text("Modo de edição ativado!"))
        page.snack_bar.open = True
        page.update()

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
                        ft.Text("Meus Dados", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.CircleAvatar(
                                    foreground_image_src="https://img.freepik.com/fotos-gratis/sueter-branco-masculino-psd-maquete-roupas-casuais-close-up_53876-148045.jpg",
                                    radius=50,
                                ),
                                ft.ListTile(
                                    title=ft.Text("Nome completo"),
                                    subtitle=ft.Text("Leonardo Silva", weight=ft.FontWeight.BOLD),
                                ),
                                ft.ListTile(
                                    title=ft.Text("CPF"),
                                    subtitle=ft.Text("123.456.789-09", weight=ft.FontWeight.BOLD),
                                ),
                                ft.ListTile(
                                    title=ft.Text("E-mail"),
                                    subtitle=ft.Text("leonardo@example.com", weight=ft.FontWeight.BOLD),
                                ),
                                ft.ListTile(
                                    title=ft.Text("Telefone"),
                                    subtitle=ft.Text("(11) 98765-4321", weight=ft.FontWeight.BOLD),
                                ),
                                ft.ElevatedButton(
                                    "Editar Dados",
                                    icon=ft.icons.EDIT,
                                    on_click=edit_profile,
                                    style=ft.ButtonStyle(
                                        bgcolor=ft.colors.GREEN,
                                        color=ft.colors.WHITE,
                                    ),
                                ),
                            ],
                            spacing=10,
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