if __name__ == "__main__":
    from PyQt5 import QtWidgets
    from mainWindow import MainWindow
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())