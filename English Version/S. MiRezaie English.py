# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 21:08:16 2024

@author: ssmir
"""
language = int(input("Choose your language: \n زبان خود را انتخاب کنید: \n 1. English \n 2. فارسی"))
if language == 1:
    symptom = int(input("Hello! \n Choose your symptom:\n **To ensure the productivity of this program, \n please keep in mind to ONLY use INTEGER NUMBERS as your input.** \n 1. Stomachache \n 2. Chest Pain\n 3. Cough\n 4. Backache\n 5. Shortage of breath"))
if symptom == 1:
   areaOfThePain = int(input("Where do you MAINLY feel the pain?\n 1. Close to the chest \n 2. Around the belly button \n 3. Generally the stomach"))
   if areaOfThePain == 1:
        backPainCheck = int(input("Do you also feel pain in the back? \n 1. Yes \n 2. No"))
        if backPainCheck == 1:
            otherAreaPainCheck = int(input("Do you also feel pain in other areas of the stomach? \n 1. Yes \n 2. No"))
            if otherAreaPainCheck == 1:
                print("Acute pancreatitis with the likelyhood of 40 to 70 percent. \n We suggest you rest and take pain killer if needed.\n Please visit your physician for more accurate diagnosis and treatment. \n Futher steps may include a hospital stay to treat dehydration \n and prescribe pain medicine, antibiotics, and nutrition.")
            elif otherAreaPainCheck == 2:
                print("Chronic Pancreatitis with the likelyhood of 15 to 30 percent OR Peptic ulcer disease with the likelyhood of 60 to 80 percent. \n We suggest you rest and take pain killer if needed.\n Please visit your physician for more accurate diagnosis and treatment. \n Futher instructions may include a hospital stay to treat dehydration \n and prescribe pain medicine, antibiotics, and nutrition.")
            else:
                print("Sorry, we don't have enough data to diagnose your problem. \n Please visit your physician.")
        elif backPainCheck == 2:
            print("GERD. We suggest ating small meals. \n Assiste gravity by elevating the head of the bed at night, and avoide bending over. \n Increase lower esophageal (LES) pressure by avoiding coffee, tea and cola \n which, because of their caffeine content, decrease LES pressure. \n Please visit your physician for more accurate diagnosis and treatment. Further instructions may inculde surgery in severe cases.")
        else:
            print("Sorry, something went wrong. Please make sure the data you have imported has the right format.")
   elif areaOfThePain == 2:
       appandixCheck = int(input("Do you also feel pain in the lower right belly? \n 1. Yes \n 2. No"))
       if appandixCheck == 1:
           print("Appendicitis with the likelyhood of 10 to 20 percent. \n Take pain killers in neccessary and visit you physician. \n Suragry may be needed.")
       else:
           print("Sorry, we don't have enough data to diagnose your problem. \n Please visit your physician.")
   elif areaOfThePain == 3:
       crampyPainCheck = int(input("Is the pain crampy? \n 1. Yes \n 2. No"))
       if crampyPainCheck == 1:
           print("Ileus with the likelyhood of 50 to 70 percent. \n Please aviod pain killers if possible, \n and visit your physicain. \n Instructions may include continuous nasogastric suction, nothing by mouth, \n IV fluids and electrolytes, a minimal amount of sedatives, \n and avoidance of opioids and anticholinergic medications.")
       else:
           print("Sorry, something went wrong. Please make sure the data you have imported has the right format.")
   else:
       print("Sorry, we don't have enough data to diagnose your problem. \n Please visit your physician.")
    print("Sorry, something went wrong. \n Please ensure the validity of the input data.")
    