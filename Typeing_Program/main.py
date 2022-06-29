import curses
import time
import random

# Initial messages
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 0, "Hi, this is a Speed Typeing Program, the program to measure your typeing speed dãã.\n")
    stdscr.addstr("Lets start! Press any key to continue...\n")
    stdscr.getkey()
    stdscr.refresh()

# Chooses the text that will be thpe
def load_text():
    with open("text.txt", "r") as file:
        lines = file.readlines()
        return random.choice(lines).strip()

# Display changes in the text
def display_text(stdscr, text_to_type, current_text, calc=0):  
    stdscr.addstr(1, 0, text_to_type)
    stdscr.addstr(2, 0, f"Words per minute: {calc}")
    stdscr.addstr(1, 0, "")

    for index, char in enumerate(current_text):
        if char == text_to_type[index]:
            stdscr.addstr(1, index, char, curses.color_pair(1))
        else:
            stdscr.addstr(1, index, char, curses.color_pair(2))

# Controls the program
def typeing_program(stdscr):
    text_to_type = load_text()
    current_text = []
    calc_speed = 0
    start_time = time.time()

    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1) 
        calc_speed = round(len(current_text) / (time_elapsed / 60) / 5)

        stdscr.clear()
        display_text(stdscr, text_to_type, current_text, calc_speed)
        stdscr.refresh()

        if(text_to_type == "".join(current_text)):
            stdscr.nodelay(False)
            stdscr.addstr("\nYou are finished! Nice!\n")
            stdscr.addstr("Press any key to continue...\n")
            stdscr.getkey()
            break
        
        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            quit()

        elif key in ("KEY_BACKSPACE", "\b", "\x7f") and len(current_text) > 0:
            current_text.pop()

        elif len(current_text) < len(text_to_type):
            current_text.append(key)

# setups the collors and inicialite program
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)

    while True:
        typeing_program(stdscr)
    
        stdscr.addstr("Would you like to play again?\n")
        stdscr.addstr("Type 1 for yes or anything else to exit? Your answer: ")
        user_choice = stdscr.getkey()

        if user_choice != "1":
            break

    stdscr.clear()
    stdscr.addstr(1, 0, "Bye Bye!")
    stdscr.getkey()
    

#Starts the program
curses.wrapper(main)
