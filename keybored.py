from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PySide6.QtCore import QTimer, QUrl
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtCore import Qt
import sys
import os

# 音階リスト
sounds = ["C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4",
          "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5",
          "C6", "C#6", "D6", "D#6", "E6", "F6", "F#6", "G6", "G#6", "A6", "A#6", "B6"]

# 音声ファイルのディレクトリ（pianosounds フォルダに音源がある前提）
SOUND_DIR = "pianosounds"

class PianoApp(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("PianoApp")
    self.setGeometry(100, 50, 900, 300)
    self.setStyleSheet("background-color: #DEB887;")  # 背景色を茶色に設定

    layout = QHBoxLayout()

    self.buttons = {}  # ボタンの辞書
    self.sounds = {}  # 音声データの辞書

    for sound in sounds:
      button = QPushButton(sound)

      # 黒鍵（シャープ）のデザイン
      if "#" in sound:
        button.setFixedSize(30, 150)
        button.setStyleSheet(
            "background-color: black; color: white; border: none;")
        original_style = "background-color: black; color: white; border: none;"
        pressed_style = "background-color: gray; color: white; border: none;"
      else:  # 白鍵のデザイン
        button.setFixedSize(50, 200)
        button.setStyleSheet(
            "background-color: white; color: black; border: 1px solid black;")
        original_style = "background-color: white; color: black; border: 1px solid black;"
        pressed_style = "background-color: lightgray; color: black; border: 1px solid black;"

      self.buttons[button] = (original_style, pressed_style)

      # 音声ファイルのパスを取得
      sound_path = os.path.join(SOUND_DIR, f"{sound}.wav")

      if os.path.exists(sound_path):
        effect = QSoundEffect()
        effect.setSource(QUrl.fromLocalFile(sound_path))  # 音源ファイルをセット
        effect.setVolume(0.8)
        self.sounds[button] = effect

      # ボタン押下時の処理を設定
      button.clicked.connect(lambda checked=False,
                             btn=button: self.on_button_clicked(btn))
      layout.addWidget(button)

    self.setLayout(layout)

  def on_button_clicked(self, button):
    """ボタンが押されたときの処理"""
    original_style, pressed_style = self.buttons[button]
    button.setStyleSheet(pressed_style)  # 一時的に色を変更

    # 音を再生
    if button in self.sounds:
      self.sounds[button].play()

    # 200ms後に元の色に戻す
    QTimer.singleShot(200, lambda: button.setStyleSheet(original_style))


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = PianoApp()
  window.show()
  sys.exit(app.exec())
