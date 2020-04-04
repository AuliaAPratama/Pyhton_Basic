import json

with open("ccNasabah.json","r") as x:
    out = json.load(x)

tesvalid = []
tesinvalid = []
for index in range(len(out)):
    CCnomer = out[index]["noCreditCard"]
    CCnomer = CCnomer.split("-")
    CCnomer = "".join(CCnomer)
    

    if CCnomer[0]=="4" and len(CCnomer) == 16:    
        if " " in CCnomer:
            tesinvalid.append(out[index])
        elif CCnomer[index].isalpha():
            tesinvalid.append(out[index])
        elif "-" in CCnomer:
            tesinvalid.append(out[index])
        elif "44444" in CCnomer:
            tesinvalid.append(out[index])
        else: 
            tesvalid.append(out[index])

    elif CCnomer[0] == "5" and len(CCnomer) == 16:
        if " " in CCnomer:
            tesinvalid.append(out[index])
        elif CCnomer[index].isalpha():
            tesinvalid.append(out[index])
        elif "-" in CCnomer:
            tesinvalid.append(out[index])
        elif "9999" in CCnomer:
            tesinvalid.append(out[index])
        else:
            tesvalid.append(out[index])

    elif CCnomer[0] == "6" and len(CCnomer) == 16:
        if " " in CCnomer:
            tesinvalid.append(out[index])
        elif CCnomer[index].isalpha():
            tesinvalid.append(out[index])
        elif "-" in CCnomer:
            tesinvalid.append(out[index])
        elif "61234" in CCnomer:
            tesinvalid.append(out[index])
        else: 
            tesvalid.append(out[index])
    else:
        tesinvalid.append(out[index])

with open("ccValid.json","w") as y:
    json.dump(tesvalid,y)
with open("ccInvalid.json","w") as z:
    json.dump(tesinvalid,z)