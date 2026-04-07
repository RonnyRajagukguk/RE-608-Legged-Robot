from forward_kinematics import run_forward
from inverse_kinematics import run_inverse

print("=== ROBOT SIMULATION ===")
print("1. Forward Kinematics")
print("2. Inverse Kinematics")

choice = input("Pilih (1/2): ")

if choice == "1":
    run_forward()
elif choice == "2":
    run_inverse()
else:
    print("Pilihan tidak valid")