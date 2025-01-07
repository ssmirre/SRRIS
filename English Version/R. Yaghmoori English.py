 # مشخصات بیمار

print("Please enter your details.")
Name = input("name: ")
Last_name = input("last Name: ")
Age =int(input("age: "))
Gender = input("gender: ")
print()
print(f"hi {Name} ! In this program, we aim to provide an initial diagnosis of your condition and offer you suggestions for solutions.")
print()


# تشخیص علائم اصلی بیمار
print("This program is currently focused on 5 main symptoms of the disease:")
print("1- Stomach pain\n2- Chest pain\n3- Cough\n4- Back pain\n5- shortness of breath")
while True :
    Main_symptoms =int(input("Please select a number to indicate your primary symptom: "))
    if 1<=int(Main_symptoms)<=5: 
        # if int(Main_symptoms) ==1:
        #     print('Now, we need to check what symptoms accompany "Stomach pain".')
        #     print()
            
        # elif int(Main_symptoms) ==2:
        #     print('Now, we need to check what symptoms accompany "Chest pain".')
        #     print()
                        
        # elif int(Main_symptoms) ==3:
        #     print('Now, we need to check what symptoms accompany "Cough".')
        #     print()
            
        # elif int(Main_symptoms) ==4:
        #     print('Now, we need to check what symptoms accompany "Back pain".')
        #     print()
                            
        if int(Main_symptoms) ==5:
            print('Now, we need to check what symptoms accompany "shortness of breath".')
            print()
            
            # تشخیص علائم همراه
            
            print("Please choose from the following symptoms.") 
            print("(If your selections are more than one, please separate them with commas (,).\nexample: 1,10,11 )")
            print("1- Cough\n2- Nocturnal shortness of breath\n3- Wheezing (the sound of excess air escaping from the lungs)\n4- Rale\n5- Chest tightness\n6- Mucoid (gelatinous)sputum\n7- Fever\n8- Palpitations\n9- Dizziness\n10- Numbness and tingling in the hands and feet\n11- Without Associated symptoms")
            print()
            
            while True :         #تنگی نفس دارد/ حلقه برای وارد کردن درست علائم همراه
                Associated_symptoms= input("Which symptoms do you have? ")
                try:
                    Associated_symptoms=set(map(int,Associated_symptoms.split(",")))
                    break     #توقف حلقه دوم/ اگر داده های علائم همراه را درست وارد کرد متوقف شو
                except ValueError :
                    print()
                    print("Please make sure to follow the guidelines below when entering data and re-enter the information:\n1- Please switch your keyboard to English.\n2- Make sure to place a comma (,) between the numbers.\n3- Do not use the spacebar.\nexample: 1,10,11")
                    
                    # تشخیص شرایط زمینه ای بیمار
                    
            print()
            print("Your associated symptoms have been recorded..")
            print()
            print (" Now, we need to determine what underlying conditions have affected your disease. ")
            print()
            print("Please select from the following conditions.") 
            print("If your selections are more than one, please separate them with commas (,).\nexample: 1,6,7 )")
            print("1- History of heart disease\n2- Environmental conditions\n3- History of smoking\n4- Pollutant\n5- Variable\n6- Chest pain\n7- Without underlying conditions")
            print()
            while True :         #حلقه برای درست وارد کردن شرایط زمینه ای
                Predisposing_factors=input("What underlying conditions do you have? ")
                try:
                    Predisposing_factors=set(map(int,Predisposing_factors.split(",")))
                    break
                except ValueError :
                    print()
                    print("Please make sure to follow the guidelines below when entering data and re-enter the information:\n1- Please switch your keyboard to English.\n2- Make sure to place a comma (,) between the numbers.\n3- Do not use the spacebar.\nexample: 1,6,7")
            
            
 # بیماری 1 : نارسایی قلبی
             
          # سابقه : بیماری قلبی
                    
            Final_diagnosis="Undiagnosed"        
            Probability_percentage="Undiagnosed"
            if Predisposing_factors=={1} and Associated_symptoms=={1}:
                Final_diagnosis="Heart failure" 
                Probability_percentage=60
            elif Predisposing_factors=={1} and Associated_symptoms=={2}:                     
                Final_diagnosis="Heart failure"
                Probability_percentage=70
            elif Predisposing_factors=={1} and Associated_symptoms=={3}:
                Final_diagnosis="Heart failure"
                Probability_percentage=50
            elif Predisposing_factors=={1} and Associated_symptoms=={1,2}:
                Final_diagnosis="Heart failure"
                Probability_percentage=80       
            elif Predisposing_factors=={1} and Associated_symptoms=={1,3}:
                Final_diagnosis="Heart failure"
                Probability_percentage=65      
            elif Predisposing_factors=={1} and Associated_symptoms=={2,3}:
                Final_diagnosis="Heart failure"
                Probability_percentage=75       
            elif Predisposing_factors=={1} and Associated_symptoms=={1,2,3}:
                Final_diagnosis="Heart failure"
                Probability_percentage=85       
            elif Predisposing_factors=={1} and Associated_symptoms=={11}:
                Final_diagnosis="Heart failure"
                Probability_percentage=10       
            
                      

