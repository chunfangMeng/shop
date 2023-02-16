from abc import abstractmethod


class SerialNumberBase(object):
    @abstractmethod
    def create_serial_number(self):
        pass


class ManageUserIndex(SerialNumberBase):
    def create_serial_number(self):
        pass


class MemberUserIndex(SerialNumberBase):
    def create_serial_number(self):
        pass
