from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import sys
import subprocess

class MainApp(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("楽器選択")
    self.setGeometry(100, 100, 300, 200)
    self.setStyleSheet("background-color: #F0F0F0;")

    layout = QVBoxLayout()

    # タイトルラベル
    title_label = QLabel("楽器を選択してください")
    title_label.setFont(QFont("Arial", 16))
    title_label.setStyleSheet("color: #333333;")
    title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(title_label)

    # ピアノボタン
    piano_button = QPushButton("ピアノ")
    piano_button.setFont(QFont("Arial", 14))
    piano_button.setStyleSheet(
        "background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px;"
    )
    piano_button.clicked.connect(self.launch_piano)
    layout.addWidget(piano_button)

    # ドラムボタン
    drum_button = QPushButton("ドラム")
    drum_button.setFont(QFont("Arial", 14))
    drum_button.setStyleSheet(
        "background-color: #2196F3; color: white; padding: 10px; border-radius: 5px;"
    )
    drum_button.clicked.connect(self.launch_drum)
    layout.addWidget(drum_button)

    self.setLayout(layout)

  def launch_piano(self):
    """ピアノアプリを起動"""
    subprocess.Popen([sys.executable, "keybored.py"])

  def launch_drum(self):
    """ドラムアプリを起動"""
    subprocess.Popen([sys.executable, "drum.py"])

if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainApp()
  window.show()
  sys.exit(app.exec())
