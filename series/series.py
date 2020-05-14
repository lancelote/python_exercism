from typing import List


def slices(series: str, length: int) -> List[str]:
    if series == "":
        raise ValueError("empty series")
    if length <= 0:
        raise ValueError(f"positive length is expected, got {length}")
    if length > len(series):
        raise ValueError(f"length {length} is larger than series '{series}'")

    return [series[i : i + length] for i in range(len(series) - length + 1)]
