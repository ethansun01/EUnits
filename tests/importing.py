import eunits

density = eunits.Quantity(1.1, 'g cm^-3')
velocity = eunits.Quantity(0.5, 'm s^-1')
diameter = eunits.Quantity(0.25, 'm')
viscosity = eunits.Quantity(3,'cP')

Re = density * velocity * diameter / viscosity
print(round(Re,3))
print(Re.as_base())