# بیماری 1 : نارسایی قلبی

# سابقه : بدون شرایط


            elif Predisposing_factors=={7} and Associated_symptoms=={1}:
                Final_diagnosis="Heart failure" 
                Probability_percentage=20
            elif Predisposing_factors=={7} and Associated_symptoms=={2}:                     
                Final_diagnosis="Heart failure"
                Probability_percentage=25
            elif Predisposing_factors=={7} and Associated_symptoms=={3}:
                Final_diagnosis="Heart failure"
                Probability_percentage=15
            elif Predisposing_factors=={7} and Associated_symptoms=={1,2}:
                Final_diagnosis="Heart failure"
                Probability_percentage=30       
            elif Predisposing_factors=={7} and Associated_symptoms=={1,3}:
                Final_diagnosis="Heart failure"
                Probability_percentage=20      
            elif Predisposing_factors=={7} and Associated_symptoms=={2,3}:
                Final_diagnosis="Heart failure"
                Probability_percentage=25       
            elif Predisposing_factors=={7} and Associated_symptoms=={1,2,3}:
                Final_diagnosis="Heart failure"
                Probability_percentage=30       
            elif Predisposing_factors=={7} and Associated_symptoms=={11}:
                Final_diagnosis="Heart failure"
                Probability_percentage=5
            
     
#############################################################################################           
            
# بیماری 2 : آسم

# سابقه : شرایط محیطس
                    

            elif Predisposing_factors=={1} and Associated_symptoms=={1}:
                Final_diagnosis="Asthma" 
                Probability_percentage=60
            elif Predisposing_factors=={1} and Associated_symptoms=={4}:                     
                Final_diagnosis="Asthma"
                Probability_percentage=75
            elif Predisposing_factors=={1} and Associated_symptoms=={5}:
                Final_diagnosis="Asthma"
                Probability_percentage=70
            elif Predisposing_factors=={1} and Associated_symptoms=={1,4}:
                Final_diagnosis="Asthma"
                Probability_percentage=85       
            elif Predisposing_factors=={1} and Associated_symptoms=={1,5}:
                Final_diagnosis="Asthma"
                Probability_percentage=80      
            elif Predisposing_factors=={1} and Associated_symptoms=={4,5}:
                Final_diagnosis="Asthma"
                Probability_percentage=58       
            elif Predisposing_factors=={1} and Associated_symptoms=={1,4,5}:
                Final_diagnosis="Asthmaم"
                Probability_percentage=90       
            elif Predisposing_factors=={1} and Associated_symptoms=={11}:
                Final_diagnosis="Asthma"
                Probability_percentage=30         
        
        
# بیماری 2 : آسم

