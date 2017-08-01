import threading
import time

class Lights:
    def __init__(self, laptop_model):
        self.set_model(laptop_model)


    def set_model(self, new_model):
        self.light_info = self.get_lights_info(new_model)

        if not self.light_info:
            print("The laptop {0} is not supported.".format(new_model))
            exit(1)


    def set_brightness(self, light, brightness):
        if self.light_info[light]:
            with open("{0}/brightness".format(self.light_info[light]), "w") as light:
                light.write(str(brightness))


    def get_max_brightness(self, light):
        if self.light_info[light]:
            with open("{0}/max_brightness".format(self.light_info[light]), "r") as max:
                return int(max.read())


    def get_brightness(self, light):
        if self.light_info[light]:
            with open("{0}/brightness".format(self.light_info[light]), "r") as max:
                return int(max.read())


    def get_lights_info(self, model):
        light_info = {}
        if model == "t460":
            light_info["screen_backlight"] = "/sys/class/backlight/intel_backlight/"
            light_info["kb_backlight"] = "/sys/class/leds/tpacpi::kbd_backlight/"
            light_info["pwr_led"] = "/sys/class/leds/tpacpi::power/"
        else:
            return None

        return light_info
