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
    # A can be a Knight or a Knave, but not both
    And(Or(AKnight, AKnave)), Not(And(AKnight, AKnave)),

    # A says "I am both a knight and a knave"
    Biconditional(AKnight, And(AKnight, AKnave))        # A is Knight if and only if he tells the truth
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A can be a Knight or a Knave, but not both
    And(Or(AKnight, AKnave)), Not(And(AKnight, AKnave)),

    # B can be a Knight or a Knave, but not both
    And(Or(BKnight, BKnave)), Not(And(BKnight, BKnave)),

    # A says "We are both knaves"
    Biconditional(AKnight, And(AKnave, BKnave))       # A is Knight if and only if he tells the truth
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A can be a Knight or a Knave, but not both
    And(Or(AKnight, AKnave)), Not(And(AKnight, AKnave)),

    # B can be a Knight or a Knave, but not both
    And(Or(BKnight, BKnave)), Not(And(BKnight, BKnave)),

    # A says "We are the same kind."
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),

    #B says "We are of different kinds"
    Biconditional(BKnight, Or(And(AKnave, BKnight), And(AKnight, BKnave)))

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A can only be a Knight or a Knave but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),

    # B can only be a Knight or a Knave but not both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),

    # C can only be a Knight or a Knave but not both
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),        


    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Biconditional(AKnight, Or(AKnight, AKnave)),

    # B says "A said 'I am a knave'."
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),                 # B is Knight if A tells the truth

    # B says "C is a knave."
    Biconditional(BKnight, CKnave),

    # C says "A is a knight."
    Biconditional(CKnight, AKnight)
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
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
