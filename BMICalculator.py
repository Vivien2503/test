import sys 
def BMICalculator(weight, height, unit):
   try:
      weight = float(weight)
      height = float(height)
      if unit.lower() == "imperial":
         bmi = 703 * weight / (height ** 2)
      else:
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
      print("Your input is invalid!")

if __name__=='__main__':
   if len(sys.argv) == 4:
      BMICalculator(sys.argv[1], sys.argv[2], sys.argv[3])
   else:
      print("Your input is invalid!")