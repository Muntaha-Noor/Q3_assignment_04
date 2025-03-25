import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()
        self.create_grid()
        
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")

        self.canvas.bind("<Motion>", self.move_eraser)

    def create_grid(self):
        self.cells = []
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                cell = self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue")
                self.cells.append(cell)

    def move_eraser(self, event):
        self.canvas.coords(self.eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
        self.erase(event.x, event.y)

    def erase(self, x, y):
        overlapping = self.canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        for item in overlapping:
            if item != self.eraser:
                self.canvas.itemconfig(item, fill="white")

if __name__ == "__main__":
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop()
    