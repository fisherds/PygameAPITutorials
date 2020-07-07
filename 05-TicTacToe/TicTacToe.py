import pygame
import sys


# --------------------------- Conversion helper functions ---------------------------

def get_row_col(mouse_x, mouse_y):
    """ Converts an x, y screen position into a row, col value. """
    # Note: the top row is row=0 (bottom row=2), left col is col=0 (right col=2)
    spacing_x = 86 + 8
    spacing_y = 98 + 5
    top_y = 50
    left_x = 50
    return (mouse_y - top_y) // spacing_y, (mouse_x - left_x) // spacing_x


def get_xy_position(row, col):
    """ Converts a row, col value into an x, y screen position (upper left corner of that location). """
    spacing_x = 86 + 11
    spacing_y = 98 + 8
    top_y = 50
    left_x = 50
    return left_x + col * spacing_x, top_y + row * spacing_y


# --------------------------- Model Object ---------------------------

class Game:
    def __init__(self):
        # Done 5: Create an empty board, called board
        #         A list that contains 3 lists, each of those lists has 3 "." values.
        #     - Create a game_state_string set to X's turn
        #     - Create a turn_counter variable set to 0
        #     - Create a game_is_over variable set to False
        self.board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
        self.game_state_string = "X's Turn"
        self.turn_counter = 0
        self.game_is_over = False

    def __repr__(self):
        """ Returns a string that represents the game. """
        # Done 7: Use a "".format() command to create a string to shows the board, turn_counter, and game_state_string
        return "Board: {}  Turn: {}  State: {}".format(self.board, self.turn_counter, self.game_state_string)

    def take_turn(self, row, col):
        """Handle the current turn of the player and update board array"""
        # Done 8: Check if game_is_over and return from this method (doing nothing) if True
        # Done 9: Check if the value for row and col are valid.  Return (doing nothing) if invalid.
        # Done 10: Check if the mark at the requested row col is ".".  Return (doing nothing) if it is not "."
        if self.game_is_over:
            print("The game is over")
            return
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid row col")
            return
        if self.board[row][col] != ".":
            print("Location not empty")
            return

        # Done 11: Determine if it is X's turn or O's turn (even turn_counter means X's turn, odd for O's turn)
        #     - Modify the board by setting the current row col to an "X" or an "O" as appropriate
        #     - Update the game_state_string as appropriate "O's Turn" or "X's Turn"
        if self.turn_counter % 2 == 0:
            self.board[row][col] = "X"
            self.game_state_string = "O's Turn"
        else:
            self.board[row][col] = "O"
            self.game_state_string = "X's Turn"

        # Done 12: Increment the turn_counter
        self.turn_counter += 1

        self.check_for_game_over()

    def check_for_game_over(self):
        # TODO 18: If the turn_counter is 9 then the game is over
        #      If >=9 update the game_is_over value and set the game_state_string to "Tie Game"
        lines = []
        lines.append(self.board[0][0] + self.board[0][1] + self.board[0][2])
        lines.append(self.board[1][0] + self.board[1][1] + self.board[1][2])
        lines.append(self.board[2][0] + self.board[2][1] + self.board[2][2])
        lines.append(self.board[0][0] + self.board[1][0] + self.board[2][0])
        lines.append(self.board[0][1] + self.board[1][1] + self.board[2][1])
        lines.append(self.board[0][2] + self.board[1][2] + self.board[2][2])
        lines.append(self.board[0][0] + self.board[1][1] + self.board[2][2])
        lines.append(self.board[0][2] + self.board[1][1] + self.board[2][0])

        # TODO 19: Use the lines list to determine if there is a winner.
        #    If there is a winner, update the game_state_string, play a sound, and set game_is_over to True.


# --------------------------- View Controller ---------------------------

class ViewController(object):

    def __init__(self, screen):
        """ Creates the view controller (the Tic-Tac-Toe game you see) """
        # Done 4: Initialize the ViewController, as follows:
        #     - Store the screen.
        #     - Create the game model object.
        #     - Create images for the board, X, and O images filenames.
        #  Use instance variables:   screen game board_image x_image o_image
        self.screen = screen
        self.game = Game()
        self.board_image = pygame.image.load("board.png")
        self.x_image = pygame.image.load("x_mark.png")
        self.o_image = pygame.image.load("o_mark.png")

    def check_event(self, event):
        """ Takes actions as necessary based on the current event. """
        # TODO 16: If the event is pygame.MOUSEBUTTONUP
        #     Get the mouse click position as x and y variables
        #     Convert the x and y variables into row and col using get_row_col
        #     Inform the model object about this event
        # TODO 17: If the event is pygame.KEYDOWN
        #     Get the pressed_keys
        #     If the key is pygame.K_SPACE, then reset the game.
        pass

    def draw(self):
        """ Draw the board based on the marked store in the board configuration array """
        # Done 13: Blit the board_image onto the screen at the x y position of row=0 col=0
        self.screen.blit(self.board_image, get_xy_position(0, 0))
        # Done 14: Use a nested loop (via range) to go over all marks of the game.board
        #    If the mark is "X", blit an X image at the x y position of row col
        #    If the mark is "O", blit an O image at the x y position of row col

        for row in range(3):
            for col in range(3):
                mark = self.game.board[row][col]
                if mark == "X":
                    self.screen.blit(self.x_image, get_xy_position(row, col))
                if mark == "O":
                    self.screen.blit(self.o_image, get_xy_position(row, col))

        # Done 15: Update the display caption to be the game.game_state_string
        pygame.display.set_caption(self.game.game_state_string)


# --------------------------- Controller ---------------------------


def main():
    pygame.init()
    pygame.mixer.music.load("win.mp3")
    screen = pygame.display.set_mode((380, 400))
    view_controller = ViewController(screen)

    # Done 6: Write test code as needed to develop your model object.
    # print(view_controller.game)   # TODO: Delete all these tests later!
    # view_controller.game.take_turn(1, 1)  # X in the middle
    # print(view_controller.game)
    # view_controller.game.take_turn(0, 2)  # O in the top right
    # print(view_controller.game)
    # view_controller.game.take_turn(0, 0)  # X in the top left
    # print(view_controller.game)
    # view_controller.game.take_turn(1, 2)  # O in the right middle
    # print(view_controller.game)
    # view_controller.game.take_turn(2, 2)  # X wins!
    # print(view_controller.game)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            view_controller.check_event(event)

        screen.fill(pygame.Color("white"))
        view_controller.draw()
        pygame.display.update()


main()
