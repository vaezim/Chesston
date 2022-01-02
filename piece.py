from PyQt5 import QtSvg, QtCore, QtGui
from PyQt5.QtCore import Qt, QMimeData

class Piece(QtSvg.QSvgWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            super().mousePressEvent(event)
            self.mousePos = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() != Qt.LeftButton:
            return
        mimeData = QMimeData()
        byteArray = QtCore.QByteArray()
        stream = QtCore.QDataStream(byteArray, QtCore.QIODevice.WriteOnly)
        stream.writeQString(self.objectName())
        stream.writeQVariant(self.mousePos)
        mimeData.setData('myApp/QtWidget', byteArray)

        drag = QtGui.QDrag(self)
        drag.setPixmap(self.grab())
        drag.setMimeData(mimeData)
        drag.setHotSpot(self.mousePos - self.rect().topLeft())
        drag.exec_()