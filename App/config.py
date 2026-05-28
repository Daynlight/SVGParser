from pathlib import Path
import arcade


# Path
SRC_PATH: Path = Path(__file__).resolve().parent

# Arcade
TITLE: str = "SVG Parser"
WINDOW_SIZE: list[int] = [800, 600]
BACKGROUND_COLOR: arcade.color = arcade.color.WHITE
FIXED_UPDATE_INTERVAL: float = 1.0 / 60.0

# Movement
MOVE_VELOCITY: float = 250.0
ZOOM_SPEED: float = 1.0
ZOOM_BOUND: tuple[float] = [0.1, 1000]