from flask import Blueprint


instance_states_controller = Blueprint('InstanceStatesController', __name__, template_folder='Controllers')


@instance_states_controller.route('/get_instance_states', methods=['GET'])
def get_instance_states():
    return 'hello'
