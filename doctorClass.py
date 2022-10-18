class doctor:
    li = ["8.30-9.00", "9.00-9.30", "9.30-10.00", "10.00-10.30",
          "10.30-11.00", "11.00-11.30", "11.30-12.00",
          "12.00-12.30", "12.30-1.00", "2.00-2.30",
          "2.30-3.00", "3.00-3.30", "3.30-4.00", "4.00-4.30",
          "4.30-5.00", "5.00-5.30"]

    new_li = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def __init__(self, regNo,name,sex,age, address, telephone):
        self.__name = name
        self.__regNo = regNo
        self.__sex = sex
        self.__age = age
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
#============================= sex ===================
    def get_sex(self):
        # print("Get method called!!!")
        return self.__sex

    def set_sex(self, sex):
        #  print("set method called!!!")
        self.__sex = sex

    def del_sex(self):
        # print("del method called!!!")
        del self.__sex

    sex = property(get_sex, set_sex, del_sex)

    # ============================= age ===================
    def get_age(self):
        # print("Get method called!!!")
        return self.__age

    def set_age(self, age):
        #  print("set method called!!!")
        self.__sex = age

    def del_age(self):
        # print("del method called!!!")
        del self.__age

    age = property(get_age, set_age, del_age)

    def space_check(self,position):
        if self.li[position - 1] == " ":
            return True
        else:
            return False

    def displayBooking(self):
        print(self.li[0])
        for x in range(0, 16):
            print("|" + self.li[x], end='')

        print("")

        for y in range(0, 16):
            if self.new_li[y] == " ":
                self.new_li[y] = "Empty"
                print("|" + self.new_li[y], end='')
            else:
                self.new_li[y] = "Booked"
                print("|" + self.new_li[y], end='')