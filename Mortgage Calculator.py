class MortgageCalculator:
    def __init__(self, principal, rate, amortization):
        """
        Initialize the mortgage calculator with loan amount, interest rate, and amortization period.
        """
        self.__principal = principal
        self.__rate = rate / 100  # Convert percentage to decimal
        self.__amortization = amortization

    def calculate_payments(self):
        """
        Calculate mortgage payments for different payment frequencies.
        """
        r_q = self.__rate  # Annual interest rate
        n = self.__amortization * 12  # Total number of months

        # Monthly Rate Calculation
        monthly_rate = (1 + r_q / 2) ** (2 / 12) - 1
        monthly_payment = (self.__principal * monthly_rate) / (1 - (1 + monthly_rate) ** -n)

        # Semi-Monthly Rate Calculation
        semi_monthly_rate = (1 + r_q / 2) ** (2 / 24) - 1
        semi_monthly_payment = (self.__principal * semi_monthly_rate) / (1 - (1 + semi_monthly_rate) ** -(2 * self.__amortization * 12))

        # Bi-Weekly Rate Calculation
        bi_weekly_rate = (1 + r_q / 2) ** (2 / 26) - 1
        bi_weekly_payment = (self.__principal * bi_weekly_rate) / (1 - (1 + bi_weekly_rate) ** -(self.__amortization * 26))

        # Weekly Rate Calculation
        weekly_rate = (1 + r_q / 2) ** (2 / 52) - 1
        weekly_payment = (self.__principal * weekly_rate) / (1 - (1 + weekly_rate) ** -(self.__amortization * 52))

        # Accelerated Bi-Weekly Payment (13 monthly payments per year instead of 12)
        rapid_bi_weekly_payment = monthly_payment / 2

        # Accelerated Weekly Payment (52 payments per year instead of 48 from standard weekly payments)
        rapid_weekly_payment = monthly_payment / 4

        return (
            f"Monthly Payment: ${monthly_payment:.2f}",
            f"Semi-monthly Payment: ${semi_monthly_payment:.2f}",
            f"Bi-weekly Payment: ${bi_weekly_payment:.2f}",
            f"Weekly Payment: ${weekly_payment:.2f}",
            f"Rapid Bi-weekly Payment: ${rapid_bi_weekly_payment:.2f}",
            f"Rapid Weekly Payment: ${rapid_weekly_payment:.2f}"
        )

# Example Usage
if __name__ == "__main__":
    calculator = MortgageCalculator(principal=400000, rate=2.7, amortization=27)
    for payment in calculator.calculate_payments():
        print(payment)
