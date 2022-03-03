print("Welcome to the MiniMe Life Insurance!");
income = int(input("Your annual income? "));
ccscore = int(input("Your credit score? "));
smoke = int(input("How many years have you been smoking? "));
surgery = int(input("How many surgeries in the past 5 years? "));

approveMsg = "Your insurance app is approved";
denyMsg = "Your application is denied";

if income>=50000:
	if ccscore>=500:
		print(approveMsg);
	else:
		if smoke<=5:
			print(approveMsg);
		else:
			if surgery<=2:
				print(approveMsg);
			else:
				print(denyMsg);
else:
	print(denyMsg);



