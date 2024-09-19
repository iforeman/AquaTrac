import factory
from factory.fuzzy import FuzzyChoice, FuzzyFloat, FuzzyInteger
from models.aquarium import Aquarium
from models.equipment import Equipment
from models.expense import Expense
from models.fish import Fish
from models.income import Income
from models.invertebrate import Invertebrate
from models.plant import Plant
from models.resource import Resource
from models.store import Store
from models.task import Task
from models.user import User
from models.water_parameter import WaterParameter
import random

class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user_{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    password = "password"  # In a real scenario, you'd use a hashed password

class StoreFactory(factory.Factory):
    class Meta:
        model = Store

    name = factory.Faker('company')
    address = factory.Faker('street_address')
    city = factory.Faker('city')
    country = factory.Faker('country')
    phone = factory.Faker('phone_number')
    email = factory.Faker('email')
    website = factory.Faker('url')

class AquariumFactory(factory.Factory):
    class Meta:
        model = Aquarium

    name = factory.Sequence(lambda n: f"Aquarium {n}")
    model = factory.Faker('word')
    tank_type = FuzzyChoice(['Community', 'Species', 'Cichlid', 'Biotype', 'Breeding', 'Planted', 'Shrimp', 'Fish-only', 'Coldwater'])
    shape = FuzzyChoice(['Cube/Rectangular', 'Bow-Front', 'Hexagonal', 'Cylinder', 'L-shaped', 'Pentagon', 'Column'])
    length = FuzzyFloat(50, 200)
    width = FuzzyFloat(30, 100)
    depth = FuzzyFloat(30, 100)
    capacity = factory.LazyAttribute(lambda obj: obj.length * obj.width * obj.depth / 1000)
    substrate = FuzzyChoice(['Gravel', 'Sand', 'Planted tank substrates', 'Clay-based substrates', 'Rocks', 'Fluorite', 'None'])
    setup_date = factory.Faker('date_this_decade')
    price = FuzzyFloat(50, 1000)
    store = factory.SubFactory(StoreFactory)
    user = factory.SubFactory(UserFactory)

class EquipmentFactory(factory.Factory):
    class Meta:
        model = Equipment

    aquarium = factory.SubFactory(AquariumFactory)
    type = FuzzyChoice(['Filter', 'Light', 'Pump', 'Heater', 'Other'])
    store = factory.SubFactory(StoreFactory)
    performance_lph = FuzzyFloat(100, 2000)
    model = factory.Faker('word')
    setup_date = factory.Faker('date_this_year')
    purchase_date = factory.Faker('date_this_year')
    unit_price = FuzzyFloat(10, 500)
    quantity = FuzzyInteger(1, 5)
    total = factory.LazyAttribute(lambda obj: obj.unit_price * obj.quantity)
    power_input = FuzzyFloat(10, 100)
    power_consumption = FuzzyFloat(5, 50)

class WaterParameterFactory(factory.Factory):
    class Meta:
        model = WaterParameter

    aquarium = factory.SubFactory(AquariumFactory)
    date = factory.Faker('date_this_month')
    temperature_min = FuzzyFloat(20, 25)
    temperature_max = FuzzyFloat(25, 30)
    ph_min = FuzzyFloat(6.0, 7.0)
    ph_max = FuzzyFloat(7.0, 8.0)
    gh_min = FuzzyFloat(4, 8)
    gh_max = FuzzyFloat(8, 12)
    kh_min = FuzzyFloat(3, 6)
    kh_max = FuzzyFloat(6, 10)
    nitrite_min = FuzzyFloat(0, 0.25)
    nitrite_max = FuzzyFloat(0.25, 0.5)
    nitrate_min = FuzzyFloat(5, 20)
    nitrate_max = FuzzyFloat(20, 40)

class FishFactory(factory.Factory):
    class Meta:
        model = Fish

    aquarium = factory.SubFactory(AquariumFactory)
    scientific_name = factory.Faker('scientific_name')
    common_name = factory.Faker('word')
    species = factory.Faker('word')
    origin = factory.Faker('country')
    quantity = FuzzyInteger(1, 10)
    max_size = FuzzyFloat(1, 30)
    min_tank_size = FuzzyFloat(10, 200)
    min_temp = FuzzyFloat(20, 25)
    max_temp = FuzzyFloat(25, 30)
    kh_min = FuzzyFloat(3, 6)
    kh_max = FuzzyFloat(6, 10)
    ph_min = FuzzyFloat(6.0, 7.0)
    ph_max = FuzzyFloat(7.0, 8.0)
    diet = FuzzyChoice(['Omnivore', 'Carnivore', 'Herbivore'])
    care_level = FuzzyChoice(['Easy', 'Moderate', 'Difficult'])
    temperament = FuzzyChoice(['Peaceful', 'Semi-aggressive', 'Aggressive'])

class PlantFactory(factory.Factory):
    class Meta:
        model = Plant

