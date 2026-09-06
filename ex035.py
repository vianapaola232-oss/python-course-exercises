print("-=" * 30)
print(f"{'TRIANGLE ANALYZER':^60}")
print("-=" * 30)
first_segment = float(input("Please enter the first segment: "))
second_segment = float(input("Please enter the second segment: "))
third_segment = float(input("Please enter the third segment: "))
if (first_segment + second_segment) <= third_segment or \
   (first_segment + third_segment) <= second_segment or \
   (third_segment + second_segment) <= first_segment:
    print("These three segments can't form a triangle.")
else:
    print("These three segments can form a triangle.")
