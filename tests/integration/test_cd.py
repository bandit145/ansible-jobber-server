import joblet_server.dsl as dsl

@dsl.task(order=1, environment=['prod, test'])
def test_thing():
	pass