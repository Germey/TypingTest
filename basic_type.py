from typing import List, Tuple, Mapping, Dict, Set, AbstractSet, Sequence, NoReturn, Any, NewType, Callable, TypeVar, \
    Union, Optional, MutableMapping

var: List[int or float] = [2, 3.5]
var2: List[List[int]] = [[1, 2], [2, 3]]

var3: Mapping[str, int] = {'width': 20, 'height': 30}
var4: Dict[str, int] = {'width': 20, 'height': 30}


def size(rect: Mapping[str, int]) -> Dict[str, int]:
    return {'width': rect['width'] + 100, 'height': rect['width'] + 100}


def describe(s: AbstractSet[int]) -> Set[int]:
    return set(s)


def square(elements: Sequence[float]) -> List[float]:
    return [x ** 2 for x in elements]


def hello() -> NoReturn:
    print('hello')


def add(a):
    return a + 1


# def add(a: Any) -> Any:
#     return a + 1


Person = NewType('Person', Tuple[str, int, float])
person = Person(('Mike', 22, 1.75))

print(Callable, type(add), isinstance(add, Callable))


def date(year: int, month: int, day: int) -> str:
    return f'{year}-{month}-{day}'


def get_date_fn() -> Callable[[int, int, int], str]:
    return date


height = 1.75
Height = TypeVar('Height', int, float, None)


def get_height() -> Height:
    return height


print(get_height())


def process(fn: Union[str, Callable]):
    if isinstance(fn, str):
        # str2fn and process
        pass
    elif isinstance(fn, Callable):
        fn()


def judge(result: bool) -> Optional[str]:
    if result: return 'Error Occurred'


print(isinstance({'a': 1}, dict))
print(isinstance({'a': 1}, Mapping))
print(isinstance({'a': 1}, MutableMapping))
