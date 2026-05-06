import flet as ft
from CompInterface.CompInterface import CompInterface
from MQTTClient.MQTTClient import MQTTClient
from Controller.Controller import Controller

def main(page: ft.Page):
    client = MQTTClient()
    app = CompInterface(page)
    controller = Controller(client, app)

    page.add(
        app._layoutW()
    )

    controller._startC()

ft.run(main)