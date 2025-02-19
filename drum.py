from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtCore import QUrl
import sys
import os

# ドラム音ファイルのディレクトリ（drumsounds フォルダに音源がある前提）
SOUND_DIR = "drumsounds"

# 各ドラムパーツの配置（ボタンの座標、サイズ）
drum_parts = {
    "kick": (180, 200, 150),  # バスドラム
    "snare": (107, 170, 90),  # スネアドラム
    "hi_hat": (20, 170, 90),  # ハイハット
    "tom1": (180, 120, 75),  # タム1
    "tom2": (270, 120, 75),  # タム2
    "floor_tom": (320, 170, 100),  # フロアタム
    "crash": (20, 20, 150),  # クラッシュシンバル
    "ride": (330, 20, 150),  # ライドシンバル
}

class DrumApp(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Drum Kit")
    self.setGeometry(100, 50, 500, 400)

    # 背景にドラム画像を設定
    self.background = QLabel(self)
    self.background.setGeometry(0, 0, 500, 400)
    self.background.setStyleSheet(
        "background-image: url('drumkit.png'); background-size: cover;")

    self.sounds = {}  # サウンドデータの辞書

    # 各ドラムボタンを作成
    for part, (x, y, size) in drum_parts.items():
      button = QPushButton("", self)
      button.setGeometry(x, y, size, size)  # (x, y, width, height)
      button.setStyleSheet(f"""
          background-color: rgba(255, 255, 255, 80);
          border-radius: {size // 2}px;
          border: 2px solid black;
      """)

      # 音声ファイルのパスを取得
      sound_path = os.path.join(SOUND_DIR, f"{part}.wav")
      if os.path.exists(sound_path):
        effect = QSoundEffect()
        effect.setSource(QUrl.fromLocalFile(sound_path))
        effect.setVolume(0.9)
        self.sounds[button] = effect

      # ボタン押下時に音を鳴らす
      button.clicked.connect(lambda checked=False,
                             btn=button: self.play_sound(btn))

  def play_sound(self, button):
    """ボタンを押したときに対応する音を再生"""
    if button in self.sounds:
      self.sounds[button].play()


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = DrumApp()
  window.show()
  sys.exit(app.exec())
