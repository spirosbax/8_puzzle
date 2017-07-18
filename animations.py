from asciimatics.renderers import FigletText, Rainbow
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
from asciimatics.effects import Cycle, Stars, RandomNoise
from asciimatics import event
import sys


def present_puzzle(length=230):
    def demo(screen):
        effects = [
            RandomNoise(screen,
                        signal=Rainbow(screen,FigletText("8 Puzzle")))
        ]
        screen.play([Scene(effects, length)], stop_on_resize=True,repeat=False)
        screen.close()
    Screen.wrapper(demo)

def present_god_mode(length=100,stars=500):
    def present(screen):
        effects = [
            Cycle(
                screen,
                FigletText("GOD MODE", font='doh'),
                int(screen.height / 2 - 13)),
            Cycle(
                screen,
                FigletText("ENGAGED", font='doom'),
                int(screen.height / 2 + 6)),
            Stars(screen, stars)
        ]
        screen.play([Scene(effects, length)],repeat=False)
        screen.close()

    Screen.wrapper(present)



