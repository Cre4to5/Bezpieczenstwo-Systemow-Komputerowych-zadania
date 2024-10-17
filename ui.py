from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QPushButton, QSlider, QVBoxLayout, QHBoxLayout

class CipherWidget(QWidget):
    _type = ""
    def __init__(self, type):
        super().__init__()
        widget_layout = QVBoxLayout()
        self._type = type
        match self._type.split("_")[0]:
            case "caesar":
                slider = QSlider(Qt.Horizontal)

                slider.setMinimum(0)
                slider.setMaximum(33)
                slider.setValue(3)
                slider.valueChanged.connect(self.respond_to_slider)
                widget_layout.addWidget(slider)
        if self._type.split("_")[1] == "cipher":
            button = QPushButton("Cipher")
        else:
            button = QPushButton("Decipher")

        button.clicked.connect(self.btn_click)

        widget_layout.addWidget(button)
        self.setLayout(widget_layout)
    def btn_click(self):
        print(f"You Clicked the {self._type} button")
    def respond_to_slider(self):
        print(f"You slid {self._type}")

class CipherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cipher Window")

        cipher = CipherWidget("caesar_cipher")
        decipher = CipherWidget("caesar_decipher")

        widget_layout = QHBoxLayout()
        widget_layout.addWidget(cipher)
        widget_layout.addWidget(decipher)
        self.setLayout(widget_layout)