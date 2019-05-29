try:
    import tkinter as tk
    from tkinter.filedialog import askopenfilename, asksaveasfilename
except ImportError:
    import Tkinter as tk
    from tkFileDialog import askopenfilename, asksaveasfilename
import random

FONT = (None, 50)
REPEATS_TO_LEARN = 3
#ネストを解く
def flatten(xss):
    return [x for xs in xss for x in xs]

def pop_up(title, content):
    toplevel = tk.Toplevel()
    label1 = tk.Label(toplevel, text=title, height=0, font=FONT)
    label1.pack()
    label2 = tk.Label(toplevel, text=content, height=0)
    label2.pack()

def read_cards(text):
    return [ (line.split(',')[0], line.split(',')[1], int(line.split(',')[2])) for line in text.split('\n') if line]

def format_cards_to_write(cards):
    return '\n'.join(','.join(card[:2])+','+str(card[2]) for card in cards)

def load_cards():
    global CARDS
    filename = askopenfilename()
    with open(filename) as f:
        CARDS = read_cards(f.read())

def save_progress():
    filename = asksaveasfilename()
    with open(filename, 'w+') as f:
        f.write(format_cards_to_write(CARDS))

root = tk.Tk()
root.title("Typing trainer")

load_button = tk.Button(root, text="Load Cards", command=load_cards)
load_button.pack()

save_button = tk.Button(root, text="Save Progress", command=save_progress)
save_button.pack()

text_to_copy = tk.Label(root, text = "Load, then type \"start\"", font=FONT)
text_to_copy.pack()


typing_ground = tk.Entry(root, font=FONT)
typing_ground.pack()
#フォーカスウィンドウをエントリーに渡す
typing_ground.focus_set()

points = tk.Label(root, text = "Score: 0", font=FONT)#初期画面
points.pack()

card = ('Type `start` to start (after loading a deck of cards)', "start", None)
def check_answer_correct(ev):
    try:
        CARDS
    except: 
        pop_up("Load Deck Before Usage", "Please load a deck of cards before starting.")
    if not CARDS:
        text_to_copy['text'] = "Congratulations! All cards learned!"
        return
    global card
    if typing_ground.get() == card[1]:
        card = random.choice( flatten([[c] * (4-c[2]) for c in CARDS]) ) 
        typing_ground.delete(0, 'end')
        text_to_copy['text'] = card[0]
        points['text'] = "Score: " + str(int(points['text'].split(': ')[-1]) + 1)
        CARDS.remove( card )
        if card[2] <= REPEATS_TO_LEARN:
            CARDS.append( (card[0], card[1], card[2] + 1) )
    elif typing_ground.get() == "???":
        text_to_copy['text'] = card[0] + ' -> ' + card[1]
        print(CARDS, card)
        CARDS.remove( [ c for c in CARDS if card[0]==c[0] and card[1]==c[1] ][0] ) 
        CARDS.append( (card[0], card[1], card[2] - 1) )
    print(card, typing_ground.get())

root.bind('<Key>', check_answer_correct)

root.mainloop()