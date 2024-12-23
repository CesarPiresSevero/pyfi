##############################################################################
#                                                                            #
#                         Python Fixed Point                                 #
#                                                                            #
##############################################################################

import math


class fi:
    """
    Fixed Point class holding information about fixed point format used

    Attributes
    ----------
        signed : bool
            Signedess (signed or unsigned)
        word_len : int
            Number of bits used to represent the value
        frac_len : int
            Fractional bits (mantissa)
        fixed: bool, optional
            Format used for convertion
                True = Floating to fixed point
                False = Fixed to floating point 
        return_val: bool, optional
            Selects type of output, return values or print
            on the console
    Methods
    -------
        _convert_to_fixed(values):
            Helper function to convert values from float to fixed
        _convert_to_float(values):
            Helper function to convert values from fixed to float
        __call__(value):
            Prints or returns the value converted to desired format
    """
    
    # Class constructor
    def __init__(self, signed=True, word_len=32, frac_len=31, 
            fixed=True, return_val=False):
        """
        Sets default word and fractional bits checking inputs

        Parameters
        ----------
            signed : bool, optional
                Signedess (signed or unsigned)
            word_len : int, optional
                Number of bits used to represent the value
            frac_len : int, optional
                Fractional bits (mantissa)
            fixed: bool, optional
                Format used for convertion.
                True = Floating to fixed point
                False = Fixed to floating point 
            return_val: bool, optional
                Selects type of output, return values or print
                on the console
        """

        self._signed = signed
        self._word_len = word_len
        _bits = self._word_len
        if(self._signed == True):
            _bits -= 1
        if(frac_len <= _bits):
            self._frac_len = frac_len
        self._fixed = fixed
        self._return_val = return_val
        
    # Signed getter and setter
    @property
    def signed(self):
        return self._signed

    @signed.setter
    def signed(self, value):
        if(type(value) == bool):
            self._signed = value

    # Word length getter and setter
    @property
    def word_len(self):
        return self._word_len

    @word_len.setter
    def wordl_len(self, value):
        self._word_len = value

    # Fractional length getter and setter
    @property
    def frac_len(self):
        return self._frac_len

    @frac_len.setter
    def frac_len(self, value):
        _bits = self._word_len
        if(self._signed == True):
            _bits -= 1
        if(value <= _bits):
            self._frac_len = value

    # Format (fixed/float) getter and setter
    @property
    def fixed(self):
        return self._fixed

    @fixed.setter
    def fixed(self, value):
        if(type(value) == bool):
            self._fixed = value
    
    # Return value getter and setter
    @property
    def return_val(self):
        return self._return_val

    @return_val.setter
    def return_val(self, value):
        if(type(value) == bool):
            self._return_val = value
    
    # Converts input float values to fixed point
    def _convert_to_fixed(self, values):
        """
        Helper function to convert floating values into fixed point

        Parameters
        ----------
        value : list
            List of floats to be converted to fixed point

        Returns
        -------
        Dictionary with:
            out_vals: list of fixed point integers
            dec_text: string with decimal representation
            hex_text: string with hexadecimal representation
            bin_text: string with binary representation
        """

        # Local variables
        dec_text = ""
        hex_text = ""
        bin_text = ""
        out_vals = []

        #Calculating fractional digits to represent floats
        precision = math.ceil(frac_len/3)
        precision_txt = "{:."+str(precision)+"f}"

        #Check if it is signed
        if(signed):
            for val in values:
                #Check if it is positive value
                if(val>0):
                    dec_text=dec_text+precision_txt.format(val)+","
                    #Check if value is above the limit
                    if(val>(2**(word_len-frac_len)-(2**(word_len-frac_len-1)))):
                        if(return_val=='None'): print("\nERROR: Value is too high, range from",(2**(word_len-frac_len)-(2**(word_len-frac_len-1))),"to",-(2**(word_len-frac_len)-(2**(word_len-frac_len-1)))," ( value:",val," index:",values.index(val),")")
                        return None
                    elif(val==(2**(word_len-frac_len)-(2**(word_len-frac_len-1)))):
                        if(return_val=='None'): print("WARNING:",(2**(word_len-frac_len)-(2**(word_len-frac_len-1))),"can not be represented,",round(((2**(word_len-frac_len)-(2**(word_len-frac_len-1)))-1/(2**word_len)),precision),"will be used instead","( index:",values.index(val),")")
                        val=(2**(word_len-frac_len)-(2**(word_len-frac_len-1)))-1/(2**word_len)
                        dec_text=''
                        dec_text=dec_text+precision_txt.format(val)+","
                    num=math.ceil(val*(2**(word_len-(word_len-frac_len))))
                    if(num>=(2**word_len)/2): num=num-1
                    #Check if value is less than minimal possible
                    if(num<=0):
                        num=0
                    hex_text=hex_text+("0x"+hex(num)[2:].zfill(int(word_len/4)))+","
                    bin_text=bin_text+("0b"+bin(num)[2:].zfill(word_len))+","   
                    if(return_val!='None'): 
                        out_vals.append(val)                            
                #If negative
                else:
                    #Check if value is above the limit
                    if((-1)*val>(2**(word_len-frac_len)-(2**(word_len-frac_len-1)))):
                        if(return_val=='None'): print("\nERROR: Value is too low, range from",(2**(word_len-frac_len)-(2**(word_len-frac_len-1))),"to",-(2**(word_len-frac_len)-(2**(word_len-frac_len-1)))," ( value:",val," index:",values.index(val),")")
                        return None
                    num=(2**word_len)+(2**(word_len-frac_len))+int(val*(2**(word_len-(word_len-frac_len)))-(2**(word_len-frac_len)))
                    #Check if value is less than minimal possible
                    if(num==2**word_len):
                        num=0
                    hex_text=hex_text+("0x"+hex(num)[2:].zfill(int(word_len/4)))+","
                    bin_text=bin_text+("0b"+bin(num)[2:].zfill(word_len))+","   
                    dec_text=dec_text+precision_txt.format(val)+"," 
                    if(return_val!='None'): 
                        out_vals.append(val)

        #If unsigned
        else:
            for val in values:
                #Check if it is positive value
                if(val<0):
                    if(return_val=='None'): print("\nERROR: Negative value ( value:",val," index:",values.index(val),")")
                    return None
                if(val>2**(word_len-frac_len)):
                    if(return_val=='None'): print("\nERROR: Value is too high ( value:",val," index:",values.index(val),")")
                    return None
                num=math.ceil(val*(2**(word_len-(word_len-frac_len)))-1)
                hex_text=hex_text+("0x"+hex(num)[2:].zfill(int(word_len/4)))+","
                bin_text=bin_text+("0b"+bin(num)[2:].zfill(word_len))+","   
                dec_text=dec_text+precision_txt.format(val)+","
                if(return_val!='None'): 
                    out_vals.append(round(val,precision))
            
        #Output values
        if(return_val=='None'):
            print("\n-Dec values:",dec_text[:-1])
            print("\n-Hex values:",hex_text[:-1])
            print("\n-Bin values:",bin_text[:-1])

        #Returning values
        if(return_val=='Dec'): return out_vals
        elif(return_val=='Hex'): return hex_text[:-1]
        elif(return_val=='Bin'): return bin_text[:-1]

    # Converts input fixed values to floating point
    def _convert_to_float(self, values):
        """
        Helper function to convert fixed point values into floating point

        Parameters
        ----------
        value : list
            List of fixed to be converted to floating point

        Returns
        -------
        Dictionary with:
            out_vals: list of floating point values (float)
            dec_text: string with decimal representation
            hex_text: string with hexadecimal representation
            bin_text: string with binary representation
        """

        # Local variables
        dec_text = ""
        hex_text = ""
        bin_text = ""
        out_vals = []

        #Calculating fractional digits to represent floats
        precision = math.ceil(frac_len/3)
        precision_txt = "{:."+str(precision)+"f}"

        #Check if it is signed
        if(signed):
            for val in values:
                if(val<1 and val!=0):
                    if(return_val=='None'): print("\nERROR: Wrong input Value, change the conversion type ( value:",val," index:",values.index(val),")")
                    return None
                #Check if it is positive value
                if(val<(2**(word_len-1))):
                    dec_text=dec_text+precision_txt.format(val/(2**(word_len-(word_len-frac_len))))+","
                    if(return_val!='None'): out_vals.append(round((val/(2**(word_len-(word_len-frac_len)))),precision))
                else:
                    dec_text=dec_text+precision_txt.format(val/(2**(word_len-(word_len-frac_len)))-(2**(word_len-frac_len)))+","
                    if(return_val!='None'):  out_vals.append(round((val/(2**(word_len-(word_len-frac_len)))-(2**(word_len-frac_len))),precision))
                hex_text=hex_text+("0x"+hex(val)[2:].zfill(int(word_len/4)))+","
                bin_text=bin_text+("0b"+bin(val)[2:].zfill(word_len))+","
        #If unsigned
        else:
            for val in values:
                if(val<1 and val!=0):
                    if(return_val=='None'): print("\nERROR: Wrong input Value, change the conversion type ( value:",val," index:",values.index(val),")")
                    return None
                dec_text=dec_text+precision_txt.format(val/(2**(word_len-(word_len-frac_len))))+","
                hex_text=hex_text+("0x"+hex(val)[2:].zfill(int(word_len/4)))+","
                bin_text=bin_text+("0b"+bin(val)[2:].zfill(word_len))+","
                if(return_val!='None'): 
                    out_vals.append(round((val/(2**(word_len-(word_len-frac_len)))),precision))

        #Output values
        if(return_val=='None'):
            print("\n-Bin values:",bin_text[:-1])
            print("\n-Hex values:",hex_text[:-1])
            print("\n-Dec values:",dec_text[:-1])

        #Returning values
        if(return_val=='Dec'): return out_vals
        elif(return_val=='Hex'): return hex_text[:-1]
        elif(return_val=='Bin'): return bin_text[:-1]

    # Class call method
    def __call__(self, value):
        """
        Prints the desired conversion based on class properties.
        Use this function for visual conversion on terminal.

        Parameters
        ----------
        value : list,float,int
            The value to be converted. It supports a list of floats,
            a list of integers, a float or a integer.

        Returns
        -------
        None
        """

        # Printing header if return_val is False
        if not self._return_val:
            print("\nPYTHON FIXED POINT CONVERTER\n")
            if(self._fixed):
                print("-Type of conversion:","Floating to fixed point")
            else: 
                print("-Type of conversion:","Fixed to floating point")
            if(self._signed): 
                print("-Signedness:","Signed")
            else: 
                print("-Signedness:","Unsigned")
            print("-Total bits:", self._word_len)
            print("-Fractional bits:", self._frac_len)
            print("-Exponent bits:", self._word_len-self._frac_len)


        #Converting input type to list
        if(type(value) == int or type(value) == float):
            values = [value]
        else:
            values = value

        return 0
        # Float to fixed point conversion
        if(self._fixed):
            converted_values = self._convert_to_fixed(values)
        # Fixed to floating point conversion
        else:
            converted_values = self._convert_to_float(values)


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
#output_values=fi(input_values,1,32,31,0,return_val='Dec')
#print(output_values)
#input("\nPress ENTER to close...")

'''
3rd Example:
    3 bin input, unsigned, 8 bits total, 0 bit fractional
'''
#input_values=[0b10000000,0b10101010,0b11111111]
#fi(input_values,0,8,0,0)
#input("\nPress ENTER to close...")

