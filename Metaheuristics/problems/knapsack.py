from algorithms.genetic import Genome
from collections import namedtuple
from algorithms import genetic

Thing = namedtuple('Thing', ['name', 'value', 'weight'])

first_example = [
    Thing('Diamant', 2400, 900),
    Thing('Svärd', 5300, 3000),
    Thing('Mugg', 930, 300),
    Thing('Halsband', 1450, 120),
    Thing('Dolk', 1740, 300),
    Thing('Hjälm', 1950, 850),
    Thing('Ring', 1500, 50),
    Thing('Pärlor', 1620,250),
    Thing('Sköld', 5800, 3500),
    Thing('Tavla', 4800, 2600),
    Thing('Ädelsten', 2100, 600),
    Thing('10x Mynt', 1300, 200),
    Thing('20x Mynt', 2600, 400),
    Thing('30x Mynt', 3900, 600),
    Thing('Mantel', 1500, 50),
    Thing('Bälte', 1650, 100),
    Thing('Spegel', 2850, 200),
    Thing('Krona', 3890, 330),
    Thing('Tiara', 3360, 270),
    Thing('Karta', 1350, 70),
]

second_example = [
    Thing('A', 100, 70),
    Thing('B', 110, 80),
    Thing('C', 120, 90),
    Thing('D', 115, 95),
    Thing('E', 105, 85),
    Thing('F', 110, 80),
    Thing('G', 130, 110),
    Thing('H', 120, 150),
    Thing('I', 120, 150),


] + first_example


def generate_things(num: int) -> [Thing]:
    return [Thing(f"thing{i}", i, i) for i in range(1, num+1)]



def fitness(genome: Genome, things: [Thing], weight_limit: int) -> int:
    if len(genome) != len(things):
        raise ValueError("genome and things must be of same length")
    weight = 0
    value = 0

    for i, thing in enumerate(things):
        if genome[i] == 1:
            weight += thing.weight
            value += thing.value

            if weight > weight_limit:
                return 0

    return value



def from_genome(genome: Genome, things: [Thing]) -> [Thing]:
    result = []
    for i, thing in enumerate(things):
        if genome[i] == 1:
            result += [thing]

    return result


def to_string(things: [Thing]):
    return f"[{', '.join([t.name for t in things])}]"


def value(things: [Thing]):
    return sum([t.value for t in things])


def weight(things: [Thing]):
    return sum([p.weight for p in things])


def print_stats(things: [Thing]):
    print(f"Saker: {to_string(things)}")
    print(f"Värde: {value(things)}")
    print(f"Vikt: {weight(things)}")
