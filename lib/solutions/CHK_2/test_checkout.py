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

    def test_checkout_ex2_new_deal_1(self):
        assert checkout_solution.checkout("BBBBBBBBBEEEEEEE") == 460

    def test_checkout_ex2_new_deal_2(self):
        assert checkout_solution.checkout("BBBBBBBBEEEEEEE") == 430

    def test_checkout_ex2_big_deal(self):
        assert checkout_solution.checkout("ABCDECBAABCABBAAAEEAA") == 665

    def test_checkout_ex2_simple_deal(self):
        assert checkout_solution.checkout("ABCDE") == 155

    def test_checkout_ex3_check_F(self):
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("FFFFFF") == 40

    def test_checkout_ex3_check_pairing(self):
        assert checkout_solution.checkout("ABCDEFABCDEF") == 300
        assert checkout_solution.checkout("CDFFAECBDEAB") == 300

    def test_checkout_ex3_check_next(self):
        assert checkout_solution.checkout("AAAAAEEBAAABBFFF") == 475

    def test_checkout_ex3_check_final(self):
        assert checkout_solution.checkout("FFABCDECBAABCABBAAAEEAAFF") == 695
