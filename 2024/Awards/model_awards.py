class Awards:
    def __init__(self, addendum, catalog, viewing, rewind, montage, removal):
        self.addendum = addendum
        self.catalog = catalog
        self.viewing = viewing
        self.rewind = rewind
        self.montage = montage
        self.removal = removal

    def __str__(self):
        return f"{self.addendum} ({self.catalog}{self.viewing})"


class AwardsModel:
    def __init__(self):
        self.awardss = {}

    def add_awards(self, dict_awards):
        awards = Awards(*dict_awards.values())
        self.awardss[awards.addendum] = awards

    def get_all_awards(self):
        return self.awardss.values()

    def get_single_awards(self, name_film):
        catalog = self.awardss[name_film]
        dict_catalog = {'название фильма': catalog.name_film,
                        'жанр': catalog.genre,
                        'режиссер': catalog.director,
                        'год выпуска': catalog.year_release,
                        'длительность': catalog.duration_film,
                        'студия': catalog.studio,
                        'актеры': catalog.actors,
                        }
        return dict_catalog


    def remove_single_movie(self, name_film):
        return self.awardss.pop(name_film)
