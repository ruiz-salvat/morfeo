from DataObjects.DTO.InstanceDTO import InstanceDTO


def map_mongo_to_instances_dto(instances_mongo):
    instances_dto = []
    for instance in instances_mongo:
        instance_dto = InstanceDTO(instance['instance_id'], instance['symbol'], instance['pattern_id'],
                                   instance['status_id'])
        instances_dto.append(instance_dto)
    return instances_dto
