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
        n_years = self.__amortization

        # Define payment frequencies and corresponding factors
        frequencies = {
            "Monthly": 12,
            "Semi-monthly": 24,
            "Bi-weekly": 26,
            "Weekly": 52
        }

        payments = {}

        for key, f in frequencies.items():
            rate = (1 + r_q / 2) ** (2 / f) - 1  # Frequency-specific interest rate
            total_payments = f * n_years
            payment = (self.__principal * rate) / (1 - (1 + rate) ** -total_payments)
            payments[key] = payment

        # Accelerated Payments
        payments["Rapid Bi-weekly"] = payments["Monthly"] / 2
        payments["Rapid Weekly"] = payments["Monthly"] / 4

        return [f"{key} Payment: ${value:.2f}" for key, value in payments.items()]

# Example Usage
if __name__ == "__main__":
    # Prompting user for input values
    principal = float(input("Enter the principal amount (loan): $"))
    rate = float(input("Enter the annual interest rate (in %): "))
    amortization = int(input("Enter the amortization period (in years): "))
    
    # Create an instance of the MortgageCalculator with user inputs
    calculator = MortgageCalculator(principal=principal, rate=rate, amortization=amortization)
    
    # Display the mortgage payments
    for payment in calculator.calculate_payments():
        print(payment)