# سابقه : بدون شرایط
                    

            elif Predisposing_factors=={7} and Associated_symptoms=={1}:
                Final_diagnosis="Asthma" 
                Probability_percentage=40
            elif Predisposing_factors=={7} and Associated_symptoms=={4}:                     
                Final_diagnosis="Asthma"
                Probability_percentage=55
            elif Predisposing_factors=={7} and Associated_symptoms=={5}:
                Final_diagnosis="Asthma"
                Probability_percentage=50
            elif Predisposing_factors=={7} and Associated_symptoms=={1,4}:
                Final_diagnosis="Asthma"
                Probability_percentage=65       
            elif Predisposing_factors=={7} and Associated_symptoms=={1,5}:
                Final_diagnosis="Asthma"
                Probability_percentage=60      
            elif Predisposing_factors=={7} and Associated_symptoms=={4,5}:
                Final_diagnosis="Asthma"
                Probability_percentage=65       
            elif Predisposing_factors=={7} and Associated_symptoms=={1,4,5}:
                Final_diagnosis="Asthma"
                Probability_percentage=70       
            elif Predisposing_factors=={7} and Associated_symptoms=={11}:
                Final_diagnosis="Asthma"
                Probability_percentage=10
                
                

#########################################################################################              
            
            
# بیماری 3 : COPD

# سابقه : مصرف سیگار
                    

            elif Predisposing_factors=={3} and Associated_symptoms=={1}:
                Final_diagnosis="COPD" 
                Probability_percentage=70
            elif Predisposing_factors=={3} and Associated_symptoms=={6}:                     
                Final_diagnosis="COPD"
                Probability_percentage=75
            elif Predisposing_factors=={3} and Associated_symptoms=={1,6}:
                Final_diagnosis="COPD"
                Probability_percentage=80
            elif Predisposing_factors=={3} and Associated_symptoms=={11}:
                Final_diagnosis="COPD"
                Probability_percentage=30
                
         
        
 # بیماری 3 : COPD

 # سابقه : آلاینده
                     

            elif Predisposing_factors=={4} and Associated_symptoms=={1}:
                Final_diagnosis="COPD" 
                Probability_percentage=65
            elif Predisposing_factors=={4} and Associated_symptoms=={6}:                     
                Final_diagnosis="COPD"
                Probability_percentage=70
            elif Predisposing_factors=={4} and Associated_symptoms=={1,6}:
                Final_diagnosis="COPD"
                Probability_percentage=75
            elif Predisposing_factors=={4} and Associated_symptoms=={11}:
                Final_diagnosis="COPD"
                Probability_percentage=25           
        
        
 # بیماری 3 : COPD

 # سابقه : بدون شرایط
                     

            elif Predisposing_factors=={7} and Associated_symptoms=={1}:
                Final_diagnosis="COPD" 
                Probability_percentage=60
            elif Predisposing_factors=={7} and Associated_symptoms=={6}:                     
                Final_diagnosis="COPD"
                Probability_percentage=65
            elif Predisposing_factors=={7} and Associated_symptoms=={1,6}:
                Final_diagnosis="COPD"
                Probability_percentage=70
            elif Predisposing_factors=={7} and Associated_symptoms=={11}:
                Final_diagnosis="COPD"
                Probability_percentage=20          
        
        
 # بیماری 3 : COPD

 # سابقه : مصرف سیگار و آلاینده
                     

            elif Predisposing_factors=={3,4} and Associated_symptoms=={1}:
                Final_diagnosis="COPD" 
                Probability_percentage=75
            elif Predisposing_factors=={3,4} and Associated_symptoms=={6}:                     
                Final_diagnosis="COPD"
                Probability_percentage=80
            elif Predisposing_factors=={3,4} and Associated_symptoms=={1,6}:
                Final_diagnosis="COPD"
                Probability_percentage=85
            elif Predisposing_factors=={3,4} and Associated_symptoms=={11}:
                Final_diagnosis="COPD"
                Probability_percentage=35 
                
                
######################################################################################            
            
            
# بیماری 4 : عفونت ریه(پنومونی)

