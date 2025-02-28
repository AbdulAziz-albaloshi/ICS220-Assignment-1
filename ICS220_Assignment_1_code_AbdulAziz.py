from enum import Enum # Import the needed modules


class Gender(Enum):
    """Class to represent Enumeration of available genders."""
    MALE = "Male"
    FEMALE = "Female"


class Customer:
    """Class to represent a customer"""

    # Constructor (The attributes are private "__")
    def __init__(self):
        self.__customer_name = ""
        self.__customer_id = ""
        self.__customer_phonenumber = 0
        self.__customer_address = ""
        self.__customer_gender = Gender.MALE

    # Setter and Getter methods (The methods/functions are public)
    def set_customer_name(self, name=""):
        # Sets the customer's name
        self.__customer_name = name

    def get_customer_name(self):
        # Gets the customer's name
        return self.__customer_name

    def set_customer_id(self, customer_id=""):
        # Sets the customer's ID
        self.__customer_id = customer_id

    def get_customer_id(self):
        # Gets the customer's ID
        return self.__customer_id

    def set_customer_phonenumber(self, phonenumber=0):
        # Sets the customer's phone number
        self.__customer_phonenumber = phonenumber

    def get_customer_phonenumber(self):
        # Gets the customer's phone number
        return self.__customer_phonenumber

    def set_customer_address(self, address=""):
        # Sets the customer's address
        self.__customer_address = address

    def get_customer_address(self):
        # Gets the customer's address
        return self.__customer_address

    def set_customer_gender(self, gender=Gender.MALE):
        # Sets the customer's gender
        if gender in Gender:
            self.__customer_gender = gender

    def get_customer_gender(self):
        # Gets the customer's gender
        return self.__customer_gender

    def customer_information(self):
        # Displays the customer's full information
        return f"Customer[Name: {self.__customer_name}, ID: {self.__customer_id}, Phone: {self.__customer_phonenumber}, Address: {self.__customer_address}, Gender: {self.__customer_gender.value}]"

    def __str__(self):
        # String representation of the Customer class
        return self.customer_information()


# Administrator Class
class Administrator:
    """Class to represent an administrator"""

    # Constructor (The attributes are private "__")
    def __init__(self):
        self.__admin_name = ""
        self.__admin_id = ""
        self.__admin_phonenumber = 0
        self.__admin_role = ""
        self.__admin_gender = Gender.MALE

    # Setter and Getter methods (The methods/functions are public)
    def set_admin_name(self, name=""):
        # Sets the administrator's name
        self.__admin_name = name

    def get_admin_name(self):
        # Gets the administrator's name
        return self.__admin_name

    def set_admin_id(self, admin_id=""):
        # Sets the administrator's ID
        self.__admin_id = admin_id

    def get_admin_id(self):
        # Gets the administrator's ID
        return self.__admin_id

    def set_admin_phonenumber(self, phonenumber=0):
        # Sets the administrator's phone number
        self.__admin_phonenumber = phonenumber

    def get_admin_phonenumber(self):
        # Gets the administrator's phone number
        return self.__admin_phonenumber

    def set_admin_role(self, role=""):
        # Sets the administrator's role
        self.__admin_role = role

    def get_admin_role(self):
        # Gets the administrator's role
        return self.__admin_role

    def set_admin_gender(self, gender=Gender.MALE):
        # Sets the administrator's gender
        if gender in Gender:
            self.__admin_gender = gender

    def get_admin_gender(self):
        # Gets the administrator's gender
        return self.__admin_gender

    def admin_information(self):
        # Displays the administrator's full information
        return f"Administrator[Name: {self.__admin_name}, ID: {self.__admin_id}, Phone: {self.__admin_phonenumber}, Role: {self.__admin_role}, Gender: {self.__admin_gender.value}]"

    def __str__(self):
        # String representation of the Administrator class
        return self.admin_information()


