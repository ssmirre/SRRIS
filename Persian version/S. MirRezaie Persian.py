# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 16:01:11 2025

@author: ssmir
"""

language = int(input("Choose your language: \n زبان خود را انتخاب کنید: \n 1. English \n 2. فارسی"))
if language == 1:
    symptom = int(input("علائم خود را انتخاب کنید:\n **برای اطمینان از عملکرد بهینه این برنامه، \n لطفا فقط از اعداد صحیح برای وارد کردن داده استفاده کنید** \n 1. شکم درد \n 2. درد قفسه سیته\n 3. سرفه\n 4. درد پست\n 5. تنگی نفس"))
if symptom == 1:
   areaOfThePain = int(input("بیشتر از همه درد را در چه ناحیه ای احساس میکنید؟\n 1. نزدیک قفسه سینه \n 2. اطراف ناف \n 3. درد جنرالیزنه شکم"))
   if areaOfThePain == 1:
        backPainCheck = int(input("آیا در پشت هم دردی احساس میکنید؟ \n 1. بله \n 2. خیر"))
        if backPainCheck == 1:
            otherAreaPainCheck = int(input("آیا در نواحی دیگری از شکم هم درد احساس میکنید؟ \n 1. بله \n 2. خیر"))
            if otherAreaPainCheck == 1:
                print("پانکراتیت حاد با احتمال 40 تا 70 درصد. \n استراحت و مسکن در صورت لزوم پیشنهاد میشود. \n لطفا برای تشخیص دقیق تر و درمان به پزشک مراجعه کنید. \nتوصیه های بعدی یتواند شامل بستری شدن در بیمارستان برای \n رفع دیهدراتیسیون،  تجویز دارو مانند آنتی بیوتیک، و توصیه های تغذیه ای باشد.")
            elif otherAreaPainCheck == 2:
                print("پانکراتیک مزمن با احتمال 15 تا 30 درصد یا زخم معده با احتمال 60 تا 80 درصد. \n استراحت و مسکن در صورت لزوم پیشنهاد میشود. \n لطفا برای تشخیص دقیق تر و درمان به پزشک مراجعه کنید. \nتوصیه های بعدی یتواند شامل بستری شدن در بیمارستان برای \n رفع دیهدراتیسیون،  تجویز دارو مانند آنتی بیوتیک، و توصیه های تغذیه ای باشد.")
            else:
                print("متسفانه داده کافی برای تشخیص بیماری شما در دسترس نیست. \n لطفا به پزشک مراجعه کنید")
        elif backPainCheck == 2:
            print("رفلاکس معده به مری.\n وعده های کوچک پیشنهاد میشود.  \nهنگام دراز کشدن، سر خود را بالاتر از سطح بئن نگه دارید. \n خم نشوید و از مصرف نوشیدنی های کافئین دار خودداری کنید. \n لطفا برای تشخیص دقیق تر و درمان، به پزشک مزاجعه کنید. \n در موارد شدید، ممکن از جراحی نیز توصیه شود.")
        else:
            print("متاسفانه خطایی پیش آماده است. لطفا از درست بودن فرمت داده وارد شده اطمینان حاصل کنید")
   elif areaOfThePain == 2:
       appandixCheck = int(input("ایا در نواحی تحتانی شکم هم درد احساس میکنید؟ \n 1. بله \n 2. خیر"))
       if appandixCheck == 1:
           print("آپاندیسیت مزمن با احتمال 10 تا 20 درصد. \n در صورت لزوم مسکن مصرف کنید و سپش به پزشک مراجعه کنید. \n جراحی ممکن است توصیه شود")
       else:
           print("متسفانه داده کافی برای تشخیص بیماری شما در دسترس نیست. \n لطفا به پزشک مراجعه کنید")
   elif areaOfThePain == 3:
       crampyPainCheck = int(input("ایا درد به صورت کرامپی است؟ \n 1. بله \n 2. خیر"))
       if crampyPainCheck == 1:
           print("انسداد حاد روده با احتمال 50 تا 70 درصد. پد تا حد امکان از مسکن دوری کنید و به پزشک مراجعه کنید. ممکن است جراحی و رعایت پروسه های مربوط به ان توصیه شود.")
       else:
           print("متاسفانه خطایی پیش آماده است. لطفا از درست بودن فرمت داده وارد شده اطمینان حاصل کنید")
   else:
       print("متسفانه داده کافی برای تشخیص بیماری شما در دسترس نیست. \n لطفا به پزشک مراجعه کنید")
else:
    print("متاسفانه خطایی پیش آماده است. لطفا از درست بودن فرمت داده وارد شده اطمینان حاصل کنید")