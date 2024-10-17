import sys
from PySide6.QtWidgets import QApplication
from ui import CipherWindow 

def main():
    app = QApplication(sys.argv)

    window = CipherWindow()
    window.show()
    
    app.exec()
if __name__ == '__main__':
    main()