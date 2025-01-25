try:
    from PySide6.QtWidgets import (
        QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton, QComboBox, QSlider, QLineEdit, QStackedWidget
    )
    from PySide6.QtCore import Qt
except ModuleNotFoundError as e:
    print("PySide6 is not installed. Please install it using 'pip install PySide6' and try again.")
    raise e

import random
from ciphers import (
    caesarCipher, caesarKey, isCaesarKey,
    polybiusCipher, polybiusKey, isPolybiusKey,
    vigenereCipher, vigenereKey, isVigenereKey,
    playfairCipher, playfairKey, isPlayfairKey,
    messageCleaner
)

class CipherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cipher App")
        self.setGeometry(100, 100, 800, 600)

        # Mapping ciphers and key generators
        self.cipher_functions = {
            "Caesar Cipher": (caesarCipher, caesarKey, isCaesarKey),
            "Polybius Square": (polybiusCipher, polybiusKey, isPolybiusKey),
            "Vigenere Cipher": (vigenereCipher, vigenereKey, isVigenereKey),
            "Playfair Cipher": (playfairCipher, playfairKey, isPlayfairKey)
        }

        # Main layout for the application
        main_layout = QVBoxLayout()

        # Dropdown to select cipher type
        self.cipher_selector = QComboBox()
        self.cipher_selector.addItems(self.cipher_functions.keys())
        self.cipher_selector.currentIndexChanged.connect(self.update_key_input)
        main_layout.addWidget(self.cipher_selector)

        # Layout for ciphering and deciphering sections
        self.cipher_decipher_layout = QHBoxLayout()

        # Create ciphering section
        self.cipher_input_widgets = {}
        self.cipher_layout = self.create_cipher_decipher_part("Cipher")
        self.cipher_decipher_layout.addLayout(self.cipher_layout)

        # Create deciphering section
        self.decipher_input_widgets = {}
        self.decipher_layout = self.create_cipher_decipher_part("Decipher")
        self.cipher_decipher_layout.addLayout(self.decipher_layout)

        main_layout.addLayout(self.cipher_decipher_layout)
        self.setLayout(main_layout)

        # Initialize key input widgets for the default selected cipher
        self.update_key_input()

    def create_cipher_decipher_part(self, mode):
        # Creates the layout for ciphering or deciphering
        layout = QVBoxLayout()

        # Title for the section ("Cipher" or "Decipher")
        title_label = QLabel(f"{mode}")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title_label)

        # Input message text box
        layout.addWidget(QLabel("Input Message:"))
        input_message = QTextEdit()
        layout.addWidget(input_message)

        # Key input section
        layout.addWidget(QLabel("Key:"))
        key_layout = QHBoxLayout()
        key_input_stack = QStackedWidget()

        # Slider for Caesar Cipher key
        caesar_slider = QSlider(Qt.Horizontal)
        caesar_slider.setMinimum(0)
        caesar_slider.setMaximum(34)
        caesar_slider.setTickInterval(1)
        caesar_slider.setTickPosition(QSlider.TicksBelow)
        caesar_slider.valueChanged.connect(lambda value: self.update_slider_label(mode, value))
        key_input_stack.addWidget(caesar_slider)

        # Text box for other cipher keys
        key_textbox = QLineEdit()
        key_input_stack.addWidget(key_textbox)

        # Label to display slider value in real-time
        slider_label = QLabel()
        slider_label.setStyleSheet("padding-left: 10px;")
        slider_label.hide()

        key_layout.addWidget(key_input_stack)

        # Store the widgets for later access based on mode
        if mode == "Cipher":
            self.cipher_input_widgets.update({
                "input_message": input_message,
                "key_stack": key_input_stack,
                "caesar_slider": caesar_slider,
                "key_textbox": key_textbox,
                "slider_label": slider_label
            })
        else:
            self.decipher_input_widgets.update({
                "input_message": input_message,
                "key_stack": key_input_stack,
                "caesar_slider": caesar_slider,
                "key_textbox": key_textbox,
                "slider_label": slider_label
            })

        key_layout.addWidget(slider_label)

        # Button to generate a random key
        random_key_button = QPushButton("\N{GAME DIE}")
        random_key_button.clicked.connect(lambda: self.generate_random_key(mode))
        key_layout.addWidget(random_key_button)

        layout.addLayout(key_layout)

        # Output message text box
        layout.addWidget(QLabel("Output Message:"))
        output_message = QTextEdit()
        output_message.setReadOnly(True)
        layout.addWidget(output_message)

        # Button to process the message (Cipher or Decipher)
        process_button = QPushButton(f"{mode}")
        process_button.clicked.connect(lambda: self.process_message(mode, input_message, output_message))
        layout.addWidget(process_button)

        return layout

    def update_key_input(self):
        # Update the key input widget (slider or textbox) based on the selected cipher
        selected_cipher = self.cipher_selector.currentText()
        for widgets in [self.cipher_input_widgets, self.decipher_input_widgets]:
            if selected_cipher == "Caesar Cipher":
                widgets["key_stack"].setCurrentWidget(widgets["caesar_slider"])
                widgets["slider_label"].show()
            else:
                widgets["key_stack"].setCurrentWidget(widgets["key_textbox"])
                widgets["slider_label"].hide()

    def update_slider_label(self, mode, value):
        # Update the label next to the slider with the current value
        widgets = self.cipher_input_widgets if mode == "Cipher" else self.decipher_input_widgets
        widgets["slider_label"].setText(str(value))

    def generate_random_key(self, mode):
        # Generate a random key for the selected cipher and update the respective widget
        selected_cipher = self.cipher_selector.currentText()
        _, key_generate, _ = self.cipher_functions[selected_cipher]
        key = key_generate()

        # Update the appropriate widget based on mode (Cipher or Decipher)
        widgets = self.cipher_input_widgets if mode == "Cipher" else self.decipher_input_widgets
        if selected_cipher == "Caesar Cipher":
            widgets["caesar_slider"].setValue(int(key))
        else:
            widgets["key_textbox"].setText(key)

    def process_message(self, mode, input_widget, output_widget):
        # Process the message for ciphering or deciphering
        selected_cipher = self.cipher_selector.currentText()
        cipher_func, _, is_key_valid = self.cipher_functions[selected_cipher]

        input_message = input_widget.toPlainText()  # Do not clean input for deciphering
        key = self.get_key(mode)

        if not is_key_valid(key):
            output_widget.setPlainText("Invalid key.")
            return

        is_deciphering = (mode == "Decipher")

        try:
            # Apply messageCleaner only for ciphering
            if not is_deciphering:
                input_message = messageCleaner(input_message)

            output_message = cipher_func(input_message, key, is_deciphering)
            output_widget.setPlainText(output_message)
        except ValueError as ve:
            output_widget.setPlainText(f"Input format error: {ve}")
        except Exception as e:
            output_widget.setPlainText(f"Error: {str(e)}")

    def get_key(self, mode):
        # Retrieve the key based on the selected cipher and mode
        selected_cipher = self.cipher_selector.currentText()
        widgets = self.cipher_input_widgets if mode == "Cipher" else self.decipher_input_widgets

        if selected_cipher == "Caesar Cipher":
            return str(widgets["caesar_slider"].value())
        else:
            return widgets["key_textbox"].text()

if __name__ == "__main__":
    try:
        app = QApplication([])
        window = CipherApp()
        window.show()
        app.exec()
    except ModuleNotFoundError:
        pass