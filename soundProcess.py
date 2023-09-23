from os import path
from pydub import AudioSegment
import librosa

# files
for i in range(11, 16):                                                                        
    src = f"soundtest16.mp3"
    dst = f"soundtest16.wav"

    # convert wav to mp3                                                            
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
