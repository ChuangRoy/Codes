from tkinter import Button
import settings
import utils
import random
import os

## Cell
class Cell:
    all = []
    def __init__ (self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

    ## Create Cells
    def create_btn_object (self, location):
        btn = Button(
            location,
            width = settings.CELL_WIDTH,
            height = settings.CELL_HEIGHT,
            text=f"{self.x}, {self.y}"
        )
        btn.bind("<Button-1>", self.left_click_actions) # Left Click
        btn.bind("<Button-3>", self.right_click_actions) # Right Click
        self.cell_btn_object = btn
        Cell.all.append(self)

    ## Left click
    def left_click_actions (self, event):
        if self.is_mine:
           self.show_mine()
        else:
            self.show_cell()

    ## Right click
    def right_click_actions (self, event):
        # flag
        pass

    ## Pick which cell is the mine
    @staticmethod
    def randomize_mines ():
        picked_cells = random.sample(Cell.all, settings.MINES)
        print(f"mines : {picked_cells}")
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def show_mine(self): ## Lost
        # A logic to interrupt this game and display loss message
        self.cell_btn_object.configure(bg="red")

    def show_cell(self):
        pass

    def __repr__ (self):
        return f"Cell({self.x}, {self.y})" 
