from base_python_package_template.main import greetings


class TestMain:
    def test_greetings_return_value(self):
        assert greetings() == "Hello, World!"

    def test_greetings_return_type(self):
        assert isinstance(greetings(), str)
