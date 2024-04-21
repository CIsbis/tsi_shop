import configInterface

from typing import List

class StubConfig():
    def get_configuration(self) -> List[str]:
        stubbed_data = {
            "email_address": "test@mail.com",
            "first_name": "John",
            "last_name": "Doe",
            "password": "1234"
        }
        return stubbed_data