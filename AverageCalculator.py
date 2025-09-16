def AverageCalculator(numbers) :
 try: 
  nums = [float(x) for x in numbers]
  average = sum(nums) / len(nums)
  print(f"Average: {average:.2f}")
 except ValueError:
  print(f"Numbers: {numbers} -> Your input is invalid!")

# Test cases
test_cases = [[3,4,5], [60,39,92], ['abc',10,20], [10,20,30,40], [100]]

if __name__ == '__main__':
  for case in test_cases:
    AverageCalculator(case)