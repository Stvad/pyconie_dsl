from state_machine.model import Event, Action
from state_machine.model_fluid import state, state_machine

tv_on = Event(code='TVON')
couch_active = Event(code='COAC')
it_is_evening = Event(code='ITEV')
new_day = Event(code='NEDY')

turn_off_tv = Action(code='TTOF')
order_pizza = Action(code='OPZZ')

pizza_is_coming = (state(
    actions=[order_pizza]
))

waiting_for_tv = (state()
                  .on(tv_on).transition_to(pizza_is_coming))

waiting_for_couch = (state()
                     .on(couch_active).transition_to(pizza_is_coming))

active = (state()
          .on(couch_active).transition_to(waiting_for_tv)
          .on(tv_on).transition_to(waiting_for_couch))

idle = (state(actions=[turn_off_tv])
        .on(it_is_evening).transition_to(active))

machine = state_machine(initial_state=idle, reset_events={new_day})

machine.handle(tv_on)
machine.handle(it_is_evening)
machine.handle(tv_on)
machine.handle(tv_on)
machine.handle(couch_active)
