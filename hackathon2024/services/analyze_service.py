from ..models import Analyze

class AnalyzeService:
    def get_all_analyzes(self):
        return Analyze.objects.all()

    def create_analyze(self, data):
        analyze = Analyze.objects.create(**data)
        return analyze