import pyaudio

import wave

import requests

CHUNK = 1024


FORMAT = pyaudio.paInt16

CHANNELS = 1

RATE = 44100

p = pyaudio.PyAudio()


stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = CHUNK)

print("start recording...")

frames = []

seconds = 7

for i in range(0,int(RATE/CHUNK*seconds)):

    data = stream.read(CHUNK)

    frames.append(data)

print("recording stopped")

stream.stop_stream()

stream.close()

p.terminate()


wf = wave.open("output.wav",'wb')

wf.setnchannels(CHANNELS)

wf.setsampwidth(p.get_sample_size(FORMAT))

wf.setframerate(RATE)

wf.writeframes(b''.join(frames))

wf.close()



url = "https://shazam-api6.p.rapidapi.com/shazam/recognize/"



files = { "upload_file": open("output.wav", "rb") }

headers = {

	"X-RapidAPI-Key": "22fd03dd82msh6d2bbbd35dbf33ep10a9e4jsncdb5007202f4",

	"X-RapidAPI-Host": "shazam-api6.p.rapidapi.com"

}

response = requests.post(url, files=files, headers=headers)

print(response.json())