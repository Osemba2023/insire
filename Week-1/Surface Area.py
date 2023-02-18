# calculate the surface area of a sphere
pi= 3.142
r=input("Enter the radius of a sphere :")
surface_area_input=(4*pi*int(r)*int(r))
print(surface_area_input)

#calculate the surface area of a cylinder
pi= 3.142
r=input("Enter the radius of the cylinder :")
h=input("Enter the height of the cylinder")
surface_area_input=(2*pi*int(r)*int(r) + 2*pi*int(r)*int(h))
print(surface_area_input)

#calculate the volume of a sphere
pi= 3.142
r=input("Enter the radius of a sphere :")
volume_input=(4/3*pi*int(r)*int(r)*int(r))
print(volume_input)