# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# limit operations to the 4 basic ones for now (+, -, *, /)
operations = ["+", "-", "*", "/"]
input_numbers = [5, 1, 1, 8]

def solve():
    # initiate dp
    dp = [{}, {}, {}, {}, {}]

    copy_of_dp

    # output
    print(dp_helper(0, dp, "", 0))


def dp_helper(index, dp, op_list, cur_number):
    print(index, cur_number, "\n")
    if index >= 4:
        if cur_number == 24:
            dp[index][cur_number] = op_list
        else:
            dp[index][cur_number] = "."

        return dp[index][cur_number]

    if dp[index].get(cur_number) is not None:
        return dp[index][cur_number]

    for operation in operations:
        evaluated = eval(str(cur_number) + operation + str(input_numbers[index]))

        dp[index][cur_number] = dp_helper(index+1, dp, op_list + operation, evaluated)
        if dp[index][cur_number] != ".":
            break

    if dp[index].get(cur_number) is None:
        dp[index][cur_number] = "."

    return dp[index][cur_number]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solve()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
