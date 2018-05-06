from django import test
from city_engine.main_view_data.trash_management import TrashManagement
from city_engine.main_view_data.employee_allocation import EmployeeAllocation
from city_engine.models import City, list_of_models, Trash, \
    list_of_buildings_in_city, WindPlant, WaterTower, DumpingGround, CityField, Building
from django.apps import apps


class CityStatsTests(test.TestCase):
    fixtures = ['basic_fixture_resources_and_employees.json']

    def setUp(self):
        self.city = City.objects.get(id=1)
        self.TM = TrashManagement(self.city)
        self.EA = EmployeeAllocation(self.city)
        self.EA.run()
        self.EA.run()

    def test_generate_trash_except_dumping_ground(self):
        dg = DumpingGround.objects.create(city=self.city, city_field=CityField.objects.get(id=2))
        result = []
        for trash in dg.trash.values():
            result.append(trash)
        self.assertEqual(result, [])

        self.TM.generate_trash()

        for trash in dg.trash.values():
            result.append(trash)
        self.assertEqual(result, [])

    def test_generate_trash(self):
        result = []
        for building in list_of_buildings_in_city(self.city):
            for trash in building.trash.values():
                result.append(trash)
        self.assertEqual(len(result), 0)

        self.TM.generate_trash()

        for building in list_of_buildings_in_city(self.city):
            for trash in building.trash.values():
                result.append(trash)
        self.assertEqual(len(result), 4)

    def test_update_time(self):
        self.TM.generate_trash()
        for building in list_of_buildings_in_city(self.city):
            for trash in building.trash.values('time'):
                self.assertEqual(trash['time'], 0)
        self.TM.update_trash_time()
        for building in list_of_buildings_in_city(self.city):
            for trash in building.trash.values('time'):
                self.assertEqual(trash['time'], 1)

    def test_trash_delete(self):
        self.TM.generate_trash()
        result = []
        for building in list_of_buildings_in_city(self.city):
            for trash in building.trash.all():
                result.append(trash)
        self.assertEqual(len(result), 4)

        for building in list_of_buildings_in_city(self.city):
            for trash in building.trash.all():
                trash.delete()

        result_after = []
        for building in list_of_buildings_in_city(self.city):
            for trash in building.trash.all():
                result_after.append(trash)

        self.assertEqual(len(result_after), 0)
