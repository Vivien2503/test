def BMICalculator(weight, height):
   try:
      weight = float(weight)
      height = float(height)
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
      print(f"{bmi:.2f}\t{category}")
   except Exception:
      print(f"Weight: {weight}, Height: {height} -> Your input is invalid!")

# Test cases (weight in kg, height in m)
test_cases = [
   (78, 1.80),
   (48, 1.78),
   (126, 1.60),
   (68.90, 1.54),
   (85.63, 1.68),
   ("abc", 1.70),
   (70, "xyz")
]

if __name__=='__main__':
   for case in test_cases:
      BMICalculator(*case)