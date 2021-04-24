import json
from flask import Blueprint
from Database.Services.InstancesService import InstancesService
from Mappers.InstancesMapper import map_mongo_to_instances_dto

instances_controller = Blueprint('InstancesController', __name__, template_folder='Controllers')

instances_service = InstancesService(is_test=False)


@instances_controller.route('/get_instances', methods=['GET'])
def get_instances():
    instances_mongo = instances_service.get_all_elements()
    instances_dto = map_mongo_to_instances_dto(instances_mongo)
    instances_dto_dict = list(map(lambda x: x.__dict__, instances_dto))
    return json.dumps(instances_dto_dict)
