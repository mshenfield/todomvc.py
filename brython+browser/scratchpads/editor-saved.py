from browser import (
    ajax,
    document,
    html,
)

main = document['main']
name = "Max"
age = 26
main.textContent = f"Hello {name}, you are {age:04d}!"
main.style = dict(backgroundColor='blue', color='white')
main.style = dict(color='green', notattr=10)

# Style
main <= html.STYLE(".huge { font-size: 50px; }")

# Toggle the class
button = html.BUTTON("Toggle Largess")

button.bind('click', lambda e: main.classList.toggle("huge"))

main <= button

# My favorite things
favorites = [
    "Programming",
    "Sweets",
    "Westworld",
]

ul = html.UL([html.LI(fav) for fav in favorites])

main <= ul

# Canvas
import math

canvas = html.CANVAS(width=200, height=200)
canvas.style = dict(border="10px black", backgroundColor="white")
ctx = canvas.getContext("2d")
draw_button = html.BUTTON("Draw a circle")

x = 50

@draw_button.bind("click")
def draw_a_circle(event):
    global x
    ctx.beginPath()
    ctx.arc(x, 100, 50, 0, math.pi * 2)
    x += 25
    ctx.stroke()

main <= canvas
main <= draw_button

# Text input
text_area = html.TEXTAREA()

@text_area.bind("keydown")
def print_keystrokes(event):
    print(text_area.value)

main <= text_area

# query selector all
buttons = document.querySelectorAll('button')
print(len(buttons))

# ajax
main <= html.H2("BACON")
bacon_div = html.DIV()
main <= bacon_div

def make_some_bacon(request):
    print(request.responseText)
    bacon_div.textContent = request.responseText

req = ajax.ajax()
req.open('GET', "https://baconipsum.com/api/?type=meat-and-filler", True)
req.bind('complete', make_some_bacon)
req.send()
