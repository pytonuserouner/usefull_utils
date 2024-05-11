import wifi_qrcode_generator as qr

"""
Программа для генерации QR кодов для прямого подключения к домашней сети
"""


qr_code = qr.wifi_qrcode(ssid='',   # Наименование сети
                         hidden=False,
                         authentication_type='WPA',     # Тип шифрования
                         password='')    # Пароль сети

qr_code.make_image().save('wifi_qrcode_pic')
