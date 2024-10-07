from locust import HttpUser, task, between, tag
import random
import json

class CalculatorUser(HttpUser):

    wait_time = between(2,4)

    def on_start(self):
        pass

    @task(20)
    @tag('add')
    def add(self):
        data = [[5,10,15], [20,40,60]]
        data_to_use = random.choice(data)
        addition_req = {
            "operation": "add",
            "operand1": data_to_use[0],
            "operand2": data_to_use[1]
        }
        with self.client.post("/calculate", catch_response=True, name='add', json=addition_req) as response:
            try:
                response_data = json.loads(response.text)
                expected_result = data_to_use[0] + data_to_use[1]
                
                if response_data['result'] != expected_result:
                    response.failure(f"Expected {expected_result}, but got {response_data['result']}")
                else:
                    response.success()
            except json.JSONDecodeError:
                response.failure("Response was not valid JSON")
            except KeyError:
                response.failure("Response did not contain 'result'")

    @task
    @tag('sub')
    def subtract(self):
        data = [[5,10,15], [20,40,60]]
        data_to_use = random.choice(data)
        subtract_req = {
            "operation": "subtract",
            "operand1": data_to_use[0],
            "operand2": data_to_use[1]
        }
        with self.client.post("/calculate", catch_response=True, name='subtract', json=subtract_req) as response:
            try:
                response_data = json.loads(response.text)
                expected_result = data_to_use[0] - data_to_use[1]
                
                if response_data['result'] != expected_result:
                    response.failure(f"Expected {expected_result}, but got {response_data['result']}")
                else:
                    response.success()
            except json.JSONDecodeError:
                response.failure("Response was not valid JSON")
            except KeyError:
                response.failure("Response did not contain 'result'")

    @task
    @tag('div')
    def divide(self):
        data = [[5,10,15], [20,40,60]]
        data_to_use = random.choice(data)
        divide_req = {
            "operation": "divide",
            "operand1": data_to_use[0],
            "operand2": data_to_use[1]
        }
        with self.client.post("/calculate", catch_response=True, name='divide', json=divide_req) as response:
            try:
                response_data = json.loads(response.text)

                if data_to_use[1] == 0:
                    response.failure("Division by zero is not allowed.")
                    return
                expected_result = data_to_use[0] / data_to_use[1]
                                
                if response_data['result'] != expected_result:
                    response.failure(f"Expected {expected_result}, but got {response_data['result']}")
                else:
                    response.success()
            except json.JSONDecodeError:
                response.failure("Response was not valid JSON")
            except KeyError:
                response.failure("Response did not contain 'result'")

    @task
    @tag('mul')
    def multiply(self):
        data = [[5,10,15], [20,40,60]]
        data_to_use = random.choice(data)
        multiply_req = {
            "operation": "multiply",
            "operand1": data_to_use[0],
            "operand2": data_to_use[1]
        }
        with self.client.post("/calculate", catch_response=True, name='multiply', json=multiply_req) as response:
            try:
                response_data = json.loads(response.text)
                expected_result = data_to_use[0] * data_to_use[1]
                
                if response_data['result'] != expected_result:
                    response.failure(f"Expected {expected_result}, but got {response_data['result']}")
                else:
                    response.success()
            except json.JSONDecodeError:
                response.failure("Response was not valid JSON")
            except KeyError:
                response.failure("Response did not contain 'result'")


if __name__ == "__main__":
    from locust import run_single_user
    CalculatorUser.host = "http://127.0.0.1:5000"
    run_single_user(CalculatorUser)
