def parse_line(line: str) -> tuple[list[str], list[str]]:
    patterns, digits = line.split('|')
    return patterns.strip().split(), digits.strip().split()