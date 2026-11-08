def kira_purata(markah):
    return sum(markah) / len(markah)

def tentukan_gred(markah):
    if markah >= 80:
        return "A"
    elif markah >= 70:
        return "B"
    elif markah >= 60:
        return "C"
    elif markah >= 50:
        return "D"
    elif markah >= 40:
        return "E"
    else:
        return "F"
