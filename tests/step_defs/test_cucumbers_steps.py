from pytest_bdd import scenarios, parsers, given, when, then

from ...cucumbers import CucumberBasket

EXTRA_TYPES: dict = {
    'Number': int
}


scenarios('../features/cucumbers.feature')


@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers', extra_types=EXTRA_TYPES), target_fixture='basket')
def busket(initial: int):
    return CucumberBasket(initial_count=initial)


@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket', extra_types=EXTRA_TYPES))
def add_cucmbers(basket: CucumberBasket, some: int):
    basket.add(some)


@when(parsers.cfparse('"{some:Number}" cucumbers are removed from the basket', extra_types=EXTRA_TYPES))
def remove_cucumbers(basket: CucumberBasket, some: int):
    basket.remove(some)


@then(parsers.cfparse('the basket contains "{total:Number}" cucumbers', extra_types=EXTRA_TYPES))
def basket_has_total(basket: CucumberBasket, total: int):
    assert basket.count == total
