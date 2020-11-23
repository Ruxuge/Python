from abc import abstractmethod


class MyList:
    @abstractmethod
    def push(self, value):
        pass

    @abstractmethod
    def find(self, value):
        pass

    @abstractmethod
    def remove(self, value):
        pass

    @abstractmethod
    def insert(self, index, value):
        pass

    @abstractmethod
    def merge(self, second_list):
        pass
