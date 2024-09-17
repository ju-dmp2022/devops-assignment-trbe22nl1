import requests
from calculator_client.client import Client
from calculator_client.api.actions import calculate
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions
from calculator_client.models import ResultResponse

class TestCalculatorAPI:
    def test_api_calculate_add(self):
        url = "http://localhost:5000/calculate"

        payload = {
                    "operation": "add",
                    "operand1": 1,
                    "operand2": 1
                    }
        response = requests.post(url, json=payload)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        # Parse the JSON response
        response_json = response.json()

        # Extract the result from the response
        result = response_json.get("result")

        # Assert that the result is as expected
        expected_result = 2
        assert result == expected_result, f"Expected result {expected_result}, but got {result}"

    def test_api_client_add(self):
        client = Client("http://localhost:5000")
        response = calculate.sync(client = client, body = Calculation(Opertions.ADD, operand1=1, operand2=1))
        assert isinstance(response, ResultResponse)
        assert response.result == 2

    def test_api_client_sub(self):
        client = Client("http://localhost:5000")
        response = calculate.sync(client = client, body = Calculation(Opertions.SUBTRACT, operand1=1, operand2=1))
        assert isinstance(response, ResultResponse)
        assert response.result == 0

    def test_api_client_mul(self):
        client = Client("http://localhost:5000")
        response = calculate.sync(client = client, body = Calculation(Opertions.MULTIPLY, operand1=2, operand2=2))
        assert isinstance(response, ResultResponse)
        assert response.result == 4

    def test_api_client_div(self):
        client = Client("http://localhost:5000")
        response = calculate.sync(client = client, body = Calculation(Opertions.DIVIDE, operand1=2, operand2=2))
        assert isinstance(response, ResultResponse)
        assert response.result == 1 