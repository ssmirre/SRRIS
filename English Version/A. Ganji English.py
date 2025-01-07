age=int(input("How old are you?"))
gender=int(input("Enter your gender. If you are female enter 1 and if you are male enter 2."))
#Now we need to ask the user what is the main symptom?
print("Hello, we are in this program to diagnose your disease and suggest you some suggestions.")
print()
print("This program is currently working on 5 main symptoms of diseases:")
Main_symptoms = ("Abdominal pain", "Chest pain", "Cough", "Back pain", "Shortness of breath")

print("1=Abdominal pain\n2=Chest pain\n3=Cough\n4=Back pain\n5=Shortness of breath")
A = int(input("Please tell me which of the following main symptoms do you have? "))

if A == 1:
    print("You have a stomach ache.")
    
    
    
    
elif A == 2:
    print("You have chest pain.")
    AreaOfThePain = int(input("Where do you MAINLY feel the pain?\n 1. Behind the sternum \n 2. Under the left breast \n 3. Along the costal cartilage\n"))
    print()
   
    if AreaOfThePain == 1:
        BackPainCheck = int(input("Do you also feel pain in the back? \n 1. Yes \n 2. No, pain often radiates to the bladder, \n arms, neck, lower jaw or upper abdomen \n 3. other options\n"))
        print()

        if BackPainCheck == 2:
           IntensityBladderPainCheck = int(input("What is the intensity of your pain? \n 1.Mild \n 2.Average \n 3.intense\n"))
           print()
           if IntensityBladderPainCheck == 1:
               associated_symptoms = int(input("What are your associated symptoms? \n 1.Shortness of breath \n 2.nausea \n 3.Shortness of breath and nausea\n"))
               if associated_symptoms == 1:
                   print("You have a 25% probability of having angina pectoris \n but for more accurate results, \n it is recommended to consult a doctor")
                   print()
                   print("Its timing: \n Usually 1 to 3 mins \n **Its aggravating factors are: \n Often activity, especially cold weather \n eating and emotional stress** \n **Its reducing agents are: \n Often resting and using nitroglycerin**")
                   print()
                   print("Use NITROGLYCERIN \n but for more accurate results, \n it is recommended to consult a doctor")
               elif associated_symptoms == 2:
                    print("You have a 20% probability of having angina pectoris \n but for more accurate results, \n it is recommended to consult a doctor")
                    print()
                    print("Its timing: \n Usually 1 to 3 mins \n **Its aggravating factors are: \n Often activity, especially cold weather \n eating and emotional stress** \n **Its reducing agents are: \n Often resting and using nitroglycerin**")
                    print()
                    print("Use NITROGLYCERIN \n but for more accurate results, \n it is recommended to consult a doctor.")
               elif associated_symptoms == 3:
                      print("You have a 30% probability of having angina pectoris \n but for more accurate results, \n it is recommended to consult a doctor")
                      print()
                      print("Its timing: \n Usually 1 to 3 mins \n **Its aggravating factors are: \n Often activity, especially cold weather \n eating and emotional stress** \n **Its reducing agents are: \n Often resting and using nitroglycerin**")
                      print()
                      print("Use NITROGLYCERIN \n but for more accurate results, \n it is recommended to consult a doctor.")

           elif IntensityBladderPainCheck == 2:
               associated_symptoms = int(input("What are your associated symptoms? \n 1.Shortness of breath \n 2.nausea \n 3.Shortness of breath and nausea\n"))
               if associated_symptoms == 1: 
                   print("You have a 40%-50% probability of having angina pectoris \n but for more accurate results, \n it is recommended to consult a doctor")
                   print()
                   print("Its timing: \n Usually 1 to 3 mins \n **Its aggravating factors are: \n Often activity, especially cold weather \n eating and emotional stress** \n **Its reducing agents are: \n Often resting and using nitroglycerin**")
                   print()
                   print("Use NITROGLYCERIN \n but for more accurate results, \n it is recommended to consult a doctor.")
               elif associated_symptoms == 2:
                   print("You have a 35%-45% probability of having angina pectoris \n but for more accurate results, \n it is recommended to consult a doctor")
                   print()
                   print("Its timing: \n Usually 1 to 3 mins \n **Its aggravating factors are: \n Often activity, especially cold weather \n eating and emotional stress** \n **Its reducing agents are: \n Often resting and using nitroglycerin**")
                   print()
                   print("Use NITROGLYCERIN \n but for more accurate results, \n it is recommended to consult a doctor.")
               elif associated_symptoms == 3:
                   print("You have a 50%-60% probability of having angina pectoris \n but for more accurate results, \n it is recommended to consult a doctor")
                   print()
                   print("Its timing: \n Usually 1 to 3 mins \n **Its aggravating factors are: \n Often activity, especially cold weather \n eating and emotional stress** \n **Its reducing agents are: \n Often resting and using nitroglycerin**")
                   print()
                   print("Use NITROGLYCERIN \n but for more accurate results, \n it is recommended to consult a doctor.") 
           elif IntensityBladderPainCheck == 3:
               associated_symptoms = int(input("What are your associated symptoms? \n 1.Shortness of breath \n 2.nausea \n 3.Shortness of breath and nausea\n"))
               if associated_symptoms == 1: 
                   print("You have a 70%-80% probability of having heart attack \n but for more accurate results, \n it is recommended to consult a doctor")
                   print()
                   print("Its timing: 20 mins to several hours \n **Activity does not always woesen this condition** \n **Rest does not lead to improvement in this condition**")
                   print()
                   print("Use NITROGLYCERIN \n and then perform \n angiography as soon as possible")
               elif associated_symptoms == 2:
                   print("You have a 65%-75% probability of having heart attack \n but for more accurate results, \n it is recommended to consult a doctor")
                   print()
                   print("Its timing: 20 mins to several hours \n **Activity does not always woesen this condition** \n **Rest does not lead to improvement in this condition**")
                   print()
                   print("Use NITROGLYCERIN \n and then perform \n angiography as soon as possible")
               elif associated_symptoms == 3:
                   print("You have a 80%-90% probability of having heart attack \n but for more accurate results, \n it is recommended to consult a doctor")
                   print()
                   print("Its timing: 20 mins to several hours \n **Activity does not always woesen this condition** \n **Rest does not lead to improvement in this condition**")
                   print()
                   print("Use NITROGLYCERIN \n and then perform \n angiography as soon as possible")
              

        elif BackPainCheck == 1:
            QualityBackPainCheck = int(input("What is the quality of your pain? \n 1.Burning \n 2.Burning and pressuring\n"))
            if QualityBackPainCheck == 1:
                IntensityBackPainCheck = int(input("What is the intensity of your pain? \n 1.Mild \n 2.intense\n"))
                if IntensityBackPainCheck == 1:
                    Cough = int(input("Do you have a cough? \n 1.Yes \n 2.No\n"))
                    if Cough == 1:
                        print("You have a 40% chance of having GERD \n but for more accurate results, \n it is recommended to consult a doctor")
                        print()
                        print("Its timing: variable \n **Its aggravating factors are: \n A large meal, bending over and lying down** \n **Its reducing agents are: \n Antacids and sometimes burping**")
                        print()
                        print("Use OMEPRAZOLE \n and if it worsens, \n administer PANTOPRAZOLE injection")
                    elif Cough == 2:
                        print("You have a 35% chance of having GERD \n but for more accurate results, \n it is recommended to consult a doctor")
                        print()
                        print("Its timing: variable \n **Its aggravating factors are: \n A large meal, bending over and lying down** \n **Its reducing agents are: \n Antacids and sometimes burping**")
                        print()
                        print("Use OMEPRAZOLE \n and if it worsens, \n administer PANTOPRAZOLE injection")
                elif IntensityBackPainCheck == 2:
                    Cough = int(input("Do you have a cough? \n 1.Yes \n 2.No\n"))
                    if Cough == 1:
                        print("You have a 60% chance of having GERD \n but for more accurate results, \n it is recommended to consult a doctor")
                        print()
                        print("Its timing: variable \n **Its aggravating factors are: \n A large meal, bending over and lying down** \n **Its reducing agents are: \n Antacids and sometimes burping**")
                        print()
                        print("Use OMEPRAZOLE \n and if it worsens, \n administer PANTOPRAZOLE injection")
                    elif Cough == 2:
                        print("You have a 50% chance of having GERD \n but for more accurate results, \n it is recommended to consult a doctor")
                        print()
                        print("Its timing: variable \n **Its aggravating factors are: \n A large meal, bending over and lying down** \n **Its reducing agents are: \n Antacids and sometimes burping**")
                        print()
                        print("Use OMEPRAZOLE \n and if it worsens, \n administer PANTOPRAZOLE injection")
            
            elif QualityBackPainCheck == 2:
                IntensityBackPainCheck = int(input("What is the intensity of your pain? \n 1.Mild \n 2.intense\n"))
                if IntensityBackPainCheck == 1:
                    Cough = int(input("Do you have a cough? \n 1.Yes \n 2.No\n"))
                    if Cough == 1:
                        print("You have a 45% chance of having GERD \n but for more accurate results, \n it is recommended to consult a doctor")
                        print()
                        print("Its timing: variable \n **Its aggravating factors are: \n A large meal, bending over and lying down** \n **Its reducing agents are: \n Antacids and sometimes burping**")
                        print()
                        print("Use OMEPRAZOLE \n and if it worsens, \n administer PANTOPRAZOLE injection")
                    elif Cough == 2:
                        print("You have a 40% chance of having GERD \n but for more accurate results, \n it is recommended to consult a doctor")
                        print()
                        print("Its timing: variable \n **Its aggravating factors are: \n A large meal, bending over and lying down** \n **Its reducing agents are: \n Antacids and sometimes burping**")
                        print()
                        print("Use OMEPRAZOLE \n and if it worsens, \n administer PANTOPRAZOLE injection")
                elif IntensityBackPainCheck == 2:
                    Cough = int(input("Do you have a cough? \n 1.Yes \n 2.No\n"))
                    if Cough == 1:
                        print("You have a 65% chance of having GERD \n but for more accurate results, \n it is recommended to consult a doctor")
                        print()
                        print("Its timing: variable \n **Its aggravating factors are: \n A large meal, bending over and lying down** \n **Its reducing agents are: \n Antacids and sometimes burping**")
                        print()
                        print("Use OMEPRAZOLE \n and if it worsens, \n administer PANTOPRAZOLE injection")
                    elif Cough == 2:
                        print("You have a 55% chance of having GERD \n but for more accurate results, \n it is recommended to consult a doctor")
                        print()
                        print("Its timing: variable \n **Its aggravating factors are: \n A large meal, bending over and lying down** \n **Its reducing agents are: \n Antacids and sometimes burping**")
                        print()
                        print("Use OMEPRAZOLE \n and if it worsens, \n administer PANTOPRAZOLE injection")     
         
        elif BackPainCheck == 3:
            print("Sorry, we don't have enough data to diagnose your problem. \n Please visit your doctor.")
     
         
    elif AreaOfThePain == 3:
        QualityCheck = int(input("Is the quality of your pain sharp, dull, or unbearable? \n 1.Yes \n 2.No \n"))
        if QualityCheck == 1:
            SensitivityCheck = int(input("Do you have localized tenderness or sensitivity to touch? \n 1.Yes \n 2.No \n"))
            if SensitivityCheck == 1:
                print("You are likely to have chest wall pain syndrome \n with a probability of 70%-80%. \n  but for more accurate results, \n it is recommended to consult a doctor")
                print()
                print("Its timing is: from hours to days \n **Its aggravating factors are: \n Coughing, chest movements, and arm movements**")
                print()
                print("If your chest wall is fractured, \n you need to rest and wait for it to heal. \n If it is not fractured, \n you should wait for the bruising to subside.")
             
            elif SensitivityCheck == 2:
                print("You are likely to have chest wall pain syndrome \n with a probability of 50%-60%. \n  but for more accurate results, \n it is recommended to consult a doctor")
                print()
                print("Its timing is: from hours to days \n **Its aggravating factors are: \n Coughing, chest movements, and arm movements**")
                print()
                print("If your chest wall is fractured, \n you need to rest and wait for it to heal. \n If it is not fractured, \n you should wait for the bruising to subside.")
                
        elif QualityCheck == 2:
            print("Sorry, we don't have enough data to diagnose your problem. \n Please visit your doctor.")
          
    elif AreaOfThePain == 2:
        PainInTheFrontCheck = int(input("Do you feel any pain in the front of your chest? \n 1.Yes \n 2.No \n"))
        if PainInTheFrontCheck == 2:
            QualityFrontCheck = int(input("Is the quality of your pain sharp, dull, or unbearable? \n 1.Yes \n 2.No \n"))
            if QualityFrontCheck == 1:
                SensitivityFrontCheck = int(input("Do you have localized tenderness or sensitivity to touch? \n 1.Yes \n 2.No \n"))
                if SensitivityFrontCheck == 1:
                    print("You are likely to have chest wall pain syndrome \n with a probability of 60%-70%. \n  but for more accurate results, \n it is recommended to consult a doctor")
                    print()
                    print("Its timing is: from hours to days \n **Its aggravating factors are: \n Coughing, chest movements, and arm movements**")
                    print()
                    print("If your chest wall is fractured, \n you need to rest and wait for it to heal. \n If it is not fractured, \n you should wait for the bruising to subside.")
                 
                elif SensitivityFrontCheck == 2:
                    print("You are likely to have chest wall pain syndrome \n with a probability of 50%-60%. \n  but for more accurate results, \n it is recommended to consult a doctor")
                    print()
                    print("Its timing is: from hours to days \n **Its aggravating factors are: \n Coughing, chest movements, and arm movements**")
                    print()
                    print("If your chest wall is fractured, \n you need to rest and wait for it to heal. \n If it is not fractured, \n you should wait for the bruising to subside.")
            
            elif QualityFrontCheck == 2:
                print("Sorry, we don't have enough data to diagnose your problem. \n Please visit your doctor.")
                
        elif PainInTheFrontCheck == 1:
            QualityFrontCheck2 = int(input("Is the quality of your pain sharp, dull, or unbearable? \n 1.Yes \n 2.No \n"))
            if QualityFrontCheck2 == 1:
                print("Now we need to determine what assosiated symptoms you are experiencing. \n please choose from the following options.")
                print(" 1.Shortness of breath \n 2.Weak heartbeat \n 3.Anxiety")
                print()
                associated_symptoms=input("Which of the assosiated symptoms do you have? \n You can select multiple options. /n Just put  ,  between the numbers.\n")
                print()
                associated_symptoms=set(map(int,associated_symptoms.split(",")))
                if associated_symptoms == {1}:
                    print("You have a 40% likelihood of having anxiety and mental health disorders. \n  but for more accurate results, \n it is recommended to consult a doctor")
                    print()
                    print("Its timing is: from hours to days \n **Its aggravating factors are: Physical activity and emotional stress**")
                    print()
                    print("Consult a psychiatrist and take prescribed medications for your nerves.")
                elif associated_symptoms == {2}:
                    print("You have a 35% likelihood of having anxiety and mental health disorders. \n  but for more accurate results, \n it is recommended to consult a doctor")
                    print()
                    print("Its timing is: from hours to days \n **Its aggravating factors are: Physical activity and emotional stress**")
                    print()
                    print("Consult a psychiatrist and take prescribed medications for your nerves.")
                elif associated_symptoms == {3}:
                    print("You have a 50% likelihood of having anxiety and mental health disorders. \n  but for more accurate results, \n it is recommended to consult a doctor")
                    print()
                    print("Its timing is: from hours to days \n **Its aggravating factors are: Physical activity and emotional stress**")
                    print()
                    print("Consult a psychiatrist and take prescribed medications for your nerves.")
                elif associated_symptoms == {1,2}:
                    print("You have a 45% likelihood of having anxiety and mental health disorders. \n  but for more accurate results, \n it is recommended to consult a doctor")
                    print()
                    print("Its timing is: from hours to days \n **Its aggravating factors are: Physical activity and emotional stress**")
                    print()
                    print("Consult a psychiatrist and take prescribed medications for your nerves.")
                elif associated_symptoms == {1,3}:
                    print("You have a 55% likelihood of having anxiety and mental health disorders. \n  but for more accurate results, \n it is recommended to consult a doctor")
                    print()
                    print("Its timing is: from hours to days \n **Its aggravating factors are: Physical activity and emotional stress**")
                    print()
                    print("Consult a psychiatrist and take prescribed medications for your nerves.")
                elif associated_symptoms == {2,3}:
                    print("You have a 50% likelihood of having anxiety and mental health disorders. \n  but for more accurate results, \n it is recommended to consult a doctor")
                    print()
                    print("Its timing is: from hours to days \n **Its aggravating factors are: Physical activity and emotional stress**")
                    print()
                    print("Consult a psychiatrist and take prescribed medications for your nerves.")
                elif associated_symptoms == {1,2,3}:
                    print("You have a 60%-70 likelihood of having anxiety and mental health disorders. \n  but for more accurate results, \n it is recommended to consult a doctor")
                    print()
                    print("Its timing is: from hours to days \n **Its aggravating factors are: Physical activity and emotional stress**")
                    print()
                    print("Consult a psychiatrist and take prescribed medications for your nerves.")

