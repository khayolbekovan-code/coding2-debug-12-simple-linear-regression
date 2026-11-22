"""Display your Homework 1 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "ee36f0e8f40fe7197e3aad3568217d37"
GRADE_HASH = "b441976b0ae5b2c4135aa68a9f4e1dbe959270db060d981417395aed9d6caa3c"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 1: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
