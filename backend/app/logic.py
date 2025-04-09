class NFTCalculator:
    def __init__(self,
                 target_raise=500000,
                 total_nfts=6969,
                 treasury_percent=0.2,
                 avg_bribe=1.8,
                 bera_price=5.7,
                 staked_percent=1.0,
                 user_nft_stake=1
                 ):
        
        self.target_raise = target_raise
        self.total_nfts = total_nfts
        self.treasury_percent = treasury_percent
        self.avg_bribe = avg_bribe
        self.bera_price = bera_price
        self.staked_percent = staked_percent
        self.user_nft_stake = user_nft_stake

    def net_available_for_sale(self):
        return round(self.total_nfts - (self.total_nfts * self.treasury_percent), 0)
    
    def price_per_nft(self):
        return round(self.target_raise / self.net_available_for_sale(), 2)
    
    def total_bribes(self):
        return 0.8 * self.target_raise
    
    def total_bgt_capture(self):
        return self.total_bribes() / self.avg_bribe

    def effective_amount_staked(self):
        return round(self.price_per_nft() * self.user_nft_stake, 2)

    def pol_earnings_per_nft(self):
        # total_earnings = 0.8 * self.target_raise  # 80% for bribes
        # return round(total_earnings / (self.total_nfts * self.staked_percent), 2)
        net_bgt_capture = self.total_bgt_capture() * self.bera_price
        return round(net_bgt_capture / (self.total_nfts * self.staked_percent), 2)

    def apr_per_nft(self, period_months=1):
        # monthly_earnings = self.pol_earnings_per_nft() / 12
        # return round((monthly_earnings * period_months) / self.price_per_nft() * 100, 2)
        return round((self.pol_earnings_per_nft() / self.price_per_nft()) * 12 * 100)

    def calculate_all(self):
        return {
            'price_per_nft': self.price_per_nft(),
            'effective_amount_staked': self.effective_amount_staked(),
            'pol_earnings_per_nft': self.pol_earnings_per_nft(),
            'apr': self.apr_per_nft(),
            'net_available_for_sale': self.net_available_for_sale(),
        }
