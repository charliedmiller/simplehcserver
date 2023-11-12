from typing import Dict


class HashicorpDemoDb:
    def add_entry(self,entry: Dict):
        print(f"Adding entry: {entry}")
        self._add_entry(entry)

    def _add_entry(self,entry: Dict):
        raise NotImplementedError

    def get_entries(self):
        raise NotImplementedError

class MemoryHashicorpDemoDb(HashicorpDemoDb):
    def __init__(self):
        self.store = []

    def _add_entry(self, entry: Dict):
        self.store.append(entry)

    def get_entries(self):
        return self.store


class MariaDBHashicorpDemoDb(HashicorpDemoDb):
    def __init__(self):
        # Place MariaDB initialization here
        raise NotImplementedError

    def _add_entry(self, entry: Dict):
        # Do a sql insert query here
        raise NotImplementedError

    def get_entries(self):
        # Do a sql query here
        raise NotImplementedError