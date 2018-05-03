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
# Not currently using price and circulating_supply but intend to in the near future
# INITIAL_INVESTMENT = 1000000


class RussellCapping:
    def __init__(self, total_mc=None, raw_data=None):
        # print('in FTSE capping', total_mc)
        # self.initial_total_mc = 187958629158
        self.initial_total_mc = total_mc
        self.raw_data = raw_data
        self.raw_data = {'1': {'symbol': 'btc', 'name': 'bitcoin', 'market_cap': 165311443750, 'price': 9790.46, 'circulating_supply': 16884950, '24hr_vol': 6447241938}, '2': {'symbol': 'eth', 'name': 'ethereum', 'market_cap': 82562827937, 'price': 843.95, 'circulating_supply': 97828811, '24hr_vol': 1807699383}, '3': {'symbol': 'xrp', 'name': 'ripple', 'market_cap': 37186884566, 'price': 0.951198, 'circulating_supply': 39094802192, '24hr_vol': 419541575}, '4': {'symbol': 'bch', 'name': 'bitcoin cash', 'market_cap': 20255044958, 'price': 1192.45, 'circulating_supply': 16986065, '24hr_vol': 397063052}, '5': {'symbol': 'ltc', 'name': 'litecoin', 'market_cap': 11575311524, 'price': 209.05, 'circulating_supply': 55369778, '24hr_vol': 831323866}, '6': {'symbol': 'ada', 'name': 'cardano', 'market_cap': 8432405947, 'price': 0.325236, 'circulating_supply': 25927070538, '24hr_vol': 125311576}, '7': {'symbol': 'neo', 'name': 'neo', 'market_cap': 7698966075, 'price': 118.45, 'circulating_supply': 65000000, '24hr_vol': 137887570}, '8': {'symbol': 'xlm', 'name': 'stellar', 'market_cap': 6525821965, 'price': 0.353362, 'circulating_supply': 18467829505, '24hr_vol': 33247258}, '9': {'symbol': 'eos', 'name': 'eos', 'market_cap': 5597242651, 'price': 8.1, 'circulating_supply': 691350755, '24hr_vol': 198538145}, '10': {'symbol': 'miota', 'name': 'iota', 'market_cap': 5268852906, 'price': 1.9, 'circulating_supply': 2779530283, '24hr_vol': 74925969}, '11': {'symbol': 'dash', 'name': 'dash', 'market_cap': 4702577778, 'price': 594.9, 'circulating_supply': 7904773, '24hr_vol': 84339925}, '12': {'symbol': 'xmr', 'name': 'monero', 'market_cap': 4331111339, 'price': 274.81, 'circulating_supply': 15760228, '24hr_vol': 51042373}, '13': {'symbol': 'etc', 'name': 'ethereum classic', 'market_cap': 3782402142, 'price': 37.78, 'circulating_supply': 100103368, '24hr_vol': 1063399080}, '14': {'symbol': 'xem', 'name': 'nem', 'market_cap': 3605289068, 'price': 0.400588, 'circulating_supply': 8999999999, '24hr_vol': 19324677}, '15': {'symbol': 'trx', 'name': 'tron', 'market_cap': 2679225981, 'price': 0.04075, 'circulating_supply': 65748192475, '24hr_vol': 180695719}, '16': {'symbol': 'ven', 'name': 'vechain', 'market_cap': 2677740130, 'price': 5.62, 'circulating_supply': 476633230, '24hr_vol': 69344641}, '17': {'symbol': 'usdt', 'name': 'tether', 'market_cap': 2221692529, 'price': 1.0, 'circulating_supply': 2217140814, '24hr_vol': 2225721236}, '18': {'symbol': 'lsk', 'name': 'lisk', 'market_cap': 2104392389, 'price': 20.59, 'circulating_supply': 102209129, '24hr_vol': 42634304}, '19': {'symbol': 'btg', 'name': 'bitcoin gold', 'market_cap': 1992686822, 'price': 118.29, 'circulating_supply': 16845290, '24hr_vol': 22649257}, '20': {'symbol': 'qtum', 'name': 'qtum', 'market_cap': 1932120869, 'price': 26.14, 'circulating_supply': 73906593, '24hr_vol': 100710011}}
        self.temp_total_mc = total_mc
        self.temp_total_mc = 380444041326
        # self.temp_raw_data = raw_data
        # self.total_weighted_mc = 0
        self.capping_percent = 0.1
        # for market in self.raw_data:
        #     self.raw_data[market]['percent_mc'] = self.raw_data[market]['market_cap'] / self.temp_total_mc
        #     self.raw_data[market]['capped'] = False

    def russell_capping(self):
        # to_cap = self.determine_constituents_to_cap()
        # if to_cap is None:
        #     return self.raw_data.copy(), self.temp_total_mc
        # uncapped_percent, uncapped_mc_sum = self.uncapped_info()
        # # print('here', to_cap)
        # for crypto in to_cap:
        #     capping_factor = self.calculate_capping_factor(crypto, uncapped_percent, uncapped_mc_sum)
        #     self.temp_total_mc -= self.raw_data[crypto]['market_cap']
        #     self.raw_data[crypto]['market_cap'] *= capping_factor
        #     self.temp_total_mc += self.raw_data[crypto]['market_cap']
        #     self.raw_data[crypto]['percent_mc'] = self.raw_data[crypto]['market_cap'] / self.temp_total_mc
        #     self.raw_data[crypto]['weighted_dollar_mc'] = self.raw_data[crypto]['percent_mc'] * INITIAL_INVESTMENT
        #     self.raw_data[crypto]['num_coins'] = self.raw_data[crypto]['weighted_dollar_mc'] / self.raw_data[crypto]['price']
        #     self.raw_data[crypto]['capped'] = True
        # print(self.raw_data)
        while True:
            uncapped_percent, uncapped_mc_sum, to_cap = self.parse_constituents()
            if not to_cap:
                break
            # print(uncapped_percent, uncapped_mc_sum, to_cap)
                # return self.raw_data.copy(), self.temp_total_mc
            # print('here2', to_cap)
            for market in to_cap:
                capping_factor = self.calculate_capping_factor(market, uncapped_percent, uncapped_mc_sum)
                self.temp_total_mc -= self.raw_data[market]['market_cap']
                self.raw_data[market]['market_cap'] *= capping_factor
                self.temp_total_mc += self.raw_data[market]['market_cap']
                self.raw_data[market]['percent_mc'] = self.raw_data[market]['market_cap'] / self.temp_total_mc
                # self.raw_data[market]['weighted_dollar_mc'] = self.raw_data[market]['percent_mc'] * INITIAL_INVESTMENT
                # self.raw_data[market]['num_coins'] = self.raw_data[market]['weighted_dollar_mc'] / self.raw_data[market]['price']
                # self.raw_data[market]['capped'] = True
            # print(self.raw_data)
        # for market in self.raw_data:
        #     self.raw_data[market]['weighted_dollar_mc'] = self.raw_data[market]['percent_mc'] * INITIAL_INVESTMENT
        #     self.raw_data[market]['num_coins'] = self.raw_data[market]['weighted_dollar_mc'] / self.raw_data[market]['price']
            # self.total_weighted_mc += self.raw_data[market]['weighted_dollar_mc']
        return self.raw_data.copy(), self.temp_total_mc#, self.total_weighted_mc

    def parse_constituents(self):
        uncapped_percent = 0
        uncapped_mc_sum = 0
        to_cap = set()
        for market in self.raw_data:
            self.raw_data[market]['percent_mc'] = self.raw_data[market]['market_cap'] / self.temp_total_mc
            # if self.raw_data[market]['percent_mc'] > self.capping_percent:
            if self.raw_data[market]['percent_mc'] > (self.capping_percent - self.capping_percent * 0.0001):
                if self.raw_data[market]['percent_mc'] < (self.capping_percent + self.capping_percent * 0.0001):
                    continue
                uncapped_percent += self.raw_data[market]['percent_mc']
                uncapped_mc_sum += self.raw_data[market]['market_cap']
                to_cap.add(market)
        if len(to_cap) == 0:
            return False, False, False
        # print(uncapped_percent, uncapped_mc_sum, to_cap.copy())
        return uncapped_percent, uncapped_mc_sum, to_cap.copy()

    # def check_uncapped(self):
    #     pass

    def calculate_capping_factor(self, index, uncapped_percent, uncapped_mc_sum):
        capping_factor = ((self.capping_percent /
                          (self.raw_data[index]['market_cap'] * uncapped_percent))
                          * uncapped_mc_sum)
        # print(index, capping_factor)
        return capping_factor

    # def determine_constituents_to_cap(self):
    #     to_cap = set()
    #     for market in self.raw_data:
    #         if self.raw_data[market]['percent_mc'] > 0.10:
    #             to_cap.add(market)
    #     if len(to_cap) == 0:
    #         return None
    #     return to_cap.copy()
    #
    # def uncapped_info(self):
    #     # Returns the percent and market cap sum of all the uncapped markets
    #     uncapped_percent = 0
    #     uncapped_mc_sum = 0
    #     for x in self.raw_data:
    #         if not self.raw_data[x]['capped']:
    #             uncapped_percent += self.raw_data[x]['percent_mc']
    #             uncapped_mc_sum += self.raw_data[x]['market_cap']
    #     return (uncapped_percent * 100), uncapped_mc_sum

    # def reset_capped_attribute(self):
    #     for market in self.raw_data:
    #         self.raw_data[market]['capped'] = False
