"""Count vowels in strings (Python).

Includes an `extended` option to normalize Unicode and count accented vowels
as base vowels.
"""
from typing import Optional
import unicodedata


def count_vowels(s: str, extended: bool = True) -> int:
    """Count vowels in a string.

    Args:
        s: input string
        extended: if True, normalize Unicode (NFD) and treat accented vowels as
                  their base (e.g. é -> e). If False, count ASCII vowels only.

    Returns:
        Number of vowels (int)
    """
    if not isinstance(s, str):
        raise TypeError("s must be a string")

    vowels = set("aeiou")
    if extended:
        normalized = unicodedata.normalize("NFD", s)
        count = 0
        for ch in normalized:
            if unicodedata.category(ch) == "Mn":
                continue
            if ch.lower() in vowels:
                count += 1
        return count

    return sum(1 for ch in s.lower() if ch in vowels)


if __name__ == "__main__":
    examples = [
        ("Hello, World!", False),
        ("Résumé", True),
        ("ÁÉÍÓÚáéíóú", True),
        ("", True),
    ]
    for text, ext in examples:
        print(repr(text), "extended=", ext, "->", count_vowels(text, extended=ext))
