class Bill:
    """
    Objects constains data about a bill, such as
    total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    creates a flatmate person who lives in the flat
    and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Create a PDF file that creates data about
    the flatmates such as their names their due
    amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


the_bill = Bill(amount=120, period="March2021")
John = Flatmate(name="John", days_in_house=20)
Marry = Flatmate(name="Mary", days_in_house=25)

print(John.pays(bill=the_bill, flatmate2=Marry))

