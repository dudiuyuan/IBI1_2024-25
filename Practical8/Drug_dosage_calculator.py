def calculate_paracetamol_mass(weight, strength):
    if not (10 <= weight <= 100):                                    #examing the weight range
        raise ValueError("Weight must be between 10 and 100 kg")
    if strength not in [120, 250]:                                   #examing the strength range
        raise ValueError("Strength must be 120 mg/5ml or 250 mg/5ml")
    
    mass_mg = 15 * weight                                            #calculating the mass
    if strength == 120:
        volume_ml = mass_mg / (120 / 5)  # transfer to 24 mg/ml
    else:
        volume_ml = mass_mg / (250 / 5)  # transfer to 50 mg/ml
    
    return volume_ml

# for example
print(f"The volume of paracetamol to be given is: {calculate_paracetamol_mass(20, 120)} ml.")  # output The volume of paracetamol to be given is: 12.5 ml
print(f"The volume of paracetamol to be given is: {calculate_paracetamol_mass(50, 250)} ml.")  # output The volume of paracetamol to be given is: 15.0 ml
input_weight = int(input("Enter the weight of the child in kg: "))  # input weight
input_strength = int(input("Enter the strength of the paracetamol in mg/5ml (120 or 250): "))  # input strength
print(f"The volume of paracetamol to be given is: {calculate_paracetamol_mass(input_weight, input_strength)} ml.")  # output the volume
