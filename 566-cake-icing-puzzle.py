import time
from sympy import sympify
import sympy


def F(a: float, b: float, c: float) -> int:
    flip_size: tuple = sympify(
        f'360/{a}'), sympify(f'360/{b}'), sympify(f'360/{sympy.sqrt(c)}')
    flip_index: int = 0
    angle = sympify(0)
    target_angle = sympify(360)
    angle += flip_size[flip_index]
    print(f"{flip_index + 1}: {angle}")
    while sympy.Mod(angle, target_angle) != 0:
        flip_index += 1
        angle += flip_size[flip_index % 3]
        print(f"{flip_index + 1}: {angle}")
        time.sleep(0.01)
    return flip_index + 1


print(F(10, 14, 16))
