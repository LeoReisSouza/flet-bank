import flet as ft
from assets.splash import splash
from assets.home import home
from assets.help import help
from assets.signup import signup
from assets.dashboard import dashboard
from assets.send_pix import send_pix
from assets.receive_pix import receive_pix
from assets.pay_bill import pay_bill
from assets.user_profile import user_profile
from assets.statement import statement
from assets.change_password import change_password

def main(page: ft.Page):
    page.title = "LeoBank"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.GREEN))

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
        elif page.route == "/dashboard":
            page.add(dashboard(page))
        elif page.route == "/send_pix":
            page.add(send_pix(page))
        elif page.route == "/receive_pix":
            page.add(receive_pix(page))
        elif page.route == "/pay_bill":
            page.add(pay_bill(page))
        elif page.route == "/user_profile":
            page.add(user_profile(page))
        elif page.route == "/statement":
            page.add(statement(page))
        elif page.route == "/change_password":
            page.add(change_password(page))
        page.update()

    page.on_route_change = route_change
    page.go(page.route or "/")

ft.app(target=main)