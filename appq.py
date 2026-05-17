import sys  
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

label = QLabel("Olá, PyQt!")
label.resize(300, 200)
label.setWindowTitle("Minha primeira janela")
label.setAlignment(Qt.AlignCenter)  # centraliza o texto

label.setStyleSheet("font-size: 20px; color: blue;")

label.show()

sys.exit(app.exec_())

