import flet as ft
import time

def splash(page):
    def navigate_to_home(e):
        page.go("/home")

    logo = ft.Image(src="https://cdn-icons-png.flaticon.com/512/2592/2592237.png", width=150, height=150)
    progress_bar = ft.ProgressBar(width=300, color=ft.colors.GREEN)

    page.splash = ft.Column(
        controls=[
            logo,
            ft.Text("LeoBank", size=40, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN),
            ft.Text("Seu banco digital favorito", size=20, color=ft.colors.GREEN_800),
            progress_bar,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.update()

    for i in range(101):
        progress_bar.value = i / 100
        time.sleep(0.03) 
        page.update()

    page.splash = None
    navigate_to_home(None)