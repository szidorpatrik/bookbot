def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)

def get_character_count(text: str) -> dict[str, int]:
    result = {}
    for char in text:
        character = char.lower()
        
        if not character.isalpha():
            continue
        
        if character not in result:
            result[character] = 0
            
        result[character] += 1
        
    return result

def sort_on(items):
    return items["num"]

def get_report(char_count: dict[str, int]) -> str:
    report = []
    chars = []
    
    for char, count in char_count.items():
        chars.append({"char": char, "num": count})
    
    chars.sort(reverse = True, key=sort_on)
    for item in chars:
        report.append(f"{item["char"]}: {item["num"]}")
        
    return "\n".join(report)
