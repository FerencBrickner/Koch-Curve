from turtle import *
from random import choice


def setup(
    *, drawing_speed: int = 0, backward_distance: int = 400, pen_width: int = 2
) -> None:
    speed(drawing_speed)
    pensize(pen_width)
    penup()
    backward(backward_distance)
    pendown()


def compute_and_draw_koch_curve(
    *,
    side_length: int | float = 16,
    level: int = 4,
    angle: int | float = 70,
    colors: list[str] = [
        "red",
        "green",
        "blue",
        "orange",
        "purple",
        "brown",
        "black",
        "lime",
        "gray",
        "magenta",
        "teal",
        "olive",
        "turquoise",
        "cyan",
        "olive",
        "sienna",
        "violet",
    ]
) -> None:
    if level == 0:
        current_color: str = choice(colors)
        pencolor(current_color)
        forward(side_length)
        return
    compute_and_draw_koch_curve(
        side_length=side_length,
        level=level - 1,
        angle=angle,
        colors=colors,
    )
    left(angle)
    compute_and_draw_koch_curve(
        side_length=side_length,
        level=level - 1,
        angle=angle,
        colors=colors,
    )
    right(2 * angle)
    compute_and_draw_koch_curve(
        side_length=side_length,
        level=level - 1,
        angle=angle,
        colors=colors,
    )
    left(angle)
    compute_and_draw_koch_curve(
        side_length=side_length, level=level - 1, angle=angle, colors=colors
    )


def main(*args, **kwargs) -> None:
    """
    Drawing a Koch curve using turtle graphics.
    https://en.wikipedia.org/wiki/L-system
    """
    setup()
    compute_and_draw_koch_curve()
    mainloop()


if __name__ == "__main__":
    main()
