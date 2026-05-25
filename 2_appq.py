import sys  
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

label = QLabel("Olá, Turma!")
label.resize(300, 200)
label.setWindowTitle("Minha primeira janela")
label.setAlignment(Qt.AlignLeft)  # alinha o texto à esquerda

label.setStyleSheet("font-size: 20px; color: blue;")

label.show()

sys.exit(app.exec_())

