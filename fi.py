##############################################################################
#																			 #
#					    Fixed Point command FI                               #
#																			 #
##############################################################################

'''
	Description: 
		This function provides the same solution as ML's fi command.
		The difference is that the output can actually be printed in the 
		screen rather than creating an object. This function also have the
		option to return a list of values with the desired type of conversion. 
		This function also provide error tracing, showing the values that are 
		not corrected input for the configuration set by the user. The first 
		value display will be in the input format.
		- This code can be used 2 ways:
		1- As a library by adding the following line in your code:

							  from fi import fi

			IMPORTANT: remember to have this file in the same folder as the 
					   file you will be calling fi function from
		2- As a standalone conversion code. Hence you can run this code using 
		command line like shown below:

								python fi.py

			IMPORTANT: remember to have terminal/prompt opened in the same 
			folder as this file
	Parameters:
		- Values: The input values of the function.
				  * The input is a PYTHON LIST of any size 
				  	(can accept also one INT or FLOAT)
				  * For dec to hex or bin conversion the values need to be in
				   dec format and for hex or bin to dec conversion values 
				   need to be bigger than 1
		- Signed: Check if the value is signed (1) or unsigned (0)
		- TotalLen: The total number of bits used
		- FracLen: The number of bits used to represent the fractional part
		- Format: Check if the input is decimal (1) or hex/bin (0)
		- ReturnVal: Check if the function returns value or just prints
					* "None": returns None, only prints values
					* "Dec" : returns a list of decimal values
					* "Hex" : returns a string of hex values
					* "Bin" : returns a string of bin values
	
	Notes: There are some examples in the bottom of the function. To use them
		   UNCOMMENT the necessary code.
'''

import math

