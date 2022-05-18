def my_algorithm(some_input):
    return [uncornify(webby) for webby in deconforbulate(some_input)]


def my_awful_copy_paste_non_solution(some_input):
    return [uncornify(webby) for webby in undepolified(some_input)]


def my_somewhat_better_solution(some_input, is_deconfobulated: bool = True):
    if is_deconfobulated:
        generator = deconforbulate
    else:
        generator = undepolified

    return [uncornify(webby) for webby in generator(some_input)]


from typing import Callable, Optional


def the_bees_knees_solution(some_input, generator: Optional[Callable] = None):
    if generator is None:
        generator = deconforbulate

    return [uncornify(webby) for webby in generator(some_input)]


from math import sqrt
from typing import Iterable


def points_in_ring(points: Iterable, radius: float, width: float) -> Iterable:
    inner = radius - 0.5 * width
    outer = radius + 0.5 * width
    for point in points:
        distance = sqrt(point[0] * point[0] + point[1] * point[1])
        if distance >= inner and distance <= outer:
            yield point


points = [[1, 2], [0, 0], [-2, 0], [-2, 3], [-3, -4], [4, 0], [5, 5]]

for point in points_in_ring(points, radius=3.5, width=1.0):
    print(f"Some complicated calculation at {point}")


from math import sqrt
from typing import Iterable, List, Optional, Callable


def euclidean(point: List[float]) -> float:
    return sqrt(sum((x * x) for x in point))


def manhattan(point: List[float]) -> float:
    return sum(abs(x) for x in point)


def points_in_ring(
    points: Iterable,
    radius: float,
    width: float,
    norm: Optional[Callable] = None,
) -> Iterable:
    if norm is None:
        norm = euclidean

    inner = radius - 0.5 * width
    outer = radius + 0.5 * width
    for point in points:
        distance = norm(point)
        if distance >= inner and distance <= outer:
            yield point


points = [[1, 2], [0, 0], [-2, 0], [-2, 3], [-3, -4], [4, 0], [5, 5]]

for point in points_in_ring(points, radius=3.5, width=1.0, norm=manhattan):
    print(f"Some complicated calculation at {point}")
