def tamgiac(canhA, canhB, canhC):
    if canhA + canhB > canhC and canhA + canhC > canhB and canhB + canhC > canhA:
        return True


def tamgiacVuong(canhA, canhB, canhC):
    if (
        canhA * canhA == (canhB * canhB + canhC * canhC)
        or canhB * canhB == (canhA * canhA + canhC * canhC)
        or canhC * canhC == (canhA * canhA + canhB * canhB)
    ):
        return True
    else:
        return "Không phải tam giác vuông."


def tamgiacCan(canhA, canhB, canhC):
    if ((canhA == canhB) or (canhB == canhC) or (canhC == canhA)) and not tamgiacDeu(
        canhA, canhB, canhC
    ):
        return True
    else:
        return "Không phải tam giác cân."


def tamgiacDeu(canhA, canhB, canhC):
    if canhA == canhB == canhC:
        return True


def TamGiac():
    canhA = int(input("Cạnh A: "))
    canhB = int(input("Cạnh B: "))
    canhC = int(input("Cạnh C: "))

    if tamgiac(canhA, canhB, canhC):
        functions = [tamgiacVuong, tamgiacCan, tamgiacDeu]
        # loop through all functions
        for function in functions:
            result = function(canhA, canhB, canhC)
            if result == True:
                print(f"{function.__name__}" + ": " + str(result))
                break
            elif result == False:
                print(f"{function.__name__}" + ": " + "False")
    else:
        print("Không phải tam giác.")
