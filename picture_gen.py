from MukeshAPI import api


image = api.ai_image("bild site")
with open("H:/22", 'wb') as file:
    file.write(image)

print("ok")
