# Python Fixed-Point Library

Python Fixed-Point Library (PyFi) provides an alternative solution to MATLAB's fi command, for free! 

The difference is that the output can actually be printed in the screen rather than just creating an fi object. This option can be quite handy while working with fixed-point implementations on limited hardware, as it usually require a lot of look up tables. Therefore, having the values available in hex format makes preparing the tables a breeze. 
There is also the option to return a list of values with the desired type of conversion, showing the values that are not corrected input for the configuration set by the user. 
This means that the input values will be checked for range based on the class configuration set by the user.

The main.py file contains 2 examples using terminal print and return values options.

## Donations

I believe in **free and open source software**! Help the OSS community by donating below:
<p align="center">
[<img src="img/paypal_button.png" width="400" height="228">](https://www.paypal.com/donate/?hosted_button_id=AMFZ83MA4Z3RA)
</p>

## Installation

Clone the repository and run the PIP editable installation:

```bash
git clone https://github.com/CesarPiresSevero/pyfi.git
pip install -e pyfi
```

A success message should be shown when the process is completed. To make sure that the package was properly installed go to a new terminal and try importing it via Python console:

```bash
python
```        
```python
import pyfi
```

If no messages are seen after this step that means that the package is properly installed

Note: it is strongly encouraged to always use Python virtual environments


## Usage

PyFi library can be imported as shown below:

```python
from pyfi import fi
```

The Fi class has only it's callable method (dunder call dunder) with only one input variable (value). Class attributes can be set with constructor or with getters and setters.

Configuring the class with constructor:

```python
fi_obj = fi(word_len = 16, frac_len = 15, fixed = False)
```

In the example above, the number of value representation was change to 16 bits. Fractional bits were set to 15 bits, meaning that no exponent bits are used. Also, the conversion format was set to fixed-point to floating-point.
The example below shows the attributes set via setters. The signedness was changed to unsigned and the returned value was set to true. Meaning that no prints will be done to console and converted values will be returned from the callable instance method.

```python
fi_obj = fi()
fi_obj.signed = False
fi_obj.return_val = True                 
```

To convert the values, the instance must be called. Input values will be converted as configured via attributes. On the example below, the default attributes will be used to demonstrate the conversion:

```python
fi_obj = fi()
fi_obj(1.0)
```

The output should be printed in the console as shown below:

<blockquote>
PYTHON FIXED POINT CONVERTER


Configuration:

-Type of conversion: Floating to fixed point

-Signedness: Signed

-Total bits: 32

-Fractional bits: 31

WARNING: 1.0 can not be represented, 0.99999999977 will be used instead ( index: 0 )


Converted values:

-Dec (Input): 0.99999999977

-Hex (Output): 0x7fffffff

-Bin (Output): 0b01111111111111111111111111111111
</blockquote>

Note: this package was only tested in Linux

## FI Class

FI class is the only class included with the PyFi at the moment. It's main purpose is to convert floating-point to fixed-point and vice-versa.

### Attributes

Below are described the FI class attributes. As explained on the usage section, they can be set via constructor or via setters.

* **signed** : bool, optional
    
Signedess of the fixed-point format. True for signed and False for unsigned.

Default is signed (True).

* **word_len** : int, optional

Number of bits used to represent the value. Usual values are 64, 32 or 16 bits.

Default is 32 bit.

* **frac_len** : int, optional

Fractional bits (mantissa). The more fractional bits, the more precision the fixed-point representation will have. 

Default is 31 bit (Q31).

* **fixed** : bool, optional

Format used for conversion. True for floating-point to fixed-point conversion and False for fixed-point to floating-point conversion.

Default is fixed-point to floating-point conversion (True).

* **return_val** : bool, optional

Selects type of output, return values or print on the console.

Default is print on console (False).

### Methods

Fi class has only one method for the user, the called instance. This was done to facilitate usage. The method only has one input:

* **value** : list,float,int
   
The value to be converted. It supports a list of floats, a list of integers, a float or a integer. The format will depend on the user configuration. The library will return an error if the input is not in the proper format.

Note: it is understood that it is not a good practice to have multiple formats for the same variable. The priority here was given to easy of use.

## Contributions

PyFi is a free and open source library (MIT license). Any contributions are most welcome!

Above all, the idea for this library is to be simple. Thus being the best companion of SW developers implementing fixed-point arithmetic.

Please, reach out if you have any improvement ideas. Feel free to create PRs as well.


