def health_status(avg):
    if 90 <= avg <= 100:
        return "Excellent Health"
    elif 80 <= avg <= 89:
        return "Good Health"
    elif 65 <= avg <= 79:
        return "Moderate Health"
    elif 50 <= avg <= 64:
        return "Fair Health"
    elif 40 <= avg <= 49:
        return "Poor Health"
    else:
        return "Critical Condition"
    
def display_summary(name,pid,age,avg,status):
    return (
        "\n--- Patient Health Report ---\n"
        f"Name: {name}\n"
        f"Patient ID: {pid}\n"
        f"Age: {age}\n"
        f"Average Health Score: {avg:.2f}\n"
        f"Health Status: {status}"
    )
    

def main():
    print("=== Patient Health Evaluation System ===\n")
name = input("Enter Patient Name: ")
pid = input("Enter Patient ID: ")
age = int(input("Enter Age: "))

bp = float(input("Enter Blood Pressure Score: "))
sugar = float(input("Enter Sugar Level Score: "))
bmi = float(input("Enter BMI Score: "))

avg_score = (bp + sugar + bmi) / 3
status = health_status(avg_score)

print(
        display_summary( 
            name,
            pid,
            age,
            avg_score,
            status
        )   
    )
if __name__ == "__main__":
    main()