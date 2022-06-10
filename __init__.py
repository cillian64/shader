from tidal import *
from app import MenuApp
import st7789
import os
from apps.shader.shaders.utils import vec2, vec3


def dirname(path):
    """ Return the directory-part of a file path """
    return "/".join(path.split("/")[:-1])


def basename(path):
    """ Return the name of a file sans extension """
    return ".".join(path.split(".")[:-1])


def clamp_and_conv(c):
    """ Take a float colour and convert it to an integer between 0 and 255 """
    return min(max(int(c * 255.0), 0), 255)

def is_shader(f):
    """ Is a filename a shader or other cruft """
    return f.endswith(".py") and f != "utils.py" and f != "__init__.py"


class ShaderWindow:
    def __init__(self, shader, buttons, parent):
        print("Loading shader " + shader)
        self.buttons = buttons
        self.parent = parent
        parent.periodic(1000, self.redraw)
        self.buttons.on_press(JOY_CENTRE, lambda: parent.pop_window())
        self.buttons.on_press(BUTTON_A, lambda: parent.pop_window())
        self.buttons.on_press(BUTTON_B, lambda: parent.pop_window())

        self.shader = getattr(__import__("apps.shader.shaders." + shader).shader.shaders, shader)

        self.iResolution = vec2(float(display.width()), float(display.height()))
        self.iTime = 0.0

    def redraw(self):
        for y in range(display.height()):
            for x in range(display.width()):
                fragCoord = vec2(x, y)
                c = self.shader.mainImage(fragCoord, self.iResolution, self.iTime)
                c = (clamp_and_conv(c.x),
                     clamp_and_conv(c.y),
                     clamp_and_conv(c.z),
                )
                display.pixel(x, y, st7789.color565(*c))

        # Render as though 1s elapses between each frame
        self.iTime += 1.0


class MyApp(MenuApp):
    BG = MAGENTA
    FG = CYAN

    def load_shader(self, path):
        """ Run the shader at the specified path """
        print("Selected item: " + path)
        shader = ShaderWindow(path, self.buttons, self)
        self.push_window(shader, activate=True)

    def get_choices(self):
        """ Return all the .py files in the shaders directory, minus their extensions """
        print("Getting choices")
        cwd = dirname(__file__)
        shaders_dir = cwd + "/shaders/"
        # The full filename of each shader excluding path:
        shaders = [basename(f) for f in os.listdir(shaders_dir) if is_shader(f)]

        # Each choice is a tuple of
        return [(shader, lambda shader=shader: self.load_shader(shader)) for shader in shaders]

    def on_start(self):
        print("start")
        self.window.set_choices(self.get_choices(), redraw=False)

    def on_activate(self):
        print("activate")
        super().on_activate()


# Set the entrypoint for the app launher
main = MyApp