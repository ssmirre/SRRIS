 # مشخصات بیمار

print("لطفا مشخصات خود را وارد کنید.")
Name = input("نام: ")
Last_name = input("نام خانوادگی: ")
Age =int(input("سن: "))
Gender = input("جنسیت: ")
print()
print(f"سلام {Name}! ما در این برنامه می خواهیم تا تشخیص اولیه از بیماری شما داشته باشیم و به شما راهکار پیشنهاد بدهیم.")
print()


# تشخیص علائم اصلی بیمار


print("این برنامه در حال حاضر روی 5 علامت اصلی بیماری کار می کند:")
print("1- درد شکم\n2- درد قفسه سینه\n3- سرفه\n4- درد کمر\n5- تنگی نفس")
while True :
    Main_symptoms =int(input("با انتخاب یک عدد، علامت اصلی بیماری خود را مشخص کنید: "))
    if 1<=int(Main_symptoms)<=5: 
        # if int(Main_symptoms) ==1:
        #     print('اکنون نیاز است که ببینیم چه علائمی همراه "درد شکم" دارید.')
        #     print()
            
        # elif int(Main_symptoms) ==2:
        #     print('اکنون نیاز است که ببینیم چه علائمی همراه "درد قفسه سینه" دارید.')
        #     print()
                        
        # elif int(Main_symptoms) ==3:
        #     print('اکنون نیاز است که ببینیم چه علائمی همراه "سرفه" دارید.')
        #     print()
            
        # elif int(Main_symptoms) ==4:
        #     print('اکنون نیاز است که ببینیم چه علائمی همراه "درد کمر" دارید.')
        #     print()
                            
        if int(Main_symptoms) ==5:
            print('اکنون نیاز است که ببینیم چه علائمی همراه "تنگی نفس" دارید.')
            print()
            
            # تشخیص علائم همراه
            
            print("از بین علائم زیر انتخاب کنید.") 
            print("(اگر انتخاب هایتان بیش از یک مورداست، بین اعداد کاما(,) بگذارید.\nمثال: 1,10,11)")
            print("1- سرفه\n2- تنگی نفس شبانه\n3- ویز(صدای خروج هوای مضاعف از ریه)\n4- خس خس\n5- گرفتگی در سینه\n6- خلط موکوئیدی(ژلاتینی)\n7- تب\n8- تپش قلب\n9- سرگیجه\n10- بی حسی و سوزن سوزن شدن دست و پا\n11- بدون علائم همراه")
            print()
            
            while True :         #تنگی نفس دارد/ حلقه برای وارد کردن درست علائم همراه
                Associated_symptoms= input("کدام علائم را دارید؟ ")
                try:
                    Associated_symptoms=set(map(int,Associated_symptoms.split(",")))
                    break     #توقف حلقه دوم/ اگر داده های علائم همراه را درست وارد کرد متوقف شو
                except ValueError :
                    print()
                    print("لطفا در موقع وارد کردن داده موارد زیر را رعایت کرده و دوباره داده را وارد کنید:\n1- کیبورد خود را انگلیسی کنید.\n2- در بین اعداد حتما کاما (,) قرار دهید.\n3- از دکمه‌ی space استفاده نکنید.\nمثال: 11,10,1")
                    
                    # تشخیص شرایط زمینه ای بیمار
                    
            print()
            print("علائم همراه شما ثبت شد.")
            print()
            print (" اکنون نیاز است تا ببینیم چه شرایط زمینه ای در بیماری شما تاثیر داشته است. ")
            print()
            print("از بین شرایط زیر انتخاب کنید.") 
            print("(اگر انتخاب هایتان بیش از یک مورداست، بین اعداد کاما(,) بگذارید.\nمثال: 1,7,6)")
            print("1- سابقه بیماری قلبی\n2- شرایط محیطی\n3- سابقه مصرف سیگار\n4- آلاینده\n5- متغیر\n6- درد قفسه سینه\n7- بدون شرایط زمینه ای")
            print()
            while True :         #حلقه برای درست وارد کردن شرایط زمینه ای
                Predisposing_factors=input("کدام شرایط زمینه ای را دارید؟ ")
                try:
                    Predisposing_factors=set(map(int,Predisposing_factors.split(",")))
                    break
                except ValueError :
                    print()
                    print("لطفا در مواقع وارد کردن داده موارد زیر را رعایت کرده و دوباره داده را وارد کنید:\n1- کیبورد خود را انگلیسی کنید.\n2- در بین اعداد حتما کاما (,) قرار دهید.\n3- از دکمه‌ی space استفاده نکنید.\nمثال: 7,6,1")
             
                
             # بیماری 1 : نارسایی قلبی
             
          # سابقه : بیماری قلبی
                    
            Final_diagnosis="تشخیص داده نشده"        
            Probability_percentage="تشخیص داده نشده"
            if Predisposing_factors=={1} and Associated_symptoms=={1}:
                Final_diagnosis="نارسایی قلبی" 
                Probability_percentage=60
            elif Predisposing_factors=={1} and Associated_symptoms=={2}:                     
                Final_diagnosis="نارسایی قلبی"
                Probability_percentage=70
            elif Predisposing_factors=={1} and Associated_symptoms=={3}:
                Final_diagnosis="نارسایی قلبی"
                Probability_percentage=50
            elif Predisposing_factors=={1} and Associated_symptoms=={1,2}:
                Final_diagnosis="نارسایی قلبی"
                Probability_percentage=80       
            elif Predisposing_factors=={1} and Associated_symptoms=={1,3}:
                Final_diagnosis="نارسایی قلبی"
                Probability_percentage=65      
            elif Predisposing_factors=={1} and Associated_symptoms=={2,3}:
                Final_diagnosis="نارسایی قلبی"
                Probability_percentage=75       
            elif Predisposing_factors=={1} and Associated_symptoms=={1,2,3}:
                Final_diagnosis="نارسایی قلبی"
                Probability_percentage=85       
            elif Predisposing_factors=={1} and Associated_symptoms=={11}:
                Final_diagnosis="نارسایی قلبی"
                Probability_percentage=10       
            
                      

