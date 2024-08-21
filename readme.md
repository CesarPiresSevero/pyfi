### Fixed Point Library

This function provides the same solution as ML's fi command. The difference is that the output can actually be printed in the screen rather than creating an object. This function also have the option to return a list of values with the desired type of conversion. This function also provide error tracing, showing the values that are not corrected input for the configuration set by the user. The first value display will be in the input format.

#### Usage

This code can be used 2 ways:
* As a library by adding the following line in your code

```
					  from fi import fi
```

Note: remember to have this file in the same folder as the file you will be calling fi function from

* As a standalone conversion code. Hence you can run this code using command line like shown below:

```
						python fi.py
```

Note: remember to have terminal/prompt opened in the same folder as this file

#### Parameters

* Values: The input values of the function.
	* The input is a PYTHON LIST of any size (can accept also one INT or FLOAT)
	* For dec to hex or bin conversion the values need to be in dec format and for hex or bin to dec conversion values need to be bigger than 1
* Signed: Check if the value is signed (1) or unsigned (0)
* TotalLen: The total number of bits used
* FracLen: The number of bits used to represent the fractional part
* Format: Check if the input is decimal (1) or hex/bin (0)
* ReturnVal: Check if the function returns value or just prints
	* "None": returns None, only prints values
	* "Dec" : returns a list of decimal values
	* "Hex" : returns a string of hex values
	* "Bin" : returns a string of bin values
