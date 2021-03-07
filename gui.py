# import libraries
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from part import *

# by hasan syhemuhamet
# mon mar 9, 1:07 done
# thanks for shahed and lara and meryem and amal
# you can share this code with friends

class App:
	def __init__(self):
		app = QApplication(sys.argv)

		# create window
		self.meryem = QWidget()
		self.meryem.setFixedSize(500,450)
		# set title name
		self.meryem.setWindowTitle("MERYEM SFLMA")
		# show window
		self.meryem.show()


		# create main_layout
		main_layout = QHBoxLayout()
		# create two layouts inside main_layout
		part_two_layout = QHBoxLayout()
		# set main_layout inside self.meryem
		self.meryem.setLayout(main_layout)
		# add one and two layout to main_layout
		main_layout.addLayout(part_two_layout)
		# done
		# create object
		panel_two = Panel_Frame()

		#part_one_layout.addWidget(panel_one)
		part_two_layout.addWidget(panel_two)

		sys.exit(app.exec_())


if __name__ == '__main__':
	App()