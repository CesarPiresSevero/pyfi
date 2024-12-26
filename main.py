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
    print(fi.__doc__)

def precision_loss():
    """
    Using PyFi to estimate precision loss for fixed point multiplications.
    """
    pass


if __name__ == "__main__":
    print("---------- PyFi Examples ----------")
    print("1: ",simple_call.__doc__)
    simple_call()
    print("2: ",precision_loss.__doc__)
    precision_loss()

