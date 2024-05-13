class Awards:
    def __init__(self, addendum, catalog, viewing, rewind, montage, removal):
        self.addendum = addendum
        self.catalog = catalog
        self.viewing = viewing
        self.rewind = rewind
        self.montage = montage
        self.removal = removal

    def __str__(self):
        return f"{self.addendum} ({self.catalog}"


class AwardsModel:
    def __init__(self):
        self.awardss = {}

    def add_awards(self, dict_awards):
        awards = Awards(*dict_awards.values())
        self.awardss[awards.addendum] = awards

    def get_all_awards(self):
        return self.awardss.values()
