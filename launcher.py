#launcher
# This is the main file that will be run to start the program
from main_menu import menu
from turtle_game import map_editor
from game_play2 import game

state=1
play=True
while play:
    if state==1:
        state=menu()
    elif state==2:
        state=map_editor()
    elif state==3:
        state=game()