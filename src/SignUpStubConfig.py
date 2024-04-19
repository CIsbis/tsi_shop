import configInterface

from typing import List

class StubConfig(configInterface):
    def get_configuration(self) -> List[str]:
        stubdata = [
            "email_address:test@mail.com",
            "first_name:John",
            "last_name:Doe",
            "password:1234 "
        ]
        return stubdata