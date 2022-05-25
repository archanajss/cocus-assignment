from dataclasses import dataclass


@dataclass
class Car:
    brand_name: str
    model: str
    number_of_doors: int
    sports_car: bool