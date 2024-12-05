from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),  # A must be either a knight or a knave
    Not(And(AKnight, AKnave)),  # A cannot be both
    Implication(AKnight, And(AKnight, AKnave)),  # If A is a knight, the statement must be true
    Implication(AKnave, Not(And(AKnight, AKnave)))  # If A is a knave, the statement is false
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Implication(AKnight, And(AKnave, BKnave)),  # If A is a knight, the statement is true
    Implication(AKnave, Not(And(AKnave, BKnave)))  # If A is a knave, the statement is false
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),  # A’s statement
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),  # A lies
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),  # B’s statement
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))  # B lies
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave."
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    Implication(AKnight, AKnight),  # A says "I am a knight."
    Implication(AKnave, AKnave),  # A says "I am a knave."
    Implication(BKnight, And(Implication(AKnight, AKnave), CKnave)),  # B’s statements
    Implication(BKnave, Not(And(Implication(AKnight, AKnave), CKnave))),
    Implication(CKnight, AKnight),  # C’s statement
    Implication(CKnave, Not(AKnight))
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        for symbol in symbols:
            if model_check(knowledge, symbol):
                print(f"    {symbol}")


if __name__ == "__main__":
    main()
