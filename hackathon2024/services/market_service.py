from ..models import Market

class MarketService:
    def get_all_markets(self):
        return Market.objects.all()

    def create_market(self, data):
        market = Market.objects.create(**data)
        return market