from unittest import TestCase, mock

import app


class TestProduct(TestCase):
    @mock.patch("product.Product.get_a_product")
    def test_product_by_id_true(self, mockProduct):
        # expected result
        mockProduct.return_value = self.expected_output_for_select_product_by_id_true
        # consumer is app.query_product_id
        res = app.query_product_id(self.test_input_for_select_product_by_id_true)
        # make sure the called with is {"id": 1}
        mockProduct.assert_called_with(self.test_input_for_select_product_by_id_true)
        # self.assertEqual(res, self.expected_output_for_select_product_by_id_true)

    @mock.patch("product.Product.get_a_product")
    def test_product_by_empty_id(self, mockProduct):
        mockProduct.return_value = self.expected_output_for_select_product_by_id_empty
        res = app.query_product_id(self.test_input_for_select_product_by_id_empty)
        self.assertEqual(res, self.expected_output_for_select_product_by_id_empty)

    # True condition for select product by id
    test_input_for_select_product_by_id_true = {"id": 1}

    expected_output_for_select_product_by_id_true = {
        "id": 1,
        "product_name": "some product",
    }

    # False condition for select product by id (ID Empty)
    test_input_for_select_product_by_id_empty = {"id": ""}

    expected_output_for_select_product_by_id_empty = {"error": "ID should not empty"}

    # False condition for select product by id (ID not match)
    test_input_for_select_product_by_id_id_not_match = {
        # asume no product with id 123
        "id": 123
    }

    expected_output_for_select_product_by_id_id_not_match = {
        "error": "No product with that ID"
    }

    # False condition for select product by id (ID not int, but string)
    test_input_for_select_product_by_id_string_datatype = {"id": "%q"}

    expected_input_for_select_product_by_id_string_datatype = {"error": TypeError}

    # False condition for select product by id (ID not int, but list)
    test_input_for_select_product_by_id_list_datatype = {"id": [1, 2, 3]}

    expected_input_for_select_product_by_id_list_datatype = {
        "error": "ID should not list type"
    }

