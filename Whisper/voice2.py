import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np

class VoiceRecorder(QWidget):
    def __init__(self):
        super().__init__()
        self.recording = False
        self.audio_data = None
        self.fs = 44100
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle('语音录音器')
        self.setGeometry(300, 300, 300, 150)
        
        layout = QVBoxLayout()
        
        self.record_button = QPushButton('开始录音')
        self.record_button.setStyleSheet("background-color: lightblue; padding: 15px;")
        self.record_button.clicked.connect(self.toggle_recording)
        
        layout.addWidget(self.record_button)
        self.setLayout(layout)
        
    def toggle_recording(self):
        if not self.recording:
            self.start_recording()
        else:
            self.stop_recording()
            
    def start_recording(self):
        self.recording = True
        self.record_button.setText('停止录音')
        self.record_button.setStyleSheet("background-color: lightcoral; padding: 15px;")
        
        # 开始录音（在后台线程中）
        self.stream = sd.InputStream(samplerate=self.fs, channels=1, dtype='int16')
        self.stream.start()
        self.audio_buffer = []
        
        QMessageBox.information(self, "录音开始", "录音已开始，请讲话...")
        
    def stop_recording(self):
        self.recording = False
        self.record_button.setText('开始录音')
        self.record_button.setStyleSheet("background-color: lightblue; padding: 15px;")
        
        # 停止录音并保存
        self.stream.stop()
        self.audio_data = np.concatenate(self.audio_buffer, axis=0)
        wav.write('output.wav', self.fs, self.audio_data)
        
        QMessageBox.information(self, "录音结束", "录音已完成，已保存为output.wav")
        
    def update_audio_buffer(self):
        # 定期读取音频数据
        if self.recording:
            data, overflowed = self.stream.read(self.fs)  # 读取1秒的数据
            self.audio_buffer.append(data)
            # 每100ms检查一次
            QTimer.singleShot(100, self.update_audio_buffer)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    recorder = VoiceRecorder()
    recorder.show()
    
    # 启动定时器读取音频数据
    from PyQt5.QtCore import QTimer
    timer = QTimer()
    timer.timeout.connect(recorder.update_audio_buffer)
    timer.start(100)
    
    sys.exit(app.exec_())


# 代码不行！！！