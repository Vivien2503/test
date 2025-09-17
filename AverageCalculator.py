import sys
def AverageCalculator(numbers):
  # Accepts a list of numbers (as floats or strings)
  try:
    nums = [float(x) for x in numbers]
    average = sum(nums) / len(nums)
    print(f"Average: {average:.2f}")
  except ValueError:
    print("Your input is invalid!")

if __name__ == '__main__':
  if len(sys.argv) > 1:
    AverageCalculator(sys.argv[1:])