# بیماری 1 : نارسایی قلبی

# سابقه : بدون شرایط


            elif Predisposing_factors=={7} and Associated_symptoms=={1}:
                Final_diagnosis="نارسایی قلبی" 
                Probability_percentage=20
            elif Predisposing_factors=={7} and Associated_symptoms=={2}:                     
                Final_diagnosis="نارسایی قلبی"
                Probability_percentage=25
            elif Predisposing_factors=={7} and Associated_symptoms=={3}:
                Final_diagnosis="نارسایی قلبی"
                Probability_percentage=15
            elif Predisposing_factors=={7} and Associated_symptoms=={1,2}:
                Final_diagnosis="نارسایی قلبی"
                Probability_percentage=30       
            elif Predisposing_factors=={7} and Associated_symptoms=={1,3}:
                Final_diagnosis="نارسایی قلبی"
                Probability_percentage=20      
            elif Predisposing_factors=={7} and Associated_symptoms=={2,3}:
                Final_diagnosis="نارسایی قلبی"
                Probability_percentage=25       
            elif Predisposing_factors=={7} and Associated_symptoms=={1,2,3}:
                Final_diagnosis="نارسایی قلبی"
                Probability_percentage=30       
            elif Predisposing_factors=={7} and Associated_symptoms=={11}:
                Final_diagnosis="نارسایی قلبی"
                Probability_percentage=5
            
     
#############################################################################################                
                
                    
# بیماری 2 : آسم

