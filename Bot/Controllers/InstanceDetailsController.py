from flask import Blueprint, request
from Database.Services.InstanceStatesService import InstanceStatesService
from Database.Services.InstancesService import InstancesService
from Mappers.InstanceDetailsMapper import map_mongo_to_instance_details_dto

instance_details_controller = Blueprint('InstanceDetailsController', __name__, template_folder='Controllers')

instances_service = InstancesService(is_test=False)
instance_states_service = InstanceStatesService(is_test=False)


@instance_details_controller.route('/get_instance_details', methods=['GET'])
def get_instance_details():
    instance_id = request.headers.get('instance_id')
    instance_id = int(instance_id)  # TODO: remove
    instances_mongo = instances_service.get_element(instance_id)
    instance_states_mongo = instance_states_service.get_element(instance_id)
    instance_details_dto = map_mongo_to_instance_details_dto(instances_mongo, instance_states_mongo)
    return instance_details_dto.__dict__
