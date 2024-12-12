import bcrypt

def hash_pin(pin: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pin.encode('utf-8'), salt).decode('utf-8')

def verify_pin(pin: str, hashed_pin: str) -> bool:
    return bcrypt.checkpw(pin.encode('utf-8'), hashed_pin.encode('utf-8'))
