def whitewashing_area(length,width,height):
    area = (length*width)+(length*2*height)+(width*2*height)
    return area
def whitewashing_cost(area, rate_per_sq_m=15):
    wcost = area*rate_per_sq_m
    return wcost
def flooring_cost(length, width, rate_per_sq_m):
    fcost = length*width*rate_per_sq_m
    return fcost
def display_costs(length,width,height):
    area = whitewashing_area(length,width,height)
    wcost = whitewashing_cost(area, 15)
    fcost1 = flooring_cost(length, width, 100)
    fcost2 = flooring_cost(length, width, 55)
    print("whirewashing area:",area)
    print("whitewashing cost:",wcost)
    print("flooring cost for mosaic:",fcost1)
    print("flooring cost for cement:",fcost2)
    
