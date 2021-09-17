def raise_exception():
    """Raise exceptie RuntimeError"""
    raise RuntimeError
    pass


def raise_exception_on_negative(x):
    """Raise exceptie RuntimeError als negatieve parameter x"""
    if x < 0:
        raise RuntimeError
    pass


def raise_exception_with_message():
    """Raise a RuntimeError exception met boodschap 'rare boel'"""
    raise RuntimeError("rare boel")


def handle_exception(x, y):
    """Geef x gedeeld door y terug

    Als y 0 is krijg je een ZeroDivisionError exceptie, verwerk deze
    met try/except en geef dan None terug.
    """
    try:
        if y == 0:
            raise RuntimeError
        div = x/y
        return div
    except RuntimeError:
        return None


class TooLazyError(RuntimeError):
    pass
def raise_custom_exception():
    """Raise a TooLazyError exception"""
    raise TooLazyError  


class TooTiredError(RuntimeError):
    pass
def raise_custom_exception_with_message():
    """Raise a TooTiredError exception with message 'te moe'"""
    raise TooTiredError


class HeightError(RuntimeError):
    pass
class WeightError(RuntimeError):
    pass
def calculate_bmi(weight, height):
    """Return the BMI

    Raise WeightError if weight <= 0
    Raise HeightError with message "lengte is 0" if height is zero
    """
    if height == 0:
        raise HeightError
    if weight <= 0:
        raise WeightError
    bmi = weight / height ** 2
    return bmi



class AgeNegativeError(RuntimeError):
    pass
class AgeTooHighError(RuntimeError):
    pass
def maximum_heartrate(age):
    """Return the maximum heartrate

    The maximum heartrate is given as 220 - age.

    Raise AgeNegativeError if age < 0
    Raise AgeTooHighError if age > 140 with message "oudste mens ooit werd 122"
    """
    
    if age < 0:
        raise AgeNegativeError
    if age > 140:
        raise AgeTooHighError

    heartrate = 220 - age
    return heartrate



