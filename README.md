# unit-integration-testing-lab
# Lab-09: Unit and Integration Testing Lab

## Student Information
Name: Adnan Shahzad
Roll Number:231400007

## Project Description
This project implements a banking application with comprehensive unit and integration testing using pytest. The application demonstrates the difference between unit testing (testing individual functions in isolation) and integration testing.

### Banking Functions:
1. deposit(balance, amount) - Adds positive amount to balance
2. withdraw(balance, amount) - Deducts amount if sufficient funds exist
3. calculate_interest(balance, rate, years) - Calculates compound interest
4. check_loan_eligibility(balance, credit_score) - Checks loan eligibility (balance ≥ 5000 and credit_score ≥ 700)
5. transfer(balance_from, balance_to, amount) - Transfers funds between accounts (uses withdraw and deposit)

## How to Run Tests

### Installation

# Clone repository
git clone https://github.com/CoderHere07/unit-integration-testing-lab.git;
cd unit-integration-testing-lab

# Install dependencies
pip install -r requirements.txt
# Run all tests (unit + integration)
pytest

# Run with detailed output
pytest -v

# Run only unit tests
pytest test_unit.py -v

# Run only integration tests
pytest test_integration.py -v

# Generate HTML test report
pytest --html=report.html -v
