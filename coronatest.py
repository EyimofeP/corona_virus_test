#Code by Pinnick_Jnr alias The Geekish Nerd
print("""
CORONAVIRUS TEST CODE 
DEVELOPED BY PINNICK_JNR
This is a simple code that ask questions to see if a person has coronavirus 
Questions are anwsered through a terminal.	
All answers should be in lower case please!!!
	""")
#Input for Patient Information
first_name = str(input("What is your first name please?:  "))
last_name = str(input("What is your last name please?:  "))
gender = str(input("What is your gender(m/f):  "))
#Input Statement for Conditions
temp_choice = int(input("What is your Temperature?(Must be a number please e.g 36):  " ))
cough_choice = str(input("Do you cough?(y/n):  "))
sneeze_choice = str(input("Do you sneeze?(y/n):   "))
fever = str(input("Do you have fever?(y/n):   "))
sore_throat = str(input("Is your throat sore?(y/n):   "))

#Conditions for CoronaVirus Test
if gender == "m" and gender != "f" and temp_choice >= 45 and cough_choice == "y" and sneeze_choice == "y" and fever == "y" and sore_throat == "y":
	print(f"You have the Virus Mr {last_name},you need to get to the nearest hospital {first_name} immediately!!!!!")
elif gender == "m" and gender != "f" and  temp_choice >= 36 and temp_choice <= 45 and cough_choice == "n" and sneeze_choice == "y" and fever == "y" and sore_throat == "n":
	print(f"You dont have the virus Mr {last_name},But you are ill {first_name}, get to the nearest health clinic!!!!")
elif gender == "m" and gender != "f":
	print(f"You're free of the virus Mr {last_name}. Please wash your hands regularly!!!! and {first_name} better Thank God")

if gender == "f" and gender != "m" and temp_choice >= 45 and cough_choice == "y" and sneeze_choice == "y" and fever == "y" and sore_throat == "y":			
	print(f"You have the Virus Miss/Mrs {last_name},you need to get to the nearest hospital {first_name} immediately!!!!!")
elif gender == "f" and gender != "m" and temp_choice >= 36 and temp_choice <= 45 and cough_choice == "n" and sneeze_choice == "y" and fever == "y" and sore_throat == "n":
	print(f"You dont have the virus Miss/Mrs {last_name},But you are ill {first_name}, get to the nearest health clinic!!!!")
elif gender == "f" and gender != "m":
	print(f"You're free of the virus Miss/Mrs {last_name}. Please wash your hands regularly!!!! and {first_name} better Thank God")


