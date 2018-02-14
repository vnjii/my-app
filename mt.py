def making_tupes(the_dict):
    the_list = []
    for k, v in the_dict.iteritems():
        the_list.append((k,v))
    return the_list
