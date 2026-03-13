import math

def calculate_emi(principal, rate, years):

    months = years * 12
    r = rate / (12 * 100)

    emi = (principal * r * (1 + r)**months) / ((1 + r)**months - 1)

    return emi


def evaluate_loan(age, income, credit_score, existing_emi, new_emi, employment):

    reasons = []

    dti = (existing_emi + new_emi) / income

    if age < 21 or age > 60:
        reasons.append("Applicant age not eligible")

    if credit_score < 650:
        reasons.append("Credit score too low")

    if dti > 0.5:
        reasons.append("Debt-to-income ratio too high")

    if employment.lower() == "student":
        reasons.append("Unstable employment status")

    if len(reasons) == 0:
        return "Approved", ["Financial profile is healthy"]

    return "Rejected", reasons