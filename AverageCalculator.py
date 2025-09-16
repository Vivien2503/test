import sys
def AverageCalculator(numbers):
  # Accepts a list of numbers (as floats or strings)
  try:
    nums = [float(x) for x in numbers]
    average = sum(nums) / len(nums)
    print(f"Average: {average:.2f}")
  except ValueError:
    print(f"Numbers: {numbers} -> Your input is invalid!")

# Test cases
test_cases = [[3,4,5], [60,39,92], ['abc',10,20], [10,20,30,40], [100]]

if __name__ == '__main__':
  # Run test cases
  for case in test_cases:
    AverageCalculator(case)
  if len(sys.argv) > 1:
    AverageCalculator(sys.argv[1:])