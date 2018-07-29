from city_engine.main_view_data.employee_allocation import EmployeeAllocation
from city_engine.main_view_data.resources_allocation import ResourceAllocation
from city_engine.main_view_data.trash_management import TrashManagement, CollectGarbage
from city_engine.models import Farm, AnimalFarm, MassConventer, TradeDistrict


class TurnCalculation:

    def __init__(self, city, data, profile):
        self.city = city
        self.data = data
        self.profile = profile

    def run(self):
        TrashManagement(self.data).run()
        EmployeeAllocation(self.city, self.data).run()
        ResourceAllocation(self.city, self.data).run()
        CollectGarbage(self.city, self.data).run()
        self.collect_mass()
        self.execute_maintenance()
        self.update_build_status()
        self.update_harvest_status()
        self.update_breeding_status()
        self.trade_district_actions()

    def trade_district_actions(self):
        for td in [td for td in self.data.list_of_buildings if isinstance(td, TradeDistrict)]:
            td.creating_goods(self.city)

    def collect_mass(self):
        for mass_collector in [mc for mc in self.data.list_of_buildings if isinstance(mc, MassConventer)]:
            mass_collector.product_mass(self.city)

    def update_breeding_status(self):
        for farm in [b for b in self.data.list_of_buildings if isinstance(b, AnimalFarm)]:
            farm.farm_operation(self.profile.current_turn, self.data.user)

    def update_harvest_status(self):
        for farm in [b for b in self.data.list_of_buildings if isinstance(b, Farm)]:
            farm.update_harvest(self.profile.current_turn, self.data.user)

    def update_build_status(self):
        for building in self.data.list_of_buildings:
            if building.if_under_construction is True:
                building.build_status()

    def calculate_maintenance_cost(self):
        return sum([b['maintenance_cost'] for b in self.data.list_of_building_with_values])

    def execute_maintenance(self):
        self.city.cash - self.calculate_maintenance_cost()
