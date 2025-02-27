import time
import random
import threading
from pynput.keyboard import Controller, GlobalHotKeys

# Initialize the keyboard controller (Taylor would say, "Shake it off" when mistakes happen)
keyboard = Controller()

# Flag to control the automation threads
automation_running = False
threads = []

def press_e_q():
    """Press either 'e' or 'q' every 0.5-1 second at random intervals."""
    while automation_running:
        time.sleep(random.uniform(0.5, 1))
        key = random.choice(['e', 'q'])
        keyboard.press(key)
        keyboard.release(key)
        print(f"Pressed {key}")  # Debug log

def press_r():
    """Press 'f' every 17-20 seconds at random intervals."""
    while automation_running:
        time.sleep(random.uniform(0.5, 1))
        keyboard.press('f')
        keyboard.release('f')
        print("Pressed f")  # Debug log

def hold_wasd():
    """
    Simulate human-like movement by randomly selecting a movement pattern:
    - Single keys: 'w', 'a', 's', 'd'
    - Diagonals: 'wa', 'wd', 'sa', 'sd'
    - Or no movement for a brief pause.
    Each pattern is held for a random duration between 0.5 and 3 seconds.
    """
    # List of possible movement patterns (empty string = pause)
    move_patterns = ['', 'w', 'a', 's', 'd', 'wa', 'wd', 'sa', 'sd']
    while automation_running:
        pattern = random.choice(move_patterns)
        if pattern:
            # Press all keys in the pattern simultaneously (for diagonals)
            for key in pattern:
                keyboard.press(key)
            duration = random.uniform(0.5, 3)
            print(f"Holding '{pattern}' for {duration:.2f} seconds")
            time.sleep(duration)
            for key in pattern:
                keyboard.release(key)
            print(f"Released '{pattern}'")
        else:
            # Pause (simulate a human taking a brief moment of inaction)
            pause_duration = random.uniform(0.2, 1)
            print(f"Pausing movement for {pause_duration:.2f} seconds")
            time.sleep(pause_duration)


def start_automation():
    """Starts the automation threads."""
    global automation_running, threads
    print("F8 clicked: Starting automation...")
    if not automation_running:
        automation_running = True
        # Create and start threads for each function
        t1 = threading.Thread(target=press_e_q)
        t2 = threading.Thread(target=press_r)
        t3 = threading.Thread(target=hold_wasd)
        threads = [t1, t2, t3]
        for t in threads:
            t.start()

def stop_automation():
    """Stops the automation and waits for threads to finish."""
    global automation_running, threads
    print("F9 clicked: Stopping automation...")
    if automation_running:
        automation_running = False
        for t in threads:
            t.join()
        threads = []

if __name__ == "__main__":
    print("Press F8 to start automation and F9 to stop automation.")
    # Global hotkeys: F8 starts and F9 stops the automation.
    with GlobalHotKeys({
        '<f8>': start_automation,
        '<f9>': stop_automation
    }) as h:
        h.join()