def fi(Values,Signed,TotalLen,FracLen,Format=1,ReturnVal='None'):

	#Converting values
	dec_text=""
	hex_text=""
	bin_text=""
	dec_vals=[]
	if(ReturnVal=='None'):
		#Printing header
		print("\nFIXED POINT CONVERSION\n")
		if(Format): print("-Type of conversion:","Decimal to Hex/Bin")
		else: print("-Type of conversion:","Hex/Bin to Decimal")
		if(Signed): print("-Signedness:","Signed")
		else: print("-Signedness:","Unsigned")
		print("-Total bits:",TotalLen)
		print("-Fractional bits:",FracLen)

	#Calculating fractional digits to represent dec
	Precision=math.ceil(FracLen/3)
	Precision_txt="{:."+str(Precision)+"f}"

	#Converting input type to list
	if(type(Values)==int or type(Values)==float):
		Values=[Values]

	#Decimal
	if(Format):
		#Check if it is signed
		if(Signed):
			for val in Values:
				#Check if it is positive value
				if(val>0):
					dec_text=dec_text+Precision_txt.format(val)+","
					#Check if value is above the limit
					if(val>(2**(TotalLen-FracLen)-(2**(TotalLen-FracLen-1)))):
						if(ReturnVal=='None'): print("\nERROR: Value is too high, range from",(2**(TotalLen-FracLen)-(2**(TotalLen-FracLen-1))),"to",-(2**(TotalLen-FracLen)-(2**(TotalLen-FracLen-1)))," ( value:",val," index:",Values.index(val),")")
						return None
					elif(val==(2**(TotalLen-FracLen)-(2**(TotalLen-FracLen-1)))):
						if(ReturnVal=='None'): print("WARNING:",(2**(TotalLen-FracLen)-(2**(TotalLen-FracLen-1))),"can not be represented,",round(((2**(TotalLen-FracLen)-(2**(TotalLen-FracLen-1)))-1/(2**TotalLen)),Precision),"will be used instead","( index:",Values.index(val),")")
						val=(2**(TotalLen-FracLen)-(2**(TotalLen-FracLen-1)))-1/(2**TotalLen)
						dec_text=''
						dec_text=dec_text+Precision_txt.format(val)+","
					num=math.ceil(val*(2**(TotalLen-(TotalLen-FracLen))))
					if(num>=(2**TotalLen)/2): num=num-1
					#Check if value is less than minimal possible
					if(num<=0):
						num=0
					hex_text=hex_text+("0x"+hex(num)[2:].zfill(int(TotalLen/4)))+","
					bin_text=bin_text+("0b"+bin(num)[2:].zfill(TotalLen))+","	
					if(ReturnVal!='None'): 
						dec_vals.append(val)							
				#If negative
				else:
					#Check if value is above the limit
					if((-1)*val>(2**(TotalLen-FracLen)-(2**(TotalLen-FracLen-1)))):
						if(ReturnVal=='None'): print("\nERROR: Value is too low, range from",(2**(TotalLen-FracLen)-(2**(TotalLen-FracLen-1))),"to",-(2**(TotalLen-FracLen)-(2**(TotalLen-FracLen-1)))," ( value:",val," index:",Values.index(val),")")
						return None
					num=(2**TotalLen)+(2**(TotalLen-FracLen))+int(val*(2**(TotalLen-(TotalLen-FracLen)))-(2**(TotalLen-FracLen)))
					#Check if value is less than minimal possible
					if(num==2**TotalLen):
						num=0
					hex_text=hex_text+("0x"+hex(num)[2:].zfill(int(TotalLen/4)))+","
					bin_text=bin_text+("0b"+bin(num)[2:].zfill(TotalLen))+","	
					dec_text=dec_text+Precision_txt.format(val)+","	
					if(ReturnVal!='None'): 
						dec_vals.append(val)

		#If unsigned
		else:
			for val in Values:
				#Check if it is positive value
				if(val<0):
					if(ReturnVal=='None'): print("\nERROR: Negative value ( value:",val," index:",Values.index(val),")")
					return None
				if(val>2**(TotalLen-FracLen)):
					if(ReturnVal=='None'): print("\nERROR: Value is too high ( value:",val," index:",Values.index(val),")")
					return None
				num=math.ceil(val*(2**(TotalLen-(TotalLen-FracLen)))-1)
				hex_text=hex_text+("0x"+hex(num)[2:].zfill(int(TotalLen/4)))+","
				bin_text=bin_text+("0b"+bin(num)[2:].zfill(TotalLen))+","	
				dec_text=dec_text+Precision_txt.format(val)+","
				if(ReturnVal!='None'): 
					dec_vals.append(round(val,Precision))
			
		#Output Values
		if(ReturnVal=='None'):
			print("\n-Dec Values:",dec_text[:-1])
			print("\n-Hex Values:",hex_text[:-1])
			print("\n-Bin Values:",bin_text[:-1])

		#Returning values
		if(ReturnVal=='Dec'): return dec_vals
		elif(ReturnVal=='Hex'): return hex_text[:-1]
		elif(ReturnVal=='Bin'): return bin_text[:-1]

	#Hex or Bin
	else:
		#Check if it is signed
		if(Signed):
			for val in Values:
				if(val<1 and val!=0):
					if(ReturnVal=='None'): print("\nERROR: Wrong input Value, change the conversion type ( value:",val," index:",Values.index(val),")")
					return None
				#Check if it is positive value
				if(val<(2**(TotalLen-1))):
					dec_text=dec_text+Precision_txt.format(val/(2**(TotalLen-(TotalLen-FracLen))))+","
					if(ReturnVal!='None'): dec_vals.append(round((val/(2**(TotalLen-(TotalLen-FracLen)))),Precision))
				else:
					dec_text=dec_text+Precision_txt.format(val/(2**(TotalLen-(TotalLen-FracLen)))-(2**(TotalLen-FracLen)))+","
					if(ReturnVal!='None'):  dec_vals.append(round((val/(2**(TotalLen-(TotalLen-FracLen)))-(2**(TotalLen-FracLen))),Precision))
				hex_text=hex_text+("0x"+hex(val)[2:].zfill(int(TotalLen/4)))+","
				bin_text=bin_text+("0b"+bin(val)[2:].zfill(TotalLen))+","
		#If unsigned
		else:
			for val in Values:
				if(val<1 and val!=0):
					if(ReturnVal=='None'): print("\nERROR: Wrong input Value, change the conversion type ( value:",val," index:",Values.index(val),")")
					return None
				dec_text=dec_text+Precision_txt.format(val/(2**(TotalLen-(TotalLen-FracLen))))+","
				hex_text=hex_text+("0x"+hex(val)[2:].zfill(int(TotalLen/4)))+","
				bin_text=bin_text+("0b"+bin(val)[2:].zfill(TotalLen))+","
				if(ReturnVal!='None'): 
					dec_vals.append(round((val/(2**(TotalLen-(TotalLen-FracLen)))),Precision))

		#Output Values
		if(ReturnVal=='None'):
			print("\n-Bin Values:",bin_text[:-1])
			print("\n-Hex Values:",hex_text[:-1])
			print("\n-Dec Values:",dec_text[:-1])

		#Returning values
		if(ReturnVal=='Dec'): return dec_vals
		elif(ReturnVal=='Hex'): return hex_text[:-1]
		elif(ReturnVal=='Bin'): return bin_text[:-1]


