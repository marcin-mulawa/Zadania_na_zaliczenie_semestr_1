# -*- coding: utf-8 -*-
# 2. Korzystając z pojęcia funkcji utwórz skrypt,
# który będzie miał możliwość zamiany temperatury pomiędzy skalami 
# Celsjusza i Fahrenheita (w obie strony). C = (F-32)x(5/9), F = (C*9/5)+32

def change_temp(temperature, scale="C"):
    
    """ Converts degrees Celsius to degrees Fahrenheit or vice versa.
    
        Parameters
        ----------
        temperature: float
            Temperature value
        scale: string
            The scale at which you entered temperature:
                C - Celsius
                F - Fahrenheit
        
        Returns
        -------
        converted temperature value
    """     
    
    if scale == 'C':
        return temperature*9/5+32
    else:
        return (temperature-32)*5/9