import sys
def WeeklyPaymentCalculator():
    if len(sys.argv) != 4:
        print(f"{' '.join(sys.argv[1:])}")
        print("Your input is invalid!")
        return
    print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]}")
    try:
        hours = float(sys.argv[1])
        normal_rate = float(sys.argv[2])
        overtime_rate = float(sys.argv[3])
        # Input validation
        if hours < 0 or normal_rate < 0 or overtime_rate < 0 or hours > 1000:
            print("Your input is invalid!")
            return
        normal_hours = min(hours, 40)
        overtime_hours = max(hours - 40, 0)
        normal_salary = normal_hours * normal_rate
        overtime_salary = overtime_hours * overtime_rate
        total_salary = normal_salary + overtime_salary
        print(f"Normal Salary:{normal_salary:.2f}, Extra Salary:{overtime_salary:.2f}, Total Salary:{total_salary:.2f}")
    except Exception:
        print("Your input is invalid!")


if __name__=='__main__':
    WeeklyPaymentCalculator()
    