# سابقه : شرایط محیطس
                    

            elif Predisposing_factors=={1} and Associated_symptoms=={1}:
                Final_diagnosis="آسم" 
                Probability_percentage=60
            elif Predisposing_factors=={1} and Associated_symptoms=={4}:                     
                Final_diagnosis="آسم"
                Probability_percentage=75
            elif Predisposing_factors=={1} and Associated_symptoms=={5}:
                Final_diagnosis="آسم"
                Probability_percentage=70
            elif Predisposing_factors=={1} and Associated_symptoms=={1,4}:
                Final_diagnosis="آسم"
                Probability_percentage=85       
            elif Predisposing_factors=={1} and Associated_symptoms=={1,5}:
                Final_diagnosis="آسم"
                Probability_percentage=80      
            elif Predisposing_factors=={1} and Associated_symptoms=={4,5}:
                Final_diagnosis="آسم"
                Probability_percentage=58       
            elif Predisposing_factors=={1} and Associated_symptoms=={1,4,5}:
                Final_diagnosis="آسم"
                Probability_percentage=90       
            elif Predisposing_factors=={1} and Associated_symptoms=={11}:
                Final_diagnosis="آسم"
                Probability_percentage=30         
        
        
# بیماری 2 : آسم

# سابقه : بدون شرایط
                    

            elif Predisposing_factors=={7} and Associated_symptoms=={1}:
                Final_diagnosis="آسم" 
                Probability_percentage=40
            elif Predisposing_factors=={7} and Associated_symptoms=={4}:                     
                Final_diagnosis="آسم"
                Probability_percentage=55
            elif Predisposing_factors=={7} and Associated_symptoms=={5}:
                Final_diagnosis="آسم"
                Probability_percentage=50
            elif Predisposing_factors=={7} and Associated_symptoms=={1,4}:
                Final_diagnosis="آسم"
                Probability_percentage=65       
            elif Predisposing_factors=={7} and Associated_symptoms=={1,5}:
                Final_diagnosis="آسم"
                Probability_percentage=60      
            elif Predisposing_factors=={7} and Associated_symptoms=={4,5}:
                Final_diagnosis="آسم"
                Probability_percentage=65       
            elif Predisposing_factors=={7} and Associated_symptoms=={1,4,5}:
                Final_diagnosis="آسم"
                Probability_percentage=70       
            elif Predisposing_factors=={7} and Associated_symptoms=={11}:
                Final_diagnosis="آسم"
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
                Final_diagnosis="عفونت ریه(پنومونی)" 
                Probability_percentage=70
            elif Predisposing_factors=={5} and Associated_symptoms=={6}:                     
                Final_diagnosis="عفونت ریه(پنومونی)"
                Probability_percentage=75
            elif Predisposing_factors=={5} and Associated_symptoms=={7}:
                Final_diagnosis="عفونت ریه(پنومونی)"
                Probability_percentage=70
            elif Predisposing_factors=={5} and Associated_symptoms=={1,6}:
                Final_diagnosis="عفونت ریه(پنومونی)"
                Probability_percentage=80       
            elif Predisposing_factors=={5} and Associated_symptoms=={1,7}:
                Final_diagnosis="عفونت ریه(پنومونی)"
                Probability_percentage=75      
            elif Predisposing_factors=={5} and Associated_symptoms=={6,7}:
                Final_diagnosis="عفونت ریه(پنومونی)"
                Probability_percentage=75       
            elif Predisposing_factors=={5} and Associated_symptoms=={1,6,7}:
                Final_diagnosis="عفونت ریه(پنومونی)"
                Probability_percentage=85       
            elif Predisposing_factors=={5} and Associated_symptoms=={11}:
                Final_diagnosis="عفونت ریه(پنومونی)"
                Probability_percentage=40 
            
        
# بیماری 4 : عفونت ریه(پنومونی)

