# Auto-Click
Here’s the `requirements.txt` file for the script:

```
pyautogui
keyboard
matplotlib
tk
numpy
```

### **How to Install Dependencies**
Run the following command in your terminal or command prompt:
```bash
pip install -r requirements.txt
```

This will install all the necessary Python packages. 🚀
Python 3.8+

---


### **Updated Python Script (Two Circles + Visual Representation)**
Got it! I'll modify the script so that:  

1️⃣ **First circle (joystick movement)** → Moves the mouse **like a Brawl Stars joystick**, with smooth movement in random directions within the radius.  
2️⃣ **Second circle (attack button)** → Just presses a button at random intervals.  
3️⃣ **Random clicks** → Still happen for extra variability.  

---

### **Updated Python Code:**
```python
import pyautogui
import keyboard
import random
import time
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
import numpy as np
import math

clicking = False
positions = []  # Stores center points and radii

def pick_positions():
    """Selects two positions with radii using a GUI."""
    global positions

    root = tk.Tk()
    root.withdraw()  # Hide the main window

    for i in range(2):  # Pick 2 positions
        messagebox.showinfo("Select Position", f"Hover over position {i+1} and press ENTER")

        while True:
            if keyboard.is_pressed("enter"):
                x, y = pyautogui.position()
                break
            time.sleep(0.1)

        radius = simpledialog.askinteger("Radius", f"Enter the clicking radius for Position {i+1} (px):", minvalue=1)
        positions.append((x, y, radius))

    root.destroy()

def visualize_click_areas():
    """Creates a visual representation of the clicking areas."""
    fig, ax = plt.subplots()
    ax.set_title("Clicking Radius Visualization")
    ax.set_xlim(0, 1920)  # Adjust according to screen resolution
    ax.set_ylim(0, 1080)  # Adjust according to screen resolution
    ax.invert_yaxis()  # Match screen coordinate system

    for i, (x, y, r) in enumerate(positions):
        circle = plt.Circle((x, y), r, color=np.random.rand(3,), alpha=0.5, label=f"Circle {i+1}")
        ax.add_patch(circle)
        ax.text(x, y, f"P{i+1}", color="black", ha="center", va="center")

    ax.legend()
    plt.show()

def joystick_movement():
    """Simulates a joystick movement within the first radius."""
    x, y, radius = positions[0]

    while clicking:
        angle = random.uniform(0, 2 * math.pi)  # Random direction
        distance = random.uniform(0, radius)  # Random distance within radius
        move_x = x + int(math.cos(angle) * distance)
        move_y = y + int(math.sin(angle) * distance)

        pyautogui.moveTo(move_x, move_y, duration=0.05)  # Smooth movement
        time.sleep(random.uniform(0.05, 0.2))  # Move frequently

def press_attack_button():
    """Presses the attack button at a fixed rate in the second radius."""
    x, y, _ = positions[1]

    while clicking:
        pyautogui.click(x, y)
        time.sleep(random.uniform(0.2, 0.5))  # Random attack speed

def random_click():
    """Performs extra random clicks for added variation."""
    while clicking:
        x, y, radius = positions[random.randint(0, 1)]  # Choose between both areas
        rand_x = x + random.randint(-radius, radius)
        rand_y = y + random.randint(-radius, radius)
        pyautogui.click(rand_x, rand_y)
        time.sleep(random.uniform(0.3, 0.7))  # Less frequent than joystick

def start_clicking():
    """Starts all clicking/movement threads."""
    global clicking
    clicking = True

    # Joystick movement
    threading.Thread(target=joystick_movement, daemon=True).start()
    
    # Attack button clicking
    threading.Thread(target=press_attack_button, daemon=True).start()

    # Extra random clicks
    threading.Thread(target=random_click, daemon=True).start()

def stop_clicking():
    """Stops all clicking/movement threads."""
    global clicking
    clicking = False
    print("Stopped clicking.")

# Run GUI to select two positions
pick_positions()

# Visualize the click areas
visualize_click_areas()

# Start clicking when the user presses "F6"
keyboard.add_hotkey("f6", start_clicking)
print("Press F6 to start clicking.")

# Stop clicking when the user presses "ESC"
keyboard.add_hotkey("esc", stop_clicking)
print("Press ESC to stop clicking.")

keyboard.wait("esc")  # Keep the script running
```

---

### **What’s New?**
✅ **First Position (Joystick)** → Moves mouse **smoothly in random directions** like a joystick.  
✅ **Second Position (Attack Button)** → Clicks like a normal attack button with random timing.  
✅ **Extra Random Clicks** → Still happen for extra unpredictability.  
✅ **Balanced Timing** → Joystick moves quickly, attack button has a controlled click rate.  

### **How to Use**
1️⃣ Run the script  
2️⃣ Hover over the **joystick position** and press **ENTER**  
3️⃣ Enter **radius for movement**  
4️⃣ Hover over the **attack button** and press **ENTER**  
5️⃣ Enter **radius for attack**  
6️⃣ Press **F6** to start  
7️⃣ Press **ESC** to stop  

---

### **How This Works:**
1. **Select Two Positions**  
   - Hover over the first position and **press ENTER**.
   - Enter the **radius** (in pixels) when prompted.
   - Repeat for the **second position**.

2. **Visualize Click Areas**  
   - The script opens a window showing two circles over a simulated screen (1920x1080 default).  
   - This helps you **estimate the size** of each clicking area.

3. **Start & Stop Clicking**  
   - **Press `F6`** to start autoclicking in both circles.  
   - **Press `ESC`** to stop.

---

### **Example: Pixel to Inch Guide**
If you're using a **96 PPI display**:
| Pixels (Radius) | Approx. Inches |
|---------------|---------------|
| 50 px | 0.52 in |
| 100 px | 1.04 in |
| 200 px | 2.08 in |
| 500 px | 5.2 in |

If you have a **high-DPI (e.g., 144 PPI) display**, divide by **144 instead of 96**.

---

### **What’s New in This Version?**
✅ **Supports two separate clicking areas**  
✅ **Displays a visualization of the clicking radius**  
✅ **Still works with F6 (Start) and ESC (Stop)**  

Now you can **visually check** how large the radius is and get clicking within two different areas! 🚀

