from behave import given, when, then
from belly import Belly

@given('I have eaten {cukes:d} cukes')
def step_given_eaten_cukes(context, cukes):
    context.belly = Belly()
    context.belly.eat(cukes)

@when('I wait {hours:d} hour')
def step_when_wait_hours(context, hours):
    context.belly.wait(hours)

@then('my Belly should growl')
def step_then_should_growl(context):
    assert context.belly.growls() == True

@then('my Belly should not growl')
def step_then_should_not_growl(context):
    assert context.belly.growls() == False
