def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    guess_text = raw.strip()
    if guess_text == "":
        return False, None, "Enter a guess."

    try:
        if "." in guess_text:
            value = int(float(guess_text))
        else:
            value = int(guess_text)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return an outcome string.

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win"

    try:
        if guess > secret:
            return "Too High"
        return "Too Low"
    except TypeError:
        guess_text = str(guess)
        secret_text = str(secret)
        if guess_text == secret_text:
            return "Win"
        if guess_text > secret_text:
            return "Too High"
        return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    if outcome in {"Too High", "Too Low"}:
        return max(0, current_score - 5)

    return current_score
