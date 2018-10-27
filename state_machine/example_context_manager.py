# from .dsl.context_manager import *

# with events():
with events:
    tv_on = 'TVON'
    it_is_evening = 'EHAC'
    couch_active = 'COAC'
    new_day = 'NEDY'

# reset_events(new_day)
#
# with commands():
#     turn_off_tv = 'TTOF'
#     order_pizza = 'OPZZ'
#
# with initial_state("idle"):
#     actions(turn_off_tv)
#     transitions[it_is_evening:'active']
#
# with state('active'):
#     transitions[
#     tv_on:'waitingForCouch',
#     couch_active:'waitingForTV']
#
# with state('waitingForTV'):
#     transitions[couch_active:'pizzaIsComing']
#
# with state('waitingForCouch'):
#     transitions[tv_on:'pizzaIsComing']
#
# with state('pizzaIsComing'):
#     actions(order_pizza)
