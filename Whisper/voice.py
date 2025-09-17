import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile

duration=5 # seconds
fs=44100 # sampling rate
print("Say something!")

audio = sd.rec(int(duration * fs),samplerate=fs,channels=1,dtype='int16')
sd.wait()

print("Recording finished")
temp_wav = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
wav.write('output.wav', fs, audio)
temp_wav.close()

