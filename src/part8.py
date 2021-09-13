def raise_exception():
    """Raise exceptie RuntimeError"""
    pass


def raise_exception_on_negative(x):
    """Raise exceptie RuntimeError als negatieve parameter x"""
    pass


def raise_exception_with_message():
    """Raise a RuntimeError exception met boodschap 'rare boel'"""
    pass


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