elif A == 3:
    print("You have a cough.")
    #We need to understand what kind of cough she/he has.
    print()
    print("Now I need to know what type of cough you have. Choose from the following factors.")
    print("1=Dry cough\n2=Mucoid sputum\n3=Purulent sputum mixed with blood\n4=Purulent sputum without blood\n5=Purulent sputum completely bloody\n6=Chronic cough, especially at night\n7=Cough that varies in certain places and times")
    print()
    cough=input("Which of the coughs do you have? You can choose multiple ones, just put , between the numbers")
    #We use split to separate the above string into numbers and ','
    #We use the map function here to convert all the input data into numeric data.
    cough=set(map(int,cough.split(",")))
    print()
    #Now we need to understand what associated symptoms you are experiencing.
    print("Now I need to understand what associated symptoms you are experiencing. Choose from the following factors.")
    print("1=Fever\n2=Headache\n3=Shortness of breath\n4=Chest pain\n5=Shivering\n6=Postnasal drip\n7=Loss of appetite\n8=Weight loss\n9=Fatigue\n10=Night snoring\n11=Cough triggers\n12=Infection\n13=History of allergies\n15=Wheezing\n16=Cough only without associated symptoms")
    print()
    associated_symptoms=input("Which of the associated symptoms do you have? You can select multiple items, just put , between the numbers.")
    associated_symptoms=set(map(int,associated_symptoms.split(",")))
    #viral lung infection
    #dry cough
    if cough=={1} and associated_symptoms=={1}:
        print("You have a 30% chance of having a viral lung infection.")
    elif cough=={1} and associated_symptoms=={2}:
        print("You have a 25% chance of having a viral lung infection.")
    elif cough=={1} and associated_symptoms=={3}:
        print("You have a 40% chance of having a viral lung infection.")
    elif cough=={1} and associated_symptoms=={1,2}:
        print("You have a 40% chance of having a viral lung infection.")     
    elif cough=={1} and associated_symptoms=={1,3}:
        print("You have a 50% chance of having a viral lung infection.")
    elif cough=={1} and associated_symptoms=={2,3}:
        print("You have a 35% chance of having a viral lung infection.")
    elif cough=={1} and associated_symptoms=={1,2,3}:
        print("You have a 60-70% chance of having a viral lung infection.")
    elif cough=={1} and associated_symptoms=={16}:
        print("You have a 20% chance of having a viral lung infection.")
       
        # Mucoid sputum
    elif cough=={2} and associated_symptoms=={1}:
        print("You have a 20% chance of having a viral lung infection.")
    elif cough=={2} and associated_symptoms=={2}:
        print("You have a 15% chance of having a viral lung infection.")
    elif cough=={2} and associated_symptoms=={3}:
        print("You have a 30% chance of having a viral lung infection.")
    elif cough=={2} and associated_symptoms=={1,2}:
        print("You have a 30% chance of having a viral lung infection.")
    elif cough=={2} and associated_symptoms=={1,3}:
        print("You have a 40% chance of having a viral lung infection.")
    elif cough=={2} and associated_symptoms=={2,3}:
        print("You have a 25% chance of having a viral lung infection.")
    elif cough=={2} and associated_symptoms=={1,2,3}:
        print("You have a 50-60% chance of having a viral lung infection.")
    elif cough=={2} and associated_symptoms=={16}:
        print("You have a 35% chance of having a viral lung infection.")
   
    # Purulent sputum
    elif cough=={4} and associated_symptoms=={1}:
        print("You have a 25% chance of having a viral lung infection.")
    elif cough=={4} and associated_symptoms=={2}:
        print("You have a 20% chance of having a viral lung infection.")
    elif cough=={4} and associated_symptoms=={3}:
        print("You have a 35% chance of having a viral lung infection.")
    elif cough=={4} and associated_symptoms=={1,2}:
        print("You have a 35% chance of having a viral lung infection.")
    elif cough=={4} and associated_symptoms=={1,3}:
        print("You have a 45% chance of having a viral lung infection.")
    elif cough=={4} and associated_symptoms=={2,3}:
        print("You have a 30% chance of having a viral lung infection.")
    elif cough=={4} and associated_symptoms=={1,2,3}:
        print("You have a 55-65% chance of having a viral lung infection.")
    elif cough=={4} and associated_symptoms=={16}:
        print("You have a 60% chance of having a viral lung infection.")
        
    #Dry cough and mucoid sputum
    elif cough=={1,2} and associated_symptoms=={1}:
        print("You have a 30-35% chance of contracting a viral lung infection.")
    elif cough=={1,2} and associated_symptoms=={2}:
        print("You have a 25-30% chance of contracting a viral lung infection.")
    elif cough=={1,2} and associated_symptoms=={3}:
        print("You have a 40-45% chance of contracting a viral lung infection.")
    elif cough=={1,2} and associated_symptoms=={1,2}:
        print("You have a 40-45% chance of contracting a viral lung infection.")
    elif cough=={1,2} and associated_symptoms=={1,3}:
        print("You have a 60-50% chance of contracting a viral lung infection.")
    elif cough=={1,2} and associated_symptoms=={2,3}:
        print("You have a 35-40% chance of contracting a viral lung infection.")
    elif cough=={1,2} and associated_symptoms=={1,2,3}:
        print("You have a 70-60 percent chance of contracting a viral lung infection.")
    elif cough=={1,2} and associated_symptoms=={16}:
        print("You have a 40 percent chance of contracting a viral lung infection.")
    
    #Dry cough and purulent sputum
    elif cough=={1,4} and associated_symptoms=={1}:
        print("You have a 35-40% chance of having a viral lung infection.")
    elif cough=={1,4} and associated_symptoms=={2}:
        print("You have a 30-35% chance of having a viral lung infection.")
    elif cough=={1,4} and associated_symptoms=={3}:
        print("You have a 45-50% chance of having a viral lung infection.")
    elif cough=={1,4} and associated_symptoms=={1,2}:
        print("You have a 30-35% chance of having a viral lung infection.") 
    elif cough=={1,4} and associated_symptoms=={1,3}:
        print("You have a 45-55% chance of having a viral lung infection.")
    elif cough=={1,4} and associated_symptoms=={2,3}:
        print("You have a 40-50% chance of having a viral lung infection.")
    elif cough=={1,4} and associated_symptoms=={1,2,3}:
        print("You have a 65-75% chance of having a viral lung infection.")
    elif cough=={1,4} and associated_symptoms=={16}:
        print("You have a 55% chance of having a viral lung infection.")
        
    # Mucoid and purulent sputum
    elif cough=={2,4} and associated_symptoms=={1}:
        print("You have a 25-30% chance of having a viral lung infection.")
    elif cough=={2,4} and associated_symptoms=={2}:
        print("You have a 20-25% chance of having a viral lung infection.")
    elif cough=={2,4} and associated_symptoms=={3}:
        print("You have a 35-40% chance of having a viral lung infection.")
    elif cough=={2,4} and associated_symptoms=={1,2}:
        print("You have a 30-35% chance of contracting a viral lung infection.")
    elif cough=={2,4} and associated_symptoms=={1,3}:
        print("You have a 45-55% chance of contracting a viral lung infection.")
    elif cough=={2,4} and associated_symptoms=={2,3}:
        print("You have a 30-40% chance of contracting a viral lung infection.")
    elif cough=={2,4} and associated_symptoms=={1,2,3}:
        print("You have a 55-65% chance of contracting a viral lung infection.")
    elif cough=={2,4} and associated_symptoms=={16}:
        print("You have a 50% chance of contracting a viral lung infection.")
    
    # Dry cough, mucoid sputum and purulent sputum
    elif cough=={1,2,4} and associated_symptoms=={1}:
        print("You have a 35-45% chance of having a viral lung infection.")
    elif cough=={1,2,4} and associated_symptoms=={2}:
        print("You have a 30-35% chance of having a viral lung infection.")
    elif cough=={1,2,4} and associated_symptoms=={3}:
        print("You have a 45-50% chance of having a viral lung infection.")
    elif cough=={1,2,4} and associated_symptoms=={1,2}:
        print("You have a 45-55% chance of having a viral lung infection.")
    elif cough=={1,2,4} and associated_symptoms=={1,3}:
        print("You have a 55-65% chance of having a viral lung infection.")
    elif cough=={1,2,4} and associated_symptoms=={2,3}:
        print("You have a 55-45% chance of having a viral lung infection.")
    elif cough=={1,2,4} and associated_symptoms=={1,2,3}:
        print("You have a 65-75% chance of having a viral lung infection.")
    elif cough=={1,2,4} and associated_symptoms=={16}:
        print("You have a 65% chance of having a viral lung infection.")
    print("Our recommended treatment is antivirals. However, the percentage of probability mentioned is approximate. Be sure to consult a doctor to get the exact dosage of the medicine and the type of antiviral")
  
    #Bacterial Lung Infection
    #Mucoid Sputum
    if cough=={2} and associated_symptoms=={1}:
        print("You have a 20% chance of having a bacterial lung infection.")
    elif cough=={2} and associated_symptoms=={3}:
        print("You have a 25% chance of having a bacterial lung infection.")
    elif cough=={2} and associated_symptoms=={4}:
        print("You have a 30% chance of having a bacterial lung infection.")
    elif cough=={2} and associated_symptoms=={5}:
        print("You have a 15% chance of having a bacterial lung infection.")
    elif cough=={2} and associated_symptoms=={1,3}:
        print("You have a 35% chance of having a bacterial lung infection.")
    elif cough=={2} and associated_symptoms=={1,4}:
        print("You have a 40% chance of having a bacterial lung infection.")
    elif cough=={2} and associated_symptoms=={1,5}:
        print("You have a 25% chance of having a bacterial lung infection.")
    elif cough=={2} and associated_symptoms=={3,4}:
        print("You have a 35% chance of having a bacterial lung infection.")
    elif cough=={2} and associated_symptoms=={3,5}:
        print("You have a 20% chance of having a bacterial lung infection.")
    elif cough=={2} and associated_symptoms=={4,5}:
        print("You have a 25% chance of having a bacterial lung infection.")
    elif cough=={2} and associated_symptoms=={1,3,4}:
        print("You have a 45% chance of having a bacterial lung infection.")
    elif cough=={2} and associated_symptoms=={1,3,5}:
        print("You have a 30% chance of having a bacterial lung infection.")
    elif cough=={2} and associated_symptoms=={3,4,5}:
        print("You have a 35% chance of having a bacterial lung infection.")
    elif cough=={2} and associated_symptoms=={1,2,3,4}:
        print("You have a 50% chance of having a bacterial lung infection.")
    elif cough=={2} and associated_symptoms=={16}:
        print("You have a 40% chance of having a bacterial lung infection.")
    
    #Purulent sputum with blood
    elif cough=={3} and associated_symptoms=={1}:
        print("You have a 35% chance of having a bacterial lung infection.")
    elif cough=={3} and associated_symptoms=={3}:
        print("You have a 40% chance of having a bacterial lung infection.")
    elif cough=={3} and associated_symptoms=={4}:
        print("You have a 45% chance of having a bacterial lung infection.")
    elif cough=={3} and associated_symptoms=={5}:
        print("You have a 30% chance of having a bacterial lung infection.")
    elif cough=={3} and associated_symptoms=={1,3}:
        print("You have a 45% chance of having a bacterial lung infection.")
    elif cough=={3} and associated_symptoms=={1,4}:
        print("You have a 45% chance of having a bacterial lung infection.") 
    elif cough=={3} and associated_symptoms=={1,5}:
        print("You have a 35% chance of having a bacterial lung infection.")
    elif cough=={3} and associated_symptoms=={3,4}:
        print("You have a 45% chance of having a bacterial lung infection.")
    elif cough=={3} and associated_symptoms=={3,5}:
        print("You have a 35% chance of having a bacterial lung infection.")
    elif cough=={3} and associated_symptoms=={4,5}:
        print("You have a 40% chance of having a bacterial lung infection.")
    elif cough=={3} and associated_symptoms=={1,3,4}:
        print("You have a 55% chance of having a bacterial lung infection.")
    elif cough=={3} and associated_symptoms=={1,3,5}:
        print("You have a 40% chance of having a bacterial lung infection.")
    elif cough=={3} and associated_symptoms=={3,4,5}:
        print("You have a 45% chance of having a bacterial lung infection.")
    elif cough=={3} and associated_symptoms=={1,2,3,4}:
        print("You have a 60% chance of having a bacterial lung infection.")
    elif cough=={3} and associated_symptoms=={16}:
        print("You have a 70% chance of having a bacterial lung infection.")
    
    #Purulent sputum without blood
    elif cough=={4} and associated_symptoms=={1}:
        print("You have a 30% chance of having a bacterial lung infection.")
    elif cough=={4} and associated_symptoms=={3}:
        print("You have a 30% chance of having a bacterial lung infection.") 
    elif cough=={4} and associated_symptoms=={4}:
        print("You have a 40% chance of having a bacterial lung infection.")
    elif cough=={4} and associated_symptoms=={5}:
        print("You have a 25% chance of having a bacterial lung infection.")
    elif cough=={4} and associated_symptoms=={1,3}:
        print("You have a 40% chance of having a bacterial lung infection.")
    elif cough=={4} and associated_symptoms=={1,4}:
        print("You have a 45% chance of having a bacterial lung infection.")
    elif cough=={4} and associated_symptoms=={1,5}:
        print("You have a 30% chance of having a bacterial lung infection.")
    elif cough=={4} and associated_symptoms=={3,4}:
        print("You have a 35% chance of having a bacterial lung infection.")
    elif cough=={4} and associated_symptoms=={3,5}:
        print("You have a 25% chance of having a bacterial lung infection.")
    elif cough=={4} and associated_symptoms=={4,5}:
        print("You have a 35% chance of having a bacterial lung infection.")
    elif cough=={4} and associated_symptoms=={1,3,4}:
        print("You have a 50% chance of having a bacterial lung infection.")
    elif cough=={4} and associated_symptoms=={1,3,5}:
        print("You have a 35% chance of having a bacterial lung infection.")
    elif cough=={4} and associated_symptoms=={3,4,5}:
        print("You have a 40% chance of having a bacterial lung infection.")
    elif cough=={4} and associated_symptoms=={1,2,3,4}:
        print("You have a 55% chance of having a bacterial lung infection.")
    elif cough=={4} and associated_symptoms=={16}:
        print("You have a 60% chance of having a bacterial lung infection.")    
        
    #Mucoid and purulent sputum stained with blood
    elif cough=={2,3} and associated_symptoms=={1}:
        print("You have a 40% chance of having a bacterial lung infection.")
    elif cough=={2,3} and associated_symptoms=={3}:
        print("You have a 45% chance of having a bacterial lung infection.")
    elif cough=={2,3} and associated_symptoms=={4}:
        print("You have a 50% chance of having a bacterial lung infection.")
    elif cough=={2,3} and associated_symptoms=={5}:
        print("You have a 35% chance of having a bacterial lung infection.")
    elif cough=={2,3} and associated_symptoms=={1,3}:
        print("You have a 50% chance of having a bacterial lung infection.")
    elif cough=={2,3} and associated_symptoms=={1,4}:
        print("You have a 55% chance of having a bacterial lung infection.")
    elif cough=={2,3} and associated_symptoms=={1,5}:
        print("You have a 40% chance of having a bacterial lung infection.")
    elif cough=={2,3} and associated_symptoms=={3,4}:
        print("You have a 45% chance of having a bacterial lung infection.")
    elif cough=={2,3} and associated_symptoms=={3,5}:
        print("You have a 35% chance of having a bacterial lung infection.")
    elif cough=={2,3} and associated_symptoms=={4,5}:
        print("You have a 40% chance of having a bacterial lung infection.")
    elif cough=={2,3} and associated_symptoms=={1,3,4}:
        print("You have a 45% chance of having a bacterial lung infection.") 
    elif cough=={2,3} and associated_symptoms=={1,3,5}:
        print("You have a 45% chance of having a bacterial lung infection.")
    elif cough=={2,3} and associated_symptoms=={3,4,5}:
        print("You have a 50% chance of having a bacterial lung infection.")
    elif cough=={2,3} and associated_symptoms=={1,2,3,4}:
        print("You have a 65% chance of having a bacterial lung infection.")
    elif cough=={2,3} and associated_symptoms=={16}:
        print("You have a 75% chance of having a bacterial lung infection.")
    
    #Mucoid and purulent sputum without blood
    elif cough=={2,4} and associated_symptoms=={1}:
        print("You have a 35% chance of having a bacterial lung infection.")
    elif cough=={2,4} and associated_symptoms=={3}:
        print("You have a 40% chance of having a bacterial lung infection.")
    elif cough=={2,4} and associated_symptoms=={4}:
        print("You have a 45% chance of having a bacterial lung infection.")
    elif cough=={2,4} and associated_symptoms=={5}:
        print("You have a 30% chance of having a bacterial lung infection.")
    elif cough=={2,4} and associated_symptoms=={1,3}:
        print("You have a 45% chance of having a bacterial lung infection.")
    elif cough=={2,4} and associated_symptoms=={1,4}:
        print("You have a 50% chance of having a bacterial lung infection.")
    elif cough=={2,4} and associated_symptoms=={1,5}:
        print("You have a 35% chance of having a bacterial lung infection.")
    elif cough=={2,4} and associated_symptoms=={3,4}:
        print("You have a 40% chance of having a bacterial lung infection.")
    elif cough=={2,4} and associated_symptoms=={3,5}:
        print("You have a 30% chance of having a bacterial lung infection.")
    elif cough=={2,4} and associated_symptoms=={4,5}:
        print("You have a 35% chance of having a bacterial lung infection.")
    elif cough=={2,4} and associated_symptoms=={1,3,4}:
        print("You have a 55% chance of having a bacterial lung infection.")
    elif cough=={2,4} and associated_symptoms=={1,3,5}:
        print("You have a 40% chance you have a bacterial lung infection.")
    elif cough=={2,4} and associated_symptoms=={3,4,5}:
        print("You have a 45% chance you have a bacterial lung infection.")
    elif cough=={2,4} and associated_symptoms=={1,2,3,4}:
        print("You have a 60% chance you have a bacterial lung infection.")
    elif cough=={2,4} and associated_symptoms=={16}:
        print("You have a 65% chance you have a bacterial lung infection.")
    
    #Purulent sputum with blood and purulent sputum without blood
    elif cough=={3,4} and associated_symptoms=={1}:
        print("You have a 35% chance of having a bacterial lung infection.")
    elif cough=={3,4} and associated_symptoms=={3}:
        print("You have a 40% chance of having a bacterial lung infection.")
    elif cough=={3,4} and associated_symptoms=={4}:
        print("You have a 45% chance of having a bacterial lung infection.")
    elif cough=={3,4} and associated_symptoms=={5}:
        print("You have a 30% chance of having a bacterial lung infection.")
    elif cough=={3,4} and associated_symptoms=={1,3}:
        print("You have a 45% chance of having a bacterial lung infection.")
    elif cough=={3,4} and associated_symptoms=={1,4}:
        print("You have a 50% chance of having a bacterial lung infection.")
    elif cough=={3,4} and associated_symptoms=={1,5}:
        print("You have a 35% chance of having a bacterial lung infection.")
    elif cough=={3,4} and associated_symptoms=={3,4}:
        print("You have a 40% chance of having a bacterial lung infection.")
    elif cough=={3,4} and associated_symptoms=={3,5}:
        print("You have a 30% chance of having a bacterial lung infection.")
    elif cough=={3,4} and associated_symptoms=={4,5}:
        print("You have a 35% chance of having a bacterial lung infection.")
    elif cough=={3,4} and associated_symptoms=={1,3,4}:
        print("You have a 55% chance of having a bacterial lung infection.")
    elif cough=={3,4} and associated_symptoms=={1,3,5}:
        print("You have a 40% chance of having a bacterial lung infection.")
    elif cough=={3,4} and associated_symptoms=={3,4,5}:
        print("You have a 50% chance of having a bacterial lung infection.")
    elif cough=={3,4} and associated_symptoms=={1,2,3,4}:
        print("You have a 60% chance of having a bacterial lung infection.")
    elif cough=={3,4} and associated_symptoms=={16}:
        print("You have a 68% chance of having a bacterial lung infection.")
    
    #Mucoid and purulent sputum with blood and purulent sputum without Blood
    elif cough=={2,3,4} and associated_symptoms=={1}:
        print("You have a 40% chance of having a bacterial lung infection.")
    elif cough=={2,3,4} and associated_symptoms=={3}:
        print("You have a 45% chance of having a bacterial lung infection.")
    elif cough=={2,3,4} and associated_symptoms=={4}:
        print("You have a 50% chance of having a bacterial lung infection.")
    elif cough=={2,3,4} and associated_symptoms=={5}:
        print("You have a 35% chance of having a bacterial lung infection.")
    elif cough=={2,3,4} and associated_symptoms=={1,3}:
        print("You have a 50% chance of having a bacterial lung infection.")
    elif cough=={2,3,4} and associated_symptoms=={1,4}:
        print("You have a 55% chance of having a bacterial lung infection.")
    elif cough=={2,3,4} and associated_symptoms=={1,5}:
        print("You have a 40% chance of having a bacterial lung infection.")
    elif cough=={2,3,4} and associated_symptoms=={3,4}:
        print("You have a 45% chance of having a bacterial lung infection.")
    elif cough=={2,3,4} and associated_symptoms=={3,5}:
        print("You have a 35% chance of having a bacterial lung infection.")
    elif cough=={2,3,4} and associated_symptoms=={4,5}:
        print("You have a 40% chance of having a bacterial lung infection.")
    elif cough=={2,3,4} and associated_symptoms=={1,3,4}:
        print("You have a 60% chance of having a bacterial lung infection.")
    elif cough=={2,3,4} and associated_symptoms=={1,3,5}:
        print("You have a 45% chance of having a bacterial lung infection.")
    elif cough=={2,3,4} and associated_symptoms=={3,4,5}:
        print("You have a 50% chance of having a bacterial lung infection.")
    elif cough=={2,3,4} and associated_symptoms=={1,2,3,4}:
        print("You have a 65% chance of having a bacterial lung infection.")
    elif cough=={2,3,4} and associated_symptoms=={16}:
        print("You have an 80% chance of having a bacterial lung infection.")
    print("Our recommended treatment is antibiotics. But The percentage of probability mentioned is approximate. Be sure to consult a doctor to receive the exact dosage of the medicine and type of antibiotic.")
    
    #Viral sinusitis or bacterial sinusitis or allergies (postnasal drip)
    #Mucoid sputum
    if cough=={2} and associated_symptoms=={6}:
        print("You have a 30% chance of having viral sinusitis and a 25% chance of having bacterial sinusitis. You have a 20% chance of having allergies.")
    
    #Purulent sputum without blood
    elif cough=={4} and associated_symptoms=={6}:
        print("You have a 25% chance of having viral sinusitis and a 20% chance of having bacterial sinusitis. You have a 15% chance of having allergies.")
    
    #Chronic cough
    elif cough=={6} and associated_symptoms=={6}:
        print("You have a 20% chance of having viral sinusitis and a 15% chance of having bacterial sinusitis. You have a 10% chance of having allergies.")
    
    #Mucoid sputum and purulent sputum without blood
    elif cough=={2,4} and associated_symptoms=={6}:
        print("You have a 35% chance of having viral sinusitis and a 30% chance of having bacterial sinusitis. You have a 25% chance of having allergies.")
    
    #Mucoid sputum and chronic cough
    elif cough=={2,6} and associated_symptoms=={6}:
        print("You have a 25% chance of having viral sinusitis and a 20% chance of having bacterial sinusitis. You have a 20% chance of having allergies.")
    
    #Purulent sputum without blood and chronic cough
    elif cough=={4,6} and associated_symptoms=={6}:
        print("You have a 35% chance of having viral sinusitis and a 25% chance of having bacterial sinusitis. You have a 20% chance of having allergies.")
    
    #Mucoid sputum and purulent sputum without blood and chronic cough
    elif cough=={2,4,6} and associated_symptoms=={6}:
        print("You have a 40% chance of having viral sinusitis, a 35% chance of having bacterial sinusitis, and a 30% chance of having allergies.")
    
    #No associated symptoms
    elif cough=={2} and associated_symptoms=={16}:
        print("You have a 50% chance of having viral sinusitis, a 20% chance of having bacterial sinusitis, and a 40% chance of having allergies.")
    elif cough=={4} and associated_symptoms=={16}:
        print("You have a 30% chance of having viral sinusitis, a 70% chance of having bacterial sinusitis, and a 10% chance of having allergies.")
    elif cough=={6} and associated_symptoms=={16}:
        print("You have a 20% chance of having viral sinusitis, a 30% chance of having bacterial sinusitis, and a 50% chance of having allergies.")
    elif cough=={2,4} and associated_symptoms=={16}:
        print("You have a 40% chance of having viral sinusitis and a 60% chance of having bacterial sinusitis. You have a 25% chance of having allergies.")
    elif cough=={2,6} and associated_symptoms=={16}:
        print("You have a 35% chance of having viral sinusitis and a 25% chance of having bacterial sinusitis. You have a 45% chance of having allergies.")
    elif cough=={4,6} and associated_symptoms=={16}:
        print("You have a 30% chance of having viral sinusitis and a 70% chance of having bacterial sinusitis. You have a 20% chance of having allergies.")
    elif cough=={2,4,6} and associated_symptoms=={16}:
        print("You have a 25% chance of having viral sinusitis and a 75% chance of having bacterial sinusitis. You have a 25% chance of having viral sinusitis and a 75% chance of having bacterial sinusitis. 30% of you have allergies.")
    print("Our suggested treatment is an anti-inflammatory such as acetaminophen if it is a virus, antibiotics if it is a bacterial agent, and antihistamines if it is an allergy. The percentage of probability mentioned is approximate. Be sure to consult a doctor for the exact dosage and type of antibiotic or anti-inflammatory drug")
    
    
    #Tuberculosis
    #Dry cough
    if cough=={1} and associated_symptoms=={1}:
        print("You have a 20% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={7}:
        print("You have a 15% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={8}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={9}:
        print("You have a 20% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={10}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={1,7}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={1,8}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={1,9}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={1,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={7,8}:
        print("You have a 20% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={7,9}:
        print("You have a 15% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={7,10}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={8,9}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={8,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={9,10}:
        print("You have a 20% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={1,7,8}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={1,7,9}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={1,7,10}:
        print("You have a 25% chance of having pulmonary tuberculosis.") 
    elif cough=={1} and associated_symptoms=={1,8,9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={1,8,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={1,9,10}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={7,8,9}:
        print("You have a 20% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={7,8,10}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={7,9,10}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={8,9,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={1,7,8,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={1,7,8,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={1,7,9,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={1,8,9,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={7,8,9,10}:
        print("There is a 50% chance of having pulmonary tuberculosis.")
    elif cough=={1} and associated_symptoms=={1,7,8,9,10}:
        print("There is a 60% chance of having pulmonary tuberculosis.")
    
    #Mucoid sputum
    elif cough=={2} and associated_symptoms=={1}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={7}:
        print("You have a 20% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={8}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={9}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={1,7}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={1,8}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={1,9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={1,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={7,8}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={7,9}:
        print("You have a 20% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={7,10}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={8,9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={8,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={9,10}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={1,7,8}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={1,7,9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={1,7,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={1,8,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={1,8,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={1,9,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={7,8,9}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={7,8,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={7,9,10}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={8,9,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={1,7,8,9}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={1,7,8,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={1,7,9,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={1,8,9,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.") 
    elif cough=={2} and associated_symptoms=={7,8,9,10}:
        print("There is a 50% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={1,7,8,9,10}:
        print("There is a 65% chance of having pulmonary tuberculosis.")
        
    #Purulent sputum mixed with blood
    elif cough=={3} and associated_symptoms=={1}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={7}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={8}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={1,7}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={1,8}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={1,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={1,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={7,8}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={7,9}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={7,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={8,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={8,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={9,10}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={1,7,8}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={1,7,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={1,7,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.") 
    elif cough=={3} and associated_symptoms=={1,8,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={1,8,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={1,9,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={7,8,9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={7,8,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={7,9,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={8,9,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={1,7,8,9}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={1,7,8,10}:
        print("You have a 60% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={1,7,9,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={1,8,9,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.") 
    elif cough=={3} and associated_symptoms=={1,7,8,9,10}:
        print("There is a 70% chance of having pulmonary tuberculosis.")
        
    #Purulent sputum full of blood
    elif cough=={5} and associated_symptoms=={1}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={7}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={8}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={1,7}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={1,8}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={1,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={1,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={7,8}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={7,9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={7,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={8,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={8,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={9,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={1,7,8}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={1,7,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={1,7,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.") 
    elif cough=={5} and associated_symptoms=={1,8,9}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={1,8,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={1,9,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={7,8,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={7,8,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={7,9,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={8,9,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={1,7,8,9}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={1,7,8,10}:
        print("You have a 65% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={1,7,9,10}:
        print("You have a 60% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={1,8,9,10}:
        print("You have a 60% chance of having pulmonary tuberculosis.") 
    elif cough=={5} and associated_symptoms=={7,8,9,10}:
        print("There is a 60% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={1,7,8,9,10}:
        print("There is a 75% chance of having pulmonary tuberculosis.")
        
    #Dry cough and mucoid sputum
    elif cough=={1,2} and associated_symptoms=={1}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={7}:
        print("You have a 20% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={8}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={9}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={1,7}:
        print("You have a 20% chance of having pulmonary tuberculosis.") 
    elif cough=={1,2} and associated_symptoms=={1,8}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={1,9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={1,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={7,8}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={7,9}:
        print("You have a 20% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={7,10}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={8,9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={8,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={9,10}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={1,7,8}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={1,7,9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={1,7,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={1,8,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={1,8,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={1,9,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={7,8,9}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={7,8,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={7,9,10}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={8,9,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={1,7,8,9}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={1,7,8,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={1,7,9,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={1,8,9,10}:
        print("You have a 60% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={7,8,9,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={1,7,8,9,10}:
        print("You have a 65% chance of having pulmonary tuberculosis.")
        
    #Dry cough and blood-tinged purulent sputum
    elif cough=={1,3} and associated_symptoms=={1}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={7}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={8}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={1,7}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={1,8}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={1,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={1,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={7,8}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={7,9}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={7,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={8,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={8,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={9,10}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={1,7,8}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={1,7,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={1,7,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={1,8,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={1,8,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={1,9,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={7,8,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.") 
    elif cough=={1,3} and associated_symptoms=={7,8,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={7,9,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={8,9,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={1,7,8,9}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={1,7,8,10}:
        print("You have a 60% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={1,7,9,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={1,8,9,10}:
        print("You have a 65% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={7,8,9,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={1,7,8,9,10}:
        print("You have a 70% chance of having pulmonary tuberculosis.")
    
    #Dry cough and purulent sputum completely bloody
    elif cough=={1,5} and associated_symptoms=={1}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={7}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={8}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={1,7}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={1,8}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={1,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={1,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={7,8}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={7,9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={7,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={8,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={8,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={9,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={1,7,8}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={1,7,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={1,7,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={1,8,9}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={1,8,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={1,9,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={7,8,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={7,8,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={7,9,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={8,9,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={1,7,8,9}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={1,7,8,10}:
        print("You have a 65% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={1,7,9,10}:
        print("You have a 60% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={1,8,9,10}:
        print("You have a 70% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={7,8,9,10}:
        print("You have a 60% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={1,7,8,9,10}:
        print("You have a 75% chance of having pulmonary tuberculosis.")
        
    #Mucoid and purulent sputum stained with blood
    elif cough=={2,3} and associated_symptoms=={1}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={7}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={8}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={1,7}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={1,8}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={1,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={1,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={7,8}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={7,9}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={7,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={8,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={8,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={9,10}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={1,7,8}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={1,7,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={1,7,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={1,8,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={1,8,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={1,9,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={7,8,9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={7,8,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={7,9,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={8,9,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={1,7,8,9}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={1,7,8,10}:
        print("You have a 60% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={1,7,9,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={1,8,9,10}:
        print("You have a 65% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={7,8,9,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={1,7,8,9,10}:
        print("You have a 70% chance of having pulmonary tuberculosis.")
        
    #Mucoid and purulent sputum full of blood
    elif cough=={2,5} and associated_symptoms=={1}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={7}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={8}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={1,7}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={1,8}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={1,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={1,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={7,8}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={7,9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={7,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={8,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={8,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={9,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={1,7,8}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={1,7,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={1,7,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={1,8,9}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={1,8,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={1,9,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={7,8,9}:
        print("You have a 45% chance of having pulmonary tuberculosis.") 
    elif cough=={2,5} and associated_symptoms=={7,8,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={7,9,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={8,9,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={1,7,8,9}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={1,7,8,10}:
        print("You have a 65% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={1,7,9,10}:
        print("You have a 60% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={1,8,9,10}:
        print("You have a 70% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={7,8,9,10}:
        print("You have a 60% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={1,7,8,9,10}:
        print("You have a 75% chance of having pulmonary tuberculosis.")
    
    #Purulent sputum mixed with blood and purulent sputum completely bloody
    elif cough=={3,5} and associated_symptoms=={1}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={7}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={8}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={1,7}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={1,8}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={1,9}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={1,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={7,8}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={7,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={7,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={8,9}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={8,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={9,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={1,7,8}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={1,7,9}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={1,7,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={1,8,9}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={1,8,10}:
        print("You have a 60% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={1,9,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={7,8,9}:
        print("You have a 50% chance of having pulmonary tuberculosis.") 
    elif cough=={3,5} and associated_symptoms=={7,8,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={7,9,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={8,9,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={1,7,8,9}:
        print("You have a 60% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={1,7,8,10}:
        print("You have a 70% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={1,7,9,10}:
        print("You have a 65% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={1,8,9,10}:
        print("You have a 75% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={7,8,9,10}:
        print("You have a 65% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={1,7,8,9,10}:
        print("You have an 80% chance of having pulmonary tuberculosis.")
    
    #Dry cough and mucoid sputum and purulent sputum mixed with blood
    elif cough=={1,2,3} and associated_symptoms=={1}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={7}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={8}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={1,7}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={1,8}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={1,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={1,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={7,8}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={7,9}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={7,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={8,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={8,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={9,10}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={1,7,8}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={1,7,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={1,7,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={1,8,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={1,8,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={1,9,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={7,8,9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={7,8,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={7,9,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={8,9,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={1,7,8,9}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={1,7,8,10}:
        print("You have a 60% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={1,7,9,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={1,8,9,10}:
        print("You have a 65% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={7,8,9,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={1,7,8,9,10}:
        print("You have a 70% chance of having pulmonary tuberculosis.")
        
    #Dry cough and mucoid sputum and purulent sputum completely bloody
    elif cough=={1,2,5} and associated_symptoms=={1}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={7}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={8}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={1,7}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={1,8}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={1,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={1,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={7,8}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={7,9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={7,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={8,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={8,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={9,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={1,7,8}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={1,7,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={1,7,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={1,8,9}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={1,8,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={1,9,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={7,8,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={7,8,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={7,9,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={8,9,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={1,7,8,9}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={1,7,8,10}:
        print("You have a 65% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={1,7,9,10}:
        print("You have a 60% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={1,8,9,10}:
        print("You have a 70% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={7,8,9,10}:
        print("You have a 60% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={1,7,8,9,10}:
        print("You have a 75% chance of having pulmonary tuberculosis.")
    
        #Mucoid sputum and purulent sputum mixed with blood and purulent sputum completely bloody
    elif cough=={2,3,5} and associated_symptoms=={1}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={7}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={8}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={1,7}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={1,8}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={1,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={1,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={7,8}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={7,9}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={7,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={8,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={8,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={9,10}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={1,7,8}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={1,7,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={1,7,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={1,8,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={1,8,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={1,9,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={7,8,9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={7,8,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={7,9,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={8,9,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={1,7,8,9}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={1,7,8,10}:
        print("You have a 60% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={1,7,9,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={1,8,9,10}:
        print("You have a 65% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={7,8,9,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={2,3,5} and associated_symptoms=={1,7,8,9,10}:
        print("You have a 70% chance of having pulmonary tuberculosis.")     

    #Dry cough and mucoid sputum and purulent sputum mixed with blood and purulent sputum completely bloody
    elif cough=={1,2,3,5} and associated_symptoms=={1}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={7}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={8}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={1,7}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={1,8}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={1,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={1,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={7,8}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={7,9}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={7,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={8,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={8,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={9,10}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={1,7,8}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={1,7,9}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={1,7,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={1,8,9}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={1,8,10}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={1,9,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={7,8,9}:
        print("You have a 35% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={7,8,10}:
        print("You have a 45% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={7,9,10}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={8,9,10}:
        print("You have a 50% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={1,7,8,9}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={1,7,8,10}:
        print("You have a 65% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={1,7,9,10}:
        print("You have a 60% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={1,8,9,10}:
        print("You have a 70% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={7,8,9,10}:
        print("You have a 60% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={1,7,8,9,10}:
        print("You have a 75% chance of having pulmonary tuberculosis.")               
        
    #No associated symptoms
    elif cough=={1} and associated_symptoms=={16}:
        print("You have a 30% chance of having pulmonary tuberculosis.")
    elif cough=={2} and associated_symptoms=={16}:
        print("You have a 25% chance of having pulmonary tuberculosis.")
    elif cough=={3} and associated_symptoms=={16}:
        print("You have an 80% chance of having pulmonary tuberculosis.")
    elif cough=={5} and associated_symptoms=={16}:
        print("You have a 65% chance of having pulmonary tuberculosis.")
    elif cough=={1,2} and associated_symptoms=={16}:
        print("You have a 40% chance of having pulmonary tuberculosis.")
    elif cough=={1,3} and associated_symptoms=={16}:
        print("You have a 70% chance of having pulmonary tuberculosis.")
    elif cough=={1,5} and associated_symptoms=={16}:
        print("You have a 55% chance of having pulmonary tuberculosis.")
    elif cough=={2,3} and associated_symptoms=={16}:
        print("You have a 75% chance of having pulmonary tuberculosis.")
    elif cough=={2,5} and associated_symptoms=={16}:
        print("You have a 60% chance of having pulmonary tuberculosis.")
    elif cough=={3,5} and associated_symptoms=={16}:
        print("You have a 72% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3} and associated_symptoms=={16}:
        print("You have an 80% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,5} and associated_symptoms=={16}:
        print("You have a 65% chance of having pulmonary tuberculosis.")
    elif cough=={1,2,3,5} and associated_symptoms=={16}:
        print("You have an 80% chance of having pulmonary tuberculosis.")
    print("The solution is to see a doctor. The percentage of probability mentioned is approximate. Be sure to see a doctor to get the exact dose and type of medicine")
    
    #Lung Abscess
    #Purulent Sputum Stained with Blood Blood
    if cough=={3} and associated_symptoms=={1}:
        print("You have a 35% chance of having a lung abscess.")
    elif cough=={3} and associated_symptoms=={12}:
        print("You have a 40% chance of having a lung abscess.")
    elif cough=={3} and associated_symptoms=={1,12}:
        print("You have a 45% chance of having a lung abscess.")
    
    #Purulent Sputum Without Blood
    elif cough=={4} and associated_symptoms=={1}:
        print("You have a 30% chance of having a lung abscess.")
    elif cough=={4} and associated_symptoms=={12}:
        print("You have a 35% chance of having a lung abscess.")
    elif cough=={4} and associated_symptoms=={1,12}:
        print("You have a 40% chance of having a lung abscess.")
    
    #Purulent sputum completely bloody
    elif cough=={5} and associated_symptoms=={1}:
        print("You have a 40% chance of having a lung abscess.")
    elif cough=={5} and associated_symptoms=={12}:
        print("You have a 45% chance of having a lung abscess.")
    elif cough=={5} and associated_symptoms=={1,12}:
        print("You have a 50% chance of having a lung abscess.")
    
    #Purulent sputum without blood and purulent sputum mixed with blood
    elif cough=={3,4} and associated_symptoms=={1}:
        print("You have a 35% chance of having a lung abscess.")
    elif cough=={3,4} and associated_symptoms=={12}:
        print("You have a 40% chance of having a lung abscess.")
    elif cough=={3,4} and associated_symptoms=={1,12}:
        print("You have a 45% chance of having a lung abscess.")
    
    #Purulent sputum without blood and purulent sputum mixed with blood
    elif cough=={3,5} and associated_symptoms=={1}:
        print("You have a 40% chance of having a lung abscess.")
    elif cough=={3,5} and associated_symptoms=={12}:
        print("You have a 45% chance of having a lung abscess.")
    elif cough=={3,5} and associated_symptoms=={1,12}:
        print("You have a 50% chance of having a lung abscess.")
    
    #Purulent sputum without blood and purulent sputum mixed with blood
    elif cough=={3,5} and associated_symptoms=={1}:
        print("You have a 35% chance of having a lung abscess.")
    elif cough=={3,5} and associated_symptoms=={12}:
        print("You have a 40% chance of having a lung abscess.")
    elif cough=={3,5} and associated_symptoms=={1,12}:
        print("You have a 45% chance of having a lung abscess.")
    
    #Purulent sputum mixed with blood and purulent sputum completely bloody
    elif cough=={4,5} and associated_symptoms=={1}:
        print("You have a 45% chance of having a lung abscess.")
    elif cough=={4,5} and associated_symptoms=={12}:
        print("You have a 50% chance of having a lung abscess.")
    elif cough=={4,5} and associated_symptoms=={1,12}:
        print("You have a 55% chance of having a lung abscess.")
    
    #Purulent sputum without blood and purulent sputum stained with blood and purulent sputum completely bloody
    elif cough=={4,5} and associated_symptoms=={1}:
        print("You have a 45% chance of having a lung abscess.")
    elif cough=={4,5} and associated_symptoms=={12}:
        print("You have a 50% chance of having a lung abscess.")
    elif cough=={4,5} and associated_symptoms=={1,12}:
        print("You have a 55% chance of having a lung abscess.")
    
    #No associated symptoms
    elif cough=={3} and associated_symptoms=={16}:
        print("You have a 60-70% chance of having a lung abscess.")
    elif cough=={5} and associated_symptoms=={16}:
        print("You have a 70-80% chance of having a lung abscess.")
    elif cough=={4,5} and associated_symptoms=={16}:
        print("You have a 60-75% chance of having a lung abscess.")
    print("The solution is to see a doctor, take antibiotics and have it checked out, and if it is serious, have surgery. The percentage of probability mentioned is approximate, be sure to see a doctor for an examination")
    
    #Asthma
    #Mucoid phlegm
    if cough=={2} and associated_symptoms=={3}:
        print("You have a 60% chance of having asthma.")
    elif cough=={2} and associated_symptoms=={13}:
        print("You have a 45% chance of having asthma.")
    elif cough=={2} and associated_symptoms=={15}:
        print("You have a 55% chance of having asthma.")
    elif cough=={2} and associated_symptoms=={3}:
        print("You have a less than 30% chance of having asthma.")
    elif cough=={2} and associated_symptoms=={3,13}:
        print("You have a 70% chance of having asthma.")
    elif cough=={2} and associated_symptoms=={3,15}:
        print("You have a 75% chance of having asthma.")
    elif cough=={2} and associated_symptoms=={13,15}:
        print("You have a 60% chance of having asthma.")
    elif cough=={2} and associated_symptoms=={1,13,15}:
        print("You have an 80% chance of having asthma.")
    elif cough=={2} and associated_symptoms=={16}:
        print("You have a 10-20% chance of having asthma.")
    print("The treatment solution is to use 'Salbutamol spray' first and if it does not improve, then use 'Fludrocortisone' corticosteroid spray. 'Salmetrol' spray can also be used as an airway dilator\n. The percentage of probability mentioned is approximate. Be sure to consult a doctor for an examination")
    
    #Gastroesophageal reflux
    #Chronic cough, especially at night
    if cough=={6} and associated_symptoms=={14}:
        print("You have a 50% chance of having gastroesophageal reflux.")
    elif cough=={6} and associated_symptoms=={15}:
        print("You have a 40% chance of having gastroesophageal reflux.")
    elif cough=={6} and associated_symptoms=={14,15}:
        print("You have a 60% chance of having gastroesophageal reflux.")
    elif cough=={6} and associated_symptoms=={16}:
        print("You have a 30% chance of having gastroesophageal reflux.")
    print("The treatment solution is to use stomach syrups such as aluminum-MGS syrup. The use of omeprazole and if it is very severe, the use of injectable pantoprazole is recommended\n . The percentage of probability mentioned is approximate. Be sure to consult a doctor for examination. ")
    
    #Chemical particles
    #Coughing varies at specific times and places
    if cough=={7} and associated_symptoms=={11}:
        print("You have a 60% chance of getting a cough from exposure to chemical particles.")
    elif cough=={7} and associated_symptoms=={16}:
        print("You have a 30% chance of getting a cough from exposure to chemical particles.")
    print("Our recommended solution is to rest and avoid further contact with the contaminant. The percentage of probability mentioned is approximate. Be sure to see a doctor for a checkup")
    
    
    
    
    

elif A == 4:
    print("You have back pain.")

elif A == 5:
    print("You have shortness of breath.")

else:
    print("Sorry, the information in this program does not currently support the disease with these symptoms. The program is being completed.")

print("\nThis program is only for the initial diagnosis of the disease. Please see a doctor for an accurate diagnosis and additional tests, and take medication after consulting a doctor.\nThank you\nSaris Programming Group")
#finish 2025/3/1