#سابقه : شرایط متغیر
                    

            elif Predisposing_factors=={5} and Associated_symptoms=={1}:
                Final_diagnosis="Lung infection(Pneumonia)" 
                Probability_percentage=70
            elif Predisposing_factors=={5} and Associated_symptoms=={6}:                     
                Final_diagnosis="Lung infection(Pneumonia)"
                Probability_percentage=75
            elif Predisposing_factors=={5} and Associated_symptoms=={7}:
                Final_diagnosis="Lung infection(Pneumonia)"
                Probability_percentage=70
            elif Predisposing_factors=={5} and Associated_symptoms=={1,6}:
                Final_diagnosis="Lung infection(Pneumonia)"
                Probability_percentage=80       
            elif Predisposing_factors=={5} and Associated_symptoms=={1,7}:
                Final_diagnosis="Lung infection(Pneumonia)"
                Probability_percentage=75      
            elif Predisposing_factors=={5} and Associated_symptoms=={6,7}:
                Final_diagnosis="Lung infection(Pneumonia)"
                Probability_percentage=75       
            elif Predisposing_factors=={5} and Associated_symptoms=={1,6,7}:
                Final_diagnosis="Lung infection(Pneumonia)"
                Probability_percentage=85       
            elif Predisposing_factors=={5} and Associated_symptoms=={11}:
                Final_diagnosis="Lung infection(Pneumonia)"
                Probability_percentage=40 
            
        
# بیماری 4 : عفونت ریه(پنومونی)

#سابقه : بدون شرایط
                    

            elif Predisposing_factors=={7} and Associated_symptoms=={1}:
                Final_diagnosis="Lung infection(Pneumonia)" 
                Probability_percentage=60
            elif Predisposing_factors=={7} and Associated_symptoms=={6}:                     
                Final_diagnosis="Lung infection(Pneumonia)"
                Probability_percentage=65
            elif Predisposing_factors=={7} and Associated_symptoms=={7}:
                Final_diagnosis="Lung infection(Pneumonia)"
                Probability_percentage=60
            elif Predisposing_factors=={7} and Associated_symptoms=={1,6}:
                Final_diagnosis="Lung infection(Pneumonia)"
                Probability_percentage=70       
            elif Predisposing_factors=={7} and Associated_symptoms=={1,7}:
                Final_diagnosis="Lung infection(Pneumonia)"
                Probability_percentage=65      
            elif Predisposing_factors=={7} and Associated_symptoms=={6,7}:
                Final_diagnosis="Lung infection(Pneumonia)"
                Probability_percentage=65       
            elif Predisposing_factors=={7} and Associated_symptoms=={1,6,7}:
                Final_diagnosis="Lung infection(Pneumonia)"
                Probability_percentage=75       
            elif Predisposing_factors=={7} and Associated_symptoms=={11}:
                Final_diagnosis="Lung infection(Pneumonia)"
                Probability_percentage=20


#####################################################################################


# بیماری 5 : اضطراب همراه(هایپرونتیالسیون)

# سابقه : درد قفسه سینه
                    

            elif Predisposing_factors=={6} and Associated_symptoms=={8}:
                Final_diagnosis="Associated anxiety(Hyperventilation)" 
                Probability_percentage=75
            elif Predisposing_factors=={6} and Associated_symptoms=={9}:                     
                Final_diagnosis="Associated anxiety(Hyperventilation)"
                Probability_percentage=80
            elif Predisposing_factors=={6} and Associated_symptoms=={10}:
                Final_diagnosis="Associated anxiety(Hyperventilation)"
                Probability_percentage=75
            elif Predisposing_factors=={6} and Associated_symptoms=={8,9}:
                Final_diagnosis="Associated anxiety(Hyperventilation)"
                Probability_percentage=85       
            elif Predisposing_factors=={6} and Associated_symptoms=={8,10}:
                Final_diagnosis="Associated anxiety(Hyperventilation)"
                Probability_percentage=80      
            elif Predisposing_factors=={6} and Associated_symptoms=={9,10}:
                Final_diagnosis="Associated anxiety(Hyperventilation)"
                Probability_percentage=85       
            elif Predisposing_factors=={6} and Associated_symptoms=={8,9,10}:
                Final_diagnosis="Associated anxiety(Hyperventilation)"
                Probability_percentage=90       
            elif Predisposing_factors=={6} and Associated_symptoms=={11}:
                Final_diagnosis="Associated anxiety(Hyperventilation)"
                Probability_percentage=50
        