#سابقه : بدون شرایط
                    

            elif Predisposing_factors=={7} and Associated_symptoms=={1}:
                Final_diagnosis="عفونت ریه(پنومونی)" 
                Probability_percentage=60
            elif Predisposing_factors=={7} and Associated_symptoms=={6}:                     
                Final_diagnosis="عفونت ریه(پنومونی)"
                Probability_percentage=65
            elif Predisposing_factors=={7} and Associated_symptoms=={7}:
                Final_diagnosis="عفونت ریه(پنومونی)"
                Probability_percentage=60
            elif Predisposing_factors=={7} and Associated_symptoms=={1,6}:
                Final_diagnosis="عفونت ریه(پنومونی)"
                Probability_percentage=70       
            elif Predisposing_factors=={7} and Associated_symptoms=={1,7}:
                Final_diagnosis="عفونت ریه(پنومونی)"
                Probability_percentage=65      
            elif Predisposing_factors=={7} and Associated_symptoms=={6,7}:
                Final_diagnosis="عفونت ریه(پنومونی)"
                Probability_percentage=65       
            elif Predisposing_factors=={7} and Associated_symptoms=={1,6,7}:
                Final_diagnosis="عفونت ریه(پنومونی)"
                Probability_percentage=75       
            elif Predisposing_factors=={7} and Associated_symptoms=={11}:
                Final_diagnosis="عفونت ریه(پنومونی)"
                Probability_percentage=20


#####################################################################################
        
        
# بیماری 5 : اضطراب همراه(هایپرونتیالسیون)

# سابقه : درد قفسه سینه
                    

            elif Predisposing_factors=={6} and Associated_symptoms=={8}:
                Final_diagnosis="اضطراب همراه(هایپرونتیلاسیون)" 
                Probability_percentage=75
            elif Predisposing_factors=={6} and Associated_symptoms=={9}:                     
                Final_diagnosis="اضطراب همراه(هایپرونتیلاسیون)"
                Probability_percentage=80
            elif Predisposing_factors=={6} and Associated_symptoms=={10}:
                Final_diagnosis="اضطراب همراه(هایپرونتیلاسیون)"
                Probability_percentage=75
            elif Predisposing_factors=={6} and Associated_symptoms=={8,9}:
                Final_diagnosis="اضطراب همراه(هایپرونتیلاسیون)"
                Probability_percentage=85       
            elif Predisposing_factors=={6} and Associated_symptoms=={8,10}:
                Final_diagnosis="اضطراب همراه(هایپرونتیلاسیون)"
                Probability_percentage=80      
            elif Predisposing_factors=={6} and Associated_symptoms=={9,10}:
                Final_diagnosis="اضطراب همراه(هایپرونتیلاسیون)"
                Probability_percentage=85       
            elif Predisposing_factors=={6} and Associated_symptoms=={8,9,10}:
                Final_diagnosis="اضطراب همراه(هایپرونتیلاسیون)"
                Probability_percentage=90       
            elif Predisposing_factors=={6} and Associated_symptoms=={11}:
                Final_diagnosis="اضطراب همراه(هایپرونتیلاسیون)"
                Probability_percentage=50
        
# بیماری 5 : اضطراب همراه(هایپرونتیلاسیون)

 # سابقه : بدون شرایط
                    

            elif Predisposing_factors=={7} and Associated_symptoms=={8}:
                Final_diagnosis="اضطراب همراه(هایپرونتیلاسیون)" 
                Probability_percentage=55
            elif Predisposing_factors=={7} and Associated_symptoms=={9}:                     
                Final_diagnosis="اضطراب همراه(هایپرونتیلاسیون)"
                Probability_percentage=60
            elif Predisposing_factors=={7} and Associated_symptoms=={10}:
                Final_diagnosis="اضطراب همراه(هایپرونتیلاسیون)"
                Probability_percentage=55
            elif Predisposing_factors=={7} and Associated_symptoms=={8,9}:
                Final_diagnosis="اضطراب همراه(هایپرونتیلاسیون)"
                Probability_percentage=65       
            elif Predisposing_factors=={7} and Associated_symptoms=={8,10}:
                Final_diagnosis="اضطراب همراه(هایپرونتیلاسیون)"
                Probability_percentage=60      
            elif Predisposing_factors=={7} and Associated_symptoms=={9,10}:
                Final_diagnosis="اضطراب همراه(هایپرونتیلاسیون)"
                Probability_percentage=65       
            elif Predisposing_factors=={7} and Associated_symptoms=={8,9,10}:
                Final_diagnosis="اضطراب همراه(هایپرونتیلاسیون)"
                Probability_percentage=70     
            elif Predisposing_factors=={7} and Associated_symptoms=={11}:
                Final_diagnosis="اضطراب همراه(هایپرونتیلاسیون)"
                Probability_percentage=30


