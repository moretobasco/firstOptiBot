from services.opti_connection import second_request

# this function puts values from the second request to datalist for the further iterating to get info user needs
def listing():
    data = second_request()
    datalist = []
    for item in data:
        datalist.append(data[item])
    return datalist


# print(listing())


# this function is searching data from datalist
def get_info(period: str = 'Jan 21', entity: str = 'Итого'):
    datalist = listing()
    final_data = [d['pl'] for d in datalist if d['month'] == period and d['company'] == entity]
    # for d in datalist:
    #     if d['month'] == period and d['company'] == entity:
    #         final_data.append(d['pl'])

    # data = next(d['pl'] for d in datalist if (d['month'] == period and d['company'] == entity))
    # final_data.append(data)

    return final_data

def parsed_data(period: str = 'Jan 21', entity: str = 'Итого') -> str:
    data = get_info(period, entity)
    result = ''.join(f"Выбранный период: {period}\nВыбранная компания: {entity}\n") + \
                   ''.join([f"{obj['plLine']}: {obj['amount']}\n" for obj in data])
    return result

print(parsed_data('Jan 21', 'Итого'))

