from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

from django.utils.translation import ugettext

class Constants(BaseConstants):
    name_in_url = 'dice_roll'
    players_per_group = None
    num_rounds = 1
    endowment = 0
    unit_price = 4

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    reported_dice = models.IntegerField(min = 1, max = 6, label = ugettext("What number would you like to report?"))

    check1 = models.IntegerField(label = ugettext("Q1: If you report 5, how much are you paid?"))

    def check1_error_message(self, value):
        print(ugettext('You entered'), value)
        if value != 5 * Constants.unit_price:
            return ugettext("Incorrect estimate. Please read the instruction carefully and revise your estimate.")


    check2 = models.IntegerField(label = ugettext("Q2: If the outcome of the die roll is 3 and you report 2, how much are you paid?"))

    def check2_error_message(self, value):
        print(ugettext('You entered'), value)
        if value != 2 * Constants.unit_price:
            return ugettext("Incorrect estimate. Please read the instruction carefully and revise your estimate.")


    check3 = models.IntegerField(label = ugettext("Q3: If the outcome of the die roll is 2 and you report 5, how much are you paid?"))

    def check3_error_message(self, value):
        print(ugettext('You entered'), value)
        if value != 5 * Constants.unit_price:
            return ugettext("Incorrect estimate. Please read the instruction carefully and revise your estimate.")

    dice = models.IntegerField(initial = 0)