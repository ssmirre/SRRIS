age = int(input("please enter your age"))
gender = int(input("please emter 1 if you are a woman and 2 if you are a man"))
print("Hello! In this programو we want to make an initial diagnosis of your illness and offer you a solution.")
print()
print("This program currently works on five main symptoms of diseases:")
main_symptoms = ("stomachache","chest pain","cough","backache","shortage of breath")
print("1.stomachache\n2.chest pain\n3.cough\n4.backache\n5.shortage of breath")
A = int(input("please enter the number matched to your main symptom"))

if A == 1:
    print("you have stomachache")
elif A == 2:
    print("you have chest pain")
elif A == 3:
    print("you have cough")
elif A == 4:
    print("you have backache")
    print()
    print("Now we need to know what associated symptoms you have, choose from the symptoms below")
    print("1.tenderness of upper back muscles and joints\n2.tenderness of spinous process\n3.pain when walking\n4.stabbing pain in knee and back of the leg\n5.numbness and muscle weakness\n6.tenderness of the muscles adjacent to the sciatic nerve\n7.pain exacerbation with sneezing, coughing, and straining during bowel movements\n8.weakness and overactive reflection in the lower back when bending forward\n9.calf pain after 30 seconds of back extension\n10.reduced range of motion of the spine\n11.pain throughout the spine\n12.vauge and deep pain\n13.local tenderness of the spinal vertebrae\n14.painful spinal movements")
    print()
    print("Note:Tenderness is pain or discomfort when an affected area is touched.")
    print()
    associated_symptoms = input("Which of the mentioned symptoms do you have? You can choose multiple ones by putting , between the numbers.")
    associated_symptoms = set(map(int,associated_symptoms.split(",")))
    if associated_symptoms == {1}:
        print("You have a 11.8% chance of having mechanical back pain.")
        print("We suggest you to rest and if the pain worsens, use pain killers. However, make sure to consult a doctor for accurate diagnosis and treatment.")
    elif associated_symptoms == {2}:
        print("You have a 17.6% chance of having mechanical back pain.")
        print("We suggest you to rest and if the pain worsens, use pain killers. However, make sure to consult a doctor for accurate diagnosis and treatment.")
    elif associated_symptoms == {3}:
        print("You have a 23.5% chance of having mechanical back pain.")
        print("We suggest you to rest and if the pain worsens, use pain killers. However, make sure to consult a doctor for accurate diagnosis and treatment.")
    elif associated_symptoms == {1,2}:
        print("You have a 29.4% chance of having mechanical back pain.")
        print("We suggest you to rest and if the pain worsens, use pain killers. However, make sure to consult a doctor for accurate diagnosis and treatment.")
    elif associated_symptoms == {1,3}:
        print("You have a 35.3% chance of having mechanical back pain.")
        print("We suggest you to rest and if the pain worsens, use pain killers. However, make sure to consult a doctor for accurate diagnosis and treatment.")
    elif associated_symptoms == {2,3}:
        print("You have a 41.2% chance of having mechanical back pain.")
        print("We suggest you to rest and if the pain worsens, use pain killers. However, make sure to consult a doctor for accurate diagnosis and treatment.")
    elif associated_symptoms == {1,2,3}:
        print("You have a 35.3% chance of having mechanical back pain.")
        print("We suggest you to rest and if the pain worsens, use pain killers. However, make sure to consult a doctor for accurate diagnosis and treatment.")
    elif associated_symptoms == {4}:
        print("You have a 14.3% chance of having sciatic pain.")
        print("We suggest you to rest and use pain killers. If the pain worsens, make sure to visit a doctor for recieving accurate treatment which can include cortone ampoule or you may require surgery.")
    elif associated_symptoms == {5}:
        print("You have a 21.4% chance of having sciatic pain.")
        print("We suggest you to rest and use pain killers. If the pain worsens, make sure to visit a doctor for recieving accurate treatment which can include cortone ampoule or you may require surgery.")
    elif associated_symptoms == {6}:
        print("You have a 28.6% chance of having sciatic pain.")
        print("We suggest you to rest and use pain killers. If the pain worsens, make sure to visit a doctor for recieving accurate treatment which can include cortone ampoule or you may require surgery.")
    elif associated_symptoms == {7}:
        print("You have a 35.7% chance of having sciatic pain.")
        print("We suggest you to rest and use pain killers. If the pain worsens, make sure to visit a doctor for recieving accurate treatment which can include cortone ampoule or you may require surgery.")
    elif associated_symptoms == {4,5}:
        print("You have a 35.7% chance of having sciatic pain.")
        print("We suggest you to rest and use pain killers. If the pain worsens, make sure to visit a doctor for recieving accurate treatment which can include cortone ampoule or you may require surgery.")
    elif associated_symptoms == {4,6}:
        print("You have a 42.9% chance of having sciatic pain.")
        print("We suggest you to rest and use pain killers. If the pain worsens, make sure to visit a doctor for recieving accurate treatment which can include cortone ampoule or you may require surgery.")
    elif associated_symptoms == {4,7}:
        print("You have a 50% chance of having sciatic pain.")
        print("We suggest you to rest and use pain killers. If the pain worsens, make sure to visit a doctor for recieving accurate treatment which can include cortone ampoule or you may require surgery.")
    elif associated_symptoms == {5,6}:
        print("You have a 50% chance of having sciatic pain.")
        print("We suggest you to rest and use pain killers. If the pain worsens, make sure to visit a doctor for recieving accurate treatment which can include cortone ampoule or you may require surgery.")
    elif associated_symptoms == {5,7}:
        print("You have a 57.1% chance of having sciatic pain.")
        print("We suggest you to rest and use pain killers. If the pain worsens, make sure to visit a doctor for recieving accurate treatment which can include cortone ampoule or you may require surgery.")
    elif associated_symptoms == {6,7}:
        print("You have a 64.3% chance of having sciatic pain.")
        print("We suggest you to rest and use pain killers. If the pain worsens, make sure to visit a doctor for recieving accurate treatment which can include cortone ampoule or you may require surgery.")
    elif associated_symptoms == {4,5,6}:
        print("You have a 64.3% chance of having sciatic pain.")
        print("We suggest you to rest and use pain killers. If the pain worsens, make sure to visit a doctor for recieving accurate treatment which can include cortone ampoule or you may require surgery.")
    elif associated_symptoms == {4,5,7}:
        print("You have a 71.4% chance of having sciatic pain.")
        print("We suggest you to rest and use pain killers. If the pain worsens, make sure to visit a doctor for recieving accurate treatment which can include cortone ampoule or you may require surgery.")
    elif associated_symptoms == {4,6,7}:
        print("You have a 78.6% chance of having sciatic pain.")
        print("We suggest you to rest and use pain killers. If the pain worsens, make sure to visit a doctor for recieving accurate treatment which can include cortone ampoule or you may require surgery.")
    elif associated_symptoms == {5,6,7}:
        print("You have a 85.7% chance of having sciatic pain.")
        print("We suggest you to rest and use pain killers. If the pain worsens, make sure to visit a doctor for recieving accurate treatment which can include cortone ampoule or you may require surgery.")
    elif associated_symptoms == {8}:
        print("You have a 21.4% chance of having spinal stenosis.")
        print("We suggest you to rest and do not lift heavy objects. If the pain worsens, make sure to visit a doctor for recieving accurate treatment which can include cortone ampoule or you may require surgery.")
    elif associated_symptoms == {9}:
        print("You have a 28.6% chance of having spinal stenosis.")
        print("We suggest you to rest and do not lift heavy objects. If the pain worsens, make sure to visit a doctor for recieving accurate treatment which can include cortone ampoule or you may require surgery.")
    elif associated_symptoms == {8,9}:
        print("You have a 50% chance of having spinal stenosis.")
        print("We suggest you to rest and do not lift heavy objects. If the pain worsens, make sure to visit a doctor for recieving accurate treatment which can include cortone ampoule or you may require surgery.")
    elif associated_symptoms == {10}:
        print("You have a 23.3% chance of having chronic pain due to rheumatological diseases.")
        print("We suggest you to rest and if the pain worsens, make sure to visit a doctor for recieving accurate treatment which can include cortone pill and rheumatic medication.")
    elif associated_symptoms == {11}:
        print("You have a 26.7% chance of having chronic pain due to rheumatological diseases.")
        print("We suggest you to rest and if the pain worsens, make sure to visit a doctor for recieving accurate treatment which can include cortone pill and rheumatic medication.")
    elif associated_symptoms == {10,11}:
        print("You have a 50% chance of having chronic pain due to rheumatological diseases.")
        print("We suggest you to rest and if the pain worsens, make sure to visit a doctor for recieving accurate treatment which can include cortone pill and rheumatic medication.")
    elif associated_symptoms == {12}:
        print("You have a 6.7% chance of having referred pain from the abdomen and back.")
        print("We suggest you to visit a doctor for treating underlying causes.")
    elif associated_symptoms == {13}:
        print("You have a 10% chance of having referred pain from the abdomen and back.")
        print("We suggest you to visit a doctor for treating underlying causes.")
    elif associated_symptoms == {14}:
        print("You have a 8% chance of having referred pain from the abdomen and back.")
        print("We suggest you to visit a doctor for treating underlying causes.")
    elif associated_symptoms == {12,13}:
        print("You have a 16.7% chance of having referred pain from the abdomen and back.")
        print("We suggest you to visit a doctor for treating underlying causes.")
    elif associated_symptoms == {12,14}:
        print("You have a 15% chance of having referred pain from the abdomen and back.")
        print("We suggest you to visit a doctor for treating underlying causes.")
    elif associated_symptoms == {13,14}:
        print("You have a 18.3% chance of having referred pain from the abdomen and back.")
        print("We suggest you to visit a doctor for treating underlying causes.")
    elif associated_symptoms == {12,13,14}:
        print("You have a 25% chance of having referred pain from the abdomen and back.")
        print("We suggest you to visit a doctor for treating underlying causes.")
    else:
        print("sorry, this program does not support entered symptoms.")
    
elif A == 5:
    print("you have shortage of breath")
else:
    print("sorry, this program does not support other symptoms.")
    