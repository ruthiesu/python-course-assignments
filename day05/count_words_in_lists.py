celestial_objects = [
    'Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid'
]
my_map = {}

for obj in celestial_objects:
    if obj in my_map:
        my_map[obj] += 1
    else:
        my_map[obj] = 1

for key, value in my_map.items():
    print(f"{key:<8}  {value:>5}")