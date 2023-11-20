import time


class TestUtil:
    @staticmethod
    def generate_unique_id_for_business(business_id):
        return f'{business_id}-{str(int(time.time() * 1000))}'
