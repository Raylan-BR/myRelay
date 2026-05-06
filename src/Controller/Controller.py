from CompInterface.CompInterface import CompInterface
from MQTTClient.MQTTClient import MQTTClient

class Controller:
    def __init__(self, client: MQTTClient, app: CompInterface):
        self.stateBroker = ''
        self.stateRelay = ''
        self.client = client
        self.client._message(self._messageC)
        self.client._connect(self._connectC)
        self.client._desconnect(self._desconnectC)
        self.app = app
        self.app._setOnClick(self._setOnClickC)

    def _startC(self):
        self.client._start()

    def _messageC(self, client, userdata, message):
        self.stateRelay = message.payload.decode()
        self.app._wninStateRelay(self.stateRelay)
    
    def _connectC(self, client, userdata, flags, reason_code, properties):
        self.stateBroker = 'Conectado'
        self.app._wninConnBroker(reason_code)
    
    def _desconnectC(self, client, userdata, flags, reason_code, properties):
        self.stateBroker = 'Desconectado'
        self.app._wninNotConnBroker(reason_code)
    
    def _setOnClickC(self, e):
        self.stateRelay = (
            'Desligado' if self.stateRelay == 'Ligado' else 'Ligado'
        )
        self.client._publish(self.stateRelay)
        self.app._setStateRelay('rele/estado', self.stateRelay)