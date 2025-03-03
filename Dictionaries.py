    #dictionary = a changeable, unordered collection of unique key:value pairs
    #             Fast because they use hashing, allows us to accessa value quickly

capitals = {'USA':'Washington DC',
            'INDIA':'New Dehli',
            'CHINA':'Beijing',
            'RUSSIA':'Moscow'}

#ways to change
capitals.update({'Germany':'berlin'}) #add a new key value
capitals.update({'USA':'Ohio'}) #update key of usa with a new value
#capitals.pop('CHINA') # removes china
#capitals.clear() #removes everything

#print(capitals['INDIA']) #prints the pair value
#print(capitals.get('GERNAMY')) #safer way here in this instance it checks if the value is there
#print(capitals.keys()) #prints only the keys
#print(capitals.values()) #prints only values
#print(capitals.items()) #prints everything

for key,value in capitals.items(): #prints all dictionaries by iterating everything once
    print(key,value)