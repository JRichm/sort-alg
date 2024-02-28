from window import Window

window = Window(1280, 720, 60)

while window.running:
    window.update()

window.close()