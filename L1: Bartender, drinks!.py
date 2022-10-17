def get_drink_by_profession(param):
    dictB = {
        "Jabroni" :	"Patron Tequila",
        "School Counselor" : "Anything with Alcohol",
        "Programmer" : "Hipster Craft Beer",
        "Bike Gang Member" : "Moonshine",
        "Politician" : "Your tax dollars",
        "Rapper" : "Cristal",
    }
    
    if param.title() in dictB.keys():
        return dictB[param.title()]
    else:
        return "Beer"
