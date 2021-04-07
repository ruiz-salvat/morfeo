def reduce(time_scale, array):
    new_array = []
    counter = 0
    aux_value = 0
    if time_scale > 1:
        for value in array:
            if counter >= time_scale - 1:
                aux_value = aux_value + value  # inserts the remaining value
                aux_value = aux_value / time_scale
                new_array.append(aux_value)
                aux_value = 0
                counter = 0
            else:
                aux_value = aux_value + value
                counter += 1
        if counter > 0:
            aux_value = aux_value / (counter + 1)
            new_array.append(aux_value)
        return new_array
    else:
        return array