    aquarium = factory.SubFactory(AquariumFactory)
    scientific_name = factory.Faker('scientific_name')
    common_name = factory.Faker('word')
    family = factory.Faker('word')
    origin = factory.Faker('country')
    quantity = FuzzyInteger(1, 10)
    max_size = FuzzyFloat(5, 50)
    height = FuzzyFloat(5, 50)
    colour = factory.Faker('color_name')
    care_level = FuzzyChoice(['Easy', 'Moderate', 'Intermediate to Expert', 'Expert'])
    lighting = FuzzyChoice(['Low', 'Medium', 'Medium to High', 'High'])
    placement = FuzzyChoice(['Foreground', 'Midground', 'Midground to Background', 'Background', 'Floating'])

class InvertebrateFactory(factory.Factory):
    class Meta:
        model = Invertebrate

    aquarium = factory.SubFactory(AquariumFactory)
    scientific_name = factory.Faker('scientific_name')
    common_name = factory.Faker('word')
    species = factory.Faker('word')
    family = factory.Faker('word')
    sub_family = factory.Faker('word')
    max_size = FuzzyFloat(0.5, 10)
    min_tank_size = FuzzyFloat(5, 100)
    min_temp = FuzzyFloat(20, 25)
    max_temp = FuzzyFloat(25, 30)
    kh_min = FuzzyFloat(3, 6)
    kh_max = FuzzyFloat(6, 10)
    ph_min = FuzzyFloat(6.0, 7.0)
    ph_max = FuzzyFloat(7.0, 8.0)
    origin = factory.Faker('country')
    quantity = FuzzyInteger(1, 20)
    size = FuzzyFloat(0.1, 5)
    colour = factory.Faker('color_name')
    diet = FuzzyChoice(['Omnivore', 'Carnivore', 'Herbivore'])
    temperament = FuzzyChoice(['Peaceful', 'Semi-aggressive', 'Aggressive'])

class ExpenseFactory(factory.Factory):
    class Meta:
        model = Expense

    aquarium = factory.SubFactory(AquariumFactory)
    date = factory.Faker('date_this_year')
    item = factory.Faker('word')
    category = FuzzyChoice(['Equipment', 'Food', 'Medication', 'Decoration', 'Maintenance'])
    store = factory.SubFactory(StoreFactory)
    unit_price = FuzzyFloat(1, 100)
    quantity = FuzzyInteger(1, 10)
    total = factory.LazyAttribute(lambda obj: obj.unit_price * obj.quantity)
    notes = factory.Faker('sentence')

class IncomeFactory(factory.Factory):
    class Meta:
        model = Income

    aquarium = factory.SubFactory(AquariumFactory)
    date = factory.Faker('date_this_year')
    designation = factory.Faker('word')
    amount = FuzzyFloat(10, 500)
    store = factory.SubFactory(StoreFactory)
    notes = factory.Faker('sentence')

class ResourceFactory(factory.Factory):
    class Meta:
        model = Resource

    title = factory.Faker('sentence')
    name = factory.Faker('word')
    type = FuzzyChoice(['Book', 'Article', 'Video', 'Website'])
    quantity = FuzzyInteger(1, 5)
    unit_price = FuzzyFloat(10, 100)
    total_price = factory.LazyAttribute(lambda obj: obj.unit_price * obj.quantity)
    store = factory.SubFactory(StoreFactory)
    aquarium = factory.SubFactory(AquariumFactory)
    content = factory.Faker('paragraph')

class TaskFactory(factory.Factory):
    class Meta:
        model = Task

    aquarium = factory.SubFactory(AquariumFactory)
    description = factory.Faker('sentence')
    due_date = factory.Faker('future_date')
    completed = factory.Faker('boolean')
    type = FuzzyChoice(['Water Change', 'Cleaning', 'Feeding', 'Medication', 'Maintenance'])
    interval = FuzzyInteger(1, 30)
    week_day = FuzzyInteger(0, 6)
