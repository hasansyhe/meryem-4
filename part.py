# import PyQt5 library
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os

class Panel_Frame(QWidget):
	def __init__(self):
		super().__init__()
		mainlayout = QHBoxLayout()
		self.setLayout(mainlayout)
		notebook = QTabWidget()
		mainlayout.addWidget(notebook)
		tab_login = QWidget()
		tab_signup = QWidget()
		notebook.addTab(tab_login, "Login")
		notebook.addTab(tab_signup, "Signup")

		main_layout_1 = QVBoxLayout()
		tab_login.setLayout(main_layout_1)

		# create mainlayout
		loginbox = QGroupBox("Log In")
		main_layout_1.addWidget(loginbox)

		main_layout_2 = QVBoxLayout()
		loginbox.setLayout(main_layout_2)

		username_1 = QLineEdit()
		username_1.setPlaceholderText("Enter Your Username")
		username_1.setStyleSheet("height:20px;padding:10px;")
		password_1 = QLineEdit()
		password_1.setPlaceholderText("Enter Your Password")
		password_1.setStyleSheet("height:20px;padding:10px;")

		main_layout_2.addWidget(username_1)
		main_layout_2.addWidget(password_1)


		actions_group_1 = QGroupBox("Actions")
		main_layout_1.addWidget(actions_group_1)
		but_layout = QHBoxLayout()
		actions_group_1.setLayout(but_layout)

		butlogin = QPushButton("Log In")
		butlogin.setStyleSheet("height:30px;")
		but_layout.addWidget(butlogin)
		re_password = QPushButton("Forget Password")
		re_password.setStyleSheet("height:30px;")
		but_layout.addWidget(re_password)

		empty_1 = QLabel("")
		main_layout_1.addWidget(empty_1)



		#------------------- sign up tab -----------------------------#
		main_layout = QVBoxLayout()
		tab_signup.setLayout(main_layout)
		logo0 = QLabel("Create New Account")
		main_layout.addWidget(logo0)

		full_name = QLineEdit()
		full_name.setStyleSheet("height:20px;padding:10px;")
		full_name.setPlaceholderText(" Enter Full  Name")
		username = QLineEdit()
		username.setStyleSheet("height:20px;padding:10px;")
		username.setPlaceholderText(" Enter Username")
		#---------------#

		layout_age_info = QHBoxLayout()
		day_input = QLineEdit()
		day_input.setStyleSheet("height:20px;padding:10px;")
		day_input.setPlaceholderText("Day")
		month_input = QLineEdit()
		month_input.setStyleSheet("height:20px;padding:10px;")
		month_input.setPlaceholderText("Month")
		year_input = QLineEdit()
		year_input.setStyleSheet("height:20px;padding:10px;")
		year_input.setPlaceholderText("Year")
		layout_age_info.addWidget(day_input)
		layout_age_info.addWidget(month_input)
		layout_age_info.addWidget(year_input)
		#---------------#
		password = QLineEdit()
		password.setStyleSheet("height:20px;padding:10px;")
		password.setPlaceholderText(" Enter Password")
		c_password = QLineEdit()
		c_password.setStyleSheet("height:20px;padding:10px;")
		c_password.setPlaceholderText(" Confirm Password")
		#--------------------------------------------------#
	

		# layout buttons
		buttons_layout = QHBoxLayout()
		create_account = QPushButton("Create Account")
		create_account.setStyleSheet("height:30px;")
		reset_input = QPushButton("Reset")
		reset_input.setStyleSheet("height:30px;")

		main_layout.addWidget(full_name)
		main_layout.addWidget(username)
		main_layout.addLayout(layout_age_info)
		main_layout.addWidget(password)
		main_layout.addWidget(c_password)
		# add butonslayout and buttons
		actions_group = QGroupBox("Actions")
		main_layout.addWidget(actions_group)
		actions_group.setLayout(buttons_layout)
		buttons_layout.addWidget(create_account)
		buttons_layout.addWidget(reset_input)

# هذا الكود معقد قليلا لانني كتبته بسرعة اذا
# وجدت اي اخطأ فالكمال لله
		