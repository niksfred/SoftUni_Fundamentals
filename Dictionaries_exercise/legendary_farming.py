materials = input().lower().split()

materials_dic = {"shards": 0, "motes": 0, "fragments": 0}
junk = {}
obtained_item = False

while True:
    
    for i in range(0, len(materials), 2):
        quantity = int(materials[i])
        material = materials[i+1]

        if materials[i+1] in materials_dic:
            materials_dic[material] += quantity
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += quantity
            
        
        if materials_dic["shards"] >= 250:
            print("Shadowmourne obtained!")
            materials_dic["shards"] -= 250
            obtained_item = True
            break
        elif materials_dic["motes"] >= 250:
            print("Dragonwrath obtained!")
            materials_dic["motes"] -= 250
            obtained_item = True
            break
        elif materials_dic["fragments"] >= 250:
            print("Valanyr obtained!")
            materials_dic["fragments"] -= 250
            obtained_item = True
            break
    
    if obtained_item == True:
        break 
    
    materials = input().lower().split()
    
sorted_materials = sorted(materials_dic.items(), key=lambda x: (-x[1], x[0]))
for key,value in sorted_materials:
    print(f"{key}: {value}")

sorted_junk = sorted(junk.items(), key=lambda x: x[0])
for key, value in sorted_junk:
    print(f"{key}: {value}")
