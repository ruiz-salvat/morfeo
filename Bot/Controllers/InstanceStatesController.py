from flask import Blueprint, request
from Database.Services.InstanceStatesService import InstanceStatesService

instance_states_controller = Blueprint('InstanceStatesController', __name__, template_folder='Controllers')

instance_states_service = InstanceStatesService(is_test=False)


@instance_states_controller.route('/get_instance_states', methods=['GET'])
def get_instance_states():
    instance_id = request.headers.get('instance_id')
    instance_id = int(instance_id) # TODO: change
    instance_states = instance_states_service.get_element(instance_id)
    return str(instance_states) # TODO: JSON serializable
