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
INITIAL_INVESTMENT = 1000000


class RussellCapping:
    def __init__(self, total_mc=None, raw_data=None, capping_percent=None):
        self.initial_total_mc = 7028635793
        self.raw_data = {'1': {'symbol': 'btc', 'name': 'bitcoin', 'market_cap': 6487950808, 'price': 431.45, 'circulating supply': 15037467, '24hr volume': '28221886', 'percent_mc': 0.9230739789450348, 'weighted_dollar_mc': 923073.9789450348, 'num_coins': 2139.4691828602035}, '2': {'symbol': 'xrp', 'name': 'ripple', 'market_cap': 202989110, 'price': 0.006053, 'circulating supply': 33537439933, '24hr volume': '273625', 'percent_mc': 0.028880299958373445, 'weighted_dollar_mc': 28880.299958373445, 'num_coins': 4771237.396063678}, '3': {'symbol': 'ltc', 'name': 'litecoin', 'market_cap': 153184845, 'price': 3.49, 'circulating supply': 43878995, '24hr volume': '1948999', 'percent_mc': 0.021794392185260296, 'weighted_dollar_mc': 21794.392185260294, 'num_coins': 6244.81151440123}, '4': {'symbol': 'eth', 'name': 'ethereum', 'market_cap': 72409494, 'price': 0.953277, 'circulating supply': 75958536, '24hr volume': '241462', 'percent_mc': 0.010302069438868135, 'weighted_dollar_mc': 10302.069438868135, 'num_coins': 10807.005140025549}, '5': {'symbol': 'dash', 'name': 'dash', 'market_cap': 19820453, 'price': 3.25, 'circulating supply': 6107434, '24hr volume': '55320', 'percent_mc': 0.002819957326532654, 'weighted_dollar_mc': 2819.957326532654, 'num_coins': 867.6791773946627}, '6': {'symbol': 'doge', 'name': 'dogecoin', 'market_cap': 15091783, 'price': 0.000147, 'circulating supply': 102497368315, '24hr volume': '105352', 'percent_mc': 0.0021471852354379064, 'weighted_dollar_mc': 2147.1852354379066, 'num_coins': 14606702.28189052}, '7': {'symbol': 'ppc', 'name': 'peercoin', 'market_cap': 9788940, 'price': 0.427738, 'circulating supply': 22885358, '24hr volume': '28242', 'percent_mc': 0.001392722611939725, 'weighted_dollar_mc': 1392.7226119397249, 'num_coins': 3256.01796412693}, '8': {'symbol': 'bts', 'name': 'bitshares', 'market_cap': 8687533, 'price': 0.003424, 'circulating supply': 2537052805, '24hr volume': '9096', 'percent_mc': 0.0012360197989846249, 'weighted_dollar_mc': 1236.019798984625, 'num_coins': 360987.09082494886}, '9': {'symbol': 'xlm', 'name': 'stellar', 'market_cap': 8386835, 'price': 0.001734, 'circulating supply': 4837356606, '24hr volume': '42572', 'percent_mc': 0.0011932379549887428, 'weighted_dollar_mc': 1193.2379549887428, 'num_coins': 688141.8425540616}, '10': {'symbol': 'nxt', 'name': 'nxt', 'market_cap': 7329199, 'price': 0.007329, 'circulating supply': 999997096, '24hr volume': '11515', 'percent_mc': 0.0010427626663056491, 'weighted_dollar_mc': 1042.7626663056492, 'num_coins': 142278.98298617126}, '11': {'symbol': 'maid', 'name': 'maidsafecoin', 'market_cap': 6560545, 'price': 0.014497, 'circulating supply': 452552412, '24hr volume': '2090', 'percent_mc': 0.0009334023263139935, 'weighted_dollar_mc': 933.4023263139935, 'num_coins': 64385.895448299205}, '12': {'symbol': 'fct', 'name': 'factom', 'market_cap': 5666723, 'price': 0.647339, 'circulating supply': 8753873, '24hr volume': '410320', 'percent_mc': 0.0008062336941179447, 'weighted_dollar_mc': 806.2336941179448, 'num_coins': 1245.4582438535988}, '13': {'symbol': 'nmc', 'name': 'namecoin', 'market_cap': 5581503, 'price': 0.420126, 'circulating supply': 13285307, '24hr volume': '44570', 'percent_mc': 0.0007941090084022796, 'weighted_dollar_mc': 794.1090084022796, 'num_coins': 1890.1686836860363}, '14': {'symbol': 'bcn', 'name': 'bytecoin', 'market_cap': 5532261, 'price': 3.1e-05, 'circulating supply': 178306134649, '24hr volume': '8936', 'percent_mc': 0.0007871030969494424, 'weighted_dollar_mc': 787.1030969494425, 'num_coins': 25390422.48224008}, '15': {'symbol': 'xmr', 'name': 'monero', 'market_cap': 5516579, 'price': 0.521568, 'circulating supply': 10576902, '24hr volume': '57544', 'percent_mc': 0.0007848719385195778, 'weighted_dollar_mc': 784.8719385195778, 'num_coins': 1504.831466883662}, '16': {'symbol': 'grc', 'name': 'gridcoin', 'market_cap': 3261647, 'price': 0.008778, 'circulating supply': 371581656, '24hr volume': '755', 'percent_mc': 0.0004640512179117829, 'weighted_dollar_mc': 464.0512179117829, 'num_coins': 52865.25608473262}, '17': {'symbol': 'nsr', 'name': 'nushares', 'market_cap': 3144968, 'price': 0.003773, 'circulating supply': 833502552, '24hr volume': 'Low Vol', 'percent_mc': 0.0004474506992000005, 'weighted_dollar_mc': 447.4506992000005, 'num_coins': 118592.81717466221}, '18': {'symbol': 'emc', 'name': 'emercoin', 'market_cap': 2886544, 'price': 0.078433, 'circulating supply': 36802553, '24hr volume': '4231', 'percent_mc': 0.0004106833936216732, 'weighted_dollar_mc': 410.6833936216732, 'num_coins': 5236.104619505479}, '19': {'symbol': 'rby', 'name': 'rubycoin', 'market_cap': 2830918, 'price': 0.125475, 'circulating supply': 22561620, '24hr volume': '3158', 'percent_mc': 0.0004027691978035602, 'weighted_dollar_mc': 402.7691978035602, 'num_coins': 3209.9557505762914}, '20': {'symbol': 'blk', 'name': 'blackcoin', 'market_cap': 2015105, 'price': 0.026803, 'circulating supply': 75182257, '24hr volume': '4367', 'percent_mc': 0.000286699305433765, 'weighted_dollar_mc': 286.699305433765, 'num_coins': 10696.537903733351}}
        self.temp_total_mc = 7028635793
        # self.temp_raw_data = raw_data
        self.total_weighted_mc = 0
        self.capping_percent = 10
        for crypto in self.raw_data:
            self.raw_data[crypto]['percent_mc'] = self.raw_data[crypto]['market_cap'] / self.temp_total_mc
            self.raw_data[crypto]['capped'] = False

    def russell_capping(self):
        to_cap = self.determine_constituents_to_cap()
        if to_cap is None:
            return self.raw_data.copy(), self.temp_total_mc
        uncapped_percent, uncapped_mc_sum = self.uncapped_info()
        # print('here', to_cap)
        for crypto in to_cap:
            capping_factor = self.calculate_capping_factor(crypto, uncapped_percent, uncapped_mc_sum)
            self.temp_total_mc -= self.raw_data[crypto]['market_cap']
            self.raw_data[crypto]['market_cap'] *= capping_factor
            self.temp_total_mc += self.raw_data[crypto]['market_cap']
            self.raw_data[crypto]['percent_mc'] = self.raw_data[crypto]['market_cap'] / self.temp_total_mc
            self.raw_data[crypto]['weighted_dollar_mc'] = self.raw_data[crypto]['percent_mc'] * INITIAL_INVESTMENT
            self.raw_data[crypto]['num_coins'] = self.raw_data[crypto]['weighted_dollar_mc'] / self.raw_data[crypto]['price']
            self.raw_data[crypto]['capped'] = True
        while True:
            uncapped_percent, uncapped_mc_sum, to_cap = self.recalculate_caps()
            if not to_cap:
                break
                # return self.raw_data.copy(), self.temp_total_mc
            # print('here2', to_cap)
            for crypto in to_cap:
                capping_factor = self.calculate_capping_factor(crypto, uncapped_percent, uncapped_mc_sum)
                self.temp_total_mc -= self.raw_data[crypto]['market_cap']
                self.raw_data[crypto]['market_cap'] *= capping_factor
                self.temp_total_mc += self.raw_data[crypto]['market_cap']
                self.raw_data[crypto]['percent_mc'] = self.raw_data[crypto]['market_cap'] / self.temp_total_mc
                self.raw_data[crypto]['weighted_dollar_mc'] = self.raw_data[crypto]['percent_mc'] * INITIAL_INVESTMENT
                self.raw_data[crypto]['num_coins'] = self.raw_data[crypto]['weighted_dollar_mc'] / self.raw_data[crypto]['price']
                self.raw_data[crypto]['capped'] = True
        for crypto in self.raw_data:
            self.raw_data[crypto]['weighted_dollar_mc'] = self.raw_data[crypto]['percent_mc'] * INITIAL_INVESTMENT
            self.raw_data[crypto]['num_coins'] = self.raw_data[crypto]['weighted_dollar_mc'] / self.raw_data[crypto]['price']
            self.total_weighted_mc += self.raw_data[crypto]['weighted_dollar_mc']
        return self.raw_data, self.temp_total_mc, self.total_weighted_mc

    def recalculate_caps(self):
        uncapped_percent = 0
        uncapped_crypto_mc_sum = 0
        to_cap = set()
        for crypto in self.raw_data:
            self.raw_data[crypto]['percent_mc'] = self.raw_data[crypto]['market_cap'] / self.temp_total_mc
            if self.raw_data[crypto]['percent_mc'] > 0.1:
                uncapped_percent += self.raw_data[crypto]['percent_mc']
                uncapped_crypto_mc_sum += self.raw_data[crypto]['market_cap']
                to_cap.add(crypto)
        if len(to_cap) == 0:
            return False, False, False
        return (uncapped_percent * 100), uncapped_crypto_mc_sum, to_cap

    def check_uncapped(self):
        pass

    def calculate_capping_factor(self, index, uncapped_percent, uncapped_mc_sum):
        capping_factor = ((self.capping_percent /
                          (self.raw_data[index]['market_cap'] * uncapped_percent))
                          * uncapped_mc_sum)
        # print(index, capping_factor)
        return capping_factor

    def determine_constituents_to_cap(self):
        to_cap = set()
        for crypto in self.raw_data:
            if self.raw_data[crypto]['percent_mc'] > 0.10:
                to_cap.add(crypto)
        if len(to_cap) == 0:
            return None
        return to_cap.copy()

    def uncapped_info(self):
        # Returns the percent and market cap sum of all the uncapped cryptos
        uncapped_percent = 0
        uncapped_crypto_mc_sum = 0
        for x in self.raw_data:
            if not self.raw_data[x]['capped']:
                uncapped_percent += self.raw_data[x]['percent_mc']
                uncapped_crypto_mc_sum += self.raw_data[x]['market_cap']
        return (uncapped_percent * 100), uncapped_crypto_mc_sum

    def reset_capped_attribute(self):
        for crypto in self.raw_data:
            self.raw_data[crypto]['capped'] = False
