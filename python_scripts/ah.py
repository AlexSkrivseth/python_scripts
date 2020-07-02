
# In the formula below, temperature (T) is expressed in degrees Celsius,
# relative humidity (rh) is expressed in %,
# and e is the base of natural logarithms 2.71828 [raised to the power of the contents of the square brackets]:
#
# Absolute Humidity (grams/m3) = 6.112 × e^[(17.67 × T)/(T+243.5)] × rh × 18.02 / (273.15+T) × 100 × 0.08314



def absolute_humidity(t=None, rh=None):
    if t and rh:
        # t is farhenheit
        T = (t - 32) * 5/9
        # T is celsius
        #T = t

        ah = 6.112 * 2.71828**((17.67 * T)/(T+243.5)) * rh * 2.1674 / (273.15+T)
        print("The absolute_humidity is {} grams/m3".format(ah))

        return ah
    else:
        return "Please give two keyword arguments eg. (t=89,rh=67)"




absolute_humidity(t=140, rh=.14)
absolute_humidity(t=130, rh=.80)
absolute_humidity(t=120, rh=.80)
absolute_humidity(t=70, rh=.20)