# Driver Class
class Driver:
    """Class to represent a delivery driver"""

    # Constructor (The attributes are private "__")
    def __init__(self):
        self.__driver_name = ""
        self.__driver_id = ""
        self.__driver_phonenumber = 0
        self.__driver_vehicle_details = ""
        self.__driver_license_num = 0

    # Setter and Getter methods (The methods/functions are public)
    def set_driver_name(self, name=""):
        # Sets the driver's name
        self.__driver_name = name

    def get_driver_name(self):
        # Gets the driver's name
        return self.__driver_name

    def set_driver_id(self, driver_id=""):
        # Sets the driver's ID
        self.__driver_id = driver_id

    def get_driver_id(self):
        # Gets the driver's ID
        return self.__driver_id

    def set_driver_phonenumber(self, phonenumber=0):
        # Sets the driver's phone number
        self.__driver_phonenumber = phonenumber

    def get_driver_phonenumber(self):
        # Gets the driver's phone number
        return self.__driver_phonenumber

    def set_driver_vehicle_details(self, details=""):
        # Sets the driver's vehicle details
        self.__driver_vehicle_details = details

    def get_driver_vehicle_details(self):
        # Gets the driver's vehicle details
        return self.__driver_vehicle_details

    def set_driver_license_num(self, license_num=0):
        # Sets the driver's license number
        self.__driver_license_num = license_num

    def get_driver_license_num(self):
        # Gets the driver's license number
        return self.__driver_license_num

    def driver_information(self):
        # Displays the driver's full information
        return f"Driver[Name: {self.__driver_name}, ID: {self.__driver_id}, Phone: {self.__driver_phonenumber}, Vehicle Details: {self.__driver_vehicle_details}, License Num: {self.__driver_license_num}]"

    def __str__(self):
        # String representation of the Driver class
        return self.driver_information()


class PaymentMethod(Enum):
    """Class to represent Enumeration of available payment methods."""
    CREDIT_CARD = "Credit Card"
    DEBIT_CARD = "Debit Card"
    PAYPAL = "PayPal"
    CASH = "Cash"


class Order:
    """Class to represent an order"""

    # Constructor (The attributes are private "__")
    def __init__(self):
        self.__order_description = ""
        self.__order_number = 0
        self.__order_total_amount = 0.0
        self.__order_weight = 0.0
        self.__payment_method = PaymentMethod.CASH

    # Setter and Getter methods (The methods/functions are public)
    def set_order_description(self, description=""):
        # Sets the order description
        self.__order_description = description

    def get_order_description(self):
        # Gets the order description
        return self.__order_description

    def set_order_number(self, order_number=0):
        # Sets the order number
        self.__order_number = order_number

    def get_order_number(self):
        # Gets the order number
        return self.__order_number

    def set_order_total_amount(self, total_amount=0.0):
        # Sets the order total amount
        self.__order_total_amount = total_amount

    def get_order_total_amount(self):
        # Gets the order total amount
        return self.__order_total_amount

    def set_order_weight(self, weight=0.0):
        # Sets the order weight
        self.__order_weight = weight

    def get_order_weight(self):
        # Gets the order weight
        return self.__order_weight

    def set_payment_method(self, method=PaymentMethod.CASH):
        # Sets the payment method
        if method in PaymentMethod:
            self.__payment_method = method

    def get_payment_method(self):
        return self.__payment_method

    def order_information(self):
        # Displays the order's full information
        return f"Order[Description: {self.__order_description}, Number: {self.__order_number}, Total Amount: AED{self.__order_total_amount}, Weight: {self.__order_weight}kg, Payment Method: {self.__payment_method.value}]"

    def __str__(self):
        # String representation of the Order class
        return self.order_information()


# Create an Object for Customer class
customer1 = Customer()
customer1.set_customer_id("202330144")
customer1.set_customer_name("Abdul Aziz")
customer1.set_customer_phonenumber(971504988670)
customer1.set_customer_address("Alkhartoom Street, Ajman")
customer1.set_customer_gender(Gender.MALE)
print(customer1)

# Create an Object for Administrator class
admin1 = Administrator()
admin1.set_admin_id("AD22910")
admin1.set_admin_name("Sujith Mathew")
admin1.set_admin_phonenumber(971501122897)
admin1.set_admin_role("Manager")
admin1.set_admin_gender(Gender.MALE)
print(admin1)

# Create an Object for Driver class
driver1 = Driver()
driver1.set_driver_id("D678554")
driver1.set_driver_name("Mohammed Jasim")
driver1.set_driver_phonenumber(971567890123)
driver1.set_driver_vehicle_details("Nissan Sunny - 2014 - Sharjah 20331 U")
driver1.set_driver_license_num(889082773)
print(driver1)

# Create an Object for Order class
order1 = Order()
order1.set_order_description("Black Samsung S25 Ultra 256 GB memory")
order1.set_order_number(122109)
order1.set_order_total_amount(4299.99)
order1.set_order_weight(0.5)
order1.set_payment_method(PaymentMethod.CREDIT_CARD)
print(order1)