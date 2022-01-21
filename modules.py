def tamgiac(canhA, canhB, canhC):
    if canhA + canhB > canhC and canhA + canhC > canhB and canhB + canhC > canhA:
        return True


def tamgiacVuong(canhA, canhB, canhC):
    # function name
    if (
        canhA * canhA == (canhB * canhB + canhC * canhC)
        or canhB * canhB == (canhA * canhA + canhC * canhC)
        or canhC * canhC == (canhA * canhA + canhB * canhB)
    ):
        return True


def tamgiacVuongCan(canhA, canhB, canhC):
    if tamgiacVuong(canhA, canhB, canhC) and tamgiacCan(canhA, canhB, canhC):
        return True


def tamgiacCan(canhA, canhB, canhC):
    if ((canhA == canhB) or (canhB == canhC) or (canhC == canhA)) and not tamgiacDeu(
        canhA, canhB, canhC
    ):
        return True


def tamgiacDeu(canhA, canhB, canhC):
    if canhA == canhB == canhC:
        return True


def TamGiac():

    canhA = float(input("Cạnh A: "))
    canhB = float(input("Cạnh B: "))
    canhC = float(input("Cạnh C: "))

    if tamgiac(canhA, canhB, canhC):
        functions = [tamgiacVuongCan, tamgiacVuong, tamgiacCan, tamgiacDeu]

        # loop through all functions
        for function in functions:
            result = function(canhA, canhB, canhC)
            if result != False and result != None:
                print(f"{function.__name__}" + ": " + str(result))
                break
    else:
        print("Không phải tam giác.")


if __name__ == "__main__":
    TamGiac()
