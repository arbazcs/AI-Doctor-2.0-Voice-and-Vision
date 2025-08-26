# # if you dont use pipenv uncomment the following:
# # from dotenv import load_dotenv
# # load_dotenv()

# #Step1a: Setup Text to Speech–TTS–model with gTTS
# import os
# from gtts import gTTS

# def text_to_speech_with_gtts_old(input_text, output_filepath):
#     language="en"

#     audioobj= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)


# input_text="Hi this is Ai with Amit!"
# text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

# #Step1b: Setup Text to Speech–TTS–model with ElevenLabs
# import elevenlabs
# from elevenlabs.client import ElevenLabs

# ELEVENLABS_API_KEY=os.environ.get("ELEVEN_API_KEY")

# def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
#     client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     audio=client.generate(
#         text= input_text,
#         voice= "Aria",
#         output_format= "mp3_22050_32",
#         model= "eleven_turbo_v2"
#     )
#     elevenlabs.save(audio, output_filepath)

# text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 

# # Step2: Use Model for Text output to Voice

# import subprocess
# import platform

# def text_to_speech_with_gtts(input_text, output_filepath):
#     language="en"

#     audioobj= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)
#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")


# input_text="Hi this is Ai with Hassan, autoplay testing!"
# #text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")


# def text_to_speech_with_elevenlabs(input_text, output_filepath):
#     client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     audio=client.generate(
#         text= input_text,
#         voice= "Aria",
#         output_format= "mp3_22050_32",
#         model= "eleven_turbo_v2"
#     )
#     elevenlabs.save(audio, output_filepath)
#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")

# text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")













# # # if you dont use pipenv uncomment the following:
# # # from dotenv import load_dotenv
# # # load_dotenv()

# # # Step1a: Setup Text to Speech–TTS–model with gTTS
# # import os
# # from gtts import gTTS
# # import subprocess
# # import platform

# # def text_to_speech_with_gtts_old(input_text, output_filepath):
# #     language = "en"
# #     audioobj = gTTS(text=input_text, lang=language, slow=False)
# #     audioobj.save(output_filepath)

# # input_text = "Hi this is Ai with Amit!"
# # text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

# # # Step1b: Setup Text to Speech–TTS–model with ElevenLabs
# # from elevenlabs import save
# # from elevenlabs.client import ElevenLabs

# # ELEVENLABS_API_KEY = os.environ.get("ELEVEN_API_KEY")

# # def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
# #     client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
# #     audio = client.generate(
# #         text=input_text,
# #         voice="Aria",
# #         output_format="wav",  # ✅ use wav for compatibility with Windows SoundPlayer
# #         model="eleven_turbo_v2"
# #     )
# #     save(audio, output_filepath)

# # # text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.wav")

# # # Step2: Use Model for Text output to Voice
# # def text_to_speech_with_gtts(input_text, output_filepath):
# #     language = "en"
# #     audioobj = gTTS(text=input_text, lang=language, slow=False)
# #     audioobj.save(output_filepath)
# #     play_audio(output_filepath)

# # def text_to_speech_with_elevenlabs(input_text, output_filepath):
# #     client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
# #     audio = client.generate(
# #         text=input_text,
# #         voice="Aria",
# #         output_format="wav",  # ✅ save as wav
# #         model="eleven_turbo_v2"
# #     )
# #     save(audio, output_filepath)
# #     play_audio(output_filepath)

# # def play_audio(output_filepath):
# #     os_name = platform.system()
# #     try:
# #         if os_name == "Darwin":  # macOS
# #             subprocess.run(['afplay', output_filepath])
# #         elif os_name == "Windows":  # Windows
# #             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
# #         elif os_name == "Linux":  # Linux
# #             subprocess.run(['aplay', output_filepath])  # or 'mpg123'/'ffplay'
# #         else:
# #             raise OSError("Unsupported operating system")
# #     except Exception as e:
# #         print(f"An error occurred while trying to play the audio: {e}")

# # # Example run:
# # # text_to_speech_with_elevenlabs("Hello, testing ElevenLabs!", "elevenlabs_testing.wav")


# voice_of_the_doctor.py

import os
import platform
import subprocess
from gtts import gTTS

# ---------- TEXT TO SPEECH with gTTS ----------
def text_to_speech(input_text, output_filepath="output.mp3"):
    language = "en"

    # Generate speech with Google TTS
    tts = gTTS(text=input_text, lang=language, slow=False)
    tts.save(output_filepath)

    # Try to auto play depending on OS
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            # Use Windows Media Player instead of SoundPlayer (better for mp3)
            subprocess.run(['powershell', '-c',
                            f'Start-Process -WindowStyle Hidden wmplayer "{output_filepath}"'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['mpg123', output_filepath])  # or 'aplay', 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"⚠️ Error playing audio: {e}")


# ---------- Example run ----------
if __name__ == "__main__":
    text_to_speech("Hello, this is your AI doctor speaking!", "doctor_voice.mp3")

