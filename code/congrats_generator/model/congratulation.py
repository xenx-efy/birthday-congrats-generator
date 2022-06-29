class Congratulation:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: str) -> None:
        self.parts.append(part)

    def list_parts(self) -> str:
        return "\n".join(self.parts)
