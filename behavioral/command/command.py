class Light:
    def on(self):
        print("Свет включен")

    def off(self):
        print("Свет выключен")


class Command:
    def execute(self):
        raise NotImplementedError


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()


class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()


light = Light()
on_cmd = LightOnCommand(light)
off_cmd = LightOffCommand(light)

remote = RemoteControl()

remote.set_command(on_cmd)
remote.press_button()

remote.set_command(off_cmd)
remote.press_button()


# =================


class MusicPlayer:

    def play(self):
        print("▶ Воспроизведение музыки")

    def stop(self):
        print("⏹ Остановлено")

    def pause(self):
        print("⏸ Музыка на паузе")


class PlayCommand(Command):
    def __init__(self, player: MusicPlayer):
        self.player = player

    def execute(self):
        self.player.play()


class StopCommand(Command):
    def __init__(self, player: MusicPlayer):
        self.player = player

    def execute(self):
        self.player.stop()


class PauseCommand(Command):
    def __init__(self, player: MusicPlayer):
        self.player = player

    def execute(self):
        self.player.pause()


player = MusicPlayer()

remote = RemoteControl()
remote.set_command(PlayCommand(player))
remote.press_button()

remote.set_command(PauseCommand(player))
remote.press_button()

remote.set_command(StopCommand(player))
remote.press_button()
