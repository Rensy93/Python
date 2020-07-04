import math


def get_data():
    xStr = input("Ge mig ett tal! enter for att avsluta.")
    tal = []
    while xStr != "":
        tal.append(float(xStr))
        xStr = input("Ge mig ett tal! enter for att avsluta.")
    return tal


def medel(tal):
    total = 0.0
    count = len(tal)
    for number in tal:
        total += number
    return total / count


def std(tal, medel):
    sum = 0
    for i in range(len(tal)):
        sum += (medel - tal[i]) ** 2
    std = sum / (len(tal) - 1)
    std = math.sqrt(std)
    return std


def main():
    tal = get_data()
    mede = medel(tal)
    st = std(tal, mede)
    print("Vi får medelvärdet {} \n standarddviationen {}".format(mede, st))

main()

# mean = meddelvärde
# median = mitten värdet i en sorterad nummer följd
# standards deviation = the amunt values tends to differ (see formlen på sidan 365)
