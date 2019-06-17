from solutions.CHK import checkout_solution


class TestCheckout():

    def test_checkout_nested_lists(self):
        assert checkout_solution.checkout("AAAABBBCCDD") == 325

    def test_checkout_bad_input(self):
        assert checkout_solution.checkout("AAAABBBCCDD23") == -1

    def test_checkout_A(self):
        input_1 = "A"
        input_2 = "AA"
        input_3 = "AAA"
        input_4 = "AAAA"
        assert checkout_solution.checkout(input_1) == 50
        assert checkout_solution.checkout(input_2) == 100
        assert checkout_solution.checkout(input_3) == 130
        assert checkout_solution.checkout(input_4) == 180

    def test_checkout_empty(self):
        assert checkout_solution.checkout("") == 0

    def test_checkout_no_deal(self):
        assert checkout_solution.checkout("CCCDDD") == 105