#######################################################################################                
                
                
# دریافت فرم
                
            while True :
                Question=input("آیا مایل به دریافت فرم هستید؟\n1- بله\n2- خیر\n")
                if Question in ["بله","1","خیر","2"]:
                    if Question in ["بله","1"]:
                        print()
                        print(f"نام : {Name}")
                        print(f"نام خانوادگی : {Last_name}")
                        print(f"سن : {Age}")
                        print(f"جنسیت : {Gender}")
                        Title="شرح حال بیمار : "
                        Disease=f"بیماری شما {Final_diagnosis} و درصد احتمال ابتلا به آن {Probability_percentage} است."
                        print(Title + Disease)
                        Title_2="توصیه درمانی : "
                        Treatment="به دلیل عدم تشخیص بیماری، درمانی به شما توصیه نمی شود."
                        if Final_diagnosis=="نارسایی قلبی":
                            Treatment="درمان پیشنهادی: \n1- می توانید از داروهای بتابلاکر مثل 'پروپنانولول' استفاده کنید.\n2- همچنین می توانید از داروهای ادرار‌آور استفاده کنید."
                            print(f"{Treatment}")
                            print()
                            print("لازم به ذکر است که این درصد ها تقریبی هستند و برای تشخیص درست تر و تعیین دوز دقیق دارو توصیه می شود که حتما به پزشک مراجعه کنید.")
                        elif Final_diagnosis=="آسم":
                            Treatment="درمان پیشنهادی: \n1- ابتدا از 'اسپری سالبوتامول' استفاده کنید.\n2- اگر بهبود حاصل نشد می توانید از 'اسپری فلودروکورتیزون' استفاده کنید.\n3- می توانید از 'اسپری سالمترول' هم به عنوان گشاد کننده‌ی راه‌های هوایی استفاده کنید."
                            print(f"{Treatment}")
                            print()
                            print("لازم به ذکر است که این درصد ها تقریبی هستند و برای تشخیص درست تر و تعیین دوز دقیق دارو توصیه می شود که حتما به پزشک مراجعه کنید.")
                        elif Final_diagnosis=="COPD":
                            Treatment="درمان پیشنهادی:\n1- اگر سیگاری هستید، سیگار را ترک کنید.\n2- می توانید از داروهای بازکننده‌ی راه‌های هوایی یا داروهای آسم مثل 'آتروونت' استفاده کنید."
                            print(f"{Treatment}")
                            print()
                            print("لازم به ذکر است که این درصد ها تقریبی هستند و برای تشخیص درست تر و تعیین دوز دقیق دارو توصیه می شود که حتما به پزشک مراجعه کنید.")
                        elif Final_diagnosis=="عفونت ریه(پنومونی)":
                            Treatment=": \n1-اگرعفونت باکتریایی باشد، می توانید از 'آنتی بیوتیک ها' استفاده کنید.\n2- اگر عفونت ویروسی باشد، می توانید از 'آنتی ویروس ها' استفاده کنید."    
                            print(f"{Treatment}")
                            print()
                            print("لازم به ذکر است که این درصد ها تقریبی هستند و برای تشخیص درست تر و تعیین دوز دقیق دارو توصیه می شود که حتما به پزشک مراجعه کنید.")
                        elif Final_diagnosis=="اضطراب همراه(هایپرونتیلاسیون)":
                            Treatment="درمان پیشنهادی: \n1- به روان پزشک مراجعه کنید.\n2- استراحت کنید."
                            print(f"{Treatment}")
                            print()
                            print("لازم به ذکر است که این درصد ها تقریبی هستند و برای تشخیص درست تر و تعیین دوز دقیق دارو توصیه می شود که حتما به پزشک مراجعه کنید.")                        
                        print()
                        print(Title_2 + Treatment )
                    
                    
                    else:
                        print()
                        print("فرمی صادر نشد.")    
                    break 
                
                
                
                else:
                    print()
                    print("لطفا داده را درست وارد کنید.")
                
                

        
            else:
                print()
                print("برنامه ما در حال آپدیت است و در حال حاضرامکان تشخیص بیماری شما با علائم و سوابق گفته شده را ندارد.\nلطفا داده های خود را اصلاح کرده و دوباره تلاش کنید. ")
                   
        
        
        
        
        break     #توقف برای حلقه اول / اگر داده های علائم اصلی درست وارد شد متوقف شو
    
    else:
        print("لطفا یک عدد از 5-1 را برای علامت اصلی بیماری خود انتخاب کنید.")
       
