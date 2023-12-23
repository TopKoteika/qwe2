from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout , QSpinBox , QHBoxLayout , QRadioButton, QGroupBox, QButtonGroup , QApplication , QStyleOptionGroupBox
menu_btn = QPushButton("Меню")
rest_btn  = QPushButton("Відрочинок")

time_spin = QSpinBox()
time_spin.setValue(3)
time_lb = QLabel("Хвилинка")

row1 = QHBoxLayout()
row1.addWidget(menu_btn)
row1.addStretch(1)
row1.addWidget(rest_btn)
row1.addWidget(time_spin)
row1.addWidget(time_lb)

question_lb = QLabel("Питаня")


btn1 = QRadioButton("Baviant1")
btn2 = QRadioButton("Baviant2")
btn3 = QRadioButton("Baviant3")
btn4 = QRadioButton("Baviant4")
row2 = QHBoxLayout()
radio_group = QButtonGroup()
radio_group.addButton(btn1)
radio_group.addButton(btn2)
radio_group.addButton(btn3)
radio_group.addButton(btn4)

group_box= QGroupBox ("Відповідь")
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn1)
col1.addWidget(btn2)
col2.addWidget(btn3)
col2.addWidget(btn4)

row2.addLayout(col1)
row2.addLayout(col2)
group_box.setLayout(row2)

main_line =  QVBoxLayout()
main_line.addLayout(row1)
main_line.addWidget(question_lb)
main_line.addWidget(group_box)