# بیماری 5 : اضطراب همراه(هایپرونتیلاسیون)

 # سابقه : بدون شرایط
                    

            elif Predisposing_factors=={7} and Associated_symptoms=={8}:
                Final_diagnosis="Associated anxiety(Hyperventilation)" 
                Probability_percentage=55
            elif Predisposing_factors=={7} and Associated_symptoms=={9}:                     
                Final_diagnosis="Associated anxiety(Hyperventilation)"
                Probability_percentage=60
            elif Predisposing_factors=={7} and Associated_symptoms=={10}:
                Final_diagnosis="Associated anxiety(Hyperventilation)"
                Probability_percentage=55
            elif Predisposing_factors=={7} and Associated_symptoms=={8,9}:
                Final_diagnosis="Associated anxiety(Hyperventilation)"
                Probability_percentage=65       
            elif Predisposing_factors=={7} and Associated_symptoms=={8,10}:
                Final_diagnosis="Associated anxiety(Hyperventilation)"
                Probability_percentage=60      
            elif Predisposing_factors=={7} and Associated_symptoms=={9,10}:
                Final_diagnosis="Associated anxiety(Hyperventilation)"
                Probability_percentage=65       
            elif Predisposing_factors=={7} and Associated_symptoms=={8,9,10}:
                Final_diagnosis="Associated anxiety(Hyperventilation)"
                Probability_percentage=70     
            elif Predisposing_factors=={7} and Associated_symptoms=={11}:
                Final_diagnosis="Associated anxiety(Hyperventilation)"
                Probability_percentage=30


#######################################################################################             
            
            
# دریافت فرم
                
            while True :
                Question=input("Are you willing to receive the form?\n1- Yes\n2- No\n")
                if Question in ["Yes","1","No","2"]:
                    if Question in ["Yes","1"]:
                        print()
                        print(f"name: {Name}")
                        print(f"last Name: {Last_name}")
                        print(f"age : {Age}")
                        print(f"gender : {Gender}")
                        Title="Patient history : "
                        Disease=f"Your condition is {Final_diagnosis}, and the likelihood of it is {Probability_percentage}%"
                        print(Title + Disease)
                        Title_2="Treatment recommendation: "
                        Treatment="Due to the lack of diagnosis, no treatment is recommended for you."
                        if Final_diagnosis=="Heart failure":
                            Treatment="Suggested treatment: \n1- You may use beta-blocker medications such as 'Propranolol'.\n2- You can also use diuretic medications."
                            print(f"{Treatment}")
                            print()
                            print("It is important to note that these percentages are approximate, and for a more accurate diagnosis and to determine the correct dosage of medication, it is recommended to consult a doctor.")
                        elif Final_diagnosis=="Asthma":
                            Treatment="Suggested treatment: \n1- First, use 'Salbutamol inhaler'.\n2- If no improvement occurs, you may use 'Fludrocortisone inhaler'.\n3- You can also use 'Salmeterol inhaler' as a bronchodilator."
                            print(f"{Treatment}")
                            print()
                            print("It is important to note that these percentages are approximate, and for a more accurate diagnosis and to determine the correct dosage of medication, it is recommended to consult a doctor.")
                        elif Final_diagnosis=="COPD":
                            Treatment="Suggested treatment: \n1- If you are a smoker, quit smoking.\n2- You may use bronchodilators or asthma medications such as 'Atrovent'."
                            print(f"{Treatment}")
                            print()
                            print("It is important to note that these percentages are approximate, and for a more accurate diagnosis and to determine the correct dosage of medication, it is recommended to consult a doctor.")
                        elif Final_diagnosis=="Lung infection(Pneumonia)":
                            Treatment="Suggested treatment: \n1-If it is a bacterial infection, you can use antibiotics. \n2- If it is a viral infection, you can use antiviral medications."    
                            print(f"{Treatment}")
                            print()
                            print("It is important to note that these percentages are approximate, and for a more accurate diagnosis and to determine the correct dosage of medication, it is recommended to consult a doctor.")
                        elif Final_diagnosis=="Associated anxiety(Hyperventilation)":
                            Treatment="Suggested treatment: \n1- Consult a psychiatrist.\n2- Get some rest."
                            print(f"{Treatment}")
                            print()
                            print("It is important to note that these percentages are approximate, and for a more accurate diagnosis and to determine the correct dosage of medication, it is recommended to consult a doctor.")                        
                        
                        print()
                        print(Title_2 + Treatment )
                    
                    
                    else:
                        print()
                        print("The form was not issued.")    
                    break 
                
                
                
                else:
                    print()
                    print("Please enter the data correctly.")
                
                

        
            else:
                print()
                print("Our system is being updated, and currently, it is unable to diagnose your condition based on the symptoms and history provided.\nPlease correct your data and try again. ")
                   
        
        
        
        
        break     #توقف برای حلقه اول / اگر داده های علائم اصلی درست وارد شد متوقف شو
    
    else:
        print("Please select a number from 1 to 5 for your primary disease symptom.")  


