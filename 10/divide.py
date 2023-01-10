def positive_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except (ZeroDivisionError):
        return 0
    except (TypeError):
        raise TypeError
    
    if result < 0:
        raise (ValueError)
    
    return result