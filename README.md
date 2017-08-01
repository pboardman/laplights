# Laplights
Laplights is a python module used to control the leds and/or backlights on a laptop.
It only has support for the Thinkpad T460 for now but adding your own model is easy.

## How to use
just import laplights like this:
`from laplights import Lights`

then you can do something like:
```python
laptop_lights = Lights("t460")
laptop_lights.set_brightness("screen_backlight", 30)
```

## Adding your laptop model
To add your laptop model just add
```python
elif model == "YOUR_MODEL":
  light_info["screen_backlight"] = "PATH_TO_YOUR_SYSCLASS_SCREEN_BACKLIGHT_DIR"
  light_info["kb_backlight"] = "PATH_TO_YOUR_SYSCLASS_KEYBOARD_BACKLIGHT_DIR"
  light_info["pwr_led"] = "PATH_TO_YOUR_SYSCLASS_PWR_LED_DIR"
  #etc... You can add more if you like
```
