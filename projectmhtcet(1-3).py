                                 #COLLEGE PREDICTOR BASED ON PERCENTILE IN MHT CET

name = input("PLEASE ENTER YOU FULL NAME: ")
state = input("ENTER YOU HOME STATE: ")
percentile = (input(""""ENTER YOUR MHT CET PERCENTILE
(note:enter the result in which you have got greater percentile): """))
preferedcity = input("""ENTER YOUR PREFERED CITY
(out of pune,mumbai,nashik & nagpur): """)
branch = input("""ENTER BRANCH IN WHICH YOU ARE INTERESTED
(out of CSE or IT only): """)
collegetype = input("""ENTER WHICH TYPE OF COLLEGE YOU ARE LOOKING FOR
(private/goverment/goverment_affiliated): """)
print("YOUR DETAILS:-")
print("YOUR NAME IS",name)
print("YOUR HOME STATE IS",state)
print("TYPE OF COLLEGE YOU WANT IS",collegetype)
                                   
                                   
                                   ###PUNE CITY###

                                    #95 ABOVE PUNE


#1GOVTPUNE
puneG95 = ["COEP Technological University (COEP)",
"Government College of Engineering and Research (GCOEAR), Avasari Khurd"]
#2PRIVPUNE
puneP95 = ["Pune Institute of Computer Technology (PICT), Dhankawadi",
"Vishwakarma Institute of Technology (VIT), Bibwewadi",
"Pimpri Chinchwad College of Engineering (PCCOE), Akurdi",
"MIT World Peace University (MIT-WPU), Kothrud",
"Army Institute of Technology (AIT), Dighi"]
#3PRIVAGOVTPUNE
punePA95 = ["Dr. D.Y. Patil Institute of Technology (DYPIT), Pimpri",
"Modern Education Society's College of Engineering (MESCOE), Wadia College Campus"]
    

                                    #90 ABOVE PUNE
puneG90 = ["Government College of Engineering & Research (GCOEARA), Avasari, Pune",
"Pimpri Chinchwad College of Engineering (PCCOE), Nigdi",
"PVG's College of Engineering & Technology (PVGCOET)"]
puneP90 = ["Dr. D.Y. Patil College of Engineering (DYPCOE), Akurdi",
"MIT World Peace University (MIT-WPU)",
"Pimpri Chinchwad College of Engineering (PCCOE), Ravet",
"Sinhgad College of Engineering (SCOE), Vadgaon (Budruk)",
"AISSMS College of Engineering"]
punePA90 = ["Vishwakarma Institute of Information Technology (VIIT), Kondhwa",
"Sinhgad College of Engineering (SCOE), Vadgaon",
"Dr. D.Y. Patil Institute of Technology, Pimpri",
"PES's Modern College of Engineering, Shivajinagar",
"AISSMS College of Engineering, Near RTO",
"Smt. Kashibai Navale College of Engineering, Vadgaon",
"Bharati Vidyapeeth's College of Engineering for Women, Katraj (For Female Candidates)"]


                                    #85 ABOVE PUNE
puneG85 = ["JSPM's Jaywantrao Sawant College of Engineering",
"Bharati Vidyapeeth`s College of Engineering, Lavale",
"Sinhgad Institute of Technology and Science (Narhe)",
"JSPM's Imperial College of Engineering (Wagholi)",
"Nutan Maharashtra Institute of Engineering & Technology"]
puneP85 = ["AISSMS College of Engineering",
"MIT Academy of Engineering (MIT AOE), Alandi",
"JSPM's Rajarshi Shahu College of Engineering",
"NBN Sinhgad School of Engineering",
"Dr. D.Y. Patil Institute of Technology (Tathawade/Akurdi)",
"Marathwada Mitra Mandal`s College of Engineering (MMCOE)"]
punePA85 = ["D.Y. Patil College of Engineering, Akurdi",
"Smt. Kashibai Navale College of Engineering (SKNCOE)",
"Sinhgad College of Engineering (SCOE), Vadgaon",
"MIT Academy of Engineering (MITAOE), Alandi",
"JSPM's Rajarshi Shahu College of Engineering"]

                                    #80 ABOVE PUNE
        
