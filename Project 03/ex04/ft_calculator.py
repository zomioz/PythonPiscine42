class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        total = 0
        for x, y in zip(V1, V2):
            total = total + (x * y)
        print(total)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        print([x + y for x, y in zip(V1, V2)])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print([x - y for x, y in zip(V1, V2)])
