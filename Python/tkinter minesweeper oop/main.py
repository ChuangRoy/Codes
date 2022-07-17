# cmd /k python "$(FULL_CURRENT_PATH)" & PAUSE & EXIT

from tkinter import *
from cell import *
import settings
import utils


root = Tk()

## Override the settings of the window
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.configure(bg="black")
root.title("Minesweeper Game")
root.resizable(False , False)

## Frames

top_frame = Frame(
    root,
    bg="black",
    width=settings.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg="black",
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg="black",
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

game_label = Label(
    top_frame,
    fg = "white",
    bg = "black",
    text = "Minesweeper Game",
    font = ("Consolas", 40)
)
game_label.place(
    x = utils.width_prct(25),
    y=0
)

## Cells

for x in range(settings.GRID_COLUMNS):
    for y in range(settings.GRID_ROWS):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x, row=y)

Cell.randomize_mines()

# Create Cell Count label
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label.place(x=0, y=0)


## Run the window
root.mainloop()

