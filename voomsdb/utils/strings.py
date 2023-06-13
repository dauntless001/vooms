from django.utils.crypto import get_random_string

def generate_ref_no(amount=16):
    """generates random characters `amount` number of times"""
    return f"{get_random_string(amount)}"