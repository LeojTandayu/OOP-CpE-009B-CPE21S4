def main():
    class TemperatureConversion:
        def __init__(self, temp =1):
            self.temp = temp

    class FahrenheitToCelcius(TemperatureConversion):
        def conversion(self):
            return(self.temp - 32 ) * (5/9)

    class KelvinToCelsius(TemperatureConversion):
        def conversion(self):
            return  self.temp - 273.15

    tempInKelvin = float(input("Enter the temperature in Kelvin : "))

    convert = KelvinToCelsius(tempInKelvin)
    print(str(convert.conversion()) + " Celsius")

    tempInFahrenheit = float(input("Enter the temperature in Fahrenheit : "))

    convert  = FahrenheitToCelcius(tempInFahrenheit)
    print(str(convert.conversion()) + " Celsius")


main()

