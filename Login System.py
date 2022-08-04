#file name is saved as Registration


def username(a):
	n=input("\nEnter the username:\n")
	
	if(a==0):
		
		flag=0
		count=0
		
		while(flag==0):
			if(n[0].isalpha()==False or n[0].isdigit()==True):
				print("Username cannot begin with special characters or numbers.")
			else:
				count=count+1
				
			for i in range(len(n)):
				if(n[i]=="@" and n[i+1]=="."):
					print("You cannot enter '.' after '@'")
					
			if(count==1):
				print("Username is valid.")
				flag=1
				
		fi=open("Registration.txt","w")
		fi.write(n)
		fi.close()
		
		
	if(a==1):
		
		fi=open("Registration.txt","r")
		z=fi.read()
		q=len(z)-len(n)
		flag1=0
		
		if(len(n)!=(len(z)-q)):
			flag1=0
			
		for i in range(len(n)):
			if(n[i]!=z[i]):
				flag1=0
			else:
				flag1=2
				
		while(flag1==0):
			s=input("Username is invalid.\n\nEnter R if you have not yet registered else enter L for retry login.\n")
			if(s=="R" or s=="r"):
				username(0)
				password(0)
				flag1=1
				
			elif(s=="L" or s=="l"):
				username(1)
				flag1=1
				
			else:
				print("Invalid entry")
				flag1=0
		
		if(flag1==2):
			password(1)		
				
	return

def password(b):	
	p=input("\nEnter the password:\n")
	
	if(b==0):
		
		fi=open("Registration.txt","r")
		z=fi.read()
		
		flag=0
		
		while(flag==0):
			count=0
			
			if(5>len(p) or len(p)>16):
				print("Password length should be in between 5-16")
			else:
				count=count+1
				
			a=[p[j] for j in range(len(p)) if p[j].isupper()==True]
			if(len(a)==0):
				print("Password must contain an upper case letter.")
			else:
				count=count+1
			
			a=[p[j] for j in range(len(p)) if p[j].islower()==True]
			if(len(a)==0):
				print("Password must contain a lower case letter.")
			else:
				count=count+1
				
			a=[p[j] for j in range(len(p)) if p[j].isdigit()==True]
			if(len(a)==0):
				print("Password must contain a digit.")
			else:
				count=count+1
				
			a=[p[j] for j in range(len(p)) if p[j].isalpha()==False and p[j].isdigit()==False]
			if(len(a)==0):
				print("Password must contain a special character.")
			else:
				count=count+1
				
			if(count==5):
				print("Password is valid.")
				flag=1
	
	
		fi=open("Registration.txt","a")
		fi.seek(len(z))
		fi.write(p)
		fi.close()
		
	if(b==1):
		
		fi=open("Registration.txt","r")
		z=fi.read()
		q=len(z)-len(p)
		
		flag1=0
		
		while(flag1==0):
			if((len(p))!=(len(z)-q)):
				flag1=0
				
			for i in range(len(p)):
				if(p[i]!=z[q+i]):
					flag1=0
					
				else:
					flag1=2
						
			while(flag1==0):
				s=input("Password is invalid.\n\nEnter F to change password.\n\nEnter R to re-enter the password.\n\n")
				
				if(s=="F" or s=="f"):
					password(0)
					print("Password updated successfully.")
					flag1=1
					
				elif(s=="R" or s=="r"):
					password(1)
					flag1=1
					
				else:
					print("Invalid entry.")
					flag1=0
					
			if(flag1==2):
				print("\nLogin successful.")
					
	return

flag=0

while(flag==0):
	
	print("\n\nWELCOME TO THE PORTAL\n")
	inp=input("Login/Register\n\nEnter 'L' for Login, if you have already registered.\n\nEnter 'R' for registering as a new user.\n")
	
	if(inp=="L" or inp=="l"):
		username(1)
		flag=1
		
	if(inp=="R" or inp=="r"):
		username(0)
		password(0)
		flag=0
