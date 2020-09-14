import param


class FruitStallController(param.Parameterized):
    """
    This controller lets the user choose a type of fruit, set the amount and then buy some.
    The docstring has two lines. Which is ignored. Lets try some whitespace.

    This is the next line after the whitespace.
    """
    title = 'Fruit Stall'
    random_attribute = 10  # not shown in GUI
    hidden_param = param.Boolean(precedence=-1,
                                 doc='This parameter is documented but due to low precedence not shown in documentation.')
    fruit = param.Selector(default='apple', objects=['apple', 'pear', 'banana'],
                           doc='Select type of fruit to buy.')
    quantity = param.Integer(5, bounds=(0, None), doc='Number of selected fruit to buy.')
    price = param.Number(0., constant=True, bounds=(0, None), doc='Price of the fruit per piece.')
    button = param.Action(lambda x: print('You bought fruit'),
                                 doc='Press this button to buy some fruit!', label='Make Purchase')

    def __init__(self, **params):
        super(FruitStallController, self).__init__(**params)

    @param.depends('fruit', watch=True)
    def _update_price(self):
        price_list = {'apple': 1.30, 'pear': 1.55, 'banana': 2.00}
        self.price = price_list[self.fruit]


class SuperMarketController(FruitStallController):
    """
    This controller extends the Fruit Stall into a Supermarket, also offering users a selection of milk and cheeses.
    """
    title = 'Supermarket'

    milk = param.Selector(default='semi-skimmed', objects=['full-fat', 'semi-skimmed', 'skimmed'],
                          doc='Select fat content for the milk.')
    cheese = param.Selector(default='Jong Belegen', objects=['Jong Belegen', 'Brie', 'Reblouchon'],
                            doc='Jong Belegen is highly recommended.')

    def __init__(self, **params):
        super(FruitStallController, self).__init__(**params)


class NormalClass(object):
    """
    This is a normal numpydoc style docstring

    Parameters
    ----------
    arg1 : :obj:`float`
        Argument 1
    arg2 : :obj:`float`
        Argument 2

    Attributes
    ----------

    arg : :obj:`float`
        Argument

    """

    def __init__(self, arg1, arg2):
        self.arg = arg1 + arg2

    def do_something(self):
        """
        This function does a thing.

        Returns
        -------
        ans : :obj:`float`
            Returns the double of the `arg` attribute.
        """
        ans = self.arg*2
        return ans


if __name__ == "__main__":

    fruit_stall = FruitStallController()
    print(fruit_stall.__doc__)  #prints normal param docstring

    supermarket = SuperMarketController()
    print(supermarket.__doc__)
