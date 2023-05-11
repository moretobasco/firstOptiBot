from services.opti_connection import second_request
import locale

# this function puts values from the second request to datalist for the further iterating to get info user needs
def listing():
    data = second_request()
    datalist = []
    for item in data:
        datalist.append(data[item])
    return datalist


# this function is searching data from datalist
def get_info(period: str, entity: str):
    datalist = listing()
    final_data = [d['pl'] for d in datalist if d['month'] == period and d['company'] == entity]
    # for d in datalist:
    #     if d['month'] == period and d['company'] == entity:
    #         final_data.append(d['pl'])

    # data = next(d['pl'] for d in datalist if (d['month'] == period and d['company'] == entity))
    # final_data.append(data)
    return final_data


def formatting(period: str, entity: str):
    data = get_info(period, entity)
    locale.setlocale(locale.LC_ALL, 'ru_RU')
    for item in data:
        if '%' in item['plLine']:
            item['amount'] = locale.format_string('%.2f%%', float(item['amount']) * 100)
        else:
            item['amount'] = locale.currency(int(item['amount']), grouping=True)
    return data



def parsed_data(period: str, entity: str):
    data = formatting(period, entity)
    result = ''.join(f"Выбранный период: <b>{period}</b>\nВыбранная компания: <b>{entity}</b>\n\n") + \
                   ''.join([f"{obj['plLine']}: {obj['amount']}\n" for obj in data])
    return result


print(parsed_data('Jan 21', 'Итого'))
