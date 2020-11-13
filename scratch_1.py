
from donkeycar.parts.controller import Joystick, JoystickController


class MyJoystick(Joystick):
    #An interface to a physical joystick available at /dev/input/js0
    def __init__(self, *args, **kwargs):
        super(MyJoystick, self).__init__(*args, **kwargs)


        self.button_names = {
            0x134 : 'Square',
            0x131 : 'Circle',
            0x133 : 'Triangle',
            0x130 : 'Cross',
            0x137 : 'R1',
            0x136 : 'L1',
            0x13a : 'Share',
            0x13b : 'Options',
            0x13c : 'Home',
            0x13e : 'RP',
            0x13d : 'LP',
            0x139 : 'R2P',
            0x138 : 'L2P',
        }


        self.axis_names = {
            0x0 : 'L Horizontal',
            0x1 : 'L Verticle',
            0x3 : 'R Horizontal',
            0x4 : 'R Verticle',
            0x5 : 'R2',
            0x2 : 'L2',
        }



class MyJoystickController(JoystickController):
    #A Controller object that maps inputs to actions
    def __init__(self, *args, **kwargs):
        super(MyJoystickController, self).__init__(*args, **kwargs)


    def init_js(self):
        #attempt to init joystick
        try:
            self.js = MyJoystick(self.dev_fn)
            self.js.init()
        except FileNotFoundError:
            print(self.dev_fn, "not found.")
            self.js = None
        return self.js is not None


    def init_trigger_maps(self):
        #init set of mapping from buttons to function calls

        self.button_down_trigger_map = {
            'Share' : self.toggle_manual_recording,
            'Triangle' : self.erase_last_N_records,
            'R1' : self.increase_max_throttle,
            'Share' : self.toggle_mode,
            'L2P' : self.emergency_stop,
            'L1' : self.decrease_max_throttle,
            'RP' : self.toggle_constant_throttle,
        }


        self.axis_trigger_map = {
            'R Horizontal' : self.set_steering,
            'L Verticle' : self.set_throttle,
        }


