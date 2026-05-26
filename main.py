#!/usr/bin/python

print ("Prosty kalkulator Python\n" \
"Wybierz opcje:\n" \
"1. Dodawanie\n" \
"2. Odejmowanie\n" \
"3. Mnozenie\n" \
"4. Dzielenie\n" \
"0. Wyjscie\n\n")

option = int(input("Wybierz opcje: "))

if option == 1:
	a = int(input("Podaj pierwsza liczbe: "))
	b = int(input("Podaj druga liczbe: "))
	print("\nWynik: ")
	print (a + b)
	exit()
elif option == 2:
	a = int(input("Podaj pierwsza liczbe: "))
	b = int(input("Podaj druga liczbe: "))
	print("\nWynik: ")
	print (a - b)
	exit()
elif option == 3:
	a = int(input("Podaj pierwsza liczbe: "))
	b = int(input("Podaj druga liczbe: "))
	print("\nWynik: ")
	print (a * b)
	exit()
elif option == 4:
	a = int(input("Podaj pierwsza liczbe: "))
	b = int(input("Podaj druga liczbe: "))
	print("\nWynik: ")
	print (a / b)
	exit()
else:
	print("Nie ma takiej opcji w menu!")
	exit()

