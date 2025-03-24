import flet as ft

def home(page):
    def go_to_signup(e):
        page.go("/signup")

    def go_to_help(e):
        page.go("/help")

    def toggle_theme(e):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        theme_button.icon = ft.icons.DARK_MODE if page.theme_mode == ft.ThemeMode.LIGHT else ft.icons.LIGHT_MODE
        page.update()

    theme_button = ft.IconButton(
        icon=ft.icons.DARK_MODE if page.theme_mode == ft.ThemeMode.LIGHT else ft.icons.LIGHT_MODE,
        on_click=toggle_theme,
        tooltip="Alternar tema",
    )

    return ft.Column(
        controls=[
            ft.Row(
                controls=[theme_button],
                alignment=ft.MainAxisAlignment.END,
            ),
            ft.Icon(ft.icons.ACCOUNT_BALANCE, size=100, color=ft.colors.GREEN),
            ft.Text("Bem-vindo ao LeoBank", size=30, weight=ft.FontWeight.BOLD),
            ft.Text("Sua solução financeira completa", size=20),
            ft.ElevatedButton(
                "Cadastre-se",
                icon=ft.icons.APP_REGISTRATION,
                on_click=go_to_signup,
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.GREEN,
                    color=ft.colors.WHITE,
                    padding=20,
                ),
            ), ft.GestureDetector(
                content=ft.Text(
                    "Preciso de ajuda",
                    size=12,
                    color=ft.colors.BLUE,
                    weight=ft.FontWeight.W_400,
                    style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                ),
                on_tap=go_to_help,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )