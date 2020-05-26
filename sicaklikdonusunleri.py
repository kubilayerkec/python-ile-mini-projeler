# Kubilay Erkeç
# kubilay@kubilay.net
# Udemy Eğitimleri: https://www.udemy.com/user/kubilay-erkec/

#Celsius        ->     Fahrenheit   ->      °F = °C × 1.8 + 32
#Fahrenheit     ->     Celsius	    ->      °C = (°F – 32) / 1.8
#Celsius	    ->     Kelvin       ->  	°K = °C + 273.15
#Kelvin         -> 	   Celsius	    ->      °C = °K – 273.15
def CelsiusToFahrenheit(celsius):
    Fahrenheit = celsius * 1.8 + 32
    return Fahrenheit

def FahrenheitToCelsius(Fahrenheit):
    Celsius = (Fahrenheit - 32) / 1.8
    return Celsius

def CelsiusToKelvin(celsius):
    Kelvin = celsius + 273.15
    return Kelvin

def KelvinToCelsius(Kelvin):
    Celsius = Kelvin - 273.15
    return Celsius

dereceAl = float(input("Lütfen celsius olarak dereceyi giriniz: "))
print("Fahrenheit: ",CelsiusToFahrenheit(dereceAl))
print("Kelvin: ",CelsiusToKelvin(dereceAl))