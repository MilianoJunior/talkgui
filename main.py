import pyaudio
import wave

CHUNK = 1024  # Número de frames por buffer
FORMAT = pyaudio.paInt16  # Formato de áudio
CHANNELS = 2  # Estéreo
RATE = 44100  # Frequência de amostragem (samples por segundo)
RECORD_SECONDS = 3  # Duração da gravação
OUTPUT_FILENAME = "output.wav"

# Inicia a PyAudio
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Gravando...")

frames = []

for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Gravação finalizada.")

# Para a gravação
stream.stop_stream()
stream.close()
p.terminate()

# Salva o áudio gravado em um arquivo
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))