
# 1. 네임드 튜플 이용
from collections import namedtuple


MyStruct = namedtuple("MyStruct", "field1 field2 field3")


m = MyStruct("foo", "bar", "baz")


# 2. 클래스 이용해 구조체 형태로 정의
from dataclasses import dataclass


@dataclass
class Product:
    weight: int = None
    price: float = None


apple = Product()
apple.price = 10
print(apple.price)