puneG80 = ["AISSMS Institute of Information Technology (IOIT)",
"JSPM`s Rajarshi Shahu College of Engineering",
"Dr. D. Y. Patil Institute of Technology (Akurdi/Pimpri)",
"Zeal College of Engineering and Research"]
puneP80 = ["MIT Academy of Engineering (MITAOE), Alandi",
"Smt. Kashibai Navale COE (SKNCOE)",
"Sinhgad College of Engineering (SCOE), Vadgaon",
"Pune Vidyarthi Griha`s COE (PVGCOE)",
"Indira College of Engineering and Management (ICEM)",
"JSPM`s Rajarshi Shahu COE, Tathawade",
"Zeal College of Engineering, Narhe"]
punePA80 = ["Trinity College of Engineering and Research",
"KJ College of Engineering and Management Research",
"Imperial College of Engineering and Research",
"Dhole Patil College of Engineering"]
                                    #75 ABOVE IN PUNE 

puneG75 = ["It is imposible to find a government college at pune for 75 percentile in MHT CET for a general category student, you should give a try for private colleges",
"IF YOU ARE ANY RESERVATION CANDIDATE PLEASE CHECKOUT THIS COLLEGES",
"JSPM`s Rajarshi Shahu College of Engineering (RSCOE), Tathawade",
"Dr. D.Y. Patil Institute of Technology (DYPIT), Pimpri",
"AISSMS College of Engineering / IIIT (Pune/Pimpri campuses)",
"Sinhgad College of Engineering (SCOE), Vadgaon",
"PVG`s College of Engineering and Technology"]
puneP75 = ["Indira College of Engineering and Management, Parandwadi",
"Zeal College of Engineering and Research, Narhe",
"Trinity Academy of Engineering, Kondhwa",
"Alard College of Engineering and Management",
"JSPM Group of Institutions (Various Campuses)"]
punePA75 = ["IF YOU ARE ANY RESERVATION CANDIDATE PLEASE CHECKOUT THIS COLLEGES",
"Indira College of Engineering and Management, Parandwadi",
"Zeal College of Engineering and Research, Narhe",
"Trinity Academy of Engineering, Kondhwa",
"Alard College of Engineering and Management",
"JSPM Group of Institutions (Various Campuses)",
"It is imposible to find a government college at pune for 75 percentile in MHT CET for a general category student, you should give a try for private colleges"]



if int(percentile)>=95:
    print("here are some colleges you can get in")#95above
    if(preferedcity=="pune"):
        if(collegetype=="goverment"):
            print(puneG95)
        elif(collegetype=="private"):
            print(puneP95)
        elif(collegetype=="goverment_affiliated"):
            print(punePA95)    
    elif(preferedcity=="mumbai"):
        if(collegetype=="goverment"):
            print(mumbaiG95)
        elif(collegetype=="private"):
            print(mumbaiP95)
        elif(collegetype=="goverment_affiliated"):
            print(mumbaiPA95)
    elif(preferedcity=="nashik"):
        if(collegetype=="goverment"):
            print(nashikG95)
        elif(collegetype=="private"):
            print(nashikP95)
        elif(collegetype=="goverment_affiliated"):
            print(nashikPA95)
    elif(preferedcity=="nagpur"):
        if(collegetype=="goverment"):
            print(nagpurG95)
        elif(collegetype=="private"):
            print(nagpurP95)
        elif(collegetype=="goverment_affiliated"):
            print(nagpurPA95)
    else:
        print("please select the appropiate city")
elif int(percentile)>=90.00 and int(percentile)<=94.99:
    print("here are some colleges you can get in")#90above 
    if(preferedcity=="pune"):
        if(collegetype=="goverment"):
            print(puneG90)
        elif(collegetype=="private"):
            print(puneP90)
        elif(collegetype=="goverment_affiliated"):
            print(punePA90)
    elif(preferedcity=="mumbai"):
        if(collegetype=="goverment"):
            print(mumbaiG90)
        elif(collegetype=="private"):
            print(mumbaiP90)
        elif(collegetype=="goverment_affiliated"):
            print(mumbaiPA90)
    elif(preferedcity=="nashik"):
        if(collegetype=="goverment"):
            print(nashikG90)
        elif(collegetype=="private"):
            print(nashikP90)
        elif(collegetype=="goverment_affiliated"):
            print(nashikPA90)
    elif(preferedcity=="nagpur"):
        if(collegetype=="goverment"):
            print(nagpurG90)
        elif(collegetype=="private"):
            print(nagpurP90)
        elif(collegetype=="goverment_affiliated"):
            print(nagpurPA90)
    else:
        print("please select the appropiate city")
