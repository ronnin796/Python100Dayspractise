import random
from pathlib import Path

from PYTHONCODES.sendmail import send_mail


def load_random_quote(quotes_file_path: Path) -> str:
    with open(quotes_file_path) as file:
        quotes = file.readlines()
    return random.choice(quotes).strip()


load_random_quote(Path(__file__).parent / "quotes.txt")

if __name__ == "__main__":
    quotes_path = Path(__file__).parent / "quotes.txt"
    quote = load_random_quote(quotes_path)

    send_mail(
        subject="Motivation Quote",
        body=f"Motivational Quote of the Day: {quote}",
    )
