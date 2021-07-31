#miles = kilometres * 0.621371
#km = miles * 1.609


def kmToMiles():
    kilometres = int(input("Type how many km you'd like to convert to miles: "))
    miles = kilometres*0.621371
    return(f"That's {miles} miles")

def milesToKm():
    miles = int(input("Type how many miles you'd like to convert to km: "))
    kilometres = miles*1.609
    return(f"That's {kilometres} km")

user = input("Type m to convert miles, or type k to convert kilometres: ")
if user == "k":
    print(kmToMiles())
elif user == "m":
    print(milesToKm())