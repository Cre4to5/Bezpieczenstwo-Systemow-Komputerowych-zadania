from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QPushButton, QSlider, QVBoxLayout, QHBoxLayout, QTextEdit, QLabel
from ciphers import message_cleaner, caesar_cipher, caesar_key, polybius_square_cipher, polybius_key

class CipherWidget(QWidget):
    _type = ""
    def __init__(self, type):
        super().__init__()
        widget_layout = QVBoxLayout()
        self._type = type
        if self._type.split("_")[1] == "cipher":
            txtInput = QTextEdit()
            txtInput.setPlaceholderText("Cipher Input")
            button = QPushButton("Cipher")
            txtOutput = QTextEdit()
            txtOutput.setPlaceholderText("Cipher Output")
        else:
            txtInput = QTextEdit()
            txtInput.setPlaceholderText("Decipher Input")
            button = QPushButton("Decipher")
            txtOutput = QTextEdit()
            txtOutput.setPlaceholderText("Decipher Output")

        button.clicked.connect(self.btn_click)
        widget_layout.addWidget(txtInput)
        match self._type.split("_")[0]:
            case "caesar":
                sliderWrapper = SliderWrapper(self._type.split("_")[1])
                widget_layout.addWidget(sliderWrapper)
        
        widget_layout.addWidget(button)
        widget_layout.addWidget(txtOutput)
        self.setLayout(widget_layout)
    def btn_click(self):
        print(f"You Clicked the {self._type} button")
class SliderWrapper(QWidget):
    _type = ""
    _label = None
    _slider = None
    def __init__(self,type):
        super().__init__()
        self._type = type
        widget_layout = QHBoxLayout()
        self._slider = QSlider(Qt.Horizontal)

        self._slider.setMinimum(0)
        self._slider.setMaximum(33)
        self._slider.setValue(3)
        self._slider.valueChanged.connect(self.respond_to_slider)

        self._label = QLabel()
        self._label.setText("3")
        
        widget_layout.addWidget(self._slider)
        widget_layout.addWidget(self._label)
        self.setLayout(widget_layout)
    def respond_to_slider(self):
        self._label.setText(str(self._slider.value()))
        print(self._slider.value())
        
class CipherWrapper(QWidget):
    def __init__(self, type):
        super().__init__()
        cipher = CipherWidget(type + "_cipher")
        decipher = CipherWidget(type + "_decipher")

        widget_layout = QHBoxLayout()
        widget_layout.addWidget(cipher)
        widget_layout.addWidget(decipher)
        self.setLayout(widget_layout)
class CipherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cipher Window")

        self.resize(800, 400)

        cipherWrapper = CipherWrapper("caesar")

        widget_layout = QVBoxLayout()
        widget_layout.addWidget(cipherWrapper)
        self.setLayout(widget_layout)