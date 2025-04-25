from abc import ABC, abstractmethod

# Abstract base class
class InterestCalculator(ABC):
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    @abstractmethod
    def calculate_interest(self):
        pass

# Intermediate class (implements common methods)
class InterestBase(InterestCalculator):
    def __init__(self, principal, rate, time):
        super().__init__(principal, rate, time)
    
    def get_common_components(self):
        return self.principal * self.rate * self.time / 100

# Simple Interest Calculator
class SimpleInterest(InterestBase):
    def calculate_interest(self):
        return self.get_common_components()

# Compound Interest Calculator
class CompoundInterest(InterestBase):
    def __init__(self, principal, rate, time, compounding_frequency=1):
        super().__init__(principal, rate, time)
        self.compounding_frequency = compounding_frequency
    
    def calculate_interest(self):
        amount = self.principal * (1 + self.rate/(100 * self.compounding_frequency)) ** (self.compounding_frequency * self.time)
        return amount - self.principal

# Main program
def main():
    # Input values
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    time = float(input("Enter time (in years): "))
    compounding = int(input("Enter compounding frequency per year (1 for annual): "))

    # Create calculators
    simple = SimpleInterest(principal, rate, time)
    compound = CompoundInterest(principal, rate, time, compounding)

    # Calculate and display results
    print(f"\nSimple Interest: {simple.calculate_interest():.2f}")
    print(f"Compound Interest: {compound.calculate_interest():.2f}")

if __name__ == "__main__":
    main()
