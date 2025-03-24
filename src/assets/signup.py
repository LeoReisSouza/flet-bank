import flet as ft

def signup(page):
    def submit_form(e):
        if not name_input.value or not email_input.value or not password_input.value or not sexo_input.value:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos!", color=ft.colors.WHITE))
            page.snack_bar.open = True
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Cadastro realizado com sucesso!", color=ft.colors.WHITE))
            page.snack_bar.open = True
            page.go("/home")
        page.update()

    name_input = ft.TextField(label="Nome Completo", icon=ft.icons.PERSON, width=300, border_color=ft.colors.GREEN)
    email_input = ft.TextField(label="E-mail", icon=ft.icons.EMAIL, width=300, border_color=ft.colors.GREEN)
    password_input = ft.TextField(label="Senha", icon=ft.icons.LOCK, password=True, width=300, border_color=ft.colors.GREEN)
    sexo_input = ft.Dropdown(
        label="Sexo",
        options=[
            ft.dropdown.Option("Masculino"),
            ft.dropdown.Option("Feminino"),
        ],
        icon=ft.icons.PERSON_OUTLINE,
        width=300,
        border_color=ft.colors.GREEN,
    )

    return ft.Column(
        controls=[
            ft.Icon(ft.icons.ACCOUNT_CIRCLE, size=100, color=ft.colors.GREEN),
            ft.Text("Cadastre-se no LeoBank", size=30, weight=ft.FontWeight.BOLD),
            name_input,
            email_input,
            password_input,
            sexo_input,
            ft.ElevatedButton(
                "Cadastrar",
                icon=ft.icons.APP_REGISTRATION,
                on_click=submit_form,
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.GREEN,
                    color=ft.colors.WHITE,
                    padding=20,
                ),
            ),
            ft.ElevatedButton(
                "Voltar",
                icon=ft.icons.ARROW_BACK,
                on_click=lambda e: page.go("/home"),
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.GREEN_800,
                    color=ft.colors.WHITE,
                    padding=20,
                ),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )