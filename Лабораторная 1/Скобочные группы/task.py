def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    stack = list()
    is_god = True
    for val in brackets_row:

        if val in "(":
            stack.append(val)

        elif val in ")":
            if not stack:
                is_god = False
                break
            open_stack = stack.pop()
            if open_stack == "(" and ")":
                continue
            is_god = False
            break

    if is_god and len(stack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
