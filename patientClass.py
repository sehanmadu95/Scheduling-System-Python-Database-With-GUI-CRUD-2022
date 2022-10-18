class patient:
    def __init__(self, name, regNo, address, telephone):
        self.__name = name
        self.__regNo = regNo
        self.__address = address
        self.__telephone = telephone

    # ============ for name attributes =================

    def get_name(self):
        # print("Get method called!!!")
        return self.__name

    def set_name(self, name):
        #  print("set method called!!!")
        self.__name = name

    def del_name(self):
        # print("del method called!!!")
        del self.__name

    name = property(get_name, set_name, del_name)

    # ============= for regNo Attribute ===============

    def get_regNo(self):
        # print("Get method called!!!")
        return self.__regNo

    def set_regNo(self, regNo):
        #  print("set method called!!!")
        self.__regNo = regNo

    def del_regNo(self):
        # print("del method called!!!")
        del self.__regNo

    regNo = property(get_regNo, set_regNo, del_regNo)

    # ==================== for Address ====================

    def get_address(self):
        # print("Get method called!!!")
        return self.__address

    def set_address(self, address):
        #  print("set method called!!!")
        self.__address = address

    def del_address(self):
        # print("del method called!!!")
        del self.__address

    address = property(get_address, set_address, del_address)

    # =========== for telephone ==============

    def get_telephone(self):
        # print("Get method called!!!")
        return self.__telephone

    def set_telephone(self, telephone):
        #  print("set method called!!!")
        self.__telephone = telephone

    def del_telephone(self):
        # print("del method called!!!")
        del self.__telephone

    telephone = property(get_telephone, set_telephone, del_telephone)