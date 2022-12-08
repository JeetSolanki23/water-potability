from data_limits.limits import parameter_type
# parameter_type = ['ph','Hardness','Solids','Chloramines','Sulfate','Conductivity','Organic_carbon','Trihalomethanes','Turbidity']
# parameter_type = ['ph','Hardness','Solids']
# parameter_type ={'ph':(5,8),'Hardness':(3,5),'Solids':(3,6)}
parameter = dict({})

def main():
    print("Enter following Details.")

    for key in parameter_type:
        value = float(input(f"{key}: "))
        parameter[key] = value

    poyebality_varyfier(parameter,parameter_type)

def poyebality_varyfier(values,limits,drinkebal=True):
    # print(values,limits)

    for i in values:
        min,max = tuple(limits[i].split("-"))
        if float(min)<=values[i]<=float(max):
            continue
        else:
            drinkebal = False
            break

    use = "not " if drinkebal==False else ""
    print(f"water is {use}good for drinking")

if __name__ == "__main__":
    main()