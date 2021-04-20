from DataObjects.DTO.InstanceDetailsDTO import InstanceDetailsDTO


def map_mongo_to_instance_details_dto(instances_mongo, instance_states_mongo):
    instance_details_dto = InstanceDetailsDTO(instances_mongo['instance_id'], instances_mongo['symbol'],
                                              instances_mongo['creation_time'], instances_mongo['pattern_id'],
                                              instances_mongo['time_scale'], instance_states_mongo['budget'],
                                              instance_states_mongo['initial_budget'], instance_states_mongo['clean_gains'],
                                              instance_states_mongo['partition_size'], instance_states_mongo['base_amount'],
                                              instance_states_mongo['n_partitions'], instance_states_mongo['n_partition_limit'])
    return instance_details_dto
