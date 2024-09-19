
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.user import User
from models.store import Store
from models.aquarium import Aquarium
from models.equipment import Equipment
from models.water_parameter import WaterParameter
from models.fish import Fish
from models.plant import Plant
from models.invertebrate import Invertebrate
from models.expense import Expense
from models.income import Income
from models.resource import Resource

class TestDatabaseModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up an in-memory SQLite database for testing
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()

    def test_user_model(self):
        user = User(username="Test User", email="test@example.com", password="password", password_hash="hashed_password")
        self.session.add(user)
        self.session.commit()
        self.assertEqual(user.username, "Test User")
        self.assertEqual(user.email, "test@example.com")

    def test_store_model(self):
        store = Store(name="Test Store", address="123 Test St")
        self.session.add(store)
        self.session.commit()
        self.assertEqual(store.name, "Test Store")
        self.assertEqual(store.address, "123 Test St")

    def test_aquarium_model(self):
        store = Store(name="Test Store")
        self.session.add(store)
        self.session.commit()
        aquarium = Aquarium(name="Test Aquarium", model="Model X", tank_type="Community", shape="Cube/Rectangular",
                            length=100.0, width=50.0, depth=40.0, capacity=200.0, substrate="Gravel",
                            setup_date="2023-01-01", price=150.0, store_id=store.id, user_id=1)
        self.session.add(aquarium)
        self.session.commit()
        self.assertIn(aquarium, store.aquariums)
        self.assertEqual(aquarium.model, "Model X")

    def test_fish_model(self):
        store = Store(name="Test Store")
        self.session.add(store)
        self.session.commit()
        aquarium = Aquarium(name="Test Aquarium", model="Model X", tank_type="Community", shape="Cube/Rectangular",
                            length=100.0, width=50.0, depth=40.0, capacity=200.0, substrate="Gravel",
                            setup_date="2023-01-01", price=150.0, store_id=store.id, user_id=1)
        self.session.add(aquarium)
        self.session.commit()
        fish = Fish(aquarium_id=aquarium.id, scientific_name="Test Fish", common_name="Test", species="Test Species",
                     origin="Test Origin", quantity=10, max_size=5.0, min_tank_size=20.0, min_temp=22.0,
                     max_temp=28.0, kh_min=3.0, kh_max=8.0, ph_min=6.5, ph_max=7.5, species_information="Test Info",
                     aquarium_care="Easy", feeding_nutrition="Test Nutrition", diet="Omnivore",
                     aquarium_type="Community", care_level="Easy", temperament="Peaceful",
                     purchase_date="2023-01-01", unit_price=10.0, store_id=store.id)
        self.session.add(fish)
        self.session.commit()
        self.assertEqual(fish.scientific_name, "Test Fish")
        self.assertEqual(fish.common_name, "Test")

    def test_plant_model(self):
        store = Store(name="Test Store")
        self.session.add(store)
        self.session.commit()
        aquarium = Aquarium(name="Test Aquarium", model="Model X", tank_type="Community", shape="Cube/Rectangular",
                            length=100.0, width=50.0, depth=40.0, capacity=200.0, substrate="Gravel",
                            setup_date="2023-01-01", price=150.0, store_id=store.id, user_id=1)
        self.session.add(aquarium)
        self.session.commit()
        plant = Plant(aquarium_id=aquarium.id, scientific_name="Test Plant", common_name="Test", family="Test Family",
                       origin="Test Origin", quantity=5, max_size=10.0, height=5.0, colour="Green",
                       care_level="Easy", lighting="Medium", placement="Foreground", purchase_date="2023-01-01",
                       min_temp=20.0, max_temp=28.0, kh_min=3.0, kh_max=8.0, ph_min=6.5, ph_max=7.5,
                       unit_price=5.0, store_id=store.id)
        self.session.add(plant)
        self.session.commit()
        self.assertEqual(plant.scientific_name, "Test Plant")
        self.assertEqual(plant.family, "Test Family")

    def test_invertebrate_model(self):
        store = Store(name="Test Store")
        self.session.add(store)
        self.session.commit()
        aquarium = Aquarium(name="Test Aquarium", model="Model X", tank_type="Community", shape="Cube/Rectangular",
                            length=100.0, width=50.0, depth=40.0, capacity=200.0, substrate="Gravel",
                            setup_date="2023-01-01", price=150.0, store_id=store.id, user_id=1)
        self.session.add(aquarium)
        self.session.commit()
        invertebrate = Invertebrate(aquarium_id=aquarium.id, scientific_name="Test Invertebrate", common_name="Test",
                                     species="Test Species", family="Test Family", sub_family="Test Subfamily",
                                     max_size=5.0, min_tank_size=10.0, min_temp=20.0, max_temp=28.0, kh_min=3.0,
                                     kh_max=8.0, ph_min=6.5, ph_max=7.5, origin="Test Origin", quantity=5,
                                     size=2.0, colour="Blue", diet="Omnivore", aquarium_type="Community",
                                     temperament="Peaceful", purchase_date="2023-01-01", unit_price=15.0, store_id=store.id)
        self.session.add(invertebrate)
        self.session.commit()
        self.assertEqual(invertebrate.scientific_name, "Test Invertebrate")
        self.assertEqual(invertebrate.sub_family, "Test Subfamily")

    def test_equipment_model(self):
        store = Store(name="Test Store")
        self.session.add(store)
        self.session.commit()
        aquarium = Aquarium(name="Test Aquarium", model="Model X", tank_type="Community", shape="Cube/Rectangular",
                            length=100.0, width=50.0, depth=40.0, capacity=200.0, substrate="Gravel",
                            setup_date="2023-01-01", price=150.0, store_id=store.id, user_id=1)
        self.session.add(aquarium)
        self.session.commit()
        equipment = Equipment(aquarium_id=aquarium.id, type="Filter", store_id=store.id, performance_lph=1000.0,
                              model="Model Y", setup_date="2023-01-01", purchase_date="2023-01-01",
                              unit_price=50.0, quantity=1, total=50.0, power_input=50.0, power_consumption=30.0,
                              run_time_duration=24.0)
        self.session.add(equipment)
        self.session.commit()
        self.assertEqual(equipment.type, "Filter")
        self.assertEqual(equipment.model, "Model Y")

    def test_water_parameter_model(self):
        store = Store(name="Test Store")
        self.session.add(store)
        self.session.commit()
        aquarium = Aquarium(name="Test Aquarium", model="Model X", tank_type="Community", shape="Cube/Rectangular",
                            length=100.0, width=50.0, depth=40.0, capacity=200.0, substrate="Gravel",
                            setup_date="2023-01-01", price=150.0, store_id=store.id, user_id=1)
        self.session.add(aquarium)
        self.session.commit()
        water_param = WaterParameter(aquarium_id=aquarium.id, date="2023-01-01")
        self.session.add(water_param)
        self.session.commit()
        self.assertEqual(water_param.date, "2023-01-01")

    def test_expense_model(self):
        store = Store(name="Test Store")
        self.session.add(store)
        self.session.commit()
        aquarium = Aquarium(name="Test Aquarium", model="Model X", tank_type="Community", shape="Cube/Rectangular",
                            length=100.0, width=50.0, depth=40.0, capacity=200.0, substrate="Gravel",
                            setup_date="2023-01-01", price=150.0, store_id=store.id, user_id=1)
        self.session.add(aquarium)
        self.session.commit()
        expense = Expense(aquarium_id=aquarium.id, date="2023-01-01", item="Test Item", category="Test Category",
                          store_id=store.id, unit_price=10.0, quantity=1, total=10.0)
        self.session.add(expense)
        self.session.commit()
        self.assertEqual(expense.item, "Test Item")
        self.assertEqual(expense.category, "Test Category")

    def test_income_model(self):
        store = Store(name="Test Store")
        self.session.add(store)
        self.session.commit()
        aquarium = Aquarium(name="Test Aquarium", model="Model X", tank_type="Community", shape="Cube/Rectangular",
                            length=100.0, width=50.0, depth=40.0, capacity=200.0, substrate="Gravel",
                            setup_date="2023-01-01", price=150.0, store_id=store.id, user_id=1)
        self.session.add(aquarium)
        self.session.commit()
        income = Income(aquarium_id=aquarium.id, date="2023-01-01", designation="Test Income", amount=100.0,
                        store_id=store.id)
        self.session.add(income)
        self.session.commit()
        self.assertEqual(income.designation, "Test Income")
        self.assertEqual(income.amount, 100.0)

    def test_resource_model(self):
        store = Store(name="Test Store")
        self.session.add(store)
        self.session.commit()
        aquarium = Aquarium(name="Test Aquarium", model="Model X", tank_type="Community", shape="Cube/Rectangular",
                            length=100.0, width=50.0, depth=40.0, capacity=200.0, substrate="Gravel",
                            setup_date="2023-01-01", price=150.0, store_id=store.id, user_id=1)
        self.session.add(aquarium)
        self.session.commit()
        resource = Resource(title="Test Resource", name="Resource Name", type="Food", quantity=10, unit_price=5.0,
                            total_price=50.0, store_id=store.id, aquarium_id=aquarium.id, content="Content of the resource")
        self.session.add(resource)
        self.session.commit()
        self.assertEqual(resource.title, "Test Resource")
        self.assertEqual(resource.content, "Content of the resource")

    def test_edge_cases(self):
        with self.assertRaises(Exception):
            invalid_fish = Fish(scientific_name=None, common_name="Invalid Fish", aquarium_id=999)

    def test_data_validation(self):
        with self.assertRaises(ValueError):
            invalid_aquarium = Aquarium(name="Invalid Aquarium", model="Invalid Model", tank_type="InvalidType",
                                        shape="Cube/Rectangular", length=0, width=0, depth=0, capacity=0,
                                        substrate="Gravel", setup_date="2023-01-01", price=150.0, store_id=1, user_id=1)

    @classmethod
    def tearDownClass(cls):
        cls.session.close()
        Base.metadata.drop_all(cls.engine)

if __name__ == '__main__':
    unittest.main()
