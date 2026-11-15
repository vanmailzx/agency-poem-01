from pathlib import Path


def main():
    poem_path = Path(__file__).resolve().parent / "poem-final.md"
    print(poem_path.read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    main()
