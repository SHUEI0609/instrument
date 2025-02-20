from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtCore import QUrl, QTimer
from PySide6.QtGui import QPixmap, QPainter
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

    # 背景画像を設定
    self.background_image = QPixmap("drumkit.png")

    self.sounds = {}  # サウンドデータの辞書
    self.button_styles = {}  # ボタンの元のスタイルを保存する辞書

    # 各ドラムボタンを作成
    for part, (x, y, size) in drum_parts.items():
      button = QPushButton("", self)
      button.setGeometry(x, y, size, size)  # (x, y, width, height)

      # ハイハット、ライドシンバル、クラッシュシンバルの色を金色に設定
      if part in ["hi_hat", "ride", "crash"]:
        style = f"""
                    background-color: rgba(255, 215, 0, 80);
                    border-radius: {size // 2}px;
                    border: 2px solid black;
                """
      else:
        style = f"""
                    background-color: rgba(255, 255, 255, 80);
                    border-radius: {size // 2}px;
                    border: 2px solid black;
                """

      button.setStyleSheet(style)
      self.button_styles[button] = style  # 元のスタイルを保存

      # 音声ファイルのパスを取得
      sound_path = os.path.join(SOUND_DIR, f"{part}.wav")
      if os.path.exists(sound_path):
        effect = QSoundEffect()
        effect.setSource(QUrl.fromLocalFile(sound_path))
        effect.setVolume(0.9)
        self.sounds[button] = effect

      # ボタン押下時に音を鳴らし、ボタンを光らせる
      button.clicked.connect(lambda checked=False,
                             btn=button: self.on_button_clicked(btn))

  def paintEvent(self, event):
    """背景画像を描画する"""
    painter = QPainter(self)
    painter.drawPixmap(0, 0, self.background_image.scaled(self.size()))

  def on_button_clicked(self, button):
    """ボタンがクリックされたときの処理"""
    if button in self.sounds:
      self.sounds[button].play()  # 音を再生

      # ボタンを明るく光らせる
      button.setStyleSheet(self.button_styles[button] + """
                background-color: rgba(255, 255, 255, 200);
            """)

      # 0.2秒後に元のスタイルに戻す
      QTimer.singleShot(200, lambda: button.setStyleSheet(
          self.button_styles[button]))


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = DrumApp()
  window.show()
  sys.exit(app.exec())
