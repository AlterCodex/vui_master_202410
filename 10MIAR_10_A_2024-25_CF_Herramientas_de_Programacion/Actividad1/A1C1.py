def FirstChar(variable_name: str) -> bool:
    if variable_name:
        first_char = variable_name[0]
        return first_char.isalpha() or first_char == '_'
    return False

