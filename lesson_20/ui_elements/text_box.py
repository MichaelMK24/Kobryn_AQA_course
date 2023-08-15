class TextBox:
    def __init__(self, text_box):
        self.element = text_box

    def click(self):
        self.element.click()

    def send_keys(self, info_to_send):
        self.element.send_keys(info_to_send)
