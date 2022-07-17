from tkinter import Button, Label, messagebox
import sys
import settings
import utils
import random
import os

## Cell
class Cell:
    all = []
    cell_cout = settings.CELL_COUNT
    cell_count_label = None
    opened_cells = 0
    def __init__ (self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
        self.opened = 0
        self.is_mine_candidate = 0

    ## Create Cells
    def create_btn_object (self, location):
        btn = Button(
            location,
            width = settings.CELL_WIDTH,
            height = settings.CELL_HEIGHT,
            # text=f"{self.x}, {self.y}"
        )
        btn.bind("<Button-1>", self.left_click_actions) # Left Click
        btn.bind("<Button-3>", self.right_click_actions) # Right Click
        self.cell_btn_object = btn
        Cell.all.append(self)


    @staticmethod
    def create_cell_count_label (location):
        label = Label (
            location,
            fg = "white",
            bg = "black",
            width = settings.CELL_WIDTH,
            height = settings.CELL_HEIGHT,
            text = f"Cells Left:{Cell.cell_cout}",
            font=("Consolas", 30)
        )
        Cell.cell_count_label = label
        # return label

    ## Left click
    def left_click_actions (self, event):
        if not self.is_mine_candidate: 
            if self.is_mine:
               self.show_mine()
            else:
                if self.surrounded_cells_mines_count == 0:
                    for cell in self.surrounded_cells:
                        cell.show_cell()
                self.show_cell()

    ## Right click
    def right_click_actions (self, event):
        # flag
        if not self.opened:
            if not self.is_mine_candidate:
                self.cell_btn_object.configure(bg="orange")
                self.is_mine_candidate = 1
                Cell.cell_cout -= 1
                self.opened = 1
                # Redraw Cell count
                if Cell.cell_count_label is not None:
                    Cell.cell_count_label.configure(text=f"Cells Left:{Cell.cell_cout}")
        elif self.is_mine_candidate:
            self.cell_btn_object.configure(bg="SystemButtonFace")
            self.is_mine_candidate = 0
            Cell.cell_cout += 1
            self.opened = 0
            # Redraw Cell count
            if Cell.cell_count_label is not None:
                Cell.cell_count_label.configure(text=f"Cells Left:{Cell.cell_cout}")

    ## Pick which cell is the mine
    @staticmethod
    def randomize_mines ():
        picked_cells = random.sample(Cell.all, settings.MINES)
        # print(f"mines : {picked_cells}")
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
        return picked_cells

    ## Get the Cell by axis
    def get_cell_by_axis (self, x, y):
        # Return a cell object based on x, y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell


    def show_mine (self): ## Lost
        # TODO:A logic to interrupt this game and display loss message
        self.cell_btn_object.configure(bg="red")
        messagebox.showerror(title="Game Over", message="You Clicked A Mine")
        sys.exit()

    def show_cell (self):
        if not self.opened:
            Cell.cell_cout -= 1
            # print(self.surrounded_cells)
            self.cell_btn_object.configure(
                    text=self.surrounded_cells_mines_count,
            )
            # Redraw Cell count
            if Cell.cell_count_label is not None:
                Cell.cell_count_label.configure(text=f"Cells Left:{Cell.cell_cout}")
            self.opened = 1
            Cell.opened_cells += 1
            if Cell.opened_cells == settings.CELL_COUNT - settings.MINES:
                messagebox.showinfo(title="You Win", message="You Win The Game !")
                sys.exit()

    @property
    def surrounded_cells (self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None ]
        return cells

    @property
    def surrounded_cells_mines_count (self):
        count = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                count += 1

        return count



    def __repr__ (self):
        return f"Cell({self.x}, {self.y})" 
