import sys 
def BMICalculator(weight, height, unit="Metric"):
   try:
      weight = float(weight)
      height = float(height)
      if unit.lower() == "imperial":
         # Convert pounds/inches to kg/m
         weight = weight * 0.45359237
         height = height * 0.0254
         unit_str = "Imperial"
      else:
         unit_str = "Metric"
      bmi = weight / (height ** 2)
      # categorize result
      if bmi <= 16:
         category = "Severe Thinness"
      elif 16 < bmi < 17:
         category = "Moderate Thinness"
      elif 17 < bmi < 18.5:
         category = "Mild Thinness"
      elif 18.5 < bmi < 25:
         category = "Normal"
      elif 25 < bmi < 30:
         category = "Overweight"
      elif 30 < bmi < 35:
         category = "Obese Class I"
      elif 35 < bmi < 40:
         category = "Obese Class II"
      else:
         category = "Obese Class III"
      print(f"{bmi:.2f}\t{category}\t({unit_str})")
   except Exception:
      print(f"Weight: {weight}, Height: {height} -> Your input is invalid!")

# Test cases (weight, height, unit)
test_cases = [
   (78, 1.80, "Metric"),
   (48, 1.78, "Metric"),
   (126, 1.60, "Metric"),
   (68.90, 1.54, "Metric"),
   (85.63, 1.68, "Metric"),
   ("abc", 1.70, "Metric"),
   (70, "xyz", "Metric"),
   (180, 70, "Imperial"),
   (150, 65, "Imperial")
]

if __name__=='__main__':
   # Run test cases
   for case in test_cases:
      BMICalculator(*case)
   if len(sys.argv) == 4:
      BMICalculator(sys.argv[1], sys.argv[2], sys.argv[3])
   elif len(sys.argv) == 3:
      BMICalculator(sys.argv[1], sys.argv[2])