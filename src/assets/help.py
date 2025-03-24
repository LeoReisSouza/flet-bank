import flet as ft

def help(page):
    def enviar_reclamacao(e):
        if not email_input.value or not reclamacao_input.value:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos!", color=ft.colors.WHITE))
            page.snack_bar.open = True
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Reclamação enviada com sucesso!", color=ft.colors.WHITE))
            page.snack_bar.open = True
            email_input.value = ""
            reclamacao_input.value = ""
            page.update()

    email_input = ft.TextField(
        label="E-mail",
        icon=ft.icons.EMAIL,
        width=300,
        border_color=ft.colors.GREEN,
    )
    reclamacao_input = ft.TextField(
        label="Descreva sua reclamação",
        multiline=True,
        min_lines=4,
        max_lines=6,
        width=300,
        border_color=ft.colors.GREEN,
    )

    return ft.Column(
        controls=[
            ft.Icon(ft.icons.HELP_OUTLINE, size=100, color=ft.colors.GREEN),
            ft.Text("Precisa de Ajuda?", size=30, weight=ft.FontWeight.BOLD),
            ft.Text("Envie sua reclamação abaixo:", size=20),
            email_input,
            reclamacao_input,
            ft.ElevatedButton(
                "Enviar Reclamação",
                icon=ft.icons.SEND,
                on_click=enviar_reclamacao,
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