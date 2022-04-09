#!/usr/bin/env python

"""
Problem description: Given a collection of horses(size X) and a racing track with a limited capacity(size Y).
Determine the fastest horse, without using a timing mechanism.
"""

import argparse
import random
from typing import List
from dataclasses import dataclass

@dataclass
class Horse:
    name: str
    speed: float

    def get_speed(self):
        return self.speed

@dataclass
class Track:
    name: str
    race_capacity: int


def race_horses(horses: List[Horse]) -> List[Horse]:
    return sorted(horses, key=Horse.get_speed, reverse=True)

def get_fastest_horse(horses: List[Horse], track: Track) -> Horse:
    if track.race_capacity < 2:
        raise ValueError(f'a track needs a minimum capacity of 2 to determine the fastest horse')
    while len(horses) > 1:
        race_group = horses[0: track.race_capacity]
        race_result = race_horses(race_group)
        for horse in race_result[1:]:
            horses.remove(horse)
    return horses

def generate_horses(amount: int) -> List[Horse]:
    horses = []
    for i in range(1, amount+1):
        name = f'horse_{i}'
        speed = random.uniform(1, 10)
        horses.append(Horse(name, speed))
    return horses


def main():
    arguments = parser.parse_args()
    horses = generate_horses(arguments.horses)
    track = Track('Hippodroom', arguments.track)
    print(f'The fastest horse is: {get_fastest_horse(horses, track)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-ho', '--horses', type=int, default=99, help='The amount of horses')
    parser.add_argument('-t', '--track', type=int, default=5, help='The amount of horses that race concurrently on the track')
    main()