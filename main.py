"""Ridiculous at First Glance, Real by the Second.

One sentence, at most 200 characters, pitching a bizarre startup idea
that sounds like a joke until the business logic lands: bottled silence,
recorded where it is genuinely quiet, sold to offices that cannot buy
quiet any other way. The turn is laugh-to-nod: "bottled silence" sounds
absurd, then the price ($9/month), the buyer (open-plan offices) and the
reason (headphones cannot cancel other people's meetings) make it a
real subscription business.
"""

import os

ENTRY = (
    "We sell bottled silence recorded in empty cathedrals to open-plan "
    "offices: $9 a month for an hour of genuine quiet, because headphones "
    "can't cancel your coworkers' meetings."
)


def main() -> None:
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert ENTRY.strip() == ENTRY
    assert ENTRY.count(".") == 1, "must be a single sentence"
    assert ENTRY.endswith("."), "pitch must end as a complete sentence"
    assert "\n" not in ENTRY, "pitch must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # No trailing newline: the file must hold exactly the pitch, byte for byte.


if __name__ == "__main__":
    main()
