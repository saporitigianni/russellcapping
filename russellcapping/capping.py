# Takes in the total market cap as a float and a dictionary of dictionaries
# with at least the attributes mentioned below, if more attributes are passed
# in, they are ignored and returned as is, if there were calculations based on
# any of the attributes mentioned below prior to passing them in, they will
# need to be updated.
#
# There should be an entry with the following structure for each market in the
# index (regardless of the need for capping):
#
# sample = {index/symbol1: {'market_cap':         float,
#                           'price':              float,
#                           'circulating_supply': int   }, (repeat x times)}


def russell_capping(raw_data=None, percent_capping=None, total_mc=None):
    if not total_mc:
        temp_total_mc = 0
        for x in raw_data:
            temp_total_mc += raw_data[x]['market_cap']
    else:
        temp_total_mc = total_mc

    while True:
        uncapped_percent, uncapped_mc_sum, to_cap = _parse_constituents(temp_total_mc, raw_data, percent_capping)
        if not to_cap:
            break
        for market in to_cap:
            capping_factor = _calculate_capping_factor(market, uncapped_percent, uncapped_mc_sum, raw_data, percent_capping)
            temp_total_mc -= raw_data[market]['market_cap']
            raw_data[market]['market_cap'] *= capping_factor
            temp_total_mc += raw_data[market]['market_cap']
            raw_data[market]['percent_mc'] = raw_data[market]['market_cap'] / temp_total_mc
    return raw_data.copy(), temp_total_mc


def _parse_constituents(temp_total_mc=None, raw_data=None, capping_percent=None):
    uncapped_percent = 0
    uncapped_mc_sum = 0
    to_cap = set()

    for market in raw_data:
        raw_data[market]['percent_mc'] = raw_data[market]['market_cap'] / temp_total_mc
        if raw_data[market]['percent_mc'] > (capping_percent - capping_percent * 0.0001):
            if raw_data[market]['percent_mc'] < (capping_percent + capping_percent * 0.0001):
                continue
            uncapped_percent += raw_data[market]['percent_mc']
            uncapped_mc_sum += raw_data[market]['market_cap']
            to_cap.add(market)
    if len(to_cap) == 0:
        return False, False, False
    return uncapped_percent, uncapped_mc_sum, to_cap.copy()


def _calculate_capping_factor(index, uncapped_percent, uncapped_mc_sum, raw_data, capping_percent):
    capping_factor = ((capping_percent /
                      (raw_data[index]['market_cap'] * uncapped_percent))
                      * uncapped_mc_sum)
    return capping_factor
