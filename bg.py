from dataclasses import dataclass
import numpy as np

def rgb_csv(color: str):
    color = color.lstrip("#")
    return np.array(tuple(int(color[i:i+2], 16)/255 for i in (0, 2, 4)))



@dataclass
class Colors():
    darkest: np.ndarray
    dark: np.ndarray
    light: np.ndarray
    lightest: np.ndarray

    shadow: np.ndarray

    primary: np.ndarray
    secondary: np.ndarray
    tertiary: np.ndarray
    error: np.ndarray

    white: np.ndarray
    gray: np.ndarray
    black: np.ndarray

    red: np.ndarray
    yellow: np.ndarray
    green: np.ndarray
    blue: np.ndarray
    purple: np.ndarray

    @property
    def brown(self):
        return (self.red * 0.5 + self.yellow * 0.5) * .7 + self.black * 0.3

    @property
    def darkbrown(self):
        return (self.red * 0.5 + self.yellow * 0.5) * .4 + self.black * 0.6


light = Colors(
    darkest=np.array((197,199,187))/255,
    dark=np.array((198,196,172))/255,
    light=np.array((193,184,133))/255,
    lightest=np.array((186,176,120))/255,

    shadow=np.array((62,0,0))/255,

    primary=np.array((138,154,123))/255,
    secondary=np.array((142,164,162))/255,
    tertiary=np.array((196,116,110))/255,
    error=np.array((196,116,110))/255,

    white=np.array((200,192,147))/255,
    gray=np.array((98,94,90))/255,
    black=np.array((40,39,39))/255,

    red=np.array((196,116,110))/255,
    yellow=np.array((196,178,138))/255,
    green=np.array((138,154,123))/255,
    blue=np.array((139,164,176))/255,
    purple=np.array((162,146,163))/255,
)


dark = Colors(
    darkest=np.array((27,25,25))/255,
    dark=np.array((32,30,30))/255,
    light=np.array((50,49,49))/255,
    lightest=np.array((61,59,59))/255,

    shadow=np.array((62,0,0))/255,

    primary=np.array((138,154,123))/255,
    secondary=np.array((142,164,162))/255,
    tertiary=np.array((196,116,110))/255,
    error=np.array((196,116,110))/255,

    white=np.array((200,192,147))/255,
    gray=np.array((98,94,90))/255,
    black=np.array((40,39,39))/255,

    red=np.array((196,116,110))/255,
    yellow=np.array((196,178,138))/255,
    green=np.array((138,154,123))/255,
    blue=np.array((139,164,176))/255,
    purple=np.array((162,146,163))/255,
)

colors = {
    "light": light,
    "dark": dark,
}

# mode = "dark"
# if mode == "light":
#     c = light
# elif mode == "dark":
#     c = dark


