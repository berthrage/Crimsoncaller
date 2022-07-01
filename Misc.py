import GameWindow
import string

class Misc:
    inMenu = True
    menuSelected = "MainMenu"
    spriteChanged = False

    def __init__(self, isSelected="NewGame"):
        self.isSelected = isSelected

    @staticmethod
    def strDirectionRtoL(string):
        return string.replace("right", "left")

    class Timer:
        def __init__(self, time=0):
            self.time = time
            self.initialTime = time
            self.stop = False

        def executeTimer(self):
            if (not self.stop):
                self.time += GameWindow.GameWindow.window.delta_time()

        def stopTimer(self):
            self.stop = True

        def resumeTimer(self):
            self.stop = False

        def resetTimer(self):
            self.time = self.initialTime



    class SelfRefDict(dict):
        def __init__(self, *args, **kw):
            super(Misc.SelfRefDict, self).__init__(*args, **kw)
            self.itemlist = super(Misc.SelfRefDict, self).keys()
            self.fmt = string.Formatter()

        def __getitem__(self, item):
            return self.fmt.vformat(dict.__getitem__(self, item), {}, self)




