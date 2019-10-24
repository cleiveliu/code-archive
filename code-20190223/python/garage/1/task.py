def main():
    salary_records = []
    salary_records = loadData(salary_records)
    command = input("Command:")
    while command != "Quit":
        if command == "Print":
            printSalaryRecords(salary_records)
        elif command == "Total":
            totalSalaryPaid(salary_records)
        elif command == "TotalEach":
            totalSalaryForEach(salary_records)
        elif command == "WhoIsMax":
            maxTotalSalary(salary_records)
        elif command == "MaxEach":
            maxTotalSalaryForEach(salary_records)
        elif command == "Sort":
            sortRecords(salary_records)
        else:
            print("Please input a valid command!")
        command = input("Command:")
    print("BYE")


def loadData(salary_records):
    if len(salary_records) == 0:
        salary_records = "Assignment3-DataFile.txt"
    assert isinstance(salary_records, str)
    try:
        with open(salary_records, "r") as f:
            lines = f.readlines()
        res = []
        for line in lines:
            tem = line.split()
            res.append(tem[:1] + list(map(int, tem[1:])))
    except BaseException:
        print("not supported file or file don't exist")

    return res


def printSalaryRecords(salary_records):
    print(
        "Name \t Jan \t Feb \t Mar \t Apr \t May \t Jun \t Jul \t Aug \t Sep \t Oct \t Nov \t Dec"
    )
    for salary_record in salary_records:
        printOneLine(salary_record)


def totalSalaryPaid(salary_records):
    totalSalary = sum(sum(salary_record[1:])
                      for salary_record in salary_records)
    print(f"Total salary paid: {totalSalary}")


def totalSalaryForEach(salary_records):
    name = input("Which staff?")
    for staff in salary_records:
        if name == staff[0]:
            print(f"{staff[0]} earns {sum(staff[1:])}")
            return
    print(f"{name} not found")


def maxTotalSalary(salary_records):
    highestSalary = []
    for staff in salary_records:
        if len(highestSalary) == 0:
            highestSalary.append([staff[0], sum(staff[1:])])

        elif sum(staff[1:]) > highestSalary[0][1]:
            highestSalary = [[staff[0], sum(staff[1:])]]
        elif sum(staff[1:]) == highestSalary[0][1]:
            highestSalary.append([staff[0], sum(staff[1:])])
    if len(highestSalary) == 1:
        print(f"{highestSalary[0][0]} earn(s) the most")
    elif len(highestSalary) == 2:
        print(
            f"{' and '.join((staff[0] for staff in highestSalary))} earn(s) the most")
    else:
        print(
            f"{', '.join((staff[0] for staff in highestSalary[:-1]))} and {highestSalary[-1][0]} earn(s) the most"
        )


def maxTotalSalaryForEach(salary_records):
    months = "January February March April May June July August September October November December".split()
    name = input("Which staff?")
    for staff in salary_records:
        if staff[0] == name:
            highestSalaryMonth = []
            for i, salary in enumerate(staff[1:]):
                if len(highestSalaryMonth) == 0:
                    highestSalaryMonth.append([months[i], salary])
                elif salary > highestSalaryMonth[0][1]:
                    highestSalaryMonth = [[months[i], salary]]
                elif salary == highestSalaryMonth[0][1]:
                    highestSalaryMonth.append([months[i], salary])
            if len(highestSalaryMonth) == 1:
                print(f"{name} earns the most in {highestSalaryMonth[0][0]}")
            elif len(highestSalaryMonth) == 2:
                print(
                    f"{name} earns the most in {highestSalaryMonth[0][0]} and {highestSalaryMonth[1][0]}"
                )
            else:
                print(
                    f"{name} earns the most in {', '.join((month[0] for month in highestSalaryMonth[:-1]))} and {highestSalaryMonth[-1][0]}"
                )
            return
    print(f"{name} not found")


def sortRecords(salary_records):
    dic = {}
    for staff in salary_records:
        dic[staff[0]] = sum(staff[1:])
    dic = sorted(dic.items(), key=lambda x: (x[1], x[0]))
    for staff in dic:
        name, salary = staff
        print(f"{name} {salary}")


def printOneLine(salary_record):
    put_str = "\t".join(map(str, salary_record))
    put_str += "\t\n"
    print(put_str, end="")


main()
