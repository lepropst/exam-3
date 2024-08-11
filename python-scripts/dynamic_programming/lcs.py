from typing import List


def print_table(table):
    col_widths = [max(len(str(val)) for val in col) for col in zip(*table)]

    for row in table:
        for val, width in zip(row, col_widths):

            print(
                f"{val if val != None else "None":{width}} ", end=""
            )        
        print()
    print("--" * 15)


def lcs(A, B, m, n):
    table = [[0 for x in range(n)] for x in range(m)]
    b = [[None for x in range(n)] for x in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0  or j == 0 :
                table[i][j] = 0
                b[i][j] = None
                continue
            if A[i].lower() == B[j].lower():
                table[i][j] = table[i - 1][j - 1] + 1
                b[i][j] = "northwest"
            elif A[i].lower() != B[j].lower():
                if table[i - 1][j] >= table[i][j - 1]:
                    table[i][j] = table[i - 1][j]
                    b[i][j] = "north"
                else:
                    table[i][j] = table[i][j - 1]
                    b[i][j] = "west"
        
        print("COMPUTING", A[i-1])
        print_table(table
        )

    col_widths = [max(len(str(val)) for val in col) for col in zip(*table)]
    print_table(table)
    print_table(b)
    return table, b


def determinelcs(b, X, i, j, lcs: List = list()):

    if i == 0 or j == 0:
        lcs.reverse()
        print("PRINTING LCS", lcs)
        return lcs
    if b[i - 1][j - 1] == "northwest":

        lcs.append(X[i - 1])
        determinelcs(b, X, i - 1, j - 1, lcs)
    elif b[i - 1][j - 1] == "north":

        determinelcs(b, X, i - 1, j, lcs)
    else:

        determinelcs(b, X, i, j - 1, lcs)
    return lcs


table, b = lcs("DDBABC","ADBDAAC", len("DDBABC"), len("ADBDAAC"))

lcs = determinelcs(b=b, X=[x for x in "DDBABC"], i=len(b)-1, j=len(b[0])-1)
print(lcs)
