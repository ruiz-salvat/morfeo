from flask import Blueprint
from Database.Services.TradesService import TradesService

trades_controller = Blueprint('TradesController', __name__, template_folder='Controllers')

trades_service = TradesService(is_test=False)


@trades_controller.route('/get_trades_list', methods=['GET'])
def get_trades_list():
    return 'rattinson russoe'
