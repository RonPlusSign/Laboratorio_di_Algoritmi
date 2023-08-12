from abc import abstractmethod


class Queue:
    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def insert(self, value: int) -> None:
        pass

    @abstractmethod
    def find_max(self):
        pass

    @abstractmethod
    def extract_max(self):
        pass
