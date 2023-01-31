def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    mycity = set(my_cities)
    othercity = set(other_cities)
    return len(mycity.symmetric_difference(othercity))

