from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from math import floor
from chess import Board, Move # pip install chess
from piece import Piece # piece.py

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setEnabled(True)
        self.resize(800, 826)
        self.setMinimumSize(QtCore.QSize(800, 826))
        self.setMaximumSize(QtCore.QSize(800, 826))
        self.setToolTip("")
        self.setToolTipDuration(0)
        self.setAutoFillBackground(False)
        self.setAcceptDrops(True)
        centralwidget = QtWidgets.QWidget()
        centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(centralwidget)

        self.frame = QtWidgets.QFrame(centralwidget)
        self.frame.setGeometry(QtCore.QRect(QtCore.QPoint(0, 0), QtCore.QPoint(800, 800)))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.board = QtWidgets.QLabel(self.frame)
        self.board.setGeometry(QtCore.QRect(QtCore.QPoint(0, 0), QtCore.QPoint(800, 800)))
        self.board.setMinimumSize(QtCore.QSize(800, 800))
        self.board.setMaximumSize(QtCore.QSize(800, 800))
        self.board.setMouseTracking(False)
        self.board.setText("")
        self.board.setPixmap(QtGui.QPixmap("images/board.png"))
        self.board.setScaledContents(True)
        self.board.setWordWrap(False)
        self.board.setIndent(0)
        self.board.setObjectName("board")

        self.msg = QMessageBox()
        self.msg.setWindowTitle("CheckMate Alert!")
        self.msg.setText("CheckMate! GGs!\n Press OK to exit.")
        self.msg.setIcon(QMessageBox.Information)
        self.msg.buttonClicked.connect(self.close) # Closes the MainWindow

        # Piece Object List (each a QSvgWidget)
        self.piece_list = [Piece() for _ in range(32)]
        self.xAxis = {0: 'a', 100: 'b', 200: 'c', 300: 'd', 400: 'e', 500: 'f', 600: 'g', 700: 'h'}
        self.yAxis = {0: '8', 100: '7', 200: '6', 300: '5', 400: '4', 500: '3', 600: '2', 700: '1'}
        self.LogicalBoard = Board()

        pieces = {1: "w_pawn", 2: "b_pawn", 3: "w_knight", 4: "b_knight", 5: "w_bishop", 6: "b_bishop",
                  7: "w_rook", 8: "b_rook", 9: "w_queen", 10: "b_queen", 11: "w_king", 12: "b_king"}
        piece_ctr = 0
        for color in range(1,3): # Pawns
            for i in range(1,9):
                path = 'images/' + pieces[color] + '.svg'
                self.piece_list[piece_ctr] = Piece(path, self)
                self.piece_list[piece_ctr].setObjectName(pieces[color]+str(i))
                self.piece_list[piece_ctr].setGeometry(QtCore.QRect(QtCore.QPoint((i-1)*100, 626 if color == 1 else 126),
                                                  QtCore.QPoint(i*100, 726 if color == 1 else 226)))
                self.piece_list[piece_ctr].show()
                piece_ctr = piece_ctr + 1
        for color in range(1, 3): # Knights
            for i in range(1, 3):
                path = 'images/' + pieces[color+2] + '.svg'
                self.piece_list[piece_ctr] = Piece(path, self)
                self.piece_list[piece_ctr].setObjectName(pieces[color+2]+str(i))
                self.piece_list[piece_ctr].setGeometry(QtCore.QRect(QtCore.QPoint(100 if i==1 else 600, 726 if color == 1 else 26),
                                               QtCore.QPoint(200 if i==1 else 700, 826 if color == 1 else 126)))
                self.piece_list[piece_ctr].show()
                piece_ctr = piece_ctr + 1
        for color in range(1, 3): # Bishops
            for i in range(1, 3):
                path = 'images/' + pieces[color+4] + '.svg'
                self.piece_list[piece_ctr] = Piece(path, self)
                self.piece_list[piece_ctr].setObjectName(pieces[color+4]+str(i))
                self.piece_list[piece_ctr].setGeometry(QtCore.QRect(QtCore.QPoint(200 if i==1 else 500, 726 if color == 1 else 26),
                                               QtCore.QPoint(300 if i==1 else 600, 826 if color == 1 else 126)))
                self.piece_list[piece_ctr].show()
                piece_ctr = piece_ctr + 1
        for color in range(1, 3): # Rooks
            for i in range(1, 3):
                path = 'images/' + pieces[color+6] + '.svg'
                self.piece_list[piece_ctr] = Piece(path, self)
                self.piece_list[piece_ctr].setObjectName(pieces[color+6]+str(i))
                self.piece_list[piece_ctr].setGeometry(QtCore.QRect(QtCore.QPoint(0 if i==1 else 700, 726 if color == 1 else 26),
                                             QtCore.QPoint(100 if i==1 else 800, 826 if color == 1 else 126)))
                self.piece_list[piece_ctr].show()
                piece_ctr = piece_ctr + 1
        for color in range(1, 3): # Queens
            path = 'images/' + pieces[color+8] + '.svg'
            self.piece_list[piece_ctr] = Piece(path, self)
            self.piece_list[piece_ctr].setObjectName(pieces[color+8]+str(i))
            self.piece_list[piece_ctr].setGeometry(QtCore.QRect(QtCore.QPoint(300, 726 if color == 1 else 26),
                                           QtCore.QPoint(400, 826 if color == 1 else 126)))
            self.piece_list[piece_ctr].show()
            piece_ctr = piece_ctr + 1
        for color in range(1, 3): # Kings
            path = 'images/' + pieces[color+10] + '.svg'
            self.piece_list[piece_ctr] = Piece(path, self)
            self.piece_list[piece_ctr].setObjectName(pieces[color+10]+str(i))
            self.piece_list[piece_ctr].setGeometry(QtCore.QRect(QtCore.QPoint(400, 726 if color == 1 else 26),
                                           QtCore.QPoint(500, 826 if color == 1 else 126)))
            self.piece_list[piece_ctr].show()
            piece_ctr = piece_ctr + 1

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('myApp/QtWidget'):
            event.accept()

    def dropEvent(self, event):
        stream = QtCore.QDataStream(event.mimeData().data('myApp/QtWidget'))
        objectName = stream.readQString()
        widget = self.findChild(QtWidgets.QWidget, objectName)
        if not widget:
            return

        # stream.readQVariant() is emptied from RAM once read, thus, calling it again will cause
        # unpriviledged-ram-read OS-level error!
        dropPoint = QtCore.QPoint(event.pos() - stream.readQVariant())
        # +50 : get the center of the event.pos() not the top left
        # y-26 : menubar offset
        dropX = round(dropPoint.x()/100)*100
        dropY = round((dropPoint.y() - 26)/100) * 100 + 26
        dropPoint.setX(dropX)
        dropPoint.setY(dropY)

        # Saving move in UCI standard format
        uci = self.xAxis[widget.pos().x()] + self.yAxis[widget.pos().y() - 26] + \
              self.xAxis[dropPoint.x()] + self.yAxis[dropPoint.y() - 26]
        if Move.from_uci(uci) in self.LogicalBoard.legal_moves:
            self.LogicalBoard.push_uci(uci)
            widget.move(dropPoint)
            if self.LogicalBoard.is_checkmate():
                self.msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NetChess"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))