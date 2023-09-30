import random
from typing import Optional, Any, Union, List, Tuple, Dict, Iterable


class Character:
    def __init__(self, armor: int, power: int):
        self.power = power
        self.armor = armor
        self.health = 100

    def hit(self, damage: int):
        self.health -= damage

    def is_alive(self) -> bool:
        return self.health > 0


c1 = Character(20, 75)
c1.hit(20)

amount: Optional[int]
amount = None

attack: Any = 1

length: Union[int, float]
length = 1.3

quotes: List[int]  # Set, FrozenSet
quotes = [1]
quotes.append(12)

player: Tuple[str, int] = ('Kramnik', 2750)

changes_in_rating: Tuple[int, ...]
changes_in_rating = (1, 2, 3, 4, 5)

chess_players: Dict[str, int] = {"Kramnik": 2750}


def random_stream(min_val: int, max_val: int) -> Iterable[int]:
    while True:
        yield random.randint(min_val, max_val)
