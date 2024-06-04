def celsius_to_fahrenheit(celsius):
    return(celsius*9/5)+32
def celsius_to_kelvin(celsius):
    return celsius + 273.15
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32)*5/9
def fahrenheit_to_kelvin(fahrenheit):
    return(fahrenheit -32)*5/9 +273.15
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
def kelvin_to_fahrenheit(kelvin):
    return(kelvin - 273.15)*9/5 +32

def main ():
    temperature = float(input("enter the temperature value:"))
    unit = input("enter the unit of measurement(C,F,K):").upper()

    if unit == 'C' :
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        print(f"{temperature} degree celsius is equal to {fahrenheit:.2f} degree fahrenheit ")
        print(f"{temperature} degree celsius is equal to {kelvin:.2f} kelvin" )
    elif unit == 'F':
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
        print(f"{temperature} degree fahrenheit is equal to {celsius:.2f} degree celsius ")
        print(f"{temperature} degree fehrenheit is equal to {kelvin:.2f} degree kelvin" )
    elif unit =='K':
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
        print(f"{temperature} degree klevin is equal to {celsius:.2f} degree celsius ")
        print(f"{temperature} degree klevin is equal to {fahrenheit:.2f} degree fahrenheit")
    else:
        print("Invalid unit of measurement.please enter C for celsius ,F for fahrenheit or K for kelvin.")

if __name__ == "__main__":
        main()    



