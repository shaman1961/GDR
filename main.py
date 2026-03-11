import sys
import random
from PyQt6 import QtWidgets, QtGui, uic
from PyQt6.QtWidgets import QGraphicsEllipseItem, QGraphicsScene
from PyQt6.QtGui import QColor, QBrush


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        
        # Создаем сцену для графики
        self.scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)
        
        # Устанавливаем размеры сцены
        self.scene.setSceneRect(0, 0, 780, 450)
        
        # Подключаем кнопку к функции
        self.pushButton.clicked.connect(self.draw_circle)
    
    def draw_circle(self):
        # Случайный диаметр от 20 до 150
        diameter = random.randint(20, 150)
        
        # Случайные координаты (с учетом размеров круга)
        x = random.randint(0, 780 - diameter)
        y = random.randint(0, 450 - diameter)
        
        # Создаем круг
        circle = QGraphicsEllipseItem(x, y, diameter, diameter)
        
        # Желтый цвет
        circle.setBrush(QBrush(QColor(255, 255, 0)))
        
        # Добавляем круг на сцену
        self.scene.addItem(circle)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())  # В PyQt6 используется exec() вместо exec_()
