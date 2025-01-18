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
    fi_obj([1.0, -0.5])

    # Converting fixed to float
    fi_obj.fixed = False
    fi_obj(0xdeadbeef)


def precision_loss():
    """
    Using PyFi to estimate precision loss for fixed point multiplications.
    """
    # Creating the FI class and changing format to Q15
    fi_obj = fi()
    fi_obj.word_len = 16
    fi_obj.frac_len = 15
    fi_obj.return_val = True

    # Multiplying the value one in a loop to check precision loss
    initial_value = 1.0
    value = initial_value
    iterations = 20
    print("Multiplying", value, "(16 bit signed) by itself",
          iterations, "times:")
    for i in range(iterations):
        fi_obj.fixed = True
        fixed_value = fi_obj(value)
        fi_obj.fixed = False
        float_value = fi_obj(fixed_value)
        value *= float_value
        print(i+1, ":", round(value, 6))

    # Calculating final error
    error = ((value - initial_value)/initial_value) * 100
    print("Final error =", round(error, 2), "%")


if __name__ == "__main__":
    print(100 * "-")
    print("-", 35 * " ", "PyFi Examples", 46 * " ", "-")
    print(100 * "-")
    print("1: ", simple_call.__doc__)
    simple_call()
    print(100 * "-")
    print("2: ", precision_loss.__doc__)
    precision_loss()
    print(100 * "-")
