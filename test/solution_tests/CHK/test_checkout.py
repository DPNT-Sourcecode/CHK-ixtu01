from solutions.CHK import checkout_solution


class TestCheckout():

    def test_checkout_nested_lists(self):
        assert checkout_solution.checkout("AAAABBBCCDD") == 325

    def test_checkout_bad_input(self):
        assert checkout_solution.checkout("AAAABBBCCDD23") == -1

    def test_checkout_empt_input(self):
        assert checkout_solution.checkout("") == -1
