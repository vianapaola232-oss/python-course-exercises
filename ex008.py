distance = float(input("Enter a distance in meters: "))

centimeters = distance * 100
millimeters = distance * 1000
kilometers = distance / 1000
hectometers = distance / 100
decameters = distance / 10
decimeters = distance * 10


print(f"""A distance of {distance:.1f} meters corresponds to 
{centimeters:g} cm 
{millimeters:g} mm
{kilometers:g} km
{hectometers:g} hm
{decameters:g} dam
{decimeters:g} dm""")
print("-=" * 30)
