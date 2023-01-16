from flat import Bill, Flatmate
from report import PdfReport

amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period, e.g. December 2020: ")

name1 = input("Whats your name? ")
days_in_house1 = int(input(f"How many days did {name1} stayed in house during the period? "))
name2 = input("Whats your mate's name? ")
days_in_house2 = int(input(f"How many days did {name2} stayed in house during the period? "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)


pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)