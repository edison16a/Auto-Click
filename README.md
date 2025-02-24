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

Yes! You can absolutely have **two circles** and randomly click in both areas. Below, I’ll update the script to let you pick **two positions** with separate radii and click randomly within both.

---

### **Pixel-to-Inch Conversion**
On **Windows**, the number of pixels per inch (**PPI or DPI**) depends on your display settings:
- **Standard displays**: ~96 PPI
- **High-resolution displays** (like 4K monitors): ~150-200+ PPI

To **estimate the radius in inches**, use this formula:
\[
\text{radius in inches} = \frac{\text{radius in pixels}}{\text{PPI}}
\]

For example, if your screen is **96 PPI**:
- **100 px ≈ 1.04 inches**
- **200 px ≈ 2.08 inches**
- **500 px ≈ 5.2 inches**

I’ll also generate a **visual representation** of the radius using `matplotlib` so you can see how big each radius is.

---

### **Updated Python Script (Two Circles + Visual Representation)**
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

clicking = False  # Global flag for clicking
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

def random_click():
    """Autoclicks randomly within the two selected circles."""
    global clicking

    while clicking:
        for x, y, radius in positions:
            rand_x = x + random.randint(-radius, radius)
            rand_y = y + random.randint(-radius, radius)
            pyautogui.click(rand_x, rand_y)
            time.sleep(random.uniform(0.1, 0.5))  # Random delay between clicks

def start_clicking():
    """Starts the autoclicking thread."""
    global clicking
    clicking = True
    thread = threading.Thread(target=random_click, daemon=True)
    thread.start()

def stop_clicking():
    """Stops the clicking process."""
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

