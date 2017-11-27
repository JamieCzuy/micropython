# wifi v0.00.001


def connect(ssid='68AA9C', pw='38576256'):
    import network
    import time

    station = network.WLAN(network.STA_IF)

    if not station.isconnected():
        print('  Connecting to {}'.format(ssid))
        station.active(True)
        station.connect(ssid, pw)

        while not station.isconnected():
            print('    waiting to connect')
            time.sleep(1)

    print('Connected (ip: {})'.format(station.ifconfig()[0]))
