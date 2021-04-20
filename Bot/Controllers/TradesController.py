import json
from flask import Blueprint, request
from Database.Services.TradesService import TradesService
from Mappers.TradesMapper import map_mongo_to_trades_list_dto
from Util.JsonEncoder import JsonEncoder

trades_controller = Blueprint('TradesController', __name__, template_folder='Controllers')

trades_service = TradesService(is_test=False)


@trades_controller.route('/get_trades_list', methods=['GET'])
def get_trades_list():
    instance_id = request.headers.get('instance_id')
    instance_id = int(instance_id)  # TODO: remove
    trades_list_mongo = trades_service.get_elements(instance_id)
    trades_list_dto = map_mongo_to_trades_list_dto(trades_list_mongo)
    trades_list_dto_dict = list(map(lambda x: x.__dict__, trades_list_dto))
    return json.dumps(trades_list_dto_dict)