elif int(percentile)>=85.00 and int(percentile)<=89.99:
    print("here are some colleges you can get in")#85above
    if(preferedcity=="pune"):
        if(collegetype=="goverment"):
            print(puneG85)
        elif(collegetype=="private"):
            print(puneP85)
        elif(collegetype=="goverment_affiliated"):
            print(punePA85)
    elif(preferedcity=="mumbai"):
        if(collegetype=="goverment"):
            print(mumbaiG85)
        elif(collegetype=="private"):
            print(mumbaiP85)
        elif(collegetype=="goverment_affiliated"):
            print(mumbaiPA85)
    elif(preferedcity=="nashik"):
        if(collegetype=="goverment"):
            print(nashikG85)
        elif(collegetype=="private"):
            print(nashikP85)
        elif(collegetype=="goverment_affiliated"):
            print(nashikPA85)
    elif(preferedcity=="nagpur"):
        if(collegetype=="goverment"):
            print(nagpurG85)
        elif(collegetype=="private"):
            print(nagpurP85)
        elif(collegetype=="goverment_affiliated"):
            print(nagpurPA85)
    else:
        print("please select the appropiate city")
elif int(percentile)>=80.00 and int(percentile)<=84.99:
    print("here are some colleges you can get in")#80above
    if(preferedcity=="pune"):
        if(collegetype=="goverment"):
            print(puneG80)
        elif(collegetype=="private"):
            print(puneP80)
        elif(collegetype=="goverment_affiliated"):
            print(punePA80)
    elif(preferedcity=="mumbai"):
        if(collegetype=="goverment"):
            print(mumbaiG80)
        elif(collegetype=="private"):
            print(mumbaiP80)
        elif(collegetype=="goverment_affiliated"):
            print(mumbaiPA80)
    elif(preferedcity=="nashik"):
        if(collegetype=="goverment"):
            print(nashikG80)
        elif(collegetype=="private"):
            print(nashikP80)
        elif(collegetype=="goverment_affiliated"):
            print(nashikPA80)
    elif(preferedcity=="nagpur"):
        if(collegetype=="goverment"):
            print(nagpurG80)
        elif(collegetype=="private"):
            print(nagpurP80)
        elif(collegetype=="goverment_affiliated"):
            print(nagpurPA80)
    else:
        print("please select the appropiate city")
elif int(percentile)>=75.00 and int(percentile)<=79.99:
    print("here are some colleges you can get in")#75above
    if(preferedcity=="pune"):
        if(collegetype=="goverment"):
            print(puneG75)
        elif(collegetype=="private"):
            print(puneP75)
        elif(collegetype=="goverment_affiliated"):
            print(punePA75)
    elif(preferedcity=="mumbai"):
        if(collegetype=="goverment"):
            print(mumbaiG75)
        elif(collegetype=="private"):
            print(mumbaiP75)
        elif(collegetype=="goverment_affiliated"):
            print(mumbaiPA75)
    elif(preferedcity=="nashik"):
        if(collegetype=="goverment"):
            print(nashikG75)
        elif(collegetype=="private"):
            print(nashikP75)
        elif(collegetype=="goverment_affiliated"):
            print(nashikPA75)
    elif(preferedcity=="nagpur"):
        if(collegetype=="goverment"):
            print(nagpurG75)
        elif(collegetype=="private"):
            print(nagpurP75)
        elif(collegetype=="goverment_affiliated"):
            print(nagpurPA75)
    else:
        print("please select the appropiate city")
