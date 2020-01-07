from collections import namedtuple
from dataclasses import dataclass
import objsize


@dataclass
class PetData:
    species: str
    name: str
    age: int


@dataclass(frozen=True)
class PetFrozen:
    species: str
    name: str
    age: int


Pet = namedtuple("Pet", "species name age")

frank = Pet(species="pigeon", name="Френк", age=None)
frank_data = PetData(species="pigeon", name="Френк", age=3)
frank_frozen = PetFrozen(species="pigeon", name="Френк", age=3)

print(objsize.get_deep_size(frank_data))
print(objsize.get_deep_size(frank))
print(objsize.get_deep_size(frank_frozen))
