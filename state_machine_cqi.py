from state_machine_model import State, Event, Action, Transition, StateMachine

tv_on = Event('tvOn', 'TVON')
couch_active = Event('couchActive', 'COAC')
it_is_evening = Event('itIsEvening', 'ITEV')
new_day = Event('newDay', 'NEDY')

turn_off_tv = Action('turnOffTv', 'TTOF')
order_pizza = Action('orderPizza', 'OPZZ')

idle = State('idle')
active = State('active')
waiting_for_couch = State('waitingForCouch')
waiting_for_tv = State('waitingForTv')
pizza_is_coming = State('pizzaIsComing')

idle.add_transition(Transition(idle, active, it_is_evening))
idle.add_actions(turn_off_tv)

active.add_transition(Transition(active, waiting_for_couch, tv_on))
active.add_transition(Transition(active, waiting_for_tv, couch_active))

waiting_for_couch.add_transition(Transition(waiting_for_couch, pizza_is_coming, couch_active))

waiting_for_tv.add_transition(Transition(waiting_for_tv, pizza_is_coming, tv_on))

pizza_is_coming.add_transition(Transition(pizza_is_coming, idle, new_day))
pizza_is_coming.add_actions(order_pizza)

machine = StateMachine(idle, idle, {new_day})


machine.handle(tv_on)
machine.handle(it_is_evening)
machine.handle(tv_on)
machine.handle(tv_on)
machine.handle(couch_active)

