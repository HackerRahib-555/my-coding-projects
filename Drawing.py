from tkinter import *
from PIL import Image, ImageDraw

# Function to start drawing
def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x + 5, y + 5, fill=current_color, width=2)
    draw_object.line([x, y, x+5, y+5], fill=current_color, width=2)

# Function to save the drawing as an image
def save_drawing():
    img.save("drawing.png")

# Functions to set the drawing color
def set_color(color):
    global current_color
    current_color = color

# Tkinter window setup
root = Tk()
root.title("Drawing Pad with Color Options")

# Create a blank image for drawing
img = Image.new("RGB", (500, 500), color="white")
draw_object = ImageDraw.Draw(img)

# Canvas for drawing
canvas = Canvas(root, width=1000, height=500, bg="white")
canvas.pack()

# Initial drawing color


# Bind mouse click event for drawing
canvas.bind("<B1-Motion>", draw)

# Color buttons
colors = {
    "Red": "red",
    "Orange": "orange",
    "Yellow": "yellow",
    "Green": "green",
    "Blue": "blue",
    "Indigo": "indigo",
    "Violet": "violet",
    "Black": "black",
    "White": "white",
    "Gray": "gray",
    "Pink": "pink",
    "Brown": "brown",
}

for color_name, color_code in colors.items():
    button = Button(root, text=color_name, command=lambda c=color_code: set_color(c))
    button.pack(side=LEFT, padx=5)

# Save button
save_button = Button(root, text="Save Drawing", command=save_drawing)
save_button.pack()

# Start the Tkinter main loop
root.mainloop()