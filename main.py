##############################################################################
#                                                                            #
#                         Python Fixed Point Main                            #
#                                                                            #
##############################################################################

from pyfi import fi

def simple_call():
    """
    Example usage of the PyFi library just printing on terminal.
    """
    # Converting float list to fixed
    fi_obj = fi()
    fi_obj([0.9,-0.9])

    # Converting fixed to float
    fi_obj.fixed = False
    fi_obj(0x73333333)

def precision_loss():
    """
    Using PyFi to estimate precision loss for fixed point multiplications.
    """
    # Creating the FI class and changing format to Q15
    fi_obj = fi()
    fi_obj.word_len = 16
    fi_obj.frac_len = 15
#     fi_obj.return_val = True
    fi_obj.return_val = False
    
    # Multiplying the value one in a loop to check precision loss
    value = 1.0
    iterations = 100
    fi_obj(value)

    fi_obj.fixed = False
    fi_obj(0x7FFF)
    print(0x7FFF)
#     for i in range(iterations):
#         fixed_value = fi_obj(value)
        



if __name__ == "__main__":
    print("---------- PyFi Examples ----------")
    print("1: ",simple_call.__doc__)
    simple_call()
    print("\n\n2: ",precision_loss.__doc__)
    precision_loss()

