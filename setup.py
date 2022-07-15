import cx_Freeze

executables = [cx_Freeze.Executable('Main.py')]

cx_Freeze.setup(
    name="Crimsoncaller",
    options={'build_exe': {'packages':['pygame'],
                           'include_files':['__pycache__',
                           'fonts',
                           'music',
                           'playercharacters',
                           'PPlay',
                            'PPlay - Copy',
                            'sprites',
                            'Animations.py',
                             'Cerbero.py',
                              'CurrentScreen.py',
                               'Demon.py',
                                'Devotee.py',
                                 'Dragon.py',
                                 'Enemy.py',
                                 'Game.py',
                                 'GameWindow.py',
                                 'HUD.py',
                                 'Input.py',
                                 'Levels.py',
                                 'MainMenu.py',
                                 'MenuSprites.py',
                                 'Misc.py',
                                 'Player FunctionalCollision but not perfect.py',
                                 'Player.py',
                                 'soma.gif',
                                 'soma-2.gif',
                                 'soma-3.gif',
                                 'temp.py',
                                 'Warrior.py',
                                 'workingAnimCycle.txt',
                                   ]}},

    executables = executables
    
)