# تشخیص بیماری
             
print()
print()
print(f"بیماری شما {Final_diagnosis} و درصد احتمال ابتلا به آن {Probability_percentage} است.")
print()
print()


# توصیه برای درمان

Treatment="به دلیل عدم تشخیص بیماری، درمانی به شما توصیه نمی شود."
if Final_diagnosis=="نارسایی قلبی":
    Treatment="درمان پیشنهادی: \n1- می توانید از داروهای بتابلاکر مثل 'پروپنانولول' استفاده کنید.\n2- همپنین می توانید از داروهای ادرار‌آور استفاده کنید."
    print(f"{Treatment}")
    print()
    print("لازم به ذکر است که این درصد ها تقریبی هستند و برای تشخیص درست تر و تعیین دوز دقیق دارو توصیه می شود که حتما به پزشک مراجعه کنید.")
elif Final_diagnosis=="آسم":
    Treatment="درمان پیشنهادی: \n1- ابتدا از 'اسپری سالبوتامول' استفاده کنید.\n2- اگر بهبود حاصل نشد می توانید از 'اسپری فلودروکورتیزون' استفاده کنید.\n3- می توانید از 'اسپری سالمترول' هم به عنوان گشاد کننده‌ی راه‌های هوایی استفاده کنید."
    print(f"{Treatment}")
    print()
    print("لازم به ذکر است که این درصد ها تقریبی هستند و برای تشخیص درست تر و تعیین دوز دقیق دارو توصیه می شود که حتما به پزشک مراجعه کنید.")
elif Final_diagnosis=="COPD":
    Treatment="درمان پیشنهادی:\n1- اگر سیگاری هستید، سیگار را ترک کنید.\n2- می توانید از داروهای بازکننده‌ی راه‌های هوایی یا داروهای آسم مثل آتروونت استفاده کنید."
    print(f"{Treatment}")
    print()
    print("لازم به ذکر است که این درصد ها تقریبی هستند و برای تشخیص درست تر و تعیین دوز دقیق دارو توصیه می شود که حتما به پزشک مراجعه کنید.")
elif Final_diagnosis=="عفونت ریه(پنومونی)":
    Treatment=": \n1-اگرعفونت باکتریایی باشد، می توانید از 'آنتی بیوتیک ها' استفاده کنید.\n2- اگر عفونت ویروسی باشد، می توانید از 'آنتی ویروس ها' استفاده کنید."    
    print(f"{Treatment}")
    print()
    print("لازم به ذکر است که این درصد ها تقریبی هستند و برای تشخیص درست تر و تعیین دوز دقیق دارو توصیه می شود که حتما به پزشک مراجعه کنید.")
elif Final_diagnosis=="اضطراب همراه(هایپرونتیلاسیون)":
    Treatment="درمان پیشنهادی: \n1- به روان پزشک مراجعه کنید.\n2- استراحت کنید."
    print(f"{Treatment}")
    print()
    print("لازم به ذکر است که این درصد ها تقریبی هستند و برای تشخیص درست تر و تعیین دوز دقیق دارو توصیه می شود که حتما به پزشک مراجعه کنید.")


# تشکر

print()
print("با تشکر - گروه برنامه نویسی ساریس")



