from pynput import keyboard, mouse
from time import sleep

class Macro:
    def __init__(self, records:list) -> None:

        self.records = records
        self.kb = keyboard.Controller()

        pass

    def route_part(self, part_number):

        sleep(0.75) #TODO: Wait for ctrl + shift + click to be released

        self.kb.type(part_number + '\t'*7)    

        for record in self.records:

            for item in record:
                print(item, end="  ")
            print()

            self.enter_record(record)

    def enter_record(self, record):
        '''Routine for entering a record when the first sequence box is highlighted.'''

        seq = record[0]
        cell = record[1]
        resource = record[2]
        usage = record[3]
        description = record[-1]

        sleep(0.1)

        self.kb.type(f"{seq}\t\t\t{cell}\r")
        self.kb.type(f"{seq}\t{resource}\t\t\t{usage}\t")
        self.close_oracle_window()
        self.kb.type('\t'*18 + description)
        self.ctrl_key('s')
        self.kb.press(keyboard.Key.down)
        self.kb.release(keyboard.Key.down)
    
    def enter_locator_pn(self, pn:str) -> None:
        '''Macro.
        Assumes that this is run when user ctrl + clicks into zoom find item box.'''

        sleep(0.75) #TODO: Wait for ctrl + shift + click to be released

        self.kb.type(f"{pn}\r\r")
        self.ctrl_key(keyboard.Key.tab)
        self.kb.press(keyboard.Key.down); self.kb.release(keyboard.Key.down)

        pass

    def enter_locator(self, locator:str) -> None:
        '''Macro.
        Assumes that this is run when user ctrl + clicks into POU locator box.'''

        sleep(0.75) #TODO: Wait for ctrl + shift + click to be released

        self.kb.type(locator)
        self.ctrl_key('s')
        self.ctrl_key(keyboard.Key.tab)
        self.kb.type(f'\t{locator}')
        self.ctrl_key('s') # Save
        self.alt_key('i') # WIP Mass Update

        pass

    def ctrl_key(self, key):
        '''ctrl + key'''

        try:
            with self.kb.pressed(keyboard.Key.ctrl):
                self.kb.press(key)
                self.kb.release(key)
        except:
            raise KeyError("Invalid key used.")
        
    def alt_key(self, key):
        '''alt + key'''

        try:
            with self.kb.pressed(keyboard.Key.alt):
                self.kb.press(key)
                self.kb.release(key)
        except:
            raise KeyError("Invalid key used.")
        
    def close_oracle_window(self):
        self.ctrl_key(keyboard.Key.f4)

class Listener:

    def __init__(self, func, use_shift=True):

        self.use_shift = use_shift
        self.func = func
        self.ctrl_pressed = False
        self.shift_pressed = False
        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.keyboard_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)

    def on_click(self, x, y, button, pressed):

        # Check if the mouse button is pressed
        if pressed and self.ctrl_pressed:
            
            if self.use_shift and not self.shift_pressed:
                return
            
            print(f"Running macro...")
            
            self.func() # Run function
            
            # Stop the listeners
            self.mouse_listener.stop()
            self.keyboard_listener.stop()
            return
            

    def on_press(self, key):
        try:
            if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                self.ctrl_pressed = True

            elif key == keyboard.Key.shift:
                self.shift_pressed = True

            elif key == keyboard.KeyCode.from_char('q'):
                self.mouse_listener.stop()
                self.keyboard_listener.stop()
        except AttributeError:
            pass

    def on_release(self, key):

        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            self.ctrl_pressed = False

        elif key == keyboard.Key.shift:
            self.shift_pressed = False

    def run(self):

        self.mouse_listener.start()
        self.keyboard_listener.start()
        self.mouse_listener.join()
        self.keyboard_listener.join()


if __name__ == "__main__":
    f = lambda: print("Function called")
    l = Listener(f)
    l.run()