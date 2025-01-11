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
    pass


if __name__ == "__main__":
    print("---------- PyFi Examples ----------")
    print("1: ",simple_call.__doc__)
    simple_call()
    print("\n\n2: ",precision_loss.__doc__)
    precision_loss()

