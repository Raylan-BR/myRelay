import flet as ft

class CompInterface:
    def __init__(self, page: ft.Page):
        self.page = page
        self.compConnBroker = ft.Text('Conectando...')
        self.compStateRelay = ft.Text('.')
        self.btnRelay = ft.Button(
                    width=200,
                    height=70,
                    disabled=True,
                    content= 'Aguardando...',
                    style=ft.ButtonStyle(
                        text_style=ft.TextStyle(size=20),
                        padding=20,
                    ),
                )
        self.page.pubsub.subscribe_topic('wninConnBroker', self._setConnBroker)
        self.page.pubsub.subscribe_topic('wninNotConnBroker', self._setConnBroker)
        self.page.pubsub.subscribe_topic('wninStateRelay', self._setStateRelay)
    def _layoutB(self):
        return ft.Container(
                expand=True,
                alignment=ft.Alignment.CENTER,
                content=(self.btnRelay)
            )
    def _layoutW(self):
        return ft.SafeArea(
            expand=True,
            content=ft.Column(
                controls=[
                    self.compConnBroker,
                    self.compStateRelay,
                    self._layoutB(),
                ],
            ),
        )
    
    def _setConnBroker(self, topic, msg):
        self.compConnBroker.value = msg
        self.compConnBroker.update()

    def _setStateRelay(self, topic, msg):
        self.compStateRelay.value = msg
        self.btnRelay.content = msg
        self.btnRelay.disabled = False
        self.page.update()

    def _setOnClick(self, callback):
        self.btnRelay.on_click = callback

    def _wninConnBroker(self, reason_code):
        if reason_code == 0:
            self.page.pubsub.send_all_on_topic('wninConnBroker', 'Conectado')
        else: 
            self.page.pubsub.send_all_on_topic('wninConnBroker', 'Não Conectado')

    def _wninNotConnBroker(self, reason_code):
        self.page.pubsub.send_all_on_topic('wninNotConnBroker', 'Desconectado')
    
    def _wninStateRelay(self, message):
        self.page.pubsub.send_all_on_topic('wninStateRelay', message)