######### Examples #########

'''
1st Example:
	1 dec input, signed, 64 bit total, 63 bit fractional
'''
#fi(-0.000000000123453411323,1,64,63)
#input("\nPress ENTER to close...")

'''
2nd Example:
	128 hex input, signed, 32 bit total, 31 bit fractional, return decimal values
'''
#input_values=[0x7fffffff,0x7fb7cef8,0x7b7a082f,0x79467c1c,0x771cfc11,0x74fd5a32,0x72e76976,0x70dafda1,0x6ed7eb40,0x6cde07a9,0x6aed28f2,0x690525f1,0x6725d639,0x654f1214,0x6380b283,0x61ba9137,0x5ffc8890,0x5e46739c,0x5c982e10,0x5af19445,0x5952833a,0x57bad88c,0x562a7275,0x54a12fc8,0x531eeff3,0x51a392f5,0x502ef961,0x4ec10457,0x4d599589,0x4bf88f2d,0x4a9dd406,0x49494759,0x47faccf0,0x46b24917,0x456fa094,0x4432b8ae,0x42fb7724,0x41c9c22c,0x409d8072,0x3f769917,0x3e54f3ad,0x3d387835,0x3c210f1d,0x3b0ea13f,0x3a0117e0,0x38f85cab,0x37f459b1,0x36f4f969,0x35fa26aa,0x3503ccac,0x3411d707,0x332431b0,0x323ac8f6,0x31558983,0x3074605a,0x2f973ad2,0x2ebe069b,0x2de8b1b5,0x2d172a74,0x2c495f7d,0x2b7f3fc2,0x2ab8ba85,0x29f5bf55,0x29363e09,0x287a26c5,0x27c169f2,0x270bf844,0x2659c2b2,0x25aaba79,0x24fed119,0x2455f853,0x23b0222a,0x230d40e3,0x226d46fd,0x21d02739,0x2135d492,0x209e4240,0x200963b3,0x1f772c96,0x1ee790cd,0x1e5a8472,0x1dcffbd5,0x1d47eb7c,0x1cc24822,0x1c3f06b5,0x1bbe1c54,0x1b3f7e52,0x1ac32232,0x1a48fda6,0x19d1068f,0x195b32fd,0x18e7792e,0x1875cf8b,0x18062ca9,0x17988749,0x172cd656,0x16c310e3,0x165b2e2e,0x15f5259b,0x1590eeb6,0x152e8132,0x14cdd4e8,0x146ee1d4,0x1411a01a,0x13b607ff,0x135c11ee,0x1303b672,0x12acee39,0x1257b212,0x1203faef,0x11b1c1df,0x11610014,0x1111aedb,0x10c3c7a3,0x107743f8,0x102c1d84,0x0fe24e0b,0x0f99cf71,0x0f529bb5,0x0f0cacf0,0x0ec7fd57,0x0e84873a,0x0e424501,0x0e013130,0x0dc14662,0x0d827f4c,0x0d44d6ba,0x0d084791]
#output_values=fi(input_values,1,32,31,0,ReturnVal='Dec')
#print(output_values)
#input("\nPress ENTER to close...")

'''
3rd Example:
	3 bin input, unsigned, 8 bits total, 0 bit fractional
'''
#input_values=[0b10000000,0b10101010,0b11111111]
#fi(input_values,0,8,0,0)
#input("\nPress ENTER to close...")