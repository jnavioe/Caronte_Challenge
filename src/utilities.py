def fetch_by_id (id, list):
#Return all the elements with the same id
    fetch_list = []
    for element in list:
        if element.id == id:
            fetch_list.append(element)
    return fetch_list