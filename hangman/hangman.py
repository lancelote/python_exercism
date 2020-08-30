from typing import List

STATUS_ONGOING = 0
STATUS_LOSE = 1
STATUS_WIN = 2

Status = int


class Hangman:
    def __init__(self, word: str) -> None:
        self.found: List[str] = []
        self.word = word
        self.unique_chars = len(set(word))
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING

    def guess(self, char: str) -> None:
        if self.remaining_guesses < -1:
            raise ValueError("no more guesses")
        if self.status in [STATUS_WIN, STATUS_LOSE]:
            raise ValueError("the game is finished")

        if char not in self.word or char in self.found:
            self.remaining_guesses -= 1
        else:
            self.found.append(char)

        if len(self.found) == self.unique_chars:
            self.status = STATUS_WIN
        if self.remaining_guesses == -1:
            self.status = STATUS_LOSE

    def get_masked_word(self) -> str:
        return "".join(x if x in self.found else "_" for x in self.word)

    def get_status(self) -> Status:
        return self.status
