import sys
import random
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QGraphicsEllipseItem, QGraphicsScene
from PyQt6.QtGui import QColor, QBrush


class Ui_MainWindow(object):
    """Класс интерфейса (генерируется из UI файла)"""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Нарисовать круг")
        self.verticalLayout.addWidget(self.pushButton)
        
        MainWindow.setCentralWidget(self.centralwidget)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        # Инициализация интерфейса
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Создаем сцену для графики
        self.scene = QGraphicsScene(self)
        self.ui.graphicsView.setScene(self.scene)
        
        # Устанавливаем размеры сцены
        self.scene.setSceneRect(0, 0, 780, 450)
        
        # Подключаем кнопку к функции
        self.ui.pushButton.clicked.connect(self.draw_circle)
    
    def draw_circle(self):
        # Случайный диаметр от 20 до 150
        diameter = random.randint(20, 150)
        
        # Случайные координаты (с учетом размеров круга)
        x = random.randint(0, 780 - diameter)
        y = random.randint(0, 450 - diameter)
        
        # Создаем круг
        circle = QGraphicsEllipseItem(x, y, diameter, diameter)
        
        # Случайный цвет (RGB)
        random_color = QColor(
            random.randint(0, 255),  # Red
            random.randint(0, 255),  # Green
            random.randint(0, 255)   # Blue
        )
        
        # Устанавливаем цвет
        circle.setBrush(QBrush(random_color))
        
        # Добавляем круг на сцену
        self.scene.addItem(circle)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
