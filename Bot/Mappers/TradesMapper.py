from DataObjects.DTO.TradesDTO import TradesDTO


def map_mongo_to_trades_list_dto(trades_list_mongo):
    trades_list_dto = []
    for trade in trades_list_mongo:
        trades_dto = TradesDTO(trade["timestamp"], trade["operation"], trade["price"], trade["quote_amount"],
                               trade["gain"])
        trades_list_dto.append(trades_dto)
    return trades_list_dto
