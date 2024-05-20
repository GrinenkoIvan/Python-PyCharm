from view_awards import AwardsUserInterface
from model_awards import AwardsModel


class ControllerAwards:
    def __init__(self):
        self.awards_model = AwardsModel()  # связь с model
        self.awards_user_interface = AwardsUserInterface()  # связь с view

    def run(self):
        awards = None
        while awards != 'q':
            awards = self.awards_user_interface.wait_awards_user_interface()
            self.check_awards(awards)

    def check_awards(self, awards):
        if awards == '1':
            awards = self.awards_user_interface.add_user_awards()
            self.awards_model.add_awards(awards)

        elif awards == '2':
            awardss = self.awards_model.get_all_awards()
            self.awards_user_interface.show_all_awards(awardss)