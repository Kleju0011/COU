from city_engine.models import list_of_models
from django.db.models import Sum
from city_engine.main_view_data.employee_allocation import EmployeeAllocation
from city_engine.main_view_data.resources_allocation import ResourceAllocation
from city_engine.main_view_data.trash_management import TrashManagement


class TurnCalculation(object):
    def __init__(self, city):
        self.city = city
        TrashManagement(self.city).run()
        EmployeeAllocation(self.city).run()
        ResourceAllocation(self.city).run()
        self.update_build_status()

    def update_build_status(self):
        for model in list_of_models:
            for building in model.objects.filter(city=self.city):
                building.build_status()
        self.city.save()


def calculate_maintenance_cost(list_of_models, city):
    total_maintenance_cost = 0
    for model in list_of_models:
        total_cost_per_model = model.objects.filter(city=city).aggregate(Sum('maintenance_cost'))['maintenance_cost__sum']
        if total_cost_per_model is not None:
            total_maintenance_cost += total_cost_per_model
    return total_maintenance_cost
