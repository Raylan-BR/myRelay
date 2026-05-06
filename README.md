# Controle remoto com MQTT e Flet

## Descrição

O **myRelay Control** é um sistema de automação que integra software e hardware para controle remoto de dispositivos de alta potência, como lâmpadas, ventiladores e outros equipamentos elétricos.

A aplicação utiliza uma interface moderna construída com **Flet**, conectando-se a um dispositivo embarcado via protocolo **MQTT**. Isso permite enviar comandos em tempo real para um relé mecânico, oferecendo uma solução simples e eficiente para automação residencial ou prototipagem IoT.

Um dos grandes diferenciais do projeto é a facilidade de distribuição: com o Flet, é possível gerar rapidamente aplicações para **Android (APK)**, além de versões para **Linux** e **Windows**, tornando o sistema altamente portátil.

---

## Tecnologias Utilizadas

- **Flet** → Interface gráfica moderna e multiplataforma  
- **Paho-MQTT** → Comunicação com o broker MQTT  
- **HiveMQ (broker público)** → Utilizado para prototipagem  
- **Python** → Linguagem principal do projeto  
- **Git** → Versionamento de código  
- **Virtual Environment** → Isolamento de dependências  

---

## Arquitetura e Boas Práticas

O projeto foi desenvolvido seguindo princípios importantes de engenharia de software:

- 🔹 **Separação de responsabilidades**
  - Camada de interface (Flet)
  - Camada de comunicação (MQTT)
  - Camada intermediária (Controller)

- 🔹 **Baixo acoplamento entre módulos**
- 🔹 **Organização para escalabilidade futura**
- 🔹 **Uso de ambiente virtual** para controle de dependências
- 🔹 **Versionamento com Git**, facilitando manutenção e colaboração

---

## Funcionalidades

- Conexão com broker MQTT (HiveMQ)
- Exibição do status de conexão na interface
- Controle de relé (Ligado / Desligado)
- Comunicação em tempo real com dispositivo embarcado

---

## Autenticação e Segurança

- Estrutura preparada para suporte a autenticação no broker MQTT  
- Possibilidade de expansão para conexões seguras (TLS/SSL)

---

## Possibilidades de Expansão

O sistema foi pensado para crescer. Algumas evoluções possíveis:

- Controle de múltiplos dispositivos simultaneamente  
- Dashboard com status em tempo real  
- Integração com sensores IoT  
- Persistência de estado dos dispositivos  
- Automações programadas (timers e rotinas)  

---

## Aplicações

- Automação residencial simples  
- Protótipos de IoT  
- Controle remoto de dispositivos elétricos  
- Estudos sobre integração software + hardware  

---