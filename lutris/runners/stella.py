"""Runner for stella Atari 2600 emulator"""
from lutris.runners.runner import Runner


class stella(Runner):
    """Atari 2600 games emulator"""
    package = "stella"
    executable = "stella"
    platform = "Atari 2600"
    game_options = [{
        "option": "main_file",
        "type": "file",
        "label": "Cartridge"
    }]
    runner_options = []

    def __init__(self, settings=None):
        super(stella, self).__init__()
        if settings:
            self.cart = settings["game"]["main_file"]

    def play(self):
        command = ['stella', "\"%s\"" % self.cart]
        return {'command': command}
