from random import choice

from PySide6 import QtWidgets, QtGui, QtCore


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setWindowTitle("pyPFC")
        self.setFixedHeight(300)

    def setup_ui(self):    
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.lbl_computer = self.MyLabel()
        self.lbl_user = self.MyLabel()
        self.btn_paper = self.MyPushButton()
        self.btn_rock = self.MyPushButton()
        self.btn_shears = self.MyPushButton()
        self.lbl_text_computer = self.MyLabel(200, 30, "Ordinateur", False)
        self.lbl_text_user = self.MyLabel(200, 30, "Joueur", False)
        self.spacer = QtWidgets.QSpacerItem(80, 0)
        self.lbl_score = self.MyLabel(200, 30, "", False)

    def modify_widgets(self):
        # CSS
        self.setStyleSheet("QLabel"
                            "{border: 3px solid white;"
                            "border-radius: 10px;"
                            "margin-right: 5px;"
                            "color: blue;"
                            "background-color: white;};"
                            "background-color: #303030;")

        # LABEL
        self.pixmap_main = QtGui.QPixmap("pfc.png")
        self.lbl_computer.setPixmap(self.pixmap_main)
        self.lbl_computer.setStyleSheet("margin-right: 10px;")
        self.lbl_user.setPixmap(self.pixmap_main)
        self.lbl_score.setAlignment(QtCore.Qt.AlignCenter)

        # BUTTON
        self.btn_paper.setIcon(QtGui.QPixmap("feuille.png"))
        self.btn_rock.setIcon(QtGui.QPixmap("pierre.png"))
        self.btn_shears.setIcon(QtGui.QPixmap("ciseaux.png"))
        [i.setIconSize(QtCore.QSize(50, 50)) for i in [self.btn_paper, self.btn_rock, self.btn_shears]]

    def create_layouts(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.left_layout = QtWidgets.QHBoxLayout()
        self.right_layout = QtWidgets.QVBoxLayout()
        self.top_layout = QtWidgets.QHBoxLayout()

    def add_widgets_to_layouts(self):
        self.left_layout.addWidget(self.lbl_computer)
        self.left_layout.addWidget(self.lbl_user)
        [self.right_layout.addWidget(i) for i in [self.btn_paper, self.btn_rock, self.btn_shears]]
        self.top_layout.addWidget(self.lbl_text_computer)
        self.top_layout.addWidget(self.lbl_text_user)
        self.top_layout.addSpacerItem(self.spacer)
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.left_layout)
        self.left_layout.addLayout(self.right_layout)
        self.main_layout.addWidget(self.lbl_score)
        
    def setup_connections(self):
        self.btn_paper.clicked.connect(lambda x: self.random(paper=True))
        self.btn_rock.clicked.connect(lambda x: self.random(rock=True))
        self.btn_shears.clicked.connect(lambda x: self.random(shears=True))

    def random(self, paper=False, rock=False, shears=False):
        self.pixmap_paper = QtGui.QPixmap("feuille.png")
        self.pixmap_rock = QtGui.QPixmap("pierre.png")
        self.pixmap_shears = QtGui.QPixmap("ciseaux.png")
        
        if paper:
            self.lbl_user.setPixmap(self.pixmap_paper)
            user_choice = 3
        elif rock:
            self.lbl_user.setPixmap(self.pixmap_rock)
            user_choice = 2
        elif shears:
            user_choice = 1
            self.lbl_user.setPixmap(self.pixmap_shears)

        cpu_choice = choice([self.pixmap_paper, self.pixmap_rock, self.pixmap_shears])       
        self.lbl_computer.setPixmap(cpu_choice)

        if cpu_choice == self.pixmap_paper: cpu_choice = 3
        elif cpu_choice == self.pixmap_rock: cpu_choice = 2
        elif cpu_choice == self.pixmap_shears: cpu_choice = 1

        if cpu_choice == user_choice: self.lbl_score.setText("EGALITE !")
        if cpu_choice == 3 and user_choice == 2: self.lbl_score.setText("CPU WIN !")
        if cpu_choice == 3 and user_choice == 1: self.lbl_score.setText("YOU WIN !")
        if cpu_choice == 2 and user_choice == 3: self.lbl_score.setText("YOU WIN !")
        if cpu_choice == 2 and user_choice == 1: self.lbl_score.setText("CPU WIN !")
        if cpu_choice == 1 and user_choice == 3: self.lbl_score.setText("CPU WIN !")
        if cpu_choice == 1 and user_choice == 2: self.lbl_score.setText("YOU WIN !")


    class MyLabel(QtWidgets.QLabel):
        def __init__(self, w=210, h=200, text="", image=True):
            super().__init__()
            self.setFixedSize(w, h) 
            self.setText(text)
            self.setAlignment(QtCore.Qt.AlignCenter)
            if not image:
                self.setStyleSheet("background-color: none;"
                                   "border: none;"
                                   "color: #fff894;"
                                   "font-size: 16px;"
                                   "font-weight: bold;")

    class MyPushButton(QtWidgets.QPushButton):
        def __init__(self):
            super().__init__()
            self.setStyleSheet("QPushButton"
                                "{border: 1px solid yellow;"
                                "border-radius: 8px;"
                                "background-color: white;"
                                "padding: 6px;};")


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec_()