# تشخیص بیماری
             
print()
print()
print(f"Your condition is {Final_diagnosis}, and the likelihood of it is {Probability_percentage}%")
print()
print()


# توصیه برای درمان

Treatment="Due to the lack of diagnosis, no treatment is recommended for you."
if Final_diagnosis=="Heart failure":
    Treatment="Suggested treatment: \n1- You may use beta-blocker medications such as 'Propranolol'.\n2- You can also use diuretic medications."
    print(f"{Treatment}")
    print()
    print("It is important to note that these percentages are approximate, and for a more accurate diagnosis and to determine the correct dosage of medication, it is recommended to consult a doctor.")
elif Final_diagnosis=="Asthma":
    Treatment="Suggested treatment: \n1- First, use 'Salbutamol inhaler'.\n2- If no improvement occurs, you may use 'Fludrocortisone inhaler'.\n3- You can also use 'Salmeterol inhaler' as a bronchodilator."
    print(f"{Treatment}")
    print()
    print("It is important to note that these percentages are approximate, and for a more accurate diagnosis and to determine the correct dosage of medication, it is recommended to consult a doctor.")
elif Final_diagnosis=="COPD":
    Treatment="Suggested treatment: \n1- If you are a smoker, quit smoking.\n2- You may use bronchodilators or asthma medications such as 'Atrovent'."
    print(f"{Treatment}")
    print()
    print("It is important to note that these percentages are approximate, and for a more accurate diagnosis and to determine the correct dosage of medication, it is recommended to consult a doctor.")
elif Final_diagnosis=="Lung infection(Pneumonia)":
    Treatment="Suggested treatment: \n1-If it is a bacterial infection, you can use antibiotics. \n2- If it is a viral infection, you can use antiviral medications."    
    print(f"{Treatment}")
    print()
    print("It is important to note that these percentages are approximate, and for a more accurate diagnosis and to determine the correct dosage of medication, it is recommended to consult a doctor.")
elif Final_diagnosis=="Associated anxiety(Hyperventilation)":
    Treatment="Suggested treatment: \n1- Consult a psychiatrist.\n2- Get some rest."
    print(f"{Treatment}")
    print()
    print("It is important to note that these percentages are approximate, and for a more accurate diagnosis and to determine the correct dosage of medication, it is recommended to consult a doctor.")


# تشکر

print()
print("Thank you! - Saris Programming Team")          
            
            
            
            
            
            
            
            
            
            
            