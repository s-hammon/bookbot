from typing import Dict, List


def word_count(text: str) -> int:
    tokens = text.split()
    return len(tokens)


def character_freq(text: str) -> Dict[str, int]:
    map: Dict[str, int] = {}
    for c in text:
        c = c.lower()
        if map.get(c):
            map[c] += 1
        else:
            map[c] = 1
    return map


def char_list(m_char: Dict[str, int]) -> List[dict]:
    chars = []
    for k, v in m_char.items():
        chars.append({"char": k, "num": v})
    chars.sort(reverse=True, key=sort_on)
    return chars


def sort_on(items) -> int:
    return items["num"]
