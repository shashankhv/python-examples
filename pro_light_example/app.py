from sinric import SinricPro
from credentials import apiKey, deviceId
from sinric import SinricProUdp

tempStates = {
    'powerLevel': 0,
    'brightnessLevel': 0
}


def power_state(did, state):
    # Alexa, turn ON/OFF Device
    print(did, state['state'])
    return True, state['state']


def set_brightness(did, state):
    # Alexa set device brightness to 40%
    print(did, 'BrightnessLevel : ', state)
    tempStates['brightnessLevel'] = state
    return True, tempStates['brightnessLevel']


def adjust_brightness(did, state):
    # Alexa increase/decrease device brightness by 44
    print(did, 'AdjustBrightnessLevel : ', state)

    tempStates['brightnessLevel'] += state
    if tempStates['brightnessLevel'] > 100:
        tempStates['brightnessLevel'] = 100
    elif tempStates['brightnessLevel'] < 0:
        tempStates['brightnessLevel'] = 0

    return True, tempStates['brightnessLevel']


def set_color(did, r, g, b):
    # Alexa set device color to Red/Green
    print(did, 'Red: ', r, 'Green: ', g, 'Blue : ', b)

    return True


def set_color_temperature(did, value):
    print(did, value)
    return True


callbacks = {
    'powerState': power_state,
    'setBrightness': set_brightness,
    'adjustBrightness': adjust_brightness,
    'setColor': set_color,
    'setColorTemperature': set_color_temperature
}

if __name__ == '__main__':
    client = SinricPro(apiKey, deviceId, callbacks)
    client.socket.enableRequestPrint(False)  # Set it to True to start printing request JSON
    udp_client = SinricProUdp(callbacks)
    udp_client.enableUdpPrint(False)  # Set it to True to start printing request UDP JSON
    client.handle_all(udp_client)
