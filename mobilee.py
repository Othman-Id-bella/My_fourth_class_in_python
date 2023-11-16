class Mobile:
    def __init__(self, companyName, storage, serialNum, name, support4k):
        self.companyName = companyName
        self.storage = storage
        self.serialNum = serialNum
        self.name = name
        self.support4k = support4k

    def info(self):
        print("Mobile Info:Company:",self.companyName,"Storage:",self.storage,"GB Serial Number:",self.serialNum,"Name:",self.name,"Supports 4K:",self.support4k)


mobile1 = Mobile("Apple", 128, "SN123456", "iPhone 12", True)
mobile2 = Mobile("Samsung", 256, "SN789012", "Galaxy S21", True)
mobile3 = Mobile("Google", 64, "SN345678", "Pixel 5", False)


mobile1.info()
mobile2.info()
mobile3.info()
