import cv2
import pandas as pd
import audiotest  # Ensure this module handles text-to-speech and sound playing

# Path to the image file and CSV file
img_path = r'c:\Users\user\Desktop\desktop everything in this folder\aiml project\colorpic.jpg'
csv_path = r'c:\Users\user\Desktop\desktop everything in this folder\aiml project\colors.csv'

# Load the image
img = cv2.imread(img_path)

# Check if the image was loaded successfully
if img is None:
    print(f"Error: Unable to open image file at {img_path}")
    exit()

# Global variables for the mouse callback function
clicked = False
r = g = b = x_pos = y_pos = 0

# Reading the CSV file with pandas and assigning column names
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv(csv_path, names=index, header=None)

# Function to calculate the closest matching color name
def get_color_name(R, G, B):
    minimum = float('inf')
    cname = None
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d < minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

# Mouse callback function to get x, y coordinates on double click
def draw_function(event, x, y, flags, param):
    global b, g, r, x_pos, y_pos, clicked
    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

# Create a window and bind the mouse callback function to it
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:
    cv2.imshow("image", img)
    if clicked:
        # Draw a rectangle and put the text of the color name and RGB values
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)
        text = get_color_name(r, g, b) + f' R={r} G={g} B={b}'
        
        # Display the text on the image
        cv2.putText(img, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        
        # For very light colors, display text in black
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        
        # Play the color information as sound
        sound = audiotest.text_to_speech(text)
        audiotest.play_sound(sound)
        
        clicked = False

    # Break the loop when the user hits the 'esc' key
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