elif int(percentile)>=70.00 and int(percentile)<=74.99 :
    print("here are some colleges you can get in")#70above
    if(preferedcity=="pune"):
        if(collegetype=="goverment"):
            print(puneG70)
        elif(collegetype=="private"):
            print(puneP70)
        elif(collegetype=="goverment_affiliated"):
            print(punePA70)
    elif(preferedcity=="mumbai"):
        if(collegetype=="goverment"):
            print(mumbaiG70)
        elif(collegetype=="private"):
            print(mumbaiP70)
        elif(collegetype=="goverment_affiliated"):
            print(mumbaiPA70)
    elif(preferedcity=="nashik"):
        if(collegetype=="goverment"):
            print(nashikG70)
        elif(collegetype=="private"):
            print(nashikP70)
        elif(collegetype=="goverment_affiliated"):
            print(nashikPA70)
    elif(preferedcity=="nagpur"):
        if(collegetype=="goverment"):
            print(nagpurG70)
        elif(collegetype=="private"):
            print(nagpurP70)
        elif(collegetype=="goverment_affiliated"):
            print(nagpurPA70)
    else:
        print("please select the appropiate city")
elif int(percentile)>=65.00 and int(percentile)<=69.99:
    print("here are some colleges you can get in")#65above
    if(preferedcity=="pune"):
        if(collegetype=="goverment"):
            print(puneG65)
        elif(collegetype=="private"):
            print(puneP65)
        elif(collegetype=="goverment_affiliated"):
            print(punePA65)
    elif(preferedcity=="mumbai"):
        if(collegetype=="goverment"):
            print(mumbaiG65)
        elif(collegetype=="private"):
            print(mumbaiP65)
        elif(collegetype=="goverment_affiliated"):
            print(mumbaiPA65)
    elif(preferedcity=="nashik"):
        if(collegetype=="goverment"):
            print(nashikG65)
        elif(collegetype=="private"):
            print(nashikP65)
        elif(collegetype=="goverment_affiliated"):
            print(nashikPA65)
    elif(preferedcity=="nagpur"):
        if(collegetype=="goverment"):
            print(nagpurG65)
        elif(collegetype=="private"):
            print(nagpurP65)
        elif(collegetype=="goverment_affiliated"):
            print(nagpurPA65)
    else:
        print("please select the appropiate city")
elif int(percentile)>=60.00 and int(percentile)<=64.99:
    print("here are some colleges you can get in")#60above
    if(preferedcity=="pune"):
        if(collegetype=="goverment"):
            print(puneG60)
        elif(collegetype=="private"):
            print(puneP60)
        elif(collegetype=="goverment_affiliated"):
            print(punePA60)
    elif(preferedcity=="mumbai"):
        if(collegetype=="goverment"):
            print(mumbaiG60)
        elif(collegetype=="private"):
            print(mumbaiP60)
        elif(collegetype=="goverment_affiliated"):
            print(mumbaiPA60)
    elif(preferedcity=="nashik"):
        if(collegetype=="goverment"):
            print(nashikG60)
        elif(collegetype=="private"):
            print(nashikP60)
        elif(collegetype=="goverment_affiliated"):
            print(nashikPA60)
    elif(preferedcity=="nagpur"):
        if(collegetype=="goverment"):
            print(nagpurG60)
        elif(collegetype=="private"):
            print(nagpurP60)
        elif(collegetype=="goverment_affiliated"):
            print(nagpurPA60)
    else:
        print("please select the appropiate city")
elif int(percentile)>=55.00 and int(percentile)<=59.99:
    print("here are some colleges you can get in")#55above
    if(preferedcity=="pune"):
        if(collegetype=="goverment"):
            print(puneG55)
        elif(collegetype=="private"):
            print(puneP55)
        elif(collegetype=="goverment_affiliated"):
            print(punePA55)
    elif(preferedcity=="mumbai"):
        if(collegetype==goverment):
            print(mumbaiG55)
        elif(collegetype=="private"):
            print(mumbaiP55)
        elif(collegetype=="goverment_affiliated"):
            print(mumbaiPA55)
    elif(preferedcity=="nashik"):
        if(collegetype=="goverment"):
            print(nashikG55)
        elif(collegetype=="private"):
            print(nashikP55)
        elif(collegetype=="goverment_affiliated"):
            print(nashikPA55)
    elif(preferedcity=="nagpur"):
        if(collegetype=="goverment"):
            print(nagpurG55)
        elif(collegetype=="private"):
            print(nagpurP55)
        elif(collegetype=="goverment_affiliated"):
            print(nagpurPA55)
    else:
        print("please select the appropiate city")
else:
    print("you have a strong chance of getting into these private colleges:-") 


                                 

