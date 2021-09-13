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
    raise RuntimeError
    try:
        pass
    except RuntimeError:
        print("rare boel")


def handle_exception(x, y):
    """Geef x gedeeld door y terug

    Als y 0 is krijg je een ZeroDivisionError exceptie, verwerk deze
    met try/except en geef dan None terug.
    """
    pass


def raise_custom_exception():
    """Raise a TooLazyError exception"""
    pass


def raise_custom_exception_with_message():
    """Raise a TooTiredError exception with message 'te moe'"""
    pass


def calculate_bmi(weight, height):
    """Return the BMI

    Raise WeightError if weight <= 0
    Raise HeightError with message "lengte is 0" if height is zero
    """
    pass


def maximum_heartrate(age):
    """Return the maximum heartrate

    The maximum heartrate is given as 220 - age.

    Raise AgeNegativeError if age < 0
    Raise AgeTooHighError if age > 140 with message "oudste mens ooit werd 122"
    """
    pass
