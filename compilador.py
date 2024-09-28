import re

class MediaCompiler:
    def __init__(self):
        self.video_loaded = None
        self.audio_loaded = None
        self.volume = 50  # Default volume

    def execute_command(self, command):
        command = command.strip()

        # Regex patterns for matching commands
        patterns = {
            'LOAD_VIDEO': r'^LOAD_VIDEO\s+(.+)$',
            'PLAY_VIDEO': r'^PLAY_VIDEO$',
            'PAUSE_VIDEO': r'^PAUSE_VIDEO$',
            'RESTART_VIDEO': r'^RESTART_VIDEO$',
            'JUMP_VIDEO': r'^JUMP\s+(\d+)$',
            'JUMP_BACK_VIDEO': r'^JUMP_BACK\s+(\d+)$',
            'NEXT_VIDEO': r'^NEXT_VIDEO$',
            'BACK_VIDEO': r'^BACK_VIDEO$',
            'STOP_VIDEO': r'^STOP_VIDEO$',
            'VOL_VIDEO': r'^VOL_VIDEO\s+(\d+)$',
            'LOAD_AUDIO': r'^LOAD_AUDIO\s+(.+)$',
            'PLAY_AUDIO': r'^PLAY_AUDIO$',
            'PAUSE_AUDIO': r'^PAUSE_AUDIO$',
            'RESTART_AUDIO': r'^RESTART_AUDIO$',
            'JUMP_AUDIO': r'^JUMP\s+(\d+)$',
            'JUMP_BACK_AUDIO': r'^JUMP_BACK\s+(\d+)$',
            'NEXT_AUDIO': r'^NEXT_AUDIO$',
            'BACK_AUDIO': r'^BACK_AUDIO$',
            'STOP_AUDIO': r'^STOP_AUDIO$',
            'VOL_AUDIO': r'^VOL_AUDIO\s+(\d+)$'
        }

        for command_type, pattern in patterns.items():
            match = re.match(pattern, command)
            if match:
                getattr(self, f'handle_{command_type.lower()}')(*match.groups())
                return True
        print("Invalid command:", command)
        

    def handle_load_video(self, name):
        self.video_loaded = name
        print(f"Video '{name}' loaded and ready to play.")

    def handle_play_video(self):
        if self.video_loaded:
            print(f"Playing video '{self.video_loaded}'.")
        else:
            print("No video loaded to play.")

    def handle_pause_video(self):
        if self.video_loaded:
            print(f"Video '{self.video_loaded}' paused.")
        else:
            print("No video loaded to pause.")

    def handle_restart_video(self):
        if self.video_loaded:
            print(f"Video '{self.video_loaded}' restarted.")
        else:
            print("No video loaded to restart.")

    def handle_jump_video(self, time):
        print(f"Jumping forward {time} seconds in video.")

    def handle_jump_back_video(self, time):
        print(f"Jumping back {time} seconds in video.")

    def handle_next_video(self):
        print("Moving to the next video.")

    def handle_back_video(self):
        print("Moving to the previous video.")

    def handle_stop_video(self):
        if self.video_loaded:
            print(f"Video '{self.video_loaded}' stopped.")
            self.video_loaded = None
        else:
            print("No video loaded to stop.")

    def handle_vol_video(self, value):
        self.volume = int(value)
        print(f"Volume set to {self.volume} for video.")

    def handle_load_audio(self, name):
        self.audio_loaded = name
        print(f"Audio '{name}' loaded and ready to play.")

    def handle_play_audio(self):
        if self.audio_loaded:
            print(f"Playing audio '{self.audio_loaded}'.")
        else:
            print("No audio loaded to play.")

    def handle_pause_audio(self):
        if self.audio_loaded:
            print(f"Audio '{self.audio_loaded}' paused.")
        else:
            print("No audio loaded to pause.")

    def handle_restart_audio(self):
        if self.audio_loaded:
            print(f"Audio '{self.audio_loaded}' restarted.")
        else:
            print("No audio loaded to restart.")

    def handle_jump_audio(self, time):
        print(f"Jumping forward {time} seconds in audio.")

    def handle_jump_back_audio(self, time):
        print(f"Jumping back {time} seconds in audio.")

    def handle_next_audio(self):
        print("Moving to the next audio.")

    def handle_back_audio(self):
        print("Moving to the previous audio.")

    def handle_stop_audio(self):
        if self.audio_loaded:
            print(f"Audio '{self.audio_loaded}' stopped.")
            self.audio_loaded = None
        else:
            print("No audio loaded to stop.")

    def handle_vol_audio(self, value):
        self.volume = int(value)
        print(f"Volume set to {self.volume} for audio.")

# Chamando
compiler = MediaCompiler()
commands = [
    "LOAD_VIDEO example_video.mp4",
    "PLAY_VIDEO",
    "PAUSE_VIDEO",
    "JUMP 30",
    "JUMP_BACK 10",
    "VOLa_VIDEO 75",
    "STOP_VIDEO",
    "LOAD_AUDIO example_audio.mp3",
    "PLAY_AUDIO",
    "VOL_AUDIO 60",
    "STOP_AUDIO"
]

# for cmd in commands:
#     executed = compiler.execute_command(cmd)
#     if not executed:
#         print(f"comando invalido: {cmd}")
#         break