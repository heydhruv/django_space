from faker import Faker
from .models import *
from Blackhole.models import Blackhole
import random
import logging

logger = logging.getLogger(__name__)
fake = Faker()


def generate_Universe_demo_data(n=100) -> None:
    try:
        for _ in range (n):
            name = fake.name()

            Universe.objects.create(
                name = name,
            )
    except Exception as e:
        logger.error(e)

def generate_galaxy_demo_data(n=100) -> None:
    try:
        for _ in range (n):
            universe = Universe.objects.all()
            blackhole = Blackhole.objects.all()

            name = fake.name()
            universe_name_id = random.choice(universe)
            size = random.randint(100,100000000)
            dark_matter = fake.boolean()
            star_count = random.randint(100,100000000000)
            center = random.choice(blackhole)
            Collision_time = random.randint(100,1000000000)

            Galaxy.objects.create(
                name = name,
                universe_name_id = universe_name_id,
                size = size,
                dark_matter = dark_matter,
                star_count = star_count,
                center = center,
                Collision_time = Collision_time,
            )
    except Exception as e:
        logger.error(e)

def generate_solar_system_demo_data(n=100) -> None:
    try:
        for _ in range (n):

            galaxy = Galaxy.objects.all()
            name = fake.name()
            galaxy_id = random.choice(galaxy)
            number_of_planets = random.randint(1,100)
            number_of_stars = random.randint(100,100000000)

            SolarSystem.objects.create(
                name = name,
                galaxy_id = galaxy_id,
                number_of_planets = number_of_planets,
                number_of_stars = number_of_stars,
            )
    except Exception as e:
        logger.error(e)

def generate_planet_demo_data(n=100) -> None:
    try:
        for _ in range (n):
            solar_system = SolarSystem.objects.all()
            name = fake.name()
            solar_system_id = random.choice(solar_system)
            size = random.randint(100,10000)
            habitable = fake.boolean()
            lowest_temperature = random.randint(0,10000)
            highest_temperature = random.randint(0,10000)
            gravity = random.randint(0,1000)

            Planet.objects.create(
                name = name,
                solar_system_id = solar_system_id,
                size = size,
                habitable = habitable,
                lowest_temperature = lowest_temperature,
                highest_temperature = highest_temperature,
                gravity = gravity,
            )
    except Exception as e:
        logger.error(e)