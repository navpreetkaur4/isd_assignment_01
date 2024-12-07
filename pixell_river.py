import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Test Window')
window.show()
sys.exit(app.exec_())
