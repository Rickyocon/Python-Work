s1 = "Name: Great Exspectation price: $5.41";

# find the substring approach
idx = s1.find("$");
s2 = s1[idx+1 : len(s1)];
print("Book Price = " + s2);


# approach: split by $
arr = s1.split("$");
s3 = arr[1];
print("Book Price = " + s3);
