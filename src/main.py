import flet as ft
from assets.splash import splash
from assets.home import home
from assets.help import help
from assets.signup import signup

def main(page: ft.Page):
    page.title = "LeoBank"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def route_change(route):
        page.controls.clear()
        if page.route == "/":
            splash(page)
        elif page.route == "/home":
            page.add(home(page))
        elif page.route == "/signup":
            page.add(signup(page))
        elif page.route == "/help": 
            page.add(help(page))
        page.update()

    page.on_route_change = route_change
    page.go(page.route or "/")

ft.app(target=main)