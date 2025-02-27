**requirements.txt**

```
pynput
```

---

### How It Works

- **Starting/Stopping:**  
  Press **F8** to start the automation. This spawns three threads:
  - One that presses **e** or **q** every 0.5–1 second.
  - One that presses **r** every 17–20 seconds.
  - One that every 1 second picks a random key from **W, A, S, D** and holds it for 0–3 seconds.
  
  Press **F9** to stop the automation, which cleanly stops and joins all threads.

- **Cross-Platform:**  
  The script uses the `pynput` library, which works on macOS as well as other platforms.

Feel free to adjust the keybinds or timing as needed. Just remember—if Taylor Swift can reinvent herself, you too can tweak your script to perfection, even if Edison sucks at chess!
