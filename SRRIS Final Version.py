language=int(input("please choose your language:\n1:فارسی\n2:English\n"))
if language==1:
    #کتابخانه rich
    import rich as ri
    from rich.console import Console
    #یک جای خالی ایجاد کنیم.
    console = Console()
    def printpercent(percent, disease):
        # نمایش ورودی‌ها به رنگ قرمز
        return f"شما به احتمال [red]{percent}[/red] درصد به بیماری [red]{disease}[/red] مبتلا شده‌اید!"


    # مشخصات بیمار

    print("لطفا مشخصات خود را وارد کنید.")
    Name = input("نام: ")
    Family_name = input("نام خانوادگی: ")
    Age =int(input("سن: "))
    Gender = input("جنسیت: ")
    print()
    print(f"سلام {Name}! ما در این برنامه می خواهیم تا تشخیص اولیه از بیماری شما داشته باشیم و به شما راهکار پیشنهاد بدهیم.")
    print()# مشخصات بیمار

    #حالا باید از کاربر بپرسیم که علامت اصلی ای که دچارش است کدام است؟
    print("این برنامه در حال حاضر روی 5 علامت اصلی بیماری ها کار می کند:")
    Main_symptoms = ("درد شکم", "درد قفسه سینه", "سرفه", "درد کمر", "تنگی نفس")

    print("1=درد شکم\n2=درد قفسه سینه\n3=سرفه\n4=درد کمر\n5=تنگی نفس")
    A = int(input("لطفا به من بگو کدام یک از علامت های اصلی زیر را داری؟ "))

    if A == 1:
        print("شما شکم درد دارید.")
        areaOfThePain = int(input("بیشتر از همه درد را در چه ناحیه ای احساس میکنید؟\n 1. نزدیک قفسه سینه \n 2. اطراف ناف \n 3.درد جنرالیزنه شکم\n"))
        if areaOfThePain == 1:
            backPainCheck = int(input("آیا در پشت هم دردی احساس میکنید؟ \n 1. بله \n 2.خیر\n"))
            if backPainCheck == 1:
                otherAreaPainCheck = int(input("آیا در نواحی دیگری از شکم هم درد احساس میکنید؟ \n 1. بله \n 2. خیر\n"))
                if otherAreaPainCheck == 1:
                    console.print(printpercent(40-70, "پانکراتیت حاد"))
                    disease="آسم"
                    Treatment="برای آسم درمان پیشنهادی:سرم و مسکن است.\nهمچنین ممکن است چیزی نخورده باشد پس معده خالی\nحتما به پزشک مراجعه شود احتمال دارد نیاز به جراحی باشد. "
                    print(Treatment)
                elif otherAreaPainCheck == 2:
                    console.print(printpercent(60-80, "زخم معده"))
                    console.print(printpercent(15-30, "پانکراتیت مزمن"))
                    disease="زخم معده  و یا پانکراتیت مزمن"
                    Treatment="درمان پیشنهادی: برای زخم معده ابتدا ضد اسید هایی مثل پنتوپرازول یا اوموپرازول و شربت معده مصرف شود\nحتما به پزک مراجعه شود و اندوسکوپی شود ممکن است دچار خون ریزی شود.\nاگر پانکراتیت مزمن باشد سریع به جراح مراجعه شود ممکن است نیاز به جراحی باشد."
                    print(Treatment)
                else:
                    print("متاسفانه داده کافی برای تشخیص بیماری شما در دسترس نیست. \n لطفا به پزشک مراجعه کنید")
            elif backPainCheck == 2:
                console.print(printpercent(60-80, "رفلاکس معده به مری"))
                disease="رفلاکس معده به مری "
                Treatment="از ضد اسید ها مثل شربت معده و یا اوموپرازولو اگر بسیار شدید باشد تزریق پنتاپرازول\nدراز بکشد و سرتان را بالاتر از سطح بدن نگه دارید."
                print(Treatment)
            else:
                    print("متاسفانه خطایی پیش آماده است. لطفا از درست بودن فرمت داده وارد شده اطمینان حاصل کنید")
        elif areaOfThePain == 2:
            appandixCheck = int(input("ایا در نواحی تحتانی شکم هم درد احساس میکنید؟ \n 1. بله \n 2.خیر\n"))
            if appandixCheck == 1:
                console.print(printpercent(10-20, "آپاندیسیت حاد"))
                disease="آپاندیسیت حاد"
                Treatment="برای اپاندیسیت حاد مصرف آنتی بیوتیک اما حتما باید زیر نظر پزشک باشد و اینکه به جراح مراجعه شود شاید نیاز به جراحی باشد"
                print(Treatment)
            elif appandixCheck==2:
                print("متاسفانه داده کافی برای تشخیص بیماری شما در دسترس نیست. \n لطفا به پزشک مراجعه کنید")
            else:
                print("متاسفانه خطایی پیش آماده است. لطفا از درست بودن فرمت داده وارد شده اطمینان حاصل کنید")
        elif areaOfThePain == 3:
            crampyPainCheck = int(input("ایا درد به صورت کرامپی است؟ \n 1. بله \n 2.خیر\n"))
            if crampyPainCheck == 1:
                console.print(printpercent(50-70, "انسداد حاد روده"))
                disease="انسداد حاد روده"
                Treatment="برای انسداد حاد روده باید به جراح مراجعه شود و تا حد امکان از دارو مسکن سرخود دوری شود"
                print(Treatment)
            elif crampyPainCheck==2:
                print("متاسفانه داده کافی برای تشخیص بیماری شما در دسترس نیست. \n لطفا به پزشک مراجعه کنید")
            else:
               print("متاسفانه خطایی پیش آماده است. لطفا از درست بودن فرمت داده وارد شده اطمینان حاصل کنید")
        else:
            print("متاسفانه خطایی پیش آماده است. لطفا از درست بودن فرمت داده وارد شده اطمینان حاصل کنید")
            
    ###################################################    
    elif A == 2:
        print("شما درد قفسه سینه دارید.")
        AreaOfThePain = int(input("بیشتر در کدام قسمت درد را احساس می کنید؟ \n 1. پشت جناغ \n 2. زیر پستان چپ \n 3. در طول غضروف دنده ای \n"))
        print()
       
        if AreaOfThePain == 1:
            BackPainCheck = int(input("آیا درد شما به پشت نیز منتشر شده است؟ \n 1. بله \n 2. خیر، درد اغلب به مثانه ها، \n بازوها، گردن، فک تحتانی یا قسمت فوقانی شکم منتشر می شود. \n 3. گزینه های دیگر\n"))
            print()

            if BackPainCheck == 2:
               IntensityBladderPainCheck = int(input("شدت درد شما چقدر است؟ \n 1.خفیف \n 2.متوسط \n 3.شدید\n"))
               print()
               if IntensityBladderPainCheck == 1:
                   associated_symptoms = int(input("علائم همراه خود را انتخاب کنید. \n 1.تنگی نفس \n 2.تهوع \n 3.تنگس نفس و تهوع \n 4.گزینه های دیگر\n"))
                   if associated_symptoms == 1:
                       console.print(printpercent(25, "آنزین صدری"))
                       disease="آنژین صدری"
                       Treatment="از نیتروگلیسیرین استفاده کنید ولی برای نتایج دقیق تر، \n برای آنژین صدری پیشنهاد می شود که به پزشک مراجعه کنید."
                       print("زمان بندی آن: \n معمولا 1 تا 3 دقیقه \n **عوامل تشدید کننده ی آن: \n اغلب فعالیت، به خصوص هوای سرد، غذا خوردن و استرس عاطفی** \n **عوامل تخفیف دهنده ی آن: \n اغلب استراحت و استفاده از نیتروگلیسیرین**")
                       print(Treatment)
                   elif associated_symptoms == 2:
                        console.print(printpercent(20, "آنزین صدری"))
                        disease="آنژین صدری"
                        Treatment="از نیتروگلیسیرین استفاده کنید ولی برای نتایج دقیق تر، \n برای آنژین صدری پیشنهاد می شود که به پزشک مراجعه کنید."
                        print("زمان بندی آن: \n معمولا 1 تا 3 دقیقه \n **عوامل تشدید کننده ی آن: \n اغلب فعالیت، به خصوص هوای سرد، غذا خوردن و استرس عاطفی** \n **عوامل تخفیف دهنده ی آن: \n اغلب استراحت و استفاده از نیتروگلیسیرین**")
                        print(Treatment)
                   elif associated_symptoms == 3:
                          console.print(printpercent(30, "آنزین صدری"))
                          disease="آنژین صدری"
                          Treatment="از نیتروگلیسیرین استفاده کنید ولی برای نتایج دقیق تر، \n برای آنژین صدری پیشنهاد می شود که به پزشک مراجعه کنید."
                          print("زمان بندی آن: \n معمولا 1 تا 3 دقیقه \n **عوامل تشدید کننده ی آن: \n اغلب فعالیت، به خصوص هوای سرد، غذا خوردن و استرس عاطفی** \n **عوامل تخفیف دهنده ی آن: \n اغلب استراحت و استفاده از نیتروگلیسیرین**")
                          print(Treatment)
                   else:
                       print("متاسفیم، اطلاعات کافی برای تشخیص مشکل شما در دسترس نیست. \n لطفا به پزشک خود مراجعه کنید.")
                        
                    
               elif IntensityBladderPainCheck == 2:
                   associated_symptoms = int(input("علائم همراه خود را انتخاب کنید. \n 1.تنگی نفس \n 2.تهوع \n 3.تنگس نفس و تهوع \n 4.گزینه های دیگر\n"))
                   if associated_symptoms == 1: 
                       console.print(printpercent(40-50, "آنزین صدری"))
                       disease="آنژین صدری"
                       Treatment="از نیتروگلیسیرین استفاده کنید ولی برای نتایج دقیق تر، \n برای آنژین صدری پیشنهاد می شود که به پزشک مراجعه کنید."
                       print("زمان بندی آن: \n معمولا 1 تا 3 دقیقه \n **عوامل تشدید کننده ی آن: \n اغلب فعالیت، به خصوص هوای سرد، غذا خوردن و استرس عاطفی** \n **عوامل تخفیف دهنده ی آن: \n اغلب استراحت و استفاده از نیتروگلیسیرین**")
                       print(Treatment)
                   elif associated_symptoms == 2:
                       console.print(printpercent(35-45, "آنزین صدری"))
                       disease="آنژین صدری"
                       Treatment="از نیتروگلیسیرین استفاده کنید ولی برای نتایج دقیق تر، \n برای آنژین صدری پیشنهاد می شود که به پزشک مراجعه کنید."
                       print("زمان بندی آن: \n معمولا 1 تا 3 دقیقه \n **عوامل تشدید کننده ی آن: \n اغلب فعالیت، به خصوص هوای سرد، غذا خوردن و استرس عاطفی** \n **عوامل تخفیف دهنده ی آن: \n اغلب استراحت و استفاده از نیتروگلیسیرین**")
                       print(Treatment)
                   elif associated_symptoms == 3:
                       console.print(printpercent(50-60, "آنزین صدری"))
                       disease="آنژین صدری"
                       Treatment="از نیتروگلیسیرین استفاده کنید ولی برای نتایج دقیق تر، \n برای آنژین صدری پیشنهاد می شود که به پزشک مراجعه کنید."
                       print("زمان بندی آن: \n معمولا 1 تا 3 دقیقه \n **عوامل تشدید کننده ی آن: \n اغلب فعالیت، به خصوص هوای سرد، غذا خوردن و استرس عاطفی** \n **عوامل تخفیف دهنده ی آن: \n اغلب استراحت و استفاده از نیتروگلیسیرین**")
                       print(Treatment)
                   elif associated_symptoms == 4:
                       print("متاسفیم، اطلاعات کافی برای تشخیص بیماری شما در دسترس نیست. \n لطفا به پزشک خود مراجعه کنید.")
                        
               elif IntensityBladderPainCheck == 3:
                   associated_symptoms = int(input("علائم همراه خود را انتخاب کنید. \n 1.تنگی نفس \n 2.تهوع \n 3.تنگس نفس و تهوع \n 4.گزینه های دیگر\n"))
                   if associated_symptoms == 1: 
                       console.print(printpercent(70-80, "سکته قلبی"))
                       disease="سکته قلبی"
                       Treatment="برای سکته قلبی از نیتروگلیسیرین استفاده کنید\n و سپس خیلی سریع آنژیوگرافی انجام دهید."
                       print("زمان بندی آن: 20 دقیقه تا چند ساعت \n **فعالیت همیشه باعث بدتر شدن این بیماری نمی شود.** \n **این بیماری با استراحت بهبود نمی یابد.**")
                       print(Treatment)
                   elif associated_symptoms == 2:
                       console.print(printpercent(65-75, "سکته قلبی"))
                       disease="سکته قلبی"
                       Treatment="از نیتروگلیسیرین استفاده کنید \n و سپس خیلی سریع آنژیوگرافی انجام دهید."
                       print("زمان بندی آن: 20 دقیقه تا چند ساعت \n **فعالیت همیشه باعث بدتر شدن این بیماری نمی شود.** \n **این بیماری با استراحت بهبود نمی یابد.**")
                       print(Treatment)
                   elif associated_symptoms == 3:
                       console.print(printpercent(80-90, "سکته قلبی"))
                       disease="سکته قلبی"
                       Treatment="برای سکته قلبی از نیتروگلیسیرین استفاده کنید\n و سپس خیلی سریع آنژیوگرافی انجام دهید."
                       print("زمان بندی آن: 20 دقیقه تا چند ساعت \n **فعالیت همیشه باعث بدتر شدن این بیماری نمی شود.** \n **این بیماری با استراحت بهبود نمی یابد.**")
                       print(Treatment)
                   elif associated_symptoms == 4:
                       print("متاسفیم، اطلاعات کافی برای تشخیص مشکل شما در دسترس نیست. \n لطفا به پزشک خود مراجعه کنید.")
              
            elif BackPainCheck == 1:
                QualityBackPainCheck = int(input("کیفیت درد شما به چه صورت است؟ \n 1.سوزاننده \n 2.سوزاننده و فشارنده \n 3.گزینه های دیگر\n"))
                if QualityBackPainCheck == 1:
                    IntensityBackPainCheck = int(input("شدت درد شما به چه صورت است؟ \n 1.متوسط \n 2.شدید\n"))
                    if IntensityBackPainCheck == 1:
                        Cough = int(input("آیا سرفه می کنید؟ \n 1.بله \n 2.خیر\n"))
                        if Cough == 1:
                            console.print(printpercent(40, "رفلاکس معده به مری"))
                            disease="رفلاکس معده به مری"
                            Treatment="برای رفلاکس معده به مری از اوموپرازول استفاده کنید\n و اگر شدید شد، پنتاپرازول تزریق کنید."
                            print("زمان بندی آن: متغیر \n **عوامل تشدید کننده ی آن: \n معده ی غذایی بزگ، خم شدن و دراز کشیدن** \n **عوامل تخفیف دهنده ی آن: \n آنتی اسید ها و گاهی آروغ زدن**")
                            print(Treatment)
                        elif Cough == 2:
                            console.print(printpercent(35, "رفلاکس معده به مری"))
                            disease="رفلاکس معده به مری"
                            Treatment="برای رفلاکس معده به مری از اوموپرازول استفاده کنید\n و اگر شدید شد، پنتاپرازول تزریق کنید."
                            print("زمان بندی آن: متغیر \n **عوامل تشدید کننده ی آن: \n معده ی غذایی بزگ، خم شدن و دراز کشیدن** \n **عوامل تخفیف دهنده ی آن: \n آنتی اسید ها و گاهی آروغ زدن**")
                            print(Treatment)
                    elif IntensityBackPainCheck == 2:
                        Cough = int(input("آیا سرفه می کنید؟ \n 1.بله \n 2.خیر\n"))
                        if Cough == 1:
                            console.print(printpercent(60, "رفلاکس معده به مری"))
                            disease="رفلاکس معده به مری"
                            Treatment="برای رفلاکس معده به مری از اوموپرازول استفاده کنید\n و اگر شدید شد، پنتاپرازول تزریق کنید."
                            print("زمان بندی آن: متغیر \n **عوامل تشدید کننده ی آن: \n معده ی غذایی بزگ، خم شدن و دراز کشیدن** \n **عوامل تخفیف دهنده ی آن: \n آنتی اسید ها و گاهی آروغ زدن**")
                            print(Treatment)
                        elif Cough == 2:
                            console.print(printpercent(50, "رفلاکس معده به مری"))
                            disease="رفلاکس معده به مری"
                            Treatment="برای رفلاکس معده به مری از اوموپرازول استفاده کنید\n و اگر شدید شد، پنتاپرازول تزریق کنید."
                            print("زمان بندی آن: متغیر \n **عوامل تشدید کننده ی آن: \n معده ی غذایی بزگ، خم شدن و دراز کشیدن** \n **عوامل تخفیف دهنده ی آن: \n آنتی اسید ها و گاهی آروغ زدن**")
                            print(Treatment)
                
                elif QualityBackPainCheck == 2:
                    IntensityBackPainCheck = int(input("شدت درد شما به چه صورت است؟ \n 1.متوسط \n 2.شدید\n"))
                    if IntensityBackPainCheck == 1:
                        Cough = int(input("آیا سرفه می کنید؟ \n 1.بله \n 2.خیر\n"))
                        if Cough == 1:
                            console.print(printpercent(45, "رفلاکس معده به مری"))
                            disease="رفلاکس معده به مری"
                            Treatment="برای رفلاکس معده به مری از اوموپرازول استفاده کنید\n و اگر شدید شد، پنتاپرازول تزریق کنید."
                            print("زمان بندی آن: متغیر \n **عوامل تشدید کننده ی آن: \n معده ی غذایی بزگ، خم شدن و دراز کشیدن** \n **عوامل تخفیف دهنده ی آن: \n آنتی اسید ها و گاهی آروغ زدن**")
                            print(Treatment)
                        elif Cough == 2:
                            console.print(printpercent(40, "رفلاکس معده به مری"))
                            disease="رفلاکس معده به مری"
                            Treatment="برای رفلاکس معده به مری از اوموپرازول استفاده کنید\n و اگر شدید شد، پنتاپرازول تزریق کنید."
                            print("زمان بندی آن: متغیر \n **عوامل تشدید کننده ی آن: \n معده ی غذایی بزگ، خم شدن و دراز کشیدن** \n **عوامل تخفیف دهنده ی آن: \n آنتی اسید ها و گاهی آروغ زدن**")
                            print(Treatment)
                    elif IntensityBackPainCheck == 2:
                        Cough = int(input("آیا سرفه می کنید؟ \n 1.بله \n 2.خیر\n"))
                        if Cough == 1:
                            console.print(printpercent(65, "رفلاکس معده به مری"))
                            disease="رفلاکس معده به مری"
                            Treatment="برای رفلاکس معده به مری از اوموپرازول استفاده کنید\n و اگر شدید شد، پنتاپرازول تزریق کنید."
                            print("زمان بندی آن: متغیر \n **عوامل تشدید کننده ی آن: \n معده ی غذایی بزگ، خم شدن و دراز کشیدن** \n **عوامل تخفیف دهنده ی آن: \n آنتی اسید ها و گاهی آروغ زدن**")
                            print(Treatment)
                        elif Cough == 2:
                            console.print(printpercent(55, "رفلاکس معده به مری"))
                            disease="رفلاکس معده به مری"
                            Treatment="برای رفلاکس معده به مری از اوموپرازول استفاده کنید\n و اگر شدید شد، پنتاپرازول تزریق کنید."
                            print("زمان بندی آن: متغیر \n **عوامل تشدید کننده ی آن: \n معده ی غذایی بزگ، خم شدن و دراز کشیدن** \n **عوامل تخفیف دهنده ی آن: \n آنتی اسید ها و گاهی آروغ زدن**")
                            print(Treatment)    
             
                elif QualityBackPainCheck == 3:
                    print("متاسفیم، اطلاعات کافی برای تشخیص مشکل شما در دسترس نیست. \n لطفا به پزشک خود مراجعه کنید.")
             
            elif BackPainCheck == 3:
                print("متاسفیم، اطلاعات کافی برای تشخیص مشکل شما در دسترس نیست. \n لطفا به پزشک خود مراجعه کنید.")
                  
        elif AreaOfThePain == 3:
            QualityCheck = int(input("آیا کیفیت درد شما تیز، مبهم و بی تاب کننده است؟ \n 1.بله \n 2.خیر \n"))
            if QualityCheck == 1:
                SensitivityCheck = int(input("آیا شما به لمس موضعی حسایت دارید؟ \n 1.بله \n 2.خیر \n"))
                if SensitivityCheck == 1:
                    console.print(printpercent(70-80, "درد دیواره قفسه سینه"))
                    disease="درد دیواره قفسه سینه"
                    Treatment="برای درد دیواره قفسه سینه اگر دیواره ی قفسه سینه ی شما شکسته باشد؛\n باید صبر و استراحت کنید. \n اگر نشکسته باشد؛ باید صبر کنید تا کبودی رفع شود."
                    print("زمان بندی آن: ساعت ها تا روز ها \n **عوامل تشدید کننده ی آن: \n سرفه، حرکات قفسه سینه و دست ها**")
                    print(Treatment)                  
                elif SensitivityCheck == 2:
                    console.print(printpercent(50-60, "درد دیواره قفسه سینه"))
                    disease="درد دیواره قفسه سینه"
                    Treatment="برای درد دیواره قفسه سینه اگر دیواره ی قفسه سینه ی شما شکسته باشد؛\n باید صبر و استراحت کنید. \n اگر نشکسته باشد؛ باید صبر کنید تا کبودی رفع شود."
                    print("زمان بندی آن: ساعت ها تا روز ها \n **عوامل تشدید کننده ی آن: \n سرفه، حرکات قفسه سینه و دست ها**")
                    print(Treatment)          
                    
            elif QualityCheck == 2:
                print("متاسفیم، اطلاعات کافی برای تشخیص مشکل شما در دسترس نیست. \n لطفا به پزشک خود مراجعه کنید.")
              
        elif AreaOfThePain == 2:
            PainInTheFrontCheck = int(input("آیا روی قدام سینه ی خود، درد احساس می کنید؟ \n 1.بله \n 2.خیر \n"))
            if PainInTheFrontCheck == 2:
                QualityFrontCheck = int(input("آیا کیفیت درد شما تیز، مبهم و بی تاب کننده است؟ \n 1.بله \n 2.خیر \n"))
                if QualityFrontCheck == 1:
                    SensitivityFrontCheck = int(input("آیا شما به لمس موضعی حسایت دارید؟ \n 1.بله \n 2.خیر \n"))
                    if SensitivityFrontCheck == 1:
                        console.print(printpercent(60-70, "درد دیواره قفسه سینه"))
                        disease="درد دیواره قفسه سینه"
                        Treatment="برای درد دیواره قفسه سینه اگر دیواره ی قفسه سینه ی شما شکسته باشد؛\n باید صبر و استراحت کنید. \n اگر نشکسته باشد؛ باید صبر کنید تا کبودی رفع شود."
                        print("زمان بندی آن: ساعت ها تا روز ها \n **عوامل تشدید کننده ی آن: \n سرفه، حرکات قفسه سینه و دست ها**")
                        print(Treatment)     
                    elif SensitivityFrontCheck == 2:
                        console.print(printpercent(50-60, "درد دیواره قفسه سینه"))
                        disease="درد دیواره قفسه سینه"
                        Treatment="برای درد دیواره قفسه سینه اگر دیواره ی قفسه سینه ی شما شکسته باشد؛\n باید صبر و استراحت کنید. \n اگر نشکسته باشد؛ باید صبر کنید تا کبودی رفع شود."
                        print("زمان بندی آن: ساعت ها تا روز ها \n **عوامل تشدید کننده ی آن: \n سرفه، حرکات قفسه سینه و دست ها**")
                        print(Treatment)          
                elif QualityFrontCheck == 2:
                    print("متاسفیم، اطلاعات کافی برای تشخیص مشکل شما در دسترس نیست. \n لطفا به پزشک خود مراجعه کنید.")
                    
            elif PainInTheFrontCheck == 1:
                QualityFrontCheck2 = int(input("آیا کیفیت درد شما تیز، مبهم و بی تاب کننده است؟ \n 1.بله \n 2.خیر \n"))
                if QualityFrontCheck2 == 1:
                    print("حال باید بفهمیم شما چه علائم همراهی دارید.")
                    print(" 1.تنگی نفس \n 2.تپش قلب ضعیف \n 3.اضطراب \n 4.گزینه های دیگر")
                    print()
                    associated_symptoms=input("کدام یک ار علائم همراه را دارید؟ \n شما میتوانید چند گزینه هم انتخاب کنید. /n فقط کافی است بین اعداد  ,  قرار دهید.\n")
                    print()
                    associated_symptoms=set(map(int,associated_symptoms.split(",")))
                    if associated_symptoms == {1}:
                        console.print(printpercent(40, "اضظزاب و اختلالات روانی"))
                        disease="اضظراب و اختلالات روانی"
                        Treatment="برای اضطراب و اختلالات روانی به روان پزشک مراجعه کرده و در صورت نیاز داروی اعصاب مصرف کنید."
                        print("زمان بندی آن: ساعت ها تا روز ها \n **عوامل تشدید کننده ی آن: فعالیت و استرس عاطفی**")
                        print(Treatment)
                    elif associated_symptoms == {2}:
                        console.print(printpercent(35, "اضظزاب و اختلالات روانی"))
                        disease="اضظراب و اختلالات روانی"
                        Treatment="برای اضطراب و اختلالات روانی به روان پزشک مراجعه کرده و در صورت نیاز داروی اعصاب مصرف کنید."
                        print("زمان بندی آن: ساعت ها تا روز ها \n **عوامل تشدید کننده ی آن: فعالیت و استرس عاطفی**")
                        print(Treatment)
                    elif associated_symptoms == {3}:
                        console.print(printpercent(50, "اضظزاب و اختلالات روانی"))
                        disease="اضظراب و اختلالات روانی"
                        Treatment="برای اضطراب و اختلالات روانی به روان پزشک مراجعه کرده و در صورت نیاز داروی اعصاب مصرف کنید."
                        print("زمان بندی آن: ساعت ها تا روز ها \n **عوامل تشدید کننده ی آن: فعالیت و استرس عاطفی**")
                        print(Treatment)
                    elif associated_symptoms == {1,2}:
                        console.print(printpercent(45, "اضظزاب و اختلالات روانی"))
                        disease="اضظراب و اختلالات روانی"
                        Treatment="برای اضطراب و اختلالات روانی به روان پزشک مراجعه کرده و در صورت نیاز داروی اعصاب مصرف کنید."
                        print("زمان بندی آن: ساعت ها تا روز ها \n **عوامل تشدید کننده ی آن: فعالیت و استرس عاطفی**")
                        print(Treatment)
                    elif associated_symptoms == {1,3}:
                        console.print(printpercent(55, "اضظزاب و اختلالات روانی"))
                        disease="اضظراب و اختلالات روانی"
                        Treatment="برای اضطراب و اختلالات روانی به روان پزشک مراجعه کرده و در صورت نیاز داروی اعصاب مصرف کنید."
                        print("زمان بندی آن: ساعت ها تا روز ها \n **عوامل تشدید کننده ی آن: فعالیت و استرس عاطفی**")
                        print(Treatment)
                    elif associated_symptoms == {2,3}:
                        console.print(printpercent(50, "اضظزاب و اختلالات روانی"))
                        disease="اضظراب و اختلالات روانی"
                        Treatment="برای اضطراب و اختلالات روانی به روان پزشک مراجعه کرده و در صورت نیاز داروی اعصاب مصرف کنید."
                        print("زمان بندی آن: ساعت ها تا روز ها \n **عوامل تشدید کننده ی آن: فعالیت و استرس عاطفی**")
                        print(Treatment)
                    elif associated_symptoms == {1,2,3}:
                        console.print(printpercent(60-70, "اضظزاب و اختلالات روانی"))
                        disease="اضظراب و اختلالات روانی"
                        Treatment="برای اضطراب و اختلالات روانی به روان پزشک مراجعه کرده و در صورت نیاز داروی اعصاب مصرف کنید."
                        print("زمان بندی آن: ساعت ها تا روز ها \n **عوامل تشدید کننده ی آن: فعالیت و استرس عاطفی**")
                        print(Treatment)
                    elif associated_symptoms == {4}:
                        print("متاسفیم، اطلاعات کافی برای تشخیص مشکل شما در دسترس نیست. \n لطفا به پزشک خود مراجعه کنید.")
                        
                         
                         
                elif QualityFrontCheck2 == 2:
                    print("متاسفیم، اطلاعات کافی برای تشخیص مشکل شما در دسترس نیست. \n لطفا به پزشک خود مراجعه کنید.")
                                
    ##################################################    
    elif A == 3:
        print("شما سرفه دارید.")
         #باید بفهیم دچار چه نوع سرفه ای است.
        print()
        print("اکنون نیاز است تا بفهمم دچار چه نوع سرفه ای هستید. از بین عوامل زیر انتخاب کنید.")
        print("1=سرفه خشک\n2=خلط موکوئیدی یا همان ژلاتینی\n3=خلط چرکی آغشته به خون\n4=خلط چرکی بدون خون\n5=خلط چرکی کاملا خونی\n6=سرفه مزمن خصوصا در شب\n7=سرفه متغیر در مکان ها و زمان خاص")
        print()
        cough=input("کدام یک از سرفه ها را دارید؟می توانید چند مورد را هم انتخاب کنید فقط کافی است بین اعداد  ,  قرار دهید")
        #از split استفاده می کنیم برای اینکه اون string بالا را اعدادش را و ',' از هم جدا می کنه
        # از تابع map اینجا استفاده می کنیم برای اینکه تمامی اطلاعات ورودی را به دیتا های عددی تبدیل کنیم.
        cough=set(map(int,cough.split(",")))
        print()
         #حالا باید بفهیم دچار چه علائم همراهی است.
        print("اکنون نیاز است تا بفهمم دچار چه علائم همراهی هستید. از بین عوامل زیر انتخاب کنید.")
        print("1=تب\n2=سردرد\n3=تنگی نفس\n4=درد قفسه سینه\n5=لرز\n6=ترشح پشت بینی\n7=بی اشتهایی\n8=کاهش وزن\n9=خستگی\n10=تعق شبانه\n11=در مواجه با محرک سرفه ایجاد می شود\n12=عفونت\n13=سابقه الرژی\n15=خس خس\n16=فقط سرفه بدون علائم همراه")
        print()
        associated_symptoms=input("کدام یک از علائم همراه را دارید؟می توانید چند مورد را هم انتخاب کنید فقط کافی است بین اعداد  ,  قرار دهید.")
        associated_symptoms=set(map(int,associated_symptoms.split(",")))
        #عفونت ریه ویروسی
        #سرفه خشک
        if cough == {1} and associated_symptoms == {1}:
            console.print(printpercent(30, "عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough == {1} and associated_symptoms == {2}:
            console.print(printpercent(25, "عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough == {1} and associated_symptoms == {3}:
            console.print(printpercent(40, "عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough == {1} and associated_symptoms == {1, 2}:
            console.print(printpercent(40, "عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough == {1} and associated_symptoms == {1, 3}:
            console.print(printpercent(50, "عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough == {1} and associated_symptoms == {2, 3}:
            console.print(printpercent(35, "عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough == {1} and associated_symptoms == {1, 2, 3}:
            console.print(printpercent(60, "عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough == {1} and associated_symptoms == {16}:
            console.print(printpercent(20, "عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"


        # خلط موکوئیدی
        elif cough=={2} and associated_symptoms=={1}:
            console.print(printpercent(20,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={2} and associated_symptoms=={2}:
            console.print(printpercent(15,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={2} and associated_symptoms=={3}:
            console.print(printpercent(30,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={2} and associated_symptoms=={1,2}:
            console.print(printpercent(30,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={2} and associated_symptoms=={1,3}:
            console.print(printpercent(40,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={2} and associated_symptoms=={2,3}:
            console.print(printpercent(25,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={2} and associated_symptoms=={1,2,3}:
            console.print(printpercent(50,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={2} and associated_symptoms=={16}:
            console.print(printpercent(35,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"


        # خلط چرکی
        elif cough=={4} and associated_symptoms=={1}:
            console.print(printpercent(25,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={4} and associated_symptoms=={2}:
            console.print(printpercent(20,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={4} and associated_symptoms=={3}:
            console.print(printpercent(35,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={4} and associated_symptoms=={1,2}:
            console.print(printpercent(35,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={4} and associated_symptoms=={1,3}:
            console.print(printpercent(45,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={4} and associated_symptoms=={2,3}:
            console.print(printpercent(30,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={4} and associated_symptoms=={1,2,3}:
            console.print(printpercent(55,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={4} and associated_symptoms=={16}:
            console.print(printpercent(60,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        # سرفه خشک و خلط موکوئیدی
        elif cough=={1,2} and associated_symptoms=={1}:
            console.print(printpercent(35,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,2} and associated_symptoms=={2}:
            console.print(printpercent(30,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,2} and associated_symptoms=={3}:
            console.print(printpercent(45,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,2} and associated_symptoms=={1,2}:
            console.print(printpercent(45,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,2} and associated_symptoms=={1,3}:
            console.print(printpercent(60,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,2} and associated_symptoms=={2,3}:
            console.print(printpercent(40,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,2} and associated_symptoms=={1,2,3}:
            console.print(printpercent(70,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,2} and associated_symptoms=={16}:
            console.print(printpercent(40,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        # سرفه خشک و خلط چرکی
        elif cough=={1,4} and associated_symptoms=={1}:
            console.print(printpercent(30,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,4} and associated_symptoms=={2}:
            console.print(printpercent(30,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,4} and associated_symptoms=={3}:
            console.print(printpercent(40,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,4} and associated_symptoms=={1,2}:
            console.print(printpercent(45,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,4} and associated_symptoms=={1,3}:
            console.print(printpercent(45,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,4} and associated_symptoms=={2,3}:
            console.print(printpercent(40,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,4} and associated_symptoms=={1,2,3}:
            console.print(printpercent(75,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,4} and associated_symptoms=={16}:
            console.print(printpercent(55,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        # خلط موکوئیدی و خلط چرکی
        elif cough=={2,4} and associated_symptoms=={1}:
            console.print(printpercent(30,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={2,4} and associated_symptoms=={2}:
            console.print(printpercent(25,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={2,4} and associated_symptoms=={3}:
            console.print(printpercent(40,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={2,4} and associated_symptoms=={1,2}:
            console.print(printpercent(35,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={2,4} and associated_symptoms=={1,3}:
            console.print(printpercent(55,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={2,4} and associated_symptoms=={2,3}:
            console.print(printpercent(40,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={2,4} and associated_symptoms=={1,2,3}:
            console.print(printpercent(65,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={2,4} and associated_symptoms=={16}:
            console.print(printpercent(50,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"

        # سرفه خشک، خلط موکوئیدی و خلط چرکی
        elif cough=={1,2,4} and associated_symptoms=={1}:
            console.print(printpercent(45,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,2,4} and associated_symptoms=={2}:
            console.print(printpercent(35,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,2,4} and associated_symptoms=={3}:
            console.print(printpercent(50,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,2,4} and associated_symptoms=={1,2}:
            console.print(printpercent(55,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,2,4} and associated_symptoms=={1,3}:
            console.print(printpercent(65,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,2,4} and associated_symptoms=={2,3}:
            console.print(printpercent(55,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,2,4} and associated_symptoms=={1,2,3}:
            console.print(printpercent(75,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        elif cough=={1,2,4} and associated_symptoms=={16}:
            console.print(printpercent(65,"عفونت ریه ویروسی"))
            disease = "عفونت ریه ویروسی"
        
            
     #عفونت ریه باکتریایی
            #خلط موکوئیدی
        if cough=={2} and associated_symptoms=={1}:
            console.print(printpercent(20,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2} and associated_symptoms=={3}:
            console.print(printpercent(25,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2} and associated_symptoms=={4}:
            console.print(printpercent(30,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2} and associated_symptoms=={5}:
            console.print(printpercent(15,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2} and associated_symptoms=={1,3}:
            console.print(printpercent(35,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2} and associated_symptoms=={1,4}:
            console.print(printpercent(40,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2} and associated_symptoms=={1,5}:
            console.print(printpercent(25,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2} and associated_symptoms=={3,4}:
            console.print(printpercent(20,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2} and associated_symptoms=={3,5}:
            console.print(printpercent(20,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2} and associated_symptoms=={4,5}:
            console.print(printpercent(25,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2} and associated_symptoms=={1,3,4}:
            console.print(printpercent(45,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2} and associated_symptoms=={1,3,5}:
            console.print(printpercent(30,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2} and associated_symptoms=={3,4,5}:
            console.print(printpercent(35,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
       
        # خلط چرکی آغشته به خون
        elif cough=={3} and associated_symptoms=={1}:
            console.print(printpercent(35,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3} and associated_symptoms=={3}:
            console.print(printpercent(40,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3} and associated_symptoms=={4}:
            console.print(printpercent(45,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3} and associated_symptoms=={5}:
            console.print(printpercent(30,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3} and associated_symptoms=={1,3}:
            console.print(printpercent(45,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3} and associated_symptoms=={1,4}:
            console.print(printpercent(50,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3} and associated_symptoms=={1,5}:
            console.print(printpercent(35,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3} and associated_symptoms=={3,4}:
            console.print(printpercent(45,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3} and associated_symptoms=={3,5}:
            console.print(printpercent(35,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3} and associated_symptoms=={4,5}:
            console.print(printpercent(40,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3} and associated_symptoms=={1,3,4}:
            console.print(printpercent(55,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3} and associated_symptoms=={1,3,5}:
            console.print(printpercent(40,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3} and associated_symptoms=={3,4,5}:
            console.print(printpercent(45,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3} and associated_symptoms=={1,2,3,4}:
            console.print(printpercent(60,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3} and associated_symptoms=={16}:
            console.print(printpercent(70,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
       
        # خلط چرکی بدون خون
        elif cough=={4} and associated_symptoms=={1}:
            console.print(printpercent(30,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={4} and associated_symptoms=={3}:
            console.print(printpercent(35,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={4} and associated_symptoms=={4}:
            console.print(printpercent(40,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={4} and associated_symptoms=={5}:
            console.print(printpercent(25,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={4} and associated_symptoms=={1,3}:
            console.print(printpercent(40,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={4} and associated_symptoms=={1,4}:
            console.print(printpercent(45,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={4} and associated_symptoms=={1,5}:
            console.print(printpercent(30,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={4} and associated_symptoms=={3,4}:
            console.print(printpercent(35,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={4} and associated_symptoms=={3,5}:
            console.print(printpercent(25,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={4} and associated_symptoms=={4,5}:
            console.print(printpercent(35,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={4} and associated_symptoms=={1,3,4}:
            console.print(printpercent(50,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={4} and associated_symptoms=={1,3,5}:
            console.print(printpercent(35,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={4} and associated_symptoms=={3,4,5}:
            console.print(printpercent(40,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={4} and associated_symptoms=={1,2,3,4}:
            console.print(printpercent(55,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={4} and associated_symptoms=={16}:
            console.print(printpercent(60,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"


        #خلط موکوئیدی و خلط چرکی آغشته به خون
        elif cough=={2,3} and associated_symptoms=={1}:
            console.print(printpercent(40,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3} and associated_symptoms=={3}:
            console.print(printpercent(45,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3} and associated_symptoms=={4}:
            console.print(printpercent(50,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3} and associated_symptoms=={5}:
            console.print(printpercent(35,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3} and associated_symptoms=={1,3}:
            console.print(printpercent(50,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3} and associated_symptoms=={1,4}:
            console.print(printpercent(55,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3} and associated_symptoms=={1,5}:
            console.print(printpercent(40,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3} and associated_symptoms=={3,4}:
            console.print(printpercent(45,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3} and associated_symptoms=={3,5}:
            console.print(printpercent(35,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3} and associated_symptoms=={4,5}:
            console.print(printpercent(40,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3} and associated_symptoms=={1,3,4}:
            console.print(printpercent(60,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3} and associated_symptoms=={1,3,5}:
            console.print(printpercent(45,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3} and associated_symptoms=={3,4,5}:
            console.print(printpercent(50,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3} and associated_symptoms=={1,2,3,4}:
            console.print(printpercent(65,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3} and associated_symptoms=={16}:
            console.print(printpercent(75,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"


        #خلط موکوئیدی و خلط چرکی بدون خون
        elif cough=={2,4} and associated_symptoms=={1}:
            console.print(printpercent(35,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,4} and associated_symptoms=={3}:
            console.print(printpercent(40,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,4} and associated_symptoms=={4}:
            console.print(printpercent(45,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,4} and associated_symptoms=={5}:
            console.print(printpercent(30,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,4} and associated_symptoms=={1,3}:
            console.print(printpercent(45,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,4} and associated_symptoms=={1,4}:
            console.print(printpercent(50,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,4} and associated_symptoms=={1,5}:
            console.print(printpercent(35,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,4} and associated_symptoms=={3,4}:
            console.print(printpercent(40,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,4} and associated_symptoms=={3,5}:
            console.print(printpercent(30,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,4} and associated_symptoms=={4,5}:
            console.print(printpercent(35,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,4} and associated_symptoms=={1,3,4}:
            console.print(printpercent(55,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,4} and associated_symptoms=={1,3,5}:
            console.print(printpercent(40,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,4} and associated_symptoms=={3,4,5}:
            console.print(printpercent(45,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,4} and associated_symptoms=={1,2,3,4}:
            console.print(printpercent(60,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,4} and associated_symptoms=={16}:
            console.print(printpercent(65,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
            
        # خلط چرکی آغشته به خون و خلط چرکی بدون خون
        elif cough=={3,4} and associated_symptoms=={1}:
            console.print(printpercent(35,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3,4} and associated_symptoms=={3}:
            console.print(printpercent(40,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3,4} and associated_symptoms=={4}:
            console.print(printpercent(45,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3,4} and associated_symptoms=={5}:
            console.print(printpercent(30,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3,4} and associated_symptoms=={1,3}:
            console.print(printpercent(45,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3,4} and associated_symptoms=={1,4}:
            console.print(printpercent(50,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3,4} and associated_symptoms=={1,5}:
            console.print(printpercent(35,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3,4} and associated_symptoms=={3,4}:
            console.print(printpercent(40,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3,4} and associated_symptoms=={3,5}:
            console.print(printpercent(30,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3,4} and associated_symptoms=={4,5}:
            console.print(printpercent(35,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3,4} and associated_symptoms=={1,3,4}:
            console.print(printpercent(55,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3,4} and associated_symptoms=={1,3,5}:
            console.print(printpercent(40,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3,4} and associated_symptoms=={3,4,5}:
            console.print(printpercent(50,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3,4} and associated_symptoms=={1,2,3,4}:
            console.print(printpercent(60,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={3,4} and associated_symptoms=={16}:
            console.print(printpercent(68,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"



        #خلط موکوئیدی و چرکی آغشته به خون و خلط چرکی بدون خون
        elif cough=={2,3,4} and associated_symptoms=={1}:
            console.print(printpercent(40,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3,4} and associated_symptoms=={3}:
            console.print(printpercent(45,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3,4} and associated_symptoms=={4}:
            console.print(printpercent(50,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3,4} and associated_symptoms=={5}:
            console.print(printpercent(35,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3,4} and associated_symptoms=={1,3}:
            console.print(printpercent(50,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3,4} and associated_symptoms=={1,4}:
            console.print(printpercent(55,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3,4} and associated_symptoms=={1,5}:
            console.print(printpercent(40,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3,4} and associated_symptoms=={3,4}:
            console.print(printpercent(45,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3,4} and associated_symptoms=={3,5}:
            console.print(printpercent(35,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3,4} and associated_symptoms=={4,5}:
            console.print(printpercent(40,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3,4} and associated_symptoms=={1,3,4}:
            console.print(printpercent(60,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3,4} and associated_symptoms=={1,3,5}:
            console.print(printpercent(45,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3,4} and associated_symptoms=={3,4,5}:
            console.print(printpercent(50,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3,4} and associated_symptoms=={1,2,3,4}:
            console.print(printpercent(65,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        elif cough=={2,3,4} and associated_symptoms=={16}:
            console.print(printpercent(80,"عفونت ریه باکتریایی"))
            disease = "عفونت ریه باکتریایی"
        

        
        
         #سینوزیت ویروسی یاسینوزیت باکتریایی و یا آلرژی)ترشح پشت بینی(
        #خلط موکوئیدی
        if cough=={2} and associated_symptoms=={6}:
            console.print(printpercent(30, "سینوزیت ویروسی"))
            console.print(printpercent(25, "سینوزیت باکتریایی"))
            console.print(printpercent(20, "آلرژی"))
            disease="سینوزیت ویروسی یا باکتریایی و یا آلرژی"        
        
        #خلط چرکی بدون خون
        elif cough=={4} and associated_symptoms=={6}:
            console.print(printpercent(25, "سینوزیت ویروسی"))
            console.print(printpercent(20, "سینوزیت باکتریایی"))
            console.print(printpercent(15, "آلرژی"))
            disease="سینوزیت ویروسی یا باکتریایی و یا آلرژی"
      
        #سرفه مزمن
        elif cough=={6} and associated_symptoms=={6}:
             console.print(printpercent(20, "سینوزیت ویروسی"))
             console.print(printpercent(15, "سینوزیت باکتریایی"))
             console.print(printpercent(10, "آلرژی"))
             disease="سینوزیت ویروسی یا باکتریایی و یا آلرژی"
      
        #خلط موکوئیدی و خلط چرکی بدون خون
        elif cough=={2,4} and associated_symptoms=={6}:
             console.print(printpercent(35, "سینوزیت ویروسی"))
             console.print(printpercent(30, "سینوزیت باکتریایی"))
             console.print(printpercent(25, "آلرژی"))
             disease="سینوزیت ویروسی یا باکتریایی و یا آلرژی"
        #خلط موکوئیدی و سرفه مزمن
        elif cough=={2,6} and associated_symptoms=={6}:
            console.print(printpercent(25, "سینوزیت ویروسی"))
            console.print(printpercent(20, "سینوزیت باکتریایی"))
            console.print(printpercent(20, "آلرژی"))
            disease="سینوزیت ویروسی یا باکتریایی و یا آلرژی"
             
        #خلط چرکی بدون خون و سرفه مزمن
        elif cough=={4,6} and associated_symptoms=={6}:
            console.print(printpercent(35, "سینوزیت ویروسی"))
            console.print(printpercent(25, "سینوزیت باکتریایی"))
            console.print(printpercent(20, "آلرژی"))
            disease="سینوزیت ویروسی یا باکتریایی و یا آلرژی"
      
        #خلط موکوئیدی و خلط چرکی بدون خون و سرفه مزمن
        elif cough=={2,4,6} and associated_symptoms=={6}:
            console.print(printpercent(40, "سینوزیت ویروسی"))
            console.print(printpercent(35, "سینوزیت باکتریایی"))
            console.print(printpercent(30, "آلرژی"))
            disease="سینوزیت ویروسی یا باکتریایی و یا آلرژی"
            
    #بدون علائم همراه
        elif cough=={2} and associated_symptoms=={16}:
             console.print(printpercent(50, "سینوزیت ویروسی"))
             console.print(printpercent(20, "سینوزیت باکتریایی"))
             console.print(printpercent(40, "آلرژی"))
             disease="سینوزیت ویروسی یا باکتریایی و یا آلرژی"
        elif cough=={4} and associated_symptoms=={16}:
             console.print(printpercent(30, "سینوزیت ویروسی"))
             console.print(printpercent(70, "سینوزیت باکتریایی"))
             console.print(printpercent(10, "آلرژی"))
             disease="سینوزیت ویروسی یا باکتریایی و یا آلرژی"
        elif cough=={6} and associated_symptoms=={16}:
             console.print(printpercent(20, "سینوزیت ویروسی"))
             console.print(printpercent(30, "سینوزیت باکتریایی"))
             console.print(printpercent(50, "آلرژی"))
             disease="سینوزیت ویروسی یا باکتریایی و یا آلرژی"
        elif cough=={2,4} and associated_symptoms=={16}:
             console.print(printpercent(40, "سینوزیت ویروسی"))
             console.print(printpercent(60, "سینوزیت باکتریایی"))
             console.print(printpercent(25, "آلرژی"))
             disease="سینوزیت ویروسی یا باکتریایی و یا آلرژی"
        elif cough=={2,6} and associated_symptoms=={16}:
             console.print(printpercent(35, "سینوزیت ویروسی"))
             console.print(printpercent(25, "سینوزیت باکتریایی"))
             console.print(printpercent(45, "آلرژی"))
             disease="سینوزیت ویروسی یا باکتریایی و یا آلرژی"
        elif cough=={4,6} and associated_symptoms=={16}:
             console.print(printpercent(30, "سینوزیت ویروسی"))
             console.print(printpercent(70, "سینوزیت باکتریایی"))
             console.print(printpercent(20, "آلرژی"))
             disease="سینوزیت ویروسی یا باکتریایی و یا آلرژی"
        elif cough=={2,4,6} and associated_symptoms=={16}:
             console.print(printpercent(25, "سینوزیت ویروسی"))
             console.print(printpercent(75, "سینوزیت باکتریایی"))
             console.print(printpercent(30, "آلرژی"))
             disease="سینوزیت ویروسی یا باکتریایی و یا آلرژی"
       
                #سل ریوی
        #سرفه خشک
        if cough == {1} and associated_symptoms == {1}:
            console.print(printpercent(20, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {7}:
            console.print(printpercent(15, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {8}:
            console.print(printpercent(25, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {9}:
            console.print(printpercent(20, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {10}:
            console.print(printpercent(30, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {1, 7}:
            console.print(printpercent(25, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {1, 8}:
            console.print(printpercent(30, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {1, 9}:
            console.print(printpercent(25, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {1, 10}:
            console.print(printpercent(35, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {7, 8}:
            console.print(printpercent(20, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {7, 9}:
            console.print(printpercent(15, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {7, 10}:
            console.print(printpercent(25, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {8, 9}:
            console.print(printpercent(25, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {8, 10}:
            console.print(printpercent(35, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {9, 10}:
            console.print(printpercent(20, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {1, 7, 8}:
            console.print(printpercent(30, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {1, 7, 9}:
            console.print(printpercent(25, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {1, 7, 10}:
            console.print(printpercent(35, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {1, 8, 9}:
            console.print(printpercent(30, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {1, 8, 10}:
            console.print(printpercent(40, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {1, 9, 10}:
            console.print(printpercent(30, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {7, 8, 9}:
            console.print(printpercent(20, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {7, 8, 10}:
            console.print(printpercent(30, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {7, 9, 10}:
            console.print(printpercent(25, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {8, 9, 10}:
            console.print(printpercent(35, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {1, 7, 8, 9}:
            console.print(printpercent(40, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {1, 7, 8, 10}:
            console.print(printpercent(50, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {1, 7, 9, 10}:
            console.print(printpercent(45, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {1, 8, 9, 10}:
            console.print(printpercent(55, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {7, 8, 9, 10}:
            console.print(printpercent(50, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {1} and associated_symptoms == {1, 7, 8, 9, 10}:
            console.print(printpercent(60, "سل ریوی"))
            disease = "سل ریوی"



        #خلط موکوئیدی
        elif cough == {2} and associated_symptoms == {1}:
            console.print(printpercent(25, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {7}:
            console.print(printpercent(20, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {8}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {9}:
            console.print(printpercent(25, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {10}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {1, 7}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {1, 8}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {1, 9}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {1, 10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {7, 8}:
            console.print(printpercent(25, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {7, 9}:
            console.print(printpercent(20, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {7, 10}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {8, 9}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {8, 10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {9, 10}:
            console.print(printpercent(25, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {1, 7, 8}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {1, 7, 9}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {1, 7, 10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {1, 8, 9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {1, 8, 10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {1, 9, 10}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {7, 8, 9}:
            console.print(printpercent(25, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {7, 8, 10}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {7, 9, 10}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {8, 9, 10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {1, 7, 8, 9}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {1, 7, 8, 10}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {1, 7, 9, 10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {1, 8, 9, 10}:
            console.print(printpercent(60, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {7, 8, 9, 10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough == {2} and associated_symptoms == {1, 7, 8, 9, 10}:
            console.print(printpercent(65, "سل ریوی"))
            disease="سل ریوی"


        #خلط چرکی اغشته به خون
        elif cough == {3} and associated_symptoms == {1}:
            console.print(printpercent(30, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {7}:
            console.print(printpercent(25, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {8}:
            console.print(printpercent(35, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {9}:
            console.print(printpercent(30, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {10}:
            console.print(printpercent(40, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {1, 7}:
            console.print(printpercent(35, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {1, 8}:
            console.print(printpercent(40, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {1, 9}:
            console.print(printpercent(35, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {1, 10}:
            console.print(printpercent(45, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {7, 8}:
            console.print(printpercent(30, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {7, 9}:
            console.print(printpercent(25, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {7, 10}:
            console.print(printpercent(35, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {8, 9}:
            console.print(printpercent(35, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {8, 10}:
            console.print(printpercent(45, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {9, 10}:
            console.print(printpercent(30, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {1, 7, 8}:
            console.print(printpercent(40, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {1, 7, 9}:
            console.print(printpercent(35, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {1, 7, 10}:
            console.print(printpercent(45, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {1, 8, 9}:
            console.print(printpercent(40, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {1, 8, 10}:
            console.print(printpercent(50, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {1, 9, 10}:
            console.print(printpercent(40, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {7, 8, 9}:
            console.print(printpercent(30, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {7, 8, 10}:
            console.print(printpercent(40, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {7, 9, 10}:
            console.print(printpercent(35, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {8, 9, 10}:
            console.print(printpercent(45, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {1, 7, 8, 9}:
            console.print(printpercent(50, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {1, 7, 8, 10}:
            console.print(printpercent(60, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {1, 7, 9, 10}:
            console.print(printpercent(55, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {1, 8, 9, 10}:
            console.print(printpercent(65, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {7, 8, 9, 10}:
            console.print(printpercent(55, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {3} and associated_symptoms == {1, 7, 8, 9, 10}:
            console.print(printpercent(70, "سل ریوی"))
            disease = "سل ریوی"
        
        # خلط چرکی کاملا خونی
        elif cough == {5} and associated_symptoms == {1}:
            console.print(printpercent(70, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {7}:
            console.print(printpercent(30, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {8}:
            console.print(printpercent(40, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {9}:
            console.print(printpercent(35, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {10}:
            console.print(printpercent(45, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {1, 7}:
            console.print(printpercent(40, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {1, 8}:
            console.print(printpercent(45, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {1, 9}:
            console.print(printpercent(40, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {1, 10}:
            console.print(printpercent(50, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {7, 8}:
            console.print(printpercent(35, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {7, 9}:
            console.print(printpercent(30, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {7, 10}:
            console.print(printpercent(40, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {8, 9}:
            console.print(printpercent(40, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {8, 10}:
            console.print(printpercent(50, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {9, 10}:
            console.print(printpercent(35, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {1, 7, 8}:
            console.print(printpercent(45, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {1, 7, 9}:
            console.print(printpercent(40, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {1, 7, 10}:
            console.print(printpercent(50, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {1, 8, 9}:
            console.print(printpercent(45, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {1, 8, 10}:
            console.print(printpercent(55, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {1, 9, 10}:
            console.print(printpercent(45, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {7, 8, 9}:
            console.print(printpercent(35, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {7, 8, 10}:
            console.print(printpercent(45, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {7, 9, 10}:
            console.print(printpercent(40, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {8, 9, 10}:
            console.print(printpercent(50, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {1, 7, 8, 9}:
            console.print(printpercent(55, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {1, 7, 8, 10}:
            console.print(printpercent(65, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {1, 7, 9, 10}:
            console.print(printpercent(60, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {1, 8, 9, 10}:
            console.print(printpercent(70, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {7, 8, 9, 10}:
            console.print(printpercent(60, "سل ریوی"))
            disease = "سل ریوی"
        elif cough == {5} and associated_symptoms == {1, 7, 8, 9, 10}:
            console.print(printpercent(75, "سل ریوی"))
            disease = "سل ریوی"

        #سرفه خشک و خلط موکوئیدی
        elif cough=={1,2} and associated_symptoms=={1}:
            console.print(printpercent(25, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={7}:
            console.print(printpercent(20, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={8}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={9}:
            console.print(printpercent(25, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={10}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={1,7}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={1,8}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={1,9}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={1,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={7,8}:
            console.print(printpercent(25, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={7,9}:
            console.print(printpercent(20, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={7,10}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={8,9}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={8,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={9,10}:
            console.print(printpercent(25, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={1,7,8}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={1,7,9}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={1,7,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={1,8,9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={1,8,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={1,9,10}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={7,8,9}:
            console.print(printpercent(25, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={7,8,10}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={7,9,10}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={8,9,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={1,7,8,9}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={1,7,8,10}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={1,7,9,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={1,8,9,10}:
            console.print(printpercent(60, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={7,8,9,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={1,7,8,9,10}:
            console.print(printpercent(65, "سل ریوی"))
            disease="سل ریوی"



        #سرفه خشک و خلط چرکی آغشته به خون
        elif cough=={1,3} and associated_symptoms=={1}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={7}:
            console.print(printpercent(25, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={8}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={9}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={1,7}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={1,8}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={1,9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={1,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={7,8}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={7,9}:
            console.print(printpercent(25, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={7,10}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={8,9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={8,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={9,10}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={1,7,8}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={1,7,9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={1,7,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={1,8,9}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={1,8,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={1,9,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={7,8,9}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={7,8,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={7,9,10}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={8,9,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={1,7,8,9}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={1,7,8,10}:
            console.print(printpercent(60, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={1,7,9,10}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={1,8,9,10}:
            console.print(printpercent(65, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={7,8,9,10}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={1,7,8,9,10}:
            console.print(printpercent(70, "سل ریوی"))
            disease="سل ریوی"


        #سرفه خشک و خلط چرکی کاملاً خونی
        elif cough=={1,5} and associated_symptoms=={1}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={7}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={8}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={1,7}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={1,8}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={1,9}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={1,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={7,8}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={7,9}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={7,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={8,9}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={8,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={9,10}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={1,7,8}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={1,7,9}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={1,7,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={1,8,9}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={1,8,10}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={1,9,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={7,8,9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={7,8,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={7,9,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={8,9,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={1,7,8,9}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={1,7,8,10}:
            console.print(printpercent(65, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={1,7,9,10}:
            console.print(printpercent(60, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={1,8,9,10}:
            console.print(printpercent(70, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={7,8,9,10}:
            console.print(printpercent(60, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={1,7,8,9,10}:
            console.print(printpercent(75, "سل ریوی"))
            disease="سل ریوی"

     
        #خلط موکوئیدی و خلط چرکی آغشته به خون
        elif cough=={2,3} and associated_symptoms=={1}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={7}:
            console.print(printpercent(25, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={8}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={9}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={1,7}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={1,8}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={1,9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={1,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={7,8}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={7,9}:
            console.print(printpercent(25, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={7,10}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={8,9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={8,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={9,10}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={1,7,8}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={1,7,9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={1,7,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={1,8,9}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={1,8,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={1,9,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={7,8,9}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={7,8,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={7,9,10}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={8,9,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={1,7,8,9}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={1,7,8,10}:
            console.print(printpercent(60, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={1,7,9,10}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={1,8,9,10}:
            console.print(printpercent(65, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={7,8,9,10}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={1,7,8,9,10}:
            console.print(printpercent(70, "سل ریوی"))
            disease="سل ریوی"



        #خلط موکوئیدی و خلط چرکی کاملاًخونی
        elif cough=={2,5} and associated_symptoms=={1}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={7}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={8}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={1,7}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={1,8}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={1,9}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={1,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={7,8}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={7,9}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={7,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={8,9}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={8,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={9,10}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={1,7,8}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={1,7,9}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={1,7,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={1,8,9}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={1,8,10}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={1,9,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={7,8,9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={7,8,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={7,9,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={8,9,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={1,7,8,9}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={1,7,8,10}:
            console.print(printpercent(65, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={1,7,9,10}:
            console.print(printpercent(60, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={1,8,9,10}:
            console.print(printpercent(70, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={7,8,9,10}:
            console.print(printpercent(60, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={1,7,8,9,10}:
            console.print(printpercent(75, "سل ریوی"))
            disease="سل ریوی"



        #خلط چرکی اغشته به خون و خلط چرکی کاملاًخونی
        elif cough=={3,5} and associated_symptoms=={1}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={7}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={8}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={9}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={1,7}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={1,8}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={1,9}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={1,10}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={7,8}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={7,9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={7,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={8,9}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={8,10}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={9,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={1,7,8}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={1,7,9}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={1,7,10}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={1,8,9}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={1,8,10}:
            console.print(printpercent(60, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={1,9,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={7,8,9}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={7,8,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={7,9,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={8,9,10}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={1,7,8,9}:
            console.print(printpercent(60, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={1,7,8,10}:
            console.print(printpercent(70, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={1,7,9,10}:
            console.print(printpercent(65, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={1,8,9,10}:
            console.print(printpercent(75, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={7,8,9,10}:
            console.print(printpercent(65, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={1,7,8,9,10}:
            console.print(printpercent(80, "سل ریوی"))
            disease="سل ریوی"
        
        # سرفه خشک و خلط موکوئیدی و خلط چرکی اغشته به خون
        elif cough=={1,2,3} and associated_symptoms=={1}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={7}:
            console.print(printpercent(25, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={8}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={9}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={1,7}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={1,8}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={1,9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={1,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={7,8}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={7,9}:
            console.print(printpercent(25, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={7,10}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={8,9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={8,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={9,10}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={1,7,8}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={1,7,9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={1,7,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={1,8,9}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={1,8,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={1,9,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={7,8,9}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={7,8,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={7,9,10}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={8,9,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={1,7,8,9}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={1,7,8,10}:
            console.print(printpercent(60, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={1,7,9,10}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={1,8,9,10}:
            console.print(printpercent(65, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={7,8,9,10}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={1,7,8,9,10}:
            console.print(printpercent(70, "سل ریوی"))
            disease="سل ریوی"

        #سرفه خشک و خلط موکوئیدی و خلط چرکی کاملاًخونی
        elif cough=={1,2,5} and associated_symptoms=={1}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={7}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={8}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={1,7}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={1,8}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={1,9}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={1,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={7,8}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={7,9}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={7,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={8,9}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={8,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={9,10}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={1,7,8}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={1,7,9}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={1,7,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={1,8,9}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={1,8,10}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={1,9,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={7,8,9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={7,8,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={7,9,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={8,9,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={1,7,8,9}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={1,7,8,10}:
            console.print(printpercent(65, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={1,7,9,10}:
            console.print(printpercent(60, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={1,8,9,10}:
            console.print(printpercent(70, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={7,8,9,10}:
            console.print(printpercent(60, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={1,7,8,9,10}:
            console.print(printpercent(75, "سل ریوی"))
            disease="سل ریوی"
        
        #خلط موکوئیدی و خلط چرکی اغشته به خون و خلط چرکی کاملاًخونی
        elif cough=={2,3,5} and associated_symptoms=={1}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={7}:
            console.print(printpercent(25, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={8}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={9}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={1,7}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={1,8}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={1,9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={1,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={7,8}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={7,9}:
            console.print(printpercent(25, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={7,10}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={8,9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={8,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={9,10}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={1,7,8}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={1,7,9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={1,7,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={1,8,9}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={1,8,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={1,9,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={7,8,9}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={7,8,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={7,9,10}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={8,9,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={1,7,8,9}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={1,7,8,10}:
            console.print(printpercent(60, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={1,7,9,10}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={1,8,9,10}:
            console.print(printpercent(65, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={7,8,9,10}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={1,7,8,9,10}:
            console.print(printpercent(70, "سل ریوی"))
            disease="سل ریوی"

            #سرفه خشک وخلط موکوئیدی و خلط چرکی اغشته به خون و خلط چرکی کاملاًخونی
        elif cough=={1,2,3,5} and associated_symptoms=={1}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={7}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={8}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={1,7}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={1,8}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={1,9}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={1,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={7,8}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={7,9}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={7,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={8,9}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={8,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={9,10}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={1,7,8}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={1,7,9}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={1,7,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={1,8,9}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={1,8,10}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={1,9,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={7,8,9}:
            console.print(printpercent(35, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={7,8,10}:
            console.print(printpercent(45, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={7,9,10}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={8,9,10}:
            console.print(printpercent(50, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={1,7,8,9}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={1,7,8,10}:
            console.print(printpercent(65, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={1,7,9,10}:
            console.print(printpercent(60, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={1,8,9,10}:
            console.print(printpercent(70, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={7,8,9,10}:
            console.print(printpercent(60, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={1,7,8,9,10}:
            console.print(printpercent(75, "سل ریوی"))
            disease="سل ریوی"
        
        # بدون علائم همراه
        elif cough=={1} and associated_symptoms=={16}:
            console.print(printpercent(30, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2} and associated_symptoms=={16}:
            console.print(printpercent(25, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3} and associated_symptoms=={16}:
            console.print(printpercent(80, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={5} and associated_symptoms=={16}:
            console.print(printpercent(65, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2} and associated_symptoms=={16}:
            console.print(printpercent(40, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,3} and associated_symptoms=={16}:
            console.print(printpercent(70, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,5} and associated_symptoms=={16}:
            console.print(printpercent(55, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3} and associated_symptoms=={16}:
            console.print(printpercent(75, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,5} and associated_symptoms=={16}:
            console.print(printpercent(60, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={3,5} and associated_symptoms=={16}:
            console.print(printpercent(72, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3} and associated_symptoms=={16}:
            console.print(printpercent(80, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,5} and associated_symptoms=={16}:
            console.print(printpercent(65, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={2,3,5} and associated_symptoms=={16}:
            console.print(printpercent(75, "سل ریوی"))
            disease="سل ریوی"
        elif cough=={1,2,3,5} and associated_symptoms=={16}:
            console.print(printpercent(80, "سل ریوی"))
            disease="سل ریوی"
       
            
        
        #آبسه ریه
        #خلط چرکی آغشته به خون خون
        if cough=={3} and associated_symptoms=={1}:
            console.print(printpercent(35, "آبسه ریه"))
            disease="آبسه ریه"
        elif cough=={3} and associated_symptoms=={12}:
            console.print(printpercent(40, "آبسه ریه"))
            disease="آبسه ریه"
        elif cough=={3} and associated_symptoms=={1,12}:
            console.print(printpercent(45, "آبسه ریه"))
            disease="آبسه ریه"
        
        #خلط چرکی بدون خون
        elif cough=={4} and associated_symptoms=={1}:
            console.print(printpercent(30, "آبسه ریه"))
            disease="آبسه ریه"
        elif cough=={4} and associated_symptoms=={12}:
            console.print(printpercent(35, "آبسه ریه"))
            disease="آبسه ریه"
        elif cough=={4} and associated_symptoms=={1,12}:
            console.print(printpercent(40, "آبسه ریه"))
            disease="آبسه ریه"
        
        #خلط چرکی کاملا خونی
        elif cough=={5} and associated_symptoms=={1}:
            console.print(printpercent(40, "آبسه ریه"))
            disease="آبسه ریه"
        elif cough=={5} and associated_symptoms=={12}:
            console.print(printpercent(45, "آبسه ریه"))
            disease="آبسه ریه"
        elif cough=={5} and associated_symptoms=={1,12}:
            console.print(printpercent(50, "آبسه ریه"))
            disease="آبسه ریه"
        
        #خلط چرکی بدون خون و خلط چرکی آغشته به خون
        elif cough=={3,4} and associated_symptoms=={1}:
            console.print(printpercent(35, "آبسه ریه"))
            disease="آبسه ریه"
        elif cough=={3,4} and associated_symptoms=={12}:
            console.print(printpercent(40, "آبسه ریه"))
            disease="آبسه ریه"
        elif cough=={3,4} and associated_symptoms=={1,12}:
            console.print(printpercent(45, "آبسه ریه"))
            disease="آبسه ریه"
        
        #خلط چرکی بدون خون و خلط چرکی آغشته به خون
        elif cough=={3,5} and associated_symptoms=={1}:
            console.print(printpercent(40, "آبسه ریه"))
            disease="آبسه ریه"
        elif cough=={3,5} and associated_symptoms=={12}:
            console.print(printpercent(45, "آبسه ریه"))
            disease="آبسه ریه"
        elif cough=={3,5} and associated_symptoms=={1,12}:
            console.print(printpercent(50, "آبسه ریه"))
            disease="آبسه ریه"
        
        #خلط  خلط چرکی بدون خون و خلط چرکی کاملا خونی
        elif cough=={3,5} and associated_symptoms=={1}:
            console.print(printpercent(35, "آبسه ریه"))
            disease="آبسه ریه"
        elif cough=={3,5} and associated_symptoms=={12}:
            console.print(printpercent(40, "آبسه ریه"))
            disease="آبسه ریه"
        elif cough=={3,5} and associated_symptoms=={1,12}:
            console.print(printpercent(45, "آبسه ریه"))
            disease="آبسه ریه"
        
        #خلط چرکی آغشته به خون و خلط چرکی کاملا خونی
        elif cough=={4,5} and associated_symptoms=={1}:
            console.print(printpercent(45, "آبسه ریه"))
            disease="آبسه ریه"
        elif cough=={4,5} and associated_symptoms=={12}:
            console.print(printpercent(50, "آبسه ریه"))
            disease="آبسه ریه"
        elif cough=={4,5} and associated_symptoms=={1,12}:
            console.print(printpercent(55, "آبسه ریه"))
            disease="آبسه ریه"
        
        #خلط چرکی بدون خون و خلط چرکی آغشته به خون و خلط چرکی کاملا خونی
        elif cough=={4,5} and associated_symptoms=={1}:
            console.print(printpercent(45, "آبسه ریه"))
            disease="آبسه ریه"
        elif cough=={4,5} and associated_symptoms=={12}:
            console.print(printpercent(50, "آبسه ریه"))
            disease="آبسه ریه"
        elif cough=={4,5} and associated_symptoms=={1,12}:
            console.print(printpercent(55, "آبسه ریه"))
            disease="آبسه ریه"
        
        #بدون علائم همراه
        elif cough=={3} and associated_symptoms=={16}:
            console.print(printpercent(65, "آبسه ریه"))
            disease="آبسه ریه"
        elif cough=={5} and associated_symptoms=={16}:
            console.print(printpercent(75, "آبسه ریه"))
            disease="آبسه ریه"
        elif cough=={4,5} and associated_symptoms=={16}:
            console.print(printpercent(70, "آبسه ریه"))
            disease="آبسه ریه"
        
        
        
    #اسم
    #خلط موکوئیدی
        if cough=={2} and associated_symptoms=={3}:
            console.print(printpercent(60, "آسم"))
            disease="آسم"
        elif cough=={2} and associated_symptoms=={13}:
            console.print(printpercent(45, "آسم"))
            disease="آسم"
        elif cough=={2} and associated_symptoms=={15}:
            console.print(printpercent(55, "آسم"))
            disease="آسم"
        elif cough=={2} and associated_symptoms=={3}:
            console.print(printpercent(30, "آسم"))
            disease="آسم"
        elif cough=={2} and associated_symptoms=={3,13}:
            console.print(printpercent(70, "آسم"))
            disease="آسم"
        elif cough=={2} and associated_symptoms=={3,15}:
            console.print(printpercent(75, "آسم"))
            disease="آسم"
        elif cough=={2} and associated_symptoms=={13,15}:
            console.print(printpercent(60, "آسم"))
            disease="آسم"
        elif cough=={2} and associated_symptoms=={1,13,15}:
            console.print(printpercent(80, "آسم"))
            disease="آسم"
        elif cough=={2} and associated_symptoms=={16}:
            console.print(printpercent(15, "آسم"))
            disease="آسم"
            
       
    #رفلاکس معده
    #سرفه مزمن در شب خصوصا
        if cough=={6} and associated_symptoms=={14}:
            console.print(printpercent(50, "رفلاکس معده"))
            disease="رفلاکس معده"
        elif cough=={6} and associated_symptoms=={15}:
            console.print(printpercent(40, "رفلاکس معده"))
            disease="رفلاکس معده"
        elif cough=={6} and associated_symptoms=={14,15}:
            console.print(printpercent(60, "رفلاکس معده"))
            disease="رفلاکس معده"
        elif cough=={6} and associated_symptoms=={16}:
            console.print(printpercent(30, "رفلاکس معده"))
            disease="رفلاکس معده"
       
        
    #ذرات شیمیایی
    #سرفه متغیر در زمان و مکان خاص
        if cough=={7} and associated_symptoms=={11}:
           console.print(printpercent(60, "تماس با ذرات شیمیایی"))
           disease="تماس با ذرات شیمیایی"
        elif cough=={7} and associated_symptoms=={16}:
           console.print(printpercent(30, "تماس با ذرات شیمیایی"))
           disease="تماس با ذرات شیمیایی"
           
           
        #درمان ها
        if disease == "عفونت ریه ویروسی":
            Treatment="درمان پیشنهادی ما برای عفونت ریه ویروسی انتی ویروس ها است.اما درصد احتمال ذکر شده تقریبی است حتما برای دریافت دوز دقیق دارو و نوع انتی ویروس به پزشک مراجه کنید"
            print(Treatment)
        elif disease=="عفونت ریه باکتریایی":
            Treatment="درمان پیشنهادی ما برای عفونت ریه باکتریایی انتی بیوتیک‌ها است.اما درصد احتمال ذکر شده تقریبی است حتما برای دریافت دوز دقیق دارو و نوع انتی بیوتیک به پزشک مراجه کنید"
            print(Treatment)
        elif disease=="سینوزیت ویروسی یا باکتریایی و یا آلرژی":
            Treatment="درمان پیشنهادی ما برای سینوزیت، اگر ویروسی باشد ضد التهاب مثل استامینوفن و اگر عامل باکتریایی باشد نیاز به انتی بیوتیک ها دارید و اگر الرژیک باشد نیاز به آنتی هیستامین است.درصد احتمال ذکر شده تقریبی است حتما برای دریافت دوز دقیق دارو و نوع انتی بیوتیک یا دارو صد التهاب به پزشک مراجه کنید"
            print(Treatment)
        elif disease=="سل ریوی":
            Treatment="راهکار ما برای آبسه ریه مراجه به پزشک است،مصرف انتی بیوتیک ها و باید برسی شود و درصورت وخیم بودن جراحی شود.درصد احتمال ذکر شده تقریبی است حتما برای معاینه پزشک مراجه کنید"
            print(Treatment)
        elif disease=="آبسه ریه":
            Treatment="راهکار مراجه به پزشک است،مصرف انتی بیوتیک ها و باید برسی شود و درصورت وخیم بودن جراحی شود.درصد احتمال ذکر شده تقریبی است حتما برای معاینه پزشک مراجه کنید"
            print(Treatment)
        elif disease=="آسم":
            Treatment="راهکار درمانی ما برای آسم این است که اول از 'اسپری سالبوتامول' استفاده شود و اگر خوب نشد در مرحله بعد از اسپری کورتون 'فلودروکورتیزون' استفاده شود.از اسپری 'سالمترول'به عنوان گشاد کننده راه هوایی هم میتوان استفاده کرد\n.درصد احتمال ذکر شده تقریبی است حتما برای معاینه پزشک مراجه کنید"
            print(Treatment)
        elif disease=="رفلاکس معده":
            Treatment="راهکار درمانی ما برای رفلاکس معده استفاده از شربت معده ها مانند شربت آلومینیوم-ام جی اس است.استفاده از اوموپرازول و اگر خیلی شدید باشد استفاده از پنتاپرازول تزریقی توصیه می شود\n .درصد احتمال ذکر شده تقریبی است حتما برای معاینه پزشک مراجه کنید"
            print(Treatment)
        elif disease=="تماس با ذرات شیمیایی":
            Treatment="راهکار پیشنهادی ما برای سرفه به دلیل ذات شیمیایی استراحت کردن است و اینکه دیگر فرد با آلاینده در تماس نباشد.درصد احتمال ذکر شده تقریبی است حتما برای معاینه پزشک مراجه کنید"
            print(Treatment)


    #######################################################    
    elif A == 4:
        print("شما کمر درد دارید.")
        print("اکنون نیاز است تا بفهمم دچار چه علائم همراهی هستید. از بین عوامل زیر انتخاب کنید.")
        print("1.تندرنس عضلات پشت قفسه سینه\n2.تندرنس ستون فقرات\n3.درد به هنگام راه رفتن\n4.درد تیرکشنده زانو به سمت ساق پا\n5.بی حسی و ضعف\n6.تندرنس عضلات مجاور عصب سیاتیک\n7.تشدید درد در با عطسه، سرفه و زور زدن حین دفع\n8.ضعف و رفلکشن بیش ازحد ناحیه تحتانی حین خم شدن به جلو\n9.درد ساق پا پس از 30 ثانیه بک اکستنشن\n10.کاهش دامنه حرکت ستون فقرات\n11.درد در کل ستون فقرات\n12.درد مبهم و عمقی\n13.تندرنس موضعی مهره‌ها\n14.حرکات دردناک ستون فقرات")
        print()
        print("توجه: تندرنس به معنای حساس بودن ناحیه آسیب دیده می باشد")
        print()
        associated_symptoms = input("کدام یک از علائم همراه را دارید؟ می توانید چند مورد را هم انتخاب کنید فقط کافی است بین اعداد  ,  قرار دهید.")
        associated_symptoms = set(map(int,associated_symptoms.split(",")))
        #درد مکانیکی کمر
        if associated_symptoms == {1}:
            console.print(printpercent(11.8, "درد مکانیکی کمر"))
            disease="درد مکانیکی کمر"
        elif associated_symptoms == {2}:
            console.print(printpercent(17.6, "درد مکانیکی کمر"))
            disease="درد مکانیکی کمر"
        elif associated_symptoms == {3}:
            console.print(printpercent(23.5, "درد مکانیکی کمر"))
            disease="درد مکانیکی کمر"
        elif associated_symptoms == {1, 2}:
            console.print(printpercent(29.4, "درد مکانیکی کمر"))
            disease="درد مکانیکی کمر"
        elif associated_symptoms == {1, 3}:
            console.print(printpercent(35.3, "درد مکانیکی کمر"))
            disease="درد مکانیکی کمر"
        elif associated_symptoms == {2, 3}:
            console.print(printpercent(41.2, "درد مکانیکی کمر"))
            disease="درد مکانیکی کمر"
        elif associated_symptoms == {1, 2, 3}:
            console.print(printpercent(35.3, "درد مکانیکی کمر"))
            disease="درد مکانیکی کمر"
         
            
        #سیاتیک
        if associated_symptoms == {4}:
            console.print(printpercent(14.3, "درد سیاتیک"))
            disease="سیاتیک"
        elif associated_symptoms == {5}:
            console.print(printpercent(21.4, "درد سیاتیک"))
            disease="سیاتیک"
        elif associated_symptoms == {6}:
            console.print(printpercent(28.6, "درد سیاتیک"))
            disease="سیاتیک"
        elif associated_symptoms == {7}:
            console.print(printpercent(35.7, "درد سیاتیک"))
            disease="سیاتیک"
        elif associated_symptoms == {4, 5}:
            console.print(printpercent(35.7, "درد سیاتیک"))
            disease="سیاتیک"
        elif associated_symptoms == {4, 6}:
            console.print(printpercent(42.9, "درد سیاتیک"))
            disease="سیاتیک"
        elif associated_symptoms == {4, 7}:
            console.print(printpercent(50, "درد سیاتیک"))
            disease="سیاتیک"
        elif associated_symptoms == {5, 6}:
            console.print(printpercent(50, "درد سیاتیک"))
            disease="سیاتیک"
        elif associated_symptoms == {5, 7}:
            console.print(printpercent(57.1, "درد سیاتیک"))
            disease="سیاتیک"
        elif associated_symptoms == {6, 7}:
            console.print(printpercent(64.3, "درد سیاتیک"))
            disease="سیاتیک"
        elif associated_symptoms == {4, 5, 6}:
            console.print(printpercent(64.3, "درد سیاتیک"))
            disease="سیاتیک"
        elif associated_symptoms == {4, 5, 7}:
            console.print(printpercent(71.4, "درد سیاتیک"))
            disease="سیاتیک"
        elif associated_symptoms == {4, 6, 7}:
            console.print(printpercent(78.6, "درد سیاتیک"))
            disease="سیاتیک"
        elif associated_symptoms == {5, 6, 7}:
            console.print(printpercent(85.7, "درد سیاتیک"))
            disease="سیاتیک"
       
        
        
      #تنگی کانال نخاعی کمر
        if associated_symptoms == {8}:
            console.print(printpercent(21.4, "تنگی کانال نخاعی کمر"))
            disease="تنگی کانال نخاعی"
        elif associated_symptoms == {9}:
            console.print(printpercent(28.6, "تنگی کانال نخاعی کمر"))
            disease="تنگی کانال نخاعی"
        elif associated_symptoms == {8, 9}:
            console.print(printpercent(50, "تنگی کانال نخاعی کمر"))
            disease="تنگی کانال نخاعی"
        
        
      #رماتولوژیک
        if associated_symptoms == {10}:
            console.print(printpercent(23.3, "درد مزمن به علت بیماری‌های رماتولوژیک"))
            disease="رماتولوژِیک"
        elif associated_symptoms == {11}:
            console.print(printpercent(26.7, "درد مزمن به علت بیماری‌های رماتولوژیک"))
            disease="رماتولوژِیک"
        elif associated_symptoms == {10, 11}:
            console.print(printpercent(50, "درد مزمن به علت بیماری‌های رماتولوژیک"))
            disease="رماتولوژِیک"
        
        
       #درد ارجاعی از کمر
        if associated_symptoms == {12}:
            console.print(printpercent(6.7, "درد ارجاعی از شکم و کمر"))
            disease="درد ارجاعی از شکم و کمر"
        elif associated_symptoms == {13}:
            console.print(printpercent(10, "درد ارجاعی از شکم و کمر"))
            disease="درد ارجاعی از شکم و کمر"
        elif associated_symptoms == {14}:
            console.print(printpercent(8, "درد ارجاعی از شکم و کمر"))
            disease="درد ارجاعی از شکم و کمر"
        elif associated_symptoms == {12, 13}:
            console.print(printpercent(16.7, "درد ارجاعی از شکم و کمر"))
            disease="درد ارجاعی از شکم و کمر"
        elif associated_symptoms == {12, 14}:
            console.print(printpercent(15, "درد ارجاعی از شکم و کمر"))
            disease="درد ارجاعی از شکم و کمر"
        elif associated_symptoms == {13, 14}:
            console.print(printpercent(18.3, "درد ارجاعی از شکم و کمر"))
            disease="درد ارجاعی از شکم و کمر"
        elif associated_symptoms == {12, 13, 14}:
            console.print(printpercent(25, "درد ارجاعی از شکم و کمر"))
            disease="درد ارجاعی از شکم و کمر"
        
     
        #درمان ها
        if disease=="درد مکانیکی کمر":
            Treatment="برای درد مکانیکی کمر پیشنهاد می‌شود تا استراحت کنید و درصورت افزایش درد، مسکن مصرف کنید. برای دریافت تشخیص و درمان دقیق به پزشک مراجعه کنید."
            print(Treatment) 
        elif disease=="سیاتیک":
            Treatment="برای سیاتیک پیشنهاد می‌شود تا استراحت کنید و مسکن مصرف کنید. درصورت افزایش درد، برای تشخیص و درمان دقیق شامل دریافت کورتون و بررسی نیاز به جراحی به پزشک مراجعه کنید."
            print(Treatment)
        elif disease=="تنگی کانال نخاعی":
            Treatment="برای تنگی کانال نخاعی پیشنهاد می‌شود تا استراحت کنید و از بلند کردن اجسام سنگین کنید. درصورت افزایش درد، برای تشخیص و درمان دقیق شامل دریافت کورتون و بررسی نیاز به جراحی به پزشک مراجعه کنید."
            print(Treatment)
        elif disease=="رماتولوژِیک":
            Treatment="برای رماتولوژیک پیشنهاد می‌شود تا استراحت کنید و درصورت افزایش درد، برای تشخیص و درمان دقیق شامل دریافت کورتون و بررسی نیاز به جراحی به پزشک مراجعه کنید."
            print(Treatment)
        elif disease=="درد ارجاعی از شکم و کمر":
            Treatment="برای درد ارجاعی از شکم و کمر پیشنهاد می‌شود تا برای درمان علل زمینه‌ای به پزشک مراجعه کنید."
            print(Treatment)
        

    #######################################################    
    elif A == 5:
        print("شما تنگی نفس دارید.")
        # تشخیص علائم همراه
        print("از بین علائم زیر انتخاب کنید.") 
        print("(اگر انتخاب هایتان بیش از یک مورداست، بین اعداد کاما(,) بگذارید.\nمثال: 1,10,11)")
        print("1- سرفه\n2- تنگی نفس شبانه\n3- ویز(صدای خروج هوای مضاعف از ریه)\n4- خس خس\n5- گرفتگی در سینه\n6- خلط موکوئیدی(ژلاتینی)\n7- تب\n8- تپش قلب\n9- سرگیجه\n10- بی حسی و سوزن سوزن شدن دست و پا\n11- بدون علائم همراه")
        print()
        Associated_symptoms= input("کدام علائم را دارید؟ ")
        Associated_symptoms=set(map(int,Associated_symptoms.split(",")))
                
        # while True :         #تنگی نفس دارد/ حلقه برای وارد کردن درست علائم همراه
        #     Associated_symptoms= input("کدام علائم را دارید؟ ")
        #     try:
        #                 Associated_symptoms=set(map(int,Associated_symptoms.split(",")))
        #                 break     #توقف حلقه دوم/ اگر داده های علائم همراه را درست وارد کرد متوقف شو
        #     except ValueError :
        #                 print()
        #                 print("لطفا در مواقع وارد کردن داده موارد زیر را رعایت کرده و دوباره داده را وارد کنید:\n1- کیبورد خود را انگلیسی کنید.\n2- در بین اعداد حتما کاما (,) قرار دهید.\n3- از دکمه‌ی space استفاده نکنید.\nمثال: 11,10,1")
                        
                        # تشخیص شرایط زمینه ای بیمار
                        
        print("علائم همراه شما ثبت شد.")
        print()
        print (" اکنون نیاز است تا ببینیم چه شرایط زمینه ای در بیماری شما تاثیر داشته است. ")
        print()
        print("از بین شرایط زیر انتخاب کنید.") 
        print("(اگر انتخاب هایتان بیش از یک مورداست، بین اعداد کاما(,) بگذارید.\nمثال: 1,7,6)")
        print("1- سابقه بیماری قلبی\n2- شرایط محیطی\n3- سابقه مصرف سیگار\n4- آلاینده\n5- متغیر\n6- درد قفسه سینه\n7- بدون شرایط زمینه ای")
        print()
        Predisposing_factors=input("کدام شرایط زمینه ای را دارید؟ ")
        Predisposing_factors=set(map(int,Predisposing_factors.split(",")))
            # while True :         #حلقه برای درست وارد کردن شرایط زمینه ای
                    # Predisposing_factors=input("کدام شرایط زمینه ای را دارید؟ ")
            #         try:
                        # Predisposing_factors=set(map(int,Predisposing_factors.split(",")))
            #             break
            #         except ValueError :
            #             print()
            #             print("لطفا در مواقع وارد کردن داده موارد زیر را رعایت کرده و دوباره داده را وارد کنید:\n1- کیبورد خود را انگلیسی کنید.\n2- در بین اعداد حتما کاما (,) قرار دهید.\n3- از دکمه‌ی space استفاده نکنید.\nمثال: 6,7,1")
                 
                    
                 # بیماری 1 : نارسایی قلبی
                 
              # سابقه : بیماری قلبی
        if Predisposing_factors=={1} and Associated_symptoms=={1}:
            console.print(printpercent(60, "نارسایی قلبی"))
            disease="نارسایی قلبی"
        elif Predisposing_factors=={1} and Associated_symptoms=={2}:                     
            console.print(printpercent(70, "نارسایی قلبی"))
            disease="نارسایی قلبی"
        elif Predisposing_factors=={1} and Associated_symptoms=={3}:
            console.print(printpercent(50, "نارسایی قلبی"))
            disease="نارسایی قلبی"
        elif Predisposing_factors=={1} and Associated_symptoms=={1,2}:
            console.print(printpercent(80, "نارسایی قلبی"))   
            disease="نارسایی قلبی"
        elif Predisposing_factors=={1} and Associated_symptoms=={1,3}:
            console.print(printpercent(65, "نارسایی قلبی"))   
            disease="نارسایی قلبی"
        elif Predisposing_factors=={1} and Associated_symptoms=={2,3}:
            console.print(printpercent(75, "نارسایی قلبی"))  
            disease="نارسایی قلبی"
        elif Predisposing_factors=={1} and Associated_symptoms=={1,2,3}:
            console.print(printpercent(85, "نارسایی قلبی"))  
            disease="نارسایی قلبی"
        elif Predisposing_factors=={1} and Associated_symptoms=={11}:
            console.print(printpercent(10, "نارسایی قلبی"))  
            disease="نارسایی قلبی"
                
    # بیماری 1 : نارسایی قلبی

    # سابقه : بدون شرایط

        elif Predisposing_factors=={7} and Associated_symptoms=={1}:
            console.print(printpercent(20, "نارسایی قلبی"))
            disease="نارسایی قلبی"
        elif Predisposing_factors=={7} and Associated_symptoms=={2}:                     
            console.print(printpercent(25, "نارسایی قلبی"))
            disease="نارسایی قلبی"
        elif Predisposing_factors=={7} and Associated_symptoms=={3}:
            console.print(printpercent(15, "نارسایی قلبی"))
            disease="نارسایی قلبی"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,2}:
            console.print(printpercent(30, "نارسایی قلبی"))  
            disease="نارسایی قلبی"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,3}:
            console.print(printpercent(20, "نارسایی قلبی"))  
            disease="نارسایی قلبی"
        elif Predisposing_factors=={7} and Associated_symptoms=={2,3}:
            console.print(printpercent(25, "نارسایی قلبی"))  
            disease="نارسایی قلبی"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,2,3}:
            console.print(printpercent(30, "نارسایی قلبی")) 
            disease="نارسایی قلبی"
        elif Predisposing_factors=={7} and Associated_symptoms=={11}:
            console.print(printpercent(5, "نارسایی قلبی"))
            disease="نارسایی قلبی"
            
        
                                     
    # بیماری 2 : آسم

    # سابقه : شرایط محیطس
                        

        if Predisposing_factors=={1} and Associated_symptoms=={1}:
            console.print(printpercent(60, "آسم"))
            disease="آسم"
        elif Predisposing_factors=={1} and Associated_symptoms=={4}:                     
            console.print(printpercent(75, "آسم"))
            disease="آسم"
        elif Predisposing_factors=={1} and Associated_symptoms=={5}:
            console.print(printpercent(70, "آسم"))
            disease="آسم"
        elif Predisposing_factors=={1} and Associated_symptoms=={1,4}:
            console.print(printpercent(85, "آسم"))   
            disease="آسم"
        elif Predisposing_factors=={1} and Associated_symptoms=={1,5}:
            console.print(printpercent(80, "آسم"))    
            disease="آسم"
        elif Predisposing_factors=={1} and Associated_symptoms=={4,5}:
            console.print(printpercent(58, "آسم"))     
            disease="آسم"
        elif Predisposing_factors=={1} and Associated_symptoms=={1,4,5}:
            console.print(printpercent(90, "آسم"))    
            disease="آسم"
        elif Predisposing_factors=={1} and Associated_symptoms=={11}:
            console.print(printpercent(30, "آسم"))   
            disease="آسم"
            
            
    # بیماری 2 : آسم

    # سابقه : بدون شرایط
                        

        elif Predisposing_factors=={7} and Associated_symptoms=={1}:
            console.print(printpercent(40, "آسم"))
            disease="آسم"
        elif Predisposing_factors=={7} and Associated_symptoms=={4}:                     
            console.print(printpercent(55, "آسم"))
            disease="آسم"
        elif Predisposing_factors=={7} and Associated_symptoms=={5}:
            console.print(printpercent(50, "آسم"))
            disease="آسم"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,4}:
            console.print(printpercent(65, "آسم")) 
            disease="آسم"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,5}:
            console.print(printpercent(60, "آسم")) 
            disease="آسم"
        elif Predisposing_factors=={7} and Associated_symptoms=={4,5}:
            console.print(printpercent(65, "آسم")) 
            disease="آسم"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,4,5}:
            console.print(printpercent(70, "آسم"))
            disease="آسم"
        elif Predisposing_factors=={7} and Associated_symptoms=={11}:
            console.print(printpercent(10, "آسم"))
            disease="آسم"
            
       
         
                    
    # بیماری 3 : COPD

    # سابقه : مصرف سیگار
                        

        if Predisposing_factors=={3} and Associated_symptoms=={1}:
            console.print(printpercent(70, "COPD"))
            disease="COPD"
        elif Predisposing_factors=={3} and Associated_symptoms=={6}:                     
            console.print(printpercent(75, "COPD"))
            disease="COPD"
        elif Predisposing_factors=={3} and Associated_symptoms=={1,6}:
            console.print(printpercent(80, "COPD"))
            disease="COPD"
        elif Predisposing_factors=={3} and Associated_symptoms=={11}:
            console.print(printpercent(30, "COPD"))
            disease="COPD"
                    
             
            
     # بیماری 3 : COPD

     # سابقه : آلاینده
                         

        elif Predisposing_factors=={4} and Associated_symptoms=={1}:
            console.print(printpercent(65, "COPD"))
            disease="COPD"
        elif Predisposing_factors=={4} and Associated_symptoms=={6}:                     
            console.print(printpercent(70, "COPD"))
            disease="COPD"
        elif Predisposing_factors=={4} and Associated_symptoms=={1,6}:
            console.print(printpercent(75, "COPD"))
            disease="COPD"
        elif Predisposing_factors=={4} and Associated_symptoms=={11}:
            console.print(printpercent(25, "COPD")) 
            disease="COPD"          
            
            
     # بیماری 3 : COPD

     # سابقه : بدون شرایط
                         

        elif Predisposing_factors=={7} and Associated_symptoms=={1}:
            console.print(printpercent(60, "COPD"))
            disease="COPD"
        elif Predisposing_factors=={7} and Associated_symptoms=={6}:                     
            console.print(printpercent(65, "COPD"))
            disease="COPD"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,6}:
            console.print(printpercent(70, "COPD"))
            disease="COPD"
        elif Predisposing_factors=={7} and Associated_symptoms=={11}:
            console.print(printpercent(20, "COPD"))
            disease="COPD"
                
            
     # بیماری 3 : COPD

     # سابقه : مصرف سیگار و آلاینده
                         

        elif Predisposing_factors=={3,4} and Associated_symptoms=={1}:
            console.print(printpercent(75, "COPD"))
            disease="COPD"
        elif Predisposing_factors=={3,4} and Associated_symptoms=={6}:                     
            console.print(printpercent(80, "COPD"))
            disease="COPD"
        elif Predisposing_factors=={3,4} and Associated_symptoms=={1,6}:
            console.print(printpercent(85, "COPD"))
            disease="COPD"
        elif Predisposing_factors=={3,4} and Associated_symptoms=={11}:
            console.print(printpercent(35, "COPD"))
            disease="COPD"
       
           
    # بیماری 4 : عفونت ریه(پنومونی)

    #سابقه : شرایط متغیر
                        

        if Predisposing_factors=={5} and Associated_symptoms=={1}:
            console.print(printpercent(70, "عفونت ریه"))
            disease="عفونت ریه"
        elif Predisposing_factors=={5} and Associated_symptoms=={6}:                     
            console.print(printpercent(75, "عفونت ریه"))
            disease="عفونت ریه"
        elif Predisposing_factors=={5} and Associated_symptoms=={7}:
            console.print(printpercent(70, "عفونت ریه"))
            disease="عفونت ریه"
        elif Predisposing_factors=={5} and Associated_symptoms=={1,6}:
            console.print(printpercent(80, "عفونت ریه"))   
            disease="عفونت ریه"
        elif Predisposing_factors=={5} and Associated_symptoms=={1,7}:
            console.print(printpercent(75, "عفونت ریه"))    
            disease="عفونت ریه"
        elif Predisposing_factors=={5} and Associated_symptoms=={6,7}:
            console.print(printpercent(75, "عفونت ریه"))  
            disease="عفونت ریه"
        elif Predisposing_factors=={5} and Associated_symptoms=={1,6,7}:
            console.print(printpercent(85, "عفونت ریه"))
            disease="عفونت ریه"
        elif Predisposing_factors=={5} and Associated_symptoms=={11}:
            console.print(printpercent(40, "عفونت ریه"))
            disease="عفونت ریه"
            
    # بیماری 4 : عفونت ریه(پنومونی)

    #سابقه : بدون شرایط
                        

        elif Predisposing_factors=={7} and Associated_symptoms=={1}:
            console.print(printpercent(60, "عفونت ریه"))
            disease="عفونت ریه"
        elif Predisposing_factors=={7} and Associated_symptoms=={6}:                     
            console.print(printpercent(65, "عفونت ریه"))
            disease="عفونت ریه"
        elif Predisposing_factors=={7} and Associated_symptoms=={7}:
            console.print(printpercent(60, "عفونت ریه"))
            disease="عفونت ریه"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,6}:
            console.print(printpercent(70, "عفونت ریه"))  
            disease="عفونت ریه"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,7}:
            console.print(printpercent(65, "عفونت ریه"))  
            disease="عفونت ریه"
        elif Predisposing_factors=={7} and Associated_symptoms=={6,7}:
            console.print(printpercent(65, "عفونت ریه"))  
            disease="عفونت ریه"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,6,7}:
            console.print(printpercent(75, "عفونت ریه"))   
            disease="عفونت ریه"
        elif Predisposing_factors=={7} and Associated_symptoms=={11}:
            console.print(printpercent(20, "عفونت ریه"))
            disease="عفونت ریه"
            
       
        
            
    # بیماری 5 : اضطراب همراه(هایپرونتیالسیون)

    # سابقه : درد قفسه سینه
                        

        if Predisposing_factors=={6} and Associated_symptoms=={8}:
            console.print(printpercent(75, "اضطراب همراه یا هایپرونتیالسیون"))
            disease="اضطراب همراه یا هایپرونتیالسیون"
        elif Predisposing_factors=={6} and Associated_symptoms=={9}:                     
            console.print(printpercent(80, "اضطراب همراه یا هایپرونتیالسیون"))
            disease="اضطراب همراه یا هایپرونتیالسیون"
        elif Predisposing_factors=={6} and Associated_symptoms=={10}:
            console.print(printpercent(75, "اضطراب همراه یا هایپرونتیالسیون"))
            disease="اضطراب همراه یا هایپرونتیالسیون"
        elif Predisposing_factors=={6} and Associated_symptoms=={8,9}:
            console.print(printpercent(85, "اضطراب همراه یا هایپرونتیالسیون"))     
            disease="اضطراب همراه یا هایپرونتیالسیون"
        elif Predisposing_factors=={6} and Associated_symptoms=={8,10}:
            console.print(printpercent(80, "اضطراب همراه یا هایپرونتیالسیون"))     
            disease="اضطراب همراه یا هایپرونتیالسیون"
        elif Predisposing_factors=={6} and Associated_symptoms=={9,10}:
            console.print(printpercent(85, "اضطراب همراه یا هایپرونتیالسیون"))      
            disease="اضطراب همراه یا هایپرونتیالسیون"
        elif Predisposing_factors=={6} and Associated_symptoms=={8,9,10}:
            console.print(printpercent(90, "اضطراب همراه یا هایپرونتیالسیون"))       
            disease="اضطراب همراه یا هایپرونتیالسیون"
        elif Predisposing_factors=={6} and Associated_symptoms=={11}:
            console.print(printpercent(50, "اضطراب همراه یا هایپرونتیالسیون"))
            disease="اضطراب همراه یا هایپرونتیالسیون"
            
    # بیماری 5 : اضطراب همراه(هایپرونتیلاسیون)

     # سابقه : بدون شرایط
                        

        elif Predisposing_factors=={7} and Associated_symptoms=={8}:
            console.print(printpercent(55, "اضطراب همراه یا هایپرونتیالسیون"))
            disease="اضطراب همراه یا هایپرونتیالسیون"
        elif Predisposing_factors=={7} and Associated_symptoms=={9}:                     
            console.print(printpercent(60, "اضطراب همراه یا هایپرونتیالسیون"))
            disease="اضطراب همراه یا هایپرونتیالسیون"
        elif Predisposing_factors=={7} and Associated_symptoms=={10}:
            console.print(printpercent(55, "اضطراب همراه یا هایپرونتیالسیون"))
            disease="اضطراب همراه یا هایپرونتیالسیون"
        elif Predisposing_factors=={7} and Associated_symptoms=={8,9}:
            console.print(printpercent(65, "اضطراب همراه یا هایپرونتیالسیون"))       
            disease="اضطراب همراه یا هایپرونتیالسیون"
        elif Predisposing_factors=={7} and Associated_symptoms=={8,10}:
            console.print(printpercent(60, "اضطراب همراه یا هایپرونتیالسیون"))     
            disease="اضطراب همراه یا هایپرونتیالسیون"
        elif Predisposing_factors=={7} and Associated_symptoms=={9,10}:
            console.print(printpercent(65, "اضطراب همراه یا هایپرونتیالسیون"))       
            disease="اضطراب همراه یا هایپرونتیالسیون"
        elif Predisposing_factors=={7} and Associated_symptoms=={8,9,10}:
            console.print(printpercent(70, "اضطراب همراه یا هایپرونتیالسیون"))    
            disease="اضطراب همراه یا هایپرونتیالسیون"
        elif Predisposing_factors=={7} and Associated_symptoms=={11}:
            console.print(printpercent(30, "اضطراب همراه یا هایپرونتیالسیون"))
            disease="اضطراب همراه یا هایپرونتیالسیون"
            
        
        
        #درمان بیماری ها
        if disease=="نارسایی قلبی":
            Treatment="درمان پیشنهادی برای نارسایی قلبی: \n1- می توانید از داروهای بتابلاکر مثل 'پروپنانولول' استفاده کنید.\n2- همپنین می توانید از داروهای ادرار‌آور استفاده کنید."
            print(Treatment)
        elif disease=="آسم":
            Treatment="درمان پیشنهادی: \n1- ابتدا از 'اسپری سالبوتامول' استفاده کنید.\n2- اگر بهبود حاصل نشد می توانید از 'اسپری فلودروکورتیزون' استفاده کنید.\n3- می توانید از 'اسپری سالمترول' هم به عنوان گشاد کننده‌ی راه‌های هوایی استفاده کنید."
            print(Treatment)
        elif disease=="COPD":
            Treatment=" درمان پیشنهادی برای COPD:\n1- اگر سیگاری هستید، سیگار را ترک کنید.\n2- می توانید از داروهای بازکننده‌ی راه‌های هوایی یا داروهای آسم مثل آتروونت استفاده کنید."
            print(Treatment)
        elif disease=="عفونت ریه":
            Treatment="درمان پیشنهادی برای عفونت ریه: \n1-اگرعفونت باکتریایی باشد، می توانید از 'آنتی بیوتیک ها' استفاده کنید.\n2- اگر عفونت ویروسی باشد، می توانید از 'آنتی ویروس ها' استفاده کنید."
            print(Treatment)
        elif disease=="اضطراب همراه یا هایپرونتیالسیون":
            Treatment="درمان پیشنهادی برای اضطراب همراه یا هایپرونتیلاسیون : \n1- به روان پزشک مراجعه کنید.\n2- استراحت کنید."
            print(Treatment)


    else:
        print("ابا عرض پوزش،اطلاعات این برنامه فعلا بیماری این علائم را پشتیبانی نمی کند.برنامه در حال کامل شدن است.")



    # دریافت فرم

    Question=int(input("آیا مایل به دریافت فرم هستید؟\n1- بله\n2- خیر\n"))
                 
    if Question==1:
        print()
        print(f"نام : {Name}")
        print(f"نام خانوادگی : {Family_name}")
        print(f"سن : {Age}")
        print(f"جنسیت : {Gender}")
        Title="شرح حال بیمار : "
        print(Title + disease)
        Title_2="توصیه درمانی : "
        print(Title_2 + Treatment )
    else:
        print()
        print("فرمی صادر نشد.")

    print("\nصرفا این برانامه برای تشخیص اولیه بیماری است،لطفا برای تشخیص دقیق و انجام آزمایشات تکمیلی به پزشک مراجعه کنید وبا مشورت پزشک دارو مصرف کنید.\nبا تشکر از شما\nگروه برنامه نویسی ساریس")
    #  پایان 403/10/17 ساعت 23:17


#########################################################################
elif language==2:
    #rich library
    import rich as ri
    from rich.console import Console
    #Create a blank space.
    console = Console()
    def printpercent(percent, disease):
    # Display entries in red
        return f"You have a [red]{percent}[/red] percent chance of having [red]{disease}[/red]!"

    # Patient details

    print("Please enter your details.")
    Name = input("Name: ")
    Family_name = input("Family_name: ")
    Age =int(input("Age: "))
    Gender = input("Gender: ")
    print()
    print(f"Hello {Name}! In this app, we want to make a preliminary diagnosis of your disease and suggest a solution for you.")
    print()# Patient details

    #Now we need to ask the user what the main symptom is?
    print("This app is currently working on 5 main symptoms of diseases:")
    Main_symptoms = ("Abdominal pain", "Chest pain", "Cough", "Back pain", "Shortness of breath")

    print("1=Abdominal pain\n2=Chest pain\n3=Cough\n4=Back pain\n5=Shortness of breath")
    A = int(input("Please tell me which of the following main symptoms do you have? "))

    if A == 1:
        print("You have a stomach ache.")
        areaOfThePain = int(input("Where do you feel the most pain?\n 1. Near the chest \n 2. Around the navel \n 3. Generalized abdominal pain\n"))
        if areaOfThePain == 1:
            backPainCheck = int(input("Do you also feel pain in your back? \n 1. Yes \n 2. No\n"))
            if backPainCheck == 1:
                otherAreaPainCheck = int(input("Do you also feel pain in other areas of your abdomen? \n 1. Yes \n 2. No\n"))
                if otherAreaPainCheck == 1:
                    console.print(printpercent(55, "Acute pancreatitis"))
                    disease="Asthma"
                    Treatment="For asthma, the recommended treatment is: Serum and painkillers.\nIt is also possible that you have not eaten anything, so your stomach is empty\nYou should definitely see a doctor, surgery may be needed "
                    print(Treatment)
                elif otherAreaPainCheck == 2:
                    console.print(printpercent(70, "gastric ulcer"))
                    console.print(printpercent(20, "chronic pancreatitis"))
                    disease="Gastric ulcer or chronic pancreatitis"
                    Treatment="Recommended treatment: For stomach ulcers, first take antacids such as pantoprazole or omeprazole and gastric syrup.\nBe sure to visit a gastroenterologist and have an endoscopy. Bleeding may occur.\nIf it is chronic pancreatitis, immediately visit a surgeon. Surgery may be required."
                    print(Treatment)
                else:
                    print("Unfortunately, there is not enough data to diagnose your condition. \n Please see a doctor")
            elif backPainCheck == 2:
                    console.print(printpercent(70, "Gastroesophageal reflux"))
                    disease="Gastroesophageal reflux"
                    Treatment="Antacids such as stomach syrup or omeprazole If very severe, injection of pantoprazole\nLie down and keep your head elevated."
                    print(Treatment)
            else:
                print("Unfortunately, there is a pre-prepared error. Please make sure the data format is correct")
        elif areaOfThePain == 2:
            appandixCheck = int(input("Do you also feel pain in the lower abdomen? \n 1. Yes \n 2. No\n"))
            if appandixCheck == 1:
                  console.print(printpercent(15, "Acute Appendicitis"))
                  disease="Acute Appendicitis"
                  Treatment="For acute appendicitis, antibiotics should be taken, but it must be under the supervision of a doctor and a visit to a surgeon may be necessary."
                  print(Treatment)
            elif appandixCheck==2:
                  print("Unfortunately, there is not enough data to diagnose your condition. \n Please see a doctor")
            else:
                  print("Unfortunately, there is a pre-prepared error. Please make sure the data format is correct")
        elif areaOfThePain == 3:
            crampyPainCheck = int(input("Is the pain crampy? \n 1. Yes \n 2. No\n"))
            if crampyPainCheck == 1:
                console.print(printpercent(60, "Acute intestinal obstruction"))
                disease="Acute intestinal obstruction"
                Treatment="Acute intestinal obstruction should be treated by a surgeon and over-the-counter painkillers should be avoided as much as possible"
                print(Treatment)
            elif crampyPainCheck==2:
                print("Unfortunately, there is not enough data available to diagnose your condition. \n Please see a doctor")
            else:
                print("Unfortunately, there is a pre-formatted error. Please make sure the data format you entered is correct")
        else:
            print("Unfortunately, there is a pre-formatted error. Please make sure the data format you entered is correct")

    elif A == 2:
        print("You have chest pain.")
        AreaOfThePain = int(input("Where do you feel the pain most? \n 1. Behind the sternum \n 2. Under the left breast \n 3. Along the costal cartilage \n"))
        print()

        if AreaOfThePain == 1:
            BackPainCheck = int(input("Does your pain radiate to your back? \n 1. Yes \n 2. No, the pain often radiates to your bladder, \n arms, neck, lower jaw, or upper abdomen. \n 3. Other options\n"))
            print()

            if BackPainCheck == 2:
                IntensityBladderPainCheck = int(input("How severe is your pain? \n 1. Mild \n 2. Moderate \n 3. Severe\n"))
                print()
                if IntensityBladderPainCheck == 1:
                    associated_symptoms = int(input("Symptoms Select your companion. \n 1. Shortness of breath \n 2. Nausea \n 3. Shortness of breath and nausea \n 4. Other options\n"))
                    if associated_symptoms == 1:
                        console.print(printpercent(25, "Angina Pectoris"))
                        disease="Angina Pectoris"
                        Treatment="Use nitroglycerin, but for more accurate results, \n it is recommended to see a doctor for angina pectoris."
                        print("Timing: \n Usually 1 to 3 minutes \n **Aggravating factors: \n Often activity, especially cold weather, eating, and emotional stress** \n **Relieving factors: \n Often rest and nitroglycerin**")
                        print(Treatment)
                    elif associated_symptoms == 2:
                        console.print(printpercent(20, "angina pectoris"))
                        disease="Angina pectoris"
                        Treatment="Use nitroglycerin, but for more accurate results, \n it is recommended to see a doctor for angina pectoris."
                        print("Timeframe: \n Usually 1 to 3 minutes \n **Aggravating factors: \n Often activity, especially cold weather, eating, and emotional stress** \n **Relieving factors: \n Often rest and nitroglycerin**")
                        print(Treatment)
                    elif associated_symptoms == 3:
                        console.print(printpercent(30, "angina pectoris"))
                        disease="Angina pectoris"
                        Treatment="Use nitroglycerin, but for more accurate results, \n it is recommended to see a doctor for angina pectoris."
                        print("Timing: \n Usually 1 to 3 minutes \n **Aggravating factors: \n Often activity, especially cold weather, eating, and emotional stress** \n **Relieving factors: \n Often rest and nitroglycerin**")
                        print(Treatment)
                    else:
                        print("Sorry, there is not enough information available to diagnose your problem. \n Please see your doctor.")
                elif IntensityBladderPainCheck == 2:
                    associated_symptoms = int(input("Select your associated symptoms. \n 1. Shortness of breath \n 2. Nausea \n 3. Shortness of breath and nausea \n 4. Other options\n"))
                    if associated_symptoms == 1:
                        console.print(printpercent(40-50, "Angina Pectoris"))
                        disease="Angina Pectoris"
                        Treatment="Use nitroglycerin, but for more accurate results, \n it is recommended to see a doctor for angina pectoris."
                        print("Timing: \n Usually 1 to 3 minutes \n **Aggravating factors: \n Often activity, especially cold weather, eating, and emotional stress** \n **Relieving factors: \n Often rest and nitroglycerin**")
                        print(Treatment)
                    elif associated_symptoms == 2:
                        console.print(printpercent(35-45, "angina pectoris"))
                        disease="Angina pectoris"
                        Treatment="Use nitroglycerin, but for more accurate results, \n it is recommended to see a doctor for angina pectoris."
                        print("Timeline: \n Usually 1 to 3 minutes \n **Aggravating factors: \n Often activity, especially cold weather, eating, and emotional stress** \n **Relieving factors: \n Often rest and nitroglycerin**")
                        print(Treatment)
                    elif associated_symptoms == 3:
                        console.print(printpercent(50-60, "Angina Pectoris"))
                        disease="Angina Pectoris"
                        Treatment="Use nitroglycerin, but for more accurate results, \n it is recommended to see a doctor for angina."
                        print("Timing: \n Usually 1 to 3 minutes \n **Aggravating factors: \n Often activity, especially cold weather, eating, and emotional stress** \n **Reducing factors: \n Often rest and nitroglycerin**")
                        print(Treatment)
                    elif associated_symptoms == 4:
                        print("Sorry, there is not enough information to diagnose your condition. \n Please see your doctor.")
                        
                elif IntensityBladderPainCheck == 3:
                    associated_symptoms = int(input("Select your associated symptoms. \n 1. Shortness of breath \n 2. Nausea \n 3. Shortness of breath and nausea \n 4. Other options\n"))
                    if associated_symptoms == 1:
                            console.print(printpercent(70-80, "Heart attack"))
                            disease="Heart attack"
                            Treatment="Use nitroglycerin for heart attack\n and then very quickly Get an angiogram."
                            print("Timing: 20 minutes to a few hours \n **Activity does not always make this condition worse.** \n **This condition does not improve with rest.**")
                            print(Treatment)
                    elif associated_symptoms == 2:
                            console.print(printpercent(65-75, "Heart attack"))
                            disease="Heart attack"
                            Treatment="Take nitroglycerin \n and then get an angiogram very quickly."
                            print("Timing: 20 minutes to a few hours \n **Activity does not always make this condition worse.** \n **This condition does not improve with rest.**")
                            print(Treatment)
                    elif associated_symptoms == 3:
                            console.print(printpercent(80-90, "Heart attack"))
                            disease="Heart attack"
                            Treatment="Take nitroglycerin for a heart attack\n and then get an angiogram very quickly."
                            print("Time frame: 20 minutes to a few hours \n **Activity does not always make this condition worse.** \n **This condition does not improve with rest.**")
                            print(Treatment)
                    elif associated_symptoms == 4:
                            print("Sorry, there is not enough information available to diagnose your problem. \n Please see your doctor.")
            elif BackPainCheck == 1:
                QualityBackPainCheck = int(input("What is the quality of your pain? \n 1. Burning \n 2. Burning and pressing \n 3. Other options\n"))
                if QualityBackPainCheck == 1:
                    IntensityBackPainCheck = int(input("What is the intensity of your pain? \n 1. Moderate \n 2. Severe\n"))
                    if IntensityBackPainCheck == 1:
                        Cough = int(input("Are you coughing? \n 1. Yes \n 2. No\n"))
                        if Cough == 1:
                            console.print(printpercent(40, "Gastroesophageal reflux"))
                            disease="Gastroesophageal reflux"
                            Treatment="Use omeprazole for gastroesophageal reflux\n and inject pantoprazole if severe."
                            print("Timing: Variable \n **Aggravating factors: \n Large stomach, bending and lying down** \n **Relieving factors: \n Antacids and sometimes burping**")
                            print(Treatment)
                        elif Cough == 2:
                            console.print(printpercent(35, "Gastroesophageal reflux"))
                            disease="Gastroesophageal reflux"
                            Treatment="Use omeprazole for gastroesophageal reflux\n and inject pantoprazole if severe."
                            print("Timing: Variable \n **Aggravating factors: \n Large stomach, bending and lying down** \n **Relieving factors: \n Antacids and sometimes burping**")
                            print(Treatment)
                    elif IntensityBackPainCheck == 2:
                        Cough = int(input("Are you coughing? \n 1.Yes \n 2.No\n"))
                        if Cough == 1:
                            console.print(printpercent(60, "Gastroesophageal reflux"))
                            disease="Gastroesophageal reflux"
                            Treatment="Use omeprazole for gastroesophageal reflux\n and if severe, inject pantoprazole."
                            print("Timing: Variable \n **Aggravating factors: \n Large stomach, bending over and lying down** \n **Relieving factors: \n Antacids and sometimes burping**")
                            print(Treatment)
                        elif Cough == 2:
                            console.print(printpercent(50, "Gastroesophageal reflux"))
                            disease="Gastroesophageal reflux"
                            Treatment="Use omeprazole for gastroesophageal reflux\n and inject pantoprazole if severe."
                            print("Timing: Variable \n **Aggravating factors: \n Large stomach, bending over and lying down** \n **Relieving factors: \n Antacids and sometimes burping**")
                            print(Treatment)
                elif QualityBackPainCheck == 2:
                    IntensityBackPainCheck = int(input("How severe is your pain? \n 1.Moderate \n 2.Severe\n"))
                    if IntensityBackPainCheck == 1:
                        Cough = int(input("Are you coughing? \n 1.Yes \n 2.No\n"))
                        if Cough == 1:
                            console.print(printpercent(45, "Gastroesophageal reflux"))
                            disease="Gastroesophageal reflux"
                            Treatment="Use omeprazole for gastroesophageal reflux\n and inject pantoprazole if severe."
                            print("Timing: Variable \n **Aggravating factors: \n Large stomach, bending and lying down** \n **Relieving factors: \n Antacids and sometimes burping**")
                            print(Treatment)
                        elif Cough == 2:
                            console.print(printpercent(40, "Gastroesophageal reflux"))
                            disease="Gastroesophageal reflux"
                            Treatment="Use omeprazole for gastroesophageal reflux\n and inject pantoprazole if severe."
                            print("Timing: Variable \n **Aggravating factors: \n Large stomach, bending and lying down** \n **Relieving factors: \n Antacids and sometimes burping**")
                            print(Treatment)
                    elif IntensityBackPainCheck == 2:
                        Cough = int(input("Are you coughing? \n 1.Yes \n 2.No\n"))
                        if Cough == 1:
                            console.print(printpercent(65, "Gastroesophageal reflux"))
                            disease="Gastroesophageal reflux"
                            Treatment="Use omeprazole for gastroesophageal reflux\n and if severe, inject pantoprazole."
                            print("Timing: Variable \n **Aggravating factors: \n Large stomach, bending and lying down** \n **Relieving factors: \n Antacids and sometimes burping**")
                            print(Treatment)
                        elif Cough == 2:
                            console.print(printpercent(55, "Gastroesophageal reflux"))
                            disease="Gastroesophageal reflux"
                            Treatment="Use omeprazole for gastroesophageal reflux\n and inject pantoprazole if severe."
                            print("Timing: Variable \n **Aggravating factors: \n Large stomach, bending and lying down** \n **Relieving factors: \n Antacids and sometimes burping**")
                            print(Treatment)

                elif QualityBackPainCheck == 3:
                    print("Sorry, there is not enough information to diagnose your problem. \n Please see your doctor.")

            elif BackPainCheck == 3:
                print("Sorry, there is not enough information to diagnose your problem. \n Please see your doctor.")
        elif AreaOfThePain == 3:
            QualityCheck = int(input("Is the quality of your pain sharp, dull, or aching? \n 1.Yes \n 2.No \n"))
            if QualityCheck == 1:
                SensitivityCheck = int(input("Are you sensitive to touch? \n 1.Yes \n 2.No \n"))
                if SensitivityCheck == 1:
                    console.print(printpercent(70-80, "chest wall pain"))
                    disease="Chest wall pain"
                    Treatment="For chest wall pain, if your chest wall is broken;\n you should wait and rest. \n If it is not broken; you should wait until the bruising heals."
                    print("Timeline: Hours to days \n **Aggravating factors: \n Coughing, chest and arm movements**")
                    print(Treatment)
                elif SensitivityCheck == 2:
                    console.print(printpercent(50-60, "Chest wall pain"))
                    disease="Chest wall pain"
                    Treatment="For chest wall pain, if your chest wall is broken;\n you should wait and rest. \n If it is not broken; you should wait for the bruising to heal."
                    print("Timing: Hours to days \n **Aggravating factors: \n Coughing, chest movement, and arms**")
                    print(Treatment)

            elif QualityCheck == 2:
                print("Sorry, there is not enough information to diagnose your problem. \n Please see your doctor.")
      
        elif AreaOfThePain == 2:
            PainInTheFrontCheck = int(input("Do you feel pain in the front of your chest? \n 1.Yes \n 2.No \n"))
            if PainInTheFrontCheck == 2:
                QualityFrontCheck = int(input("Is the quality of your pain sharp, dull, or aching? \n 1.Yes \n 2.No \n"))
                if QualityFrontCheck == 1:
                    SensitivityFrontCheck = int(input("Do you feel sensitive to touch? \n 1.Yes \n 2.No \n"))
                    if SensitivityFrontCheck == 1:
                        console.print(printpercent(60-70, "chest wall pain"))
                        disease="chest wall pain"
                        Treatment="For chest wall pain, if your chest wall is broken;\n you should wait and rest. \n If it is not broken; you should wait until the bruising has healed."
                        print("Timing: Hours to days \n **Aggravating factors:\n Coughing, chest and arm movements**")
                        print(Treatment)
                    elif SensitivityFrontCheck == 2:
                        console.print(printpercent(50-60, "chest wall pain"))
                        disease="chest wall pain"
                        Treatment="For chest wall pain, if your chest wall is broken;\n you should wait and rest. \n If it is not broken; You should wait for the bruising to resolve."
                        print("Timeline: Hours to days \n **Aggravating factors: \n Coughing, chest and arm movements**")
                        print(Treatment)
                elif QualityFrontCheck == 2:
                    print("Sorry, there is not enough information available to diagnose your problem. \n Please see your doctor.")
            elif PainInTheFrontCheck == 1:
                QualityFrontCheck2 = int(input("Is the quality of your pain sharp, dull, and aching? \n 1.Yes \n 2.No \n"))
                if QualityFrontCheck2 == 1:
                    print("Now we need to find out what associated symptoms you have.")
                    print(" 1.Shortness of breath \n 2.Weak heartbeat \n 3.Anxiety \n 4.Other options")
                    print()
                    associated_symptoms=input("Which of the associated symptoms do you have? \n You can choose multiple options. /n Just put , between the numbers.\n")
                    print()
                    associated_symptoms=set(map(int,associated_symptoms.split(",")))
                    if associated_symptoms == {1}:
                        console.print(printpercent(40, "Anxiety and mental disorders"))
                        disease="Anxiety and mental disorders"
                        Treatment="See a psychiatrist for anxiety and mental disorders and take neuroleptics if necessary "
                        print("Timeframe: Hours to days \n **Aggravators: Activity and emotional stress**")
                        print(Treatment)
                    elif associated_symptoms == {2}:
                        console.print(printpercent(35, "Anxiety and mental disorders"))
                        disease="Anxiety and mental disorders"
                        Treatment="See a psychiatrist for anxiety and mental disorders and take neuroleptics if needed."
                        print("Timeframe: Hours to days \n **Aggravators: Activity and emotional stress**")
                        print(Treatment)
                    elif associated_symptoms == {3}:
                        console.print(printpercent(50, "Anxiety and mental disorders"))
                        disease="Anxiety and mental disorders"
                        Treatment="See a psychiatrist for anxiety and mental disorders and take neuroleptics if needed."
                        print("Timeline: Hours to days \n **Aggravators: Activity and emotional stress**")
                        print(Treatment)
                    elif associated_symptoms == {1,2}:
                        console.print(printpercent(45, "Anxiety and mental disorders"))
                        disease="Anxiety and mental disorders"
                        Treatment="See a psychiatrist for anxiety and mental disorders and take neuroleptics if needed."
                        print("Timeline: Hours to days \n **Aggravators: Activity and emotional stress**")
                        print(Treatment)
                    elif associated_symptoms == {1,3}:
                        console.print(printpercent(55, "Anxiety and mental disorders"))
                        disease="Anxiety and mental disorders"
                        Treatment="See a psychiatrist for anxiety and mental disorders and take neuroleptics if needed."
                        print("Timeline: Hours to days \n **Aggravators: Activity and emotional stress**")
                        print(Treatment)
                    elif associated_symptoms == {2,3}:
                        console.print(printpercent(50, "Anxiety and mental disorders"))
                        disease="Anxiety and mental disorders"
                        Treatment="See a psychiatrist for anxiety and mental disorders and take neuroleptics if needed."
                        print("Timeline: Hours to days \n **Aggravators: Activity and emotional stress**")
                        print(Treatment)
                    elif associated_symptoms == {1,2,3}:
                        console.print(printpercent(60-70, "Anxiety and mental disorders"))
                        disease="Anxiety and mental disorders"
                        Treatment="See a psychiatrist for anxiety and mental disorders and take neuroleptics if needed."
                        print("Timeline: Hours to days \n **Aggravating factors: Activity and emotional stress**")
                        print(Treatment)
                    elif associated_symptoms == {4}:
                        print("Sorry, there is not enough information to diagnose your problem. \n Please see your doctor.")
                        
            elif QualityFrontCheck2 == 2:
                print("Sorry, there is not enough information to diagnose your problem. \n Please see your doctor.")
                
    ##################################
    elif A == 3:
        print("You have a cough.")
        #We need to understand what type of cough you have.
        print()
        print("Now I need to understand what type of cough you have. Choose from the following factors.")
        print("1=Dry cough\n2=Mucoid sputum\n3=Purulent sputum mixed with blood\n4=Purulent sputum without blood\n5=Purulent sputum completely bloody\n6=Chronic cough especially at night\n7=Cough that varies in places and times")
        print()
        cough=input("Which of the coughs do you have? You can choose multiple cases, just put , between the numbers")
        #We use split to separate the above string from its numbers and ','
        #We use the map function here to convert all the input information into numerical data.
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
        if cough == {1} and associated_symptoms == {1}:
            console.print(printpercent(30, "viral lung infection"))
            disease = "viral lung infection"
        elif cough == {1} and associated_symptoms == {2}:
            console.print(printpercent(25, "viral lung infection"))
            disease = "viral lung infection"
        elif cough == {1} and associated_symptoms == {3}:
            console.print(printpercent(40, "viral lung infection"))
            disease = "viral lung infection"
        elif cough == {1} and associated_symptoms == {1, 2}:
            console.print(printpercent(40, "viral lung infection"))
            disease = "viral lung infection"
        elif cough == {1} and associated_symptoms == {1, 2}:
            console.print(printpercent(50, "viral lung infection"))
            disease = "viral lung infection"
        elif cough == {1} and associated_symptoms == {2, 3}:
            console.print(printpercent(35, "viral lung infection"))
            disease = "viral lung infection"
        elif cough == {1} and associated_symptoms == {1, 2, 3}:
            console.print(printpercent(60, "viral lung infection"))
            disease = "viral lung infection"
        elif cough == {1} and associated_symptoms == {16}:
            console.print(printpercent(20, "viral lung infection"))
            disease = "viral lung infection"
        
        # Mucoid sputum
        elif cough=={2} and associated_symptoms=={1}:
            console.print(printpercent(20,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={2} and associated_symptoms=={2}:
            console.print(printpercent(15,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={2} and associated_symptoms=={3}:
            console.print(printpercent(30,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={2} and associated_symptoms=={1,2}:
            console.print(printpercent(30,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={2} and associated_symptoms=={1,3}:
            console.print(printpercent(40,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={2} and associated_symptoms=={2,3}:
            console.print(printpercent(25,"Viral Lung Infection"))
            disease = "Viral Lung Infection"
        elif cough=={2} and associated_symptoms=={1,2,3}:
            console.print(printpercent(50,"Viral Lung Infection"))
            disease = "Viral Lung Infection"
        elif cough=={2} and associated_symptoms=={16}:
            console.print(printpercent(35,"Viral Lung Infection"))
            disease = "Viral Lung Infection"
        # Purulent sputum
        elif cough=={4} and associated_symptoms=={1}:
            console.print(printpercent(25,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={4} and associated_symptoms=={2}:
            console.print(printpercent(20,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={4} and associated_symptoms=={3}:
            console.print(printpercent(35,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={4} and associated_symptoms=={1,2}:
            console.print(printpercent(35,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={4} and associated_symptoms=={1,3}:
            console.print(printpercent(45,"Viral Lung Infection"))
            disease = "Viral Lung Infection"
        elif cough=={4} and associated_symptoms=={2,3}:
            console.print(printpercent(30,"Viral Lung Infection"))
            disease = "Viral Lung Infection"
        elif cough=={4} and associated_symptoms=={1,2,3}:
            console.print(printpercent(55,"Viral Lung Infection"))
            disease = "Viral Lung Infection"
        elif cough=={4} and associated_symptoms=={16}:
            console.print(printpercent(60,"Viral Lung Infection"))
            disease = "Viral Lung Infection"
        
        # Dry cough and mucoid sputum
        elif cough=={1,2} and associated_symptoms=={1}:
            console.print(printpercent(35,"Lung Infection viral"))
            disease = "viral lung infection"
        elif cough=={1,2} and associated_symptoms=={2}:
            console.print(printpercent(30,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={1,2} and associated_symptoms=={3}:
            console.print(printpercent(45,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={1,2} and associated_symptoms=={1,2}:
            console.print(printpercent(45,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={1,2} and associated_symptoms=={1,3}:
            console.print(printpercent(60,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={1,2} and associated_symptoms=={2,3}:
            console.print(printpercent(40,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={1,2} and associated_symptoms=={1,2,3}:
            console.print(printpercent(70,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={1,2} and associated_symptoms=={16}:
            console.print(printpercent(40,"viral lung infection"))
            disease = "viral lung infection"
        
        # Dry cough and purulent sputum
        elif cough=={1,4} and associated_symptoms=={1}:
            console.print(printpercent(30,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={1,4} and associated_symptoms=={2}:
            console.print(printpercent(30,"Viral Lung Infection"))
            disease = "Viral Lung Infection"
        elif cough=={1,4} and associated_symptoms=={3}:
            console.print(printpercent(40,"Viral Lung Infection"))
            disease = "Viral Lung Infection"
        elif cough=={1,4} and associated_symptoms=={1,2}:
            console.print(printpercent(45,"Viral Lung Infection"))
            disease = "Viral Lung Infection"
        elif cough=={1,4} and associated_symptoms=={1,3}:
            console.print(printpercent(45,"Viral Lung Infection"))
            disease = "Viral Lung Infection"
        elif cough=={1,4} and associated_symptoms=={2,3}:
            console.print(printpercent(40,"Viral Lung Infection"))
            disease = "Viral lung infection"
        elif cough=={1,4} and associated_symptoms=={1,2,3}:
            console.print(printpercent(75,"Viral lung infection"))
            disease = "Viral lung infection"
        elif cough=={1,4} and associated_symptoms=={16}:
            console.print(printpercent(55,"Viral lung infection"))
            disease = "Viral lung infection"
        # Mucoid and purulent sputum
        elif cough=={2,4} and associated_symptoms=={1}:
            console.print(printpercent(30,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={2,4} and associated_symptoms=={2}:
            console.print(printpercent(25,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={2,4} and associated_symptoms=={3}:
            console.print(printpercent(40,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={2,4} and associated_symptoms=={1,2}:
            console.print(printpercent(35,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={2,4} and associated_symptoms=={1,3}:
            console.print(printpercent(55,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={2,4} and associated_symptoms=={2,3}:
            console.print(printpercent(40,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={2,4} and associated_symptoms=={1,2,3}:
            console.print(printpercent(65,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={2,4} and associated_symptoms=={16}:
            console.print(printpercent(50,"viral lung infection"))
            disease = "viral lung infection"
        
        # Dry cough, mucoid sputum, and purulent sputum
        elif cough=={1,2,4} and associated_symptoms=={1}:
            console.print(printpercent(45,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={1,2,4} and associated_symptoms=={2}:
            console.print(printpercent(35,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={1,2,4} and associated_symptoms=={3}:
            console.print(printpercent(50,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={1,2,4} and associated_symptoms=={1,2}:
            console.print(printpercent(55,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={1,2,4} and associated_symptoms=={1,3}:
            console.print(printpercent(65,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={1,2,4} and associated_symptoms=={2,3}:
            console.print(printpercent(55,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={1,2,4} and associated_symptoms=={1,2,3}:
            console.print(printpercent(75,"viral lung infection"))
            disease = "viral lung infection"
        elif cough=={1,2,4} and associated_symptoms=={16}:
            console.print(printpercent(65,"viral lung infection"))
            disease = "viral lung infection"
        
        
        #bacterial lung infection
        #mucous sputum
        if cough=={2} and associated_symptoms=={1}:
            console.print(printpercent(20,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2} and associated_symptoms=={3}:
            console.print(printpercent(25,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2} and associated_symptoms=={4}:
            console.print(printpercent(30,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2} and associated_symptoms=={5}:
            console.print(printpercent(15,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2} and associated_symptoms=={1,3}:
            console.print(printpercent(35,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2} and associated_symptoms=={1,4}:
            console.print(printpercent(40,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2} and associated_symptoms=={1,5}:
            console.print(printpercent(25,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2} and associated_symptoms=={3,4}:
            console.print(printpercent(20,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2} and associated_symptoms=={3,5}:
            console.print(printpercent(20,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2} and associated_symptoms=={4,5}:
            console.print(printpercent(25,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2} and associated_symptoms=={1,3,4}:
            console.print(printpercent(45,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2} and associated_symptoms=={1,3,5}:
            console.print(printpercent(30,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2} and associated_symptoms=={3,4,5}:
            console.print(printpercent(35,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        # Blood-tinged purulent sputum
        elif cough=={3} and associated_symptoms=={1}:
            console.print(printpercent(35,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={3} and associated_symptoms=={3}:
            console.print(printpercent(40,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={3} and associated_symptoms=={4}:
            console.print(printpercent(45,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={3} and associated_symptoms=={5}:
            console.print(printpercent(30,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={3} and associated_symptoms=={1,3}:
            console.print(printpercent(45,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={3} and associated_symptoms=={1,4}:
            console.print(printpercent(50,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={3} and associated_symptoms=={1,5}:
            console.print(printpercent(35,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={3} and associated_symptoms=={3,4}:
            console.print(printpercent(45,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={3} and associated_symptoms=={3,5}:
            console.print(printpercent(35,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={3} and associated_symptoms=={3,5}:
            console.print(printpercent(35,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={3} and associated_symptoms=={4,5}:
            console.print(printpercent(40,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={3} and associated_symptoms=={1,3,4}:
            console.print(printpercent(55,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={3} and associated_symptoms=={1,3,5}:
            console.print(printpercent(40,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={3} and associated_symptoms=={3,4,5}:
            console.print(printpercent(45,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={3} and associated_symptoms=={1,2,3,4}:
            console.print(printpercent(60,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={3} and associated_symptoms=={16}:
            console.print(printpercent(70,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
       # Purulent sputum without blood
        elif cough=={4} and associated_symptoms=={1}:
            console.print(printpercent(30,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={4} and associated_symptoms=={3}:
            console.print(printpercent(35,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={4} and associated_symptoms=={4}:
            console.print(printpercent(40,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={4} and associated_symptoms=={5}:
            console.print(printpercent(25,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={4} and associated_symptoms=={1,3}:
            console.print(printpercent(40,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={4} and associated_symptoms=={1,4}:
            console.print(printpercent(45,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={4} and associated_symptoms=={1,5}:
            console.print(printpercent(30,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={4} and associated_symptoms=={3,4}:
            console.print(printpercent(35,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={4} and associated_symptoms=={3,5}:
            console.print(printpercent(25,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={4} and associated_symptoms=={4,5}:
            console.print(printpercent(35,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={4} and associated_symptoms=={1,3,4}:
            console.print(printpercent(50,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={4} and associated_symptoms=={1,3,5}:
            console.print(printpercent(35,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={4} and associated_symptoms=={3,4,5}:
            console.print(printpercent(40,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={4} and associated_symptoms=={1,2,3,4}:
            console.print(printpercent(55,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={4} and associated_symptoms=={16}:
            console.print(printpercent(60,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        #Mucoid and purulent sputum stained with blood
        elif cough=={2,3} and associated_symptoms=={1}:
            console.print(printpercent(40,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={2,3} and associated_symptoms=={3}:
            console.print(printpercent(45,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={2,3} and associated_symptoms=={4}:
            console.print(printpercent(50,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={2,3} and associated_symptoms=={5}:
            console.print(printpercent(35,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={2,3} and associated_symptoms=={1,3}:
            console.print(printpercent(50,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,3} and associated_symptoms=={1,4}:
            console.print(printpercent(55,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,3} and associated_symptoms=={1,5}:
            console.print(printpercent(40,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,3} and associated_symptoms=={3,4}:
            console.print(printpercent(45,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,3} and associated_symptoms=={3,5}:
            console.print(printpercent(35,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,3} and associated_symptoms=={4,5}:
            console.print(printpercent(40,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,3} and associated_symptoms=={1,3,4}:
            console.print(printpercent(60,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,3} and associated_symptoms=={1,3,5}:
            console.print(printpercent(45,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,3} and associated_symptoms=={3,4,5}:
            console.print(printpercent(50,"Bacterial Lung Infection"))
            disease = "Bacterial lung infection"
        elif cough=={2,3} and associated_symptoms=={1,2,3,4}:
            console.print(printpercent(65,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={2,3} and associated_symptoms=={16}:
            console.print(printpercent(75,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        #Mucoid sputum and purulent sputum without blood
        elif cough=={2,4} and associated_symptoms=={1}:
            console.print(printpercent(35,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={2,4} and associated_symptoms=={3}:
            console.print(printpercent(40,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={2,4} and associated_symptoms=={4}:
            console.print(printpercent(45,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={2,4} and associated_symptoms=={5}:
            console.print(printpercent(30,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={2,4} and associated_symptoms=={1,3}:
            console.print(printpercent(45,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={2,4} and associated_symptoms=={1,4}:
            console.print(printpercent(50,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={2,4} and associated_symptoms=={1,5}:
            console.print(printpercent(35,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,4} and associated_symptoms=={3,4}:
            console.print(printpercent(40,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,4} and associated_symptoms=={3,5}:
            console.print(printpercent(30,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,4} and associated_symptoms=={4,5}:
            console.print(printpercent(35,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,4} and associated_symptoms=={1,3,4}:
            console.print(printpercent(55,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,4} and associated_symptoms=={1,3,5}:
            console.print(printpercent(40,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,4} and associated_symptoms=={3,4,5}:
            console.print(printpercent(45,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,4} and associated_symptoms=={1,2,3,4}:
            console.print(printpercent(60,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,4} and associated_symptoms=={16}:
            console.print(printpercent(65,"Bacterial Lung Infection"))
            disease = "Bacterial lung infection"
        # Bloody purulent sputum and bloodless purulent sputum
        elif cough=={3,4} and associated_symptoms=={1}:
            console.print(printpercent(35,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={3,4} and associated_symptoms=={3}:
            console.print(printpercent(40,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={3,4} and associated_symptoms=={4}:
            console.print(printpercent(45,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={3,4} and associated_symptoms=={5}:
            console.print(printpercent(30,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={3,4} and associated_symptoms=={1,3}:
            console.print(printpercent(45,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={3,4} and associated_symptoms=={1,4}:
            console.print(printpercent(50,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={3,4} and associated_symptoms=={1,5}:
            console.print(printpercent(35,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={3,4} and associated_symptoms=={3,4}:
            console.print(printpercent(40,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={3,4} and associated_symptoms=={3,5}:
            console.print(printpercent(30,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={3,4} and associated_symptoms=={4,5}:
            console.print(printpercent(35,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={3,4} and associated_symptoms=={1,3,4}:
            console.print(printpercent(55,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={3,4} and associated_symptoms=={1,3,5}:
            console.print(printpercent(40,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={3,4} and associated_symptoms=={3,4,5}:
            console.print(printpercent(50,"Bacterial Lung Infection" ))
            disease = "Bacterial lung infection"
        elif cough=={3,4} and associated_symptoms=={1,2,3,4}:
            console.print(printpercent(60,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={3,4} and associated_symptoms=={16}:
            console.print(printpercent(68,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        #Mucoid and purulent sputum with blood and purulent sputum without blood
        elif cough=={2,3,4} and associated_symptoms=={1}:
            console.print(printpercent(40,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={2,3,4} and associated_symptoms=={3}:
            console.print(printpercent(45,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,3,4} and associated_symptoms=={4}:
            console.print(printpercent(50,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,3,4} and associated_symptoms=={5}:
            console.print(printpercent(35,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,3,4} and associated_symptoms=={1,3}:
            console.print(printpercent(50,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,3,4} and associated_symptoms=={1,4}:
            console.print(printpercent(55,"Bacterial Lung Infection"))
            disease = "Bacterial lung infection"
        elif cough=={2,3,4} and associated_symptoms=={1,5}:
            console.print(printpercent(40,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={2,3,4} and associated_symptoms=={3,4}:
            console.print(printpercent(45,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={2,3,4} and associated_symptoms=={3,5}:
            console.print(printpercent(35,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={2,3,4} and associated_symptoms=={4,5}:
            console.print(printpercent(40,"Bacterial lung infection"))
            disease = "Bacterial lung infection"
        elif cough=={2,3,4} and associated_symptoms=={1,3,4}:
            console.print(printpercent(60,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,3,4} and associated_symptoms=={1,3,5}:
            console.print(printpercent(45,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,3,4} and associated_symptoms=={3,4,5}:
            console.print(printpercent(50,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,3,4} and associated_symptoms=={1,2,3,4}:
            console.print(printpercent(65,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        elif cough=={2,3,4} and associated_symptoms=={16}:
            console.print(printpercent(80,"Bacterial Lung Infection"))
            disease = "Bacterial Lung Infection"
        
        
        #viral or bacterial sinusitis or allergies (postnasal drip)
        #mucous sputum
        if cough=={2} and associated_symptoms=={6}:
            console.print(printpercent(30, "viral sinusitis"))
            console.print(printpercent(25, "bacterial sinusitis"))
            console.print(printpercent(20, "allergy"))
            disease="viral or bacterial sinusitis or allergies"
        
        #purulent sputum without blood
        elif cough=={4} and associated_symptoms=={6}:
            console.print(printpercent(25, "viral sinusitis"))
            console.print(printpercent(20, "bacterial sinusitis"))
            console.print(printpercent(15, "allergy"))
            disease="viral or bacterial sinusitis or allergies"
            
        #chronic cough
        elif cough=={6} and associated_symptoms=={6}:
            console.print(printpercent(20, "viral sinusitis"))
            console.print(printpercent(15, "bacterial sinusitis"))
            console.print(printpercent(10, "allergies"))
            disease="viral or bacterial sinusitis or allergies"
        
        #mucous and purulent sputum without blood
        elif cough=={2,4} and associated_symptoms=={6}:
            console.print(printpercent(35, "viral sinusitis"))
            console.print(printpercent(30, "bacterial sinusitis"))
            console.print(printpercent(25, "allergies"))
            disease="viral or bacterial sinusitis or allergies"
        #mucous and chronic cough
        elif cough=={2,6} and associated_symptoms=={6}:
            console.print(printpercent(25, "viral sinusitis"))
            console.print(printpercent(20, "sinusitis bacterial"))
            console.print(printpercent(20, "allergy"))
            disease="Viral or bacterial sinusitis or allergy"
        
        #Purulent sputum without blood and chronic cough
        elif cough=={4,6} and associated_symptoms=={6}:
            console.print(printpercent(35, "Viral sinusitis"))
            console.print(printpercent(25, "Bacterial sinusitis"))
            console.print(printpercent(20, "allergy"))
            disease="Viral or bacterial sinusitis or allergy"
            
        #Mucoid sputum and purulent sputum without blood and chronic cough
        elif cough=={2,4,6} and associated_symptoms=={6}:
            console.print(printpercent(40, "Viral sinusitis"))
            console.print(printpercent(35, "Bacterial sinusitis"))
            console.print(printpercent(30, "allergy"))
            disease="Viral sinusitis or bacterial or allergic"
        
        #No associated symptoms
        elif cough=={2} and associated_symptoms=={16}:
            console.print(printpercent(50, "viral sinusitis"))
            console.print(printpercent(20, "bacterial sinusitis"))
            console.print(printpercent(40, "allergy"))
            disease="viral or bacterial sinusitis or allergic"
        elif cough=={4} and associated_symptoms=={16}:
            console.print(printpercent(30, "viral sinusitis"))
            console.print(printpercent(70, "bacterial sinusitis"))
            console.print(printpercent(10, "allergy"))
            disease="viral or bacterial sinusitis or allergic"
        elif cough=={6} and associated_symptoms=={16}:
            console.print(printpercent(20, "viral sinusitis"))
            console.print(printpercent(30, "bacterial sinusitis"))
            console.print(printpercent(50, "allergies"))
            disease="viral or bacterial sinusitis or allergies"
        elif cough=={2,4} and associated_symptoms=={16}:
            console.print(printpercent(40, "viral sinusitis"))
            console.print(printpercent(60, "bacterial sinusitis"))
            console.print(printpercent(25, "allergies"))
            disease="viral or bacterial sinusitis or allergies"
        elif cough=={2,6} and associated_symptoms=={16}:
            console.print(printpercent(35, "viral sinusitis"))
            console.print(printpercent(25, "bacterial sinusitis"))
            console.print(printpercent(45, "allergies"))
            disease="viral or bacterial sinusitis or allergies"
        elif cough=={4,6} and associated_symptoms=={16}:
            console.print(printpercent(30, "viral sinusitis"))
            console.print(printpercent(70, "bacterial sinusitis"))
            console.print(printpercent(20, "allergies"))
            disease="viral or bacterial sinusitis or allergies"
        elif cough=={2,4,6} and associated_symptoms=={16}:
            console.print(printpercent(25, "viral sinusitis"))
            console.print(printpercent(75, "bacterial sinusitis"))
            console.print(printpercent(30, "allergies"))
            disease="viral or bacterial sinusitis or allergies"
        
        #pulmonary tuberculosis
        #dry cough
        if cough == {1} and associated_symptoms == {1}:
            console.print(printpercent(20, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {7}:
            console.print(printpercent(15, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {8}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {9}:
            console.print(printpercent(20, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {10}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {1, 7}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {1, 8}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {1, 9}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {1, 10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {7, 8}:
            console.print(printpercent(20, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {7, 9}:
            console.print(printpercent(15, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {7, 10}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {8, 9}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {8, 10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {9, 10}:
            console.print(printpercent(20, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {1, 7, 8}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {1, 7, 9}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {1, 7, 10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {1, 8, 9}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {1, 8, 10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {1, 9, 10}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {7, 8, 9}:
            console.print(printpercent(20, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {7, 8, 10}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {7, 9, 10}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {8, 9, 10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {1, 7, 8, 9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {1, 7, 8, 10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {1, 7, 9, 10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {1, 8, 9, 10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {7, 8, 9, 10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {1} and associated_symptoms == {1, 7, 8, 9, 10}:
            console.print(printpercent(60, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        #mucous sputum
        elif cough == {2} and associated_symptoms == {1}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {7}:
            console.print(printpercent(20, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {8}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {9}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {1, 7}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {1, 8}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {1, 9}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {1, 10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {7, 8}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {7, 9}:
            console.print(printpercent(20, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {7, 10}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {8, 9}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {8, 10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {9, 10}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {1, 7, 8}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {1, 7, 9}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {1, 7, 10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {1, 8, 9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {1, 8, 10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {1, 9, 10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {7, 8, 9}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {7, 8, 10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {7, 9, 10}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {8, 9, 10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {1, 7, 8, 9}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {1, 7, 8, 10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {1, 7, 9, 10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {1, 8, 9, 10}:
            console.print(printpercent(60, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough == {2} and associated_symptoms == {7, 8, 9, 10}:
            console.print(printpercent(50, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough == {2} and associated_symptoms == {1, 7, 8, 9, 10}:
            console.print(printpercent(65, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        ########################
        #blood-tinged sputum
        elif cough == {3} and associated_symptoms == {1}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {7}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {8}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {9}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {1, 7}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {1, 8}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {1, 9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {1, 10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {7, 8}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {7, 9}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {7, 10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {8, 9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {8, 10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {9, 10}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {1, 7, 8}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {1, 7, 9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {1, 7, 10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {1, 8, 9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {1, 8, 10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease = "tuberculosis Pulmonary"
        elif cough == {3} and associated_symptoms == {1, 9, 10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {7, 8, 9}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {7, 8, 10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {7, 9, 10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {8, 9, 10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {1, 7, 8, 9}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {1, 7, 8, 10}:
            console.print(printpercent(60, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {1, 7, 9, 10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {1, 8, 9, 10}:
            console.print(printpercent(65, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {7, 8, 9, 10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {3} and associated_symptoms == {1, 7, 8, 9, 10}:
            console.print(printpercent(70, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        
        # Purulent sputum completely bloody
        elif cough == {5} and associated_symptoms == {1}:
            console.print(printpercent(70, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {7}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {8}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {1, 7}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {1, 8}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {1, 9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {1, 10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {7, 8}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {7, 9}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {7, 10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {8, 9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {8, 10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {9, 10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {1, 7, 8}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {1, 7, 9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {1, 7, 10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {1, 8, 9}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {1, 8, 10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {1, 9, 10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {7, 8, 9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {7, 8, 10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {7, 9, 10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {8, 9, 10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {1, 7, 8, 9}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {1, 7, 8, 10}:
            console.print(printpercent(65, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {1, 7, 9, 10}:
            console.print(printpercent(60, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {1, 8, 9, 10}:
            console.print(printpercent(70, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {7, 8, 9, 10}:
            console.print(printpercent(60, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        elif cough == {5} and associated_symptoms == {1, 7, 8, 9, 10}:
            console.print(printpercent(75, "pulmonary tuberculosis"))
            disease = "pulmonary tuberculosis"
        
        #Dry cough and mucoid sputum
        elif cough=={1,2} and associated_symptoms=={1}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={7}:
            console.print(printpercent(20, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={8}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={9}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={1,7}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={1,8}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={1,9}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={1,10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={7,8}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={7,9}:
            console.print(printpercent(20, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={7,10}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={8,9}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={8,10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={9,10}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={1,7,8}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={1,7,9}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={1,7,10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={1,8,9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={1,8,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis Pulmonary"
        elif cough=={1,2} and associated_symptoms=={1,9,10}:
            console.print(printpercent(35, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={1,2} and associated_symptoms=={7,8,9}:
            console.print(printpercent(25, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={1,2} and associated_symptoms=={7,8,10}:
            console.print(printpercent(35, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={1,2} and associated_symptoms=={7,9,10}:
            console.print(printpercent(30, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={1,2} and associated_symptoms=={8,9,10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={1,7,8,9}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={1,7,8,10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={1,7,9,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={1,8,9,10}:
            console.print(printpercent(60, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={7,8,9,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={1,7,8,9,10}:
            console.print(printpercent(65, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        
        #Dry cough and blood-tinged purulent sputum
        elif cough=={1,3} and associated_symptoms=={1}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={7}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={8}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={9}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis Pulmonary"
        elif cough=={1,3} and associated_symptoms=={1,7}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="Pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={1,8}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="Pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={1,9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="Pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={1,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="Pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={7,8}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="Pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={7,9}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={7,10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={8,9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={8,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={9,10}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={1,7,8}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={1,7,9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={1,7,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={1,8,9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={1,8,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis Pulmonary"
        elif cough=={1,3} and associated_symptoms=={1,9,10}:
            console.print(printpercent(40, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={1,3} and associated_symptoms=={7,8,9}:
            console.print(printpercent(30, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={1,3} and associated_symptoms=={7,8,10}:
            console.print(printpercent(40, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={1,3} and associated_symptoms=={7,9,10}:
            console.print(printpercent(35, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={1,3} and associated_symptoms=={8,9,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={1,7,8,9}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={1,7,8,10}:
            console.print(printpercent(60, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={1,7,9,10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={1,8,9,10}:
            console.print(printpercent(65, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={7,8,9,10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={1,7,8,9,10}:
            console.print(printpercent(70, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        
        #Dry cough and purulent sputum completely bloody
        elif cough=={1,5} and associated_symptoms=={1}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={7}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={8}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={1,7}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={1,8}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={1,9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={1,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={7,8}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={7,9}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={7,10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={8,9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={8,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={9,10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={1,7,8}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={1,7,9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={1,7,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={1,8,9}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={1,8,10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis Pulmonary"
        elif cough=={1,5} and associated_symptoms=={1,9,10}:
            console.print(printpercent(45, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={1,5} and associated_symptoms=={7,8,9}:
            console.print(printpercent(35, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={1,5} and associated_symptoms=={7,8,10}:
            console.print(printpercent(45, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={1,5} and associated_symptoms=={7,9,10}:
            console.print(printpercent(40, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={1,5} and associated_symptoms=={8,9,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={1,7,8,9}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={1,7,8,10}:
            console.print(printpercent(65, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={1,7,9,10}:
            console.print(printpercent(60, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={1,8,9,10}:
            console.print(printpercent(70, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={7,8,9,10}:
            console.print(printpercent(60, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={1,7,8,9,10}:
            console.print(printpercent(75, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        
        #Mucoid and purulent sputum stained with blood
        elif cough=={2,3} and associated_symptoms=={1}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={7}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={8}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={9}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis Pulmonary"
        elif cough=={2,3} and associated_symptoms=={1,7}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="Pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={1,8}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="Pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={1,9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="Pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={1,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="Pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={7,8}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="Pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={7,9}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={7,10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={8,9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={8,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={9,10}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={1,7,8}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={1,7,9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={1,7,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={1,8,9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={1,8,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis Pulmonary"
        elif cough=={2,3} and associated_symptoms=={1,9,10}:
            console.print(printpercent(40, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={2,3} and associated_symptoms=={7,8,9}:
            console.print(printpercent(30, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={2,3} and associated_symptoms=={7,8,10}:
            console.print(printpercent(40, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={2,3} and associated_symptoms=={7,9,10}:
            console.print(printpercent(35, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={2,3} and associated_symptoms=={8,9,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={1,7,8,9}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={1,7,8,10}:
            console.print(printpercent(60, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={1,7,9,10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={1,8,9,10}:
            console.print(printpercent(65, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={7,8,9,10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={1,7,8,9,10}:
            console.print(printpercent(70, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        
        #Mucoid and purulent sputum full of blood
        elif cough=={2,5} and associated_symptoms=={1}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,5} and associated_symptoms=={7}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,5} and associated_symptoms=={8}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,5} and associated_symptoms=={9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,5} and associated_symptoms=={10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis Pulmonary"
        elif cough=={2,5} and associated_symptoms=={1,7}:
            console.print(printpercent(40, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={2,5} and associated_symptoms=={1,8}:
            console.print(printpercent(45, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={2,5} and associated_symptoms=={1,9}:
            console.print(printpercent(40, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={2,5} and associated_symptoms=={1,10}:
            console.print(printpercent(50, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={2,5} and associated_symptoms=={7,8}:
            console.print(printpercent(35, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={2,5} and associated_symptoms=={7,9}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,5} and associated_symptoms=={7,10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,5} and associated_symptoms=={8,9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,5} and associated_symptoms=={8,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,5} and associated_symptoms=={9,10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,5} and associated_symptoms=={1,7,8}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,5} and associated_symptoms=={1,7,9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,5} and associated_symptoms=={1,7,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,5} and associated_symptoms=={1,8,9}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,5} and associated_symptoms=={1,8,10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis Pulmonary"
        elif cough=={2,5} and associated_symptoms=={1,9,10}:
            console.print(printpercent(45, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={2,5} and associated_symptoms=={7,8,9}:
            console.print(printpercent(35, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={2,5} and associated_symptoms=={7,8,10}:
            console.print(printpercent(45, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={2,5} and associated_symptoms=={7,9,10}:
            console.print(printpercent(40, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={2,5} and associated_symptoms=={8,9,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,5} and associated_symptoms=={1,7,8,9}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,5} and associated_symptoms=={1,7,8,10}:
            console.print(printpercent(65, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,5} and associated_symptoms=={1,7,9,10}:
            console.print(printpercent(60, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,5} and associated_symptoms=={1,8,9,10}:
            console.print(printpercent(70, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,5} and associated_symptoms=={7,8,9,10}:
            console.print(printpercent(60, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,5} and associated_symptoms=={1,7,8,9,10}:
            console.print(printpercent(75, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        
        #Purulent sputum mixed with blood and purulent sputum completely bloody
        elif cough=={3,5} and associated_symptoms=={1}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={7}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={8}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={1,7}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={1,8}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={1,9}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={1,10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={7,8}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis Pulmonary"
        elif cough=={3,5} and associated_symptoms=={7,9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="Pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={7,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="Pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={8,9}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="Pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={8,10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="Pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={9,10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="Tuberculosis Pulmonary"
        elif cough=={3,5} and associated_symptoms=={1,7,8}:
            console.print(printpercent(50, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={3,5} and associated_symptoms=={1,7,9}:
            console.print(printpercent(45, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={3,5} and associated_symptoms=={1,7,10}:
            console.print(printpercent(55, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={3,5} and associated_symptoms=={1,8,9}:
            console.print(printpercent(50, "Pulmonary Tuberculosis"))
            disease="Pulmonary Tuberculosis"
        elif cough=={3,5} and associated_symptoms=={1,8,10}:
            console.print(printpercent(60, "Pulmonary Tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={1,9,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={7,8,9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={7,8,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={7,9,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={8,9,10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={1,7,8,9}:
            console.print(printpercent(60, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={1,7,8,10}:
            console.print(printpercent(70, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={1,7,9,10}:
            console.print(printpercent(65, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={1,8,9,10}:
            console.print(printpercent(75, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={7,8,9,10}:
            console.print(printpercent(65, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={1,7,8,9,10}:
            console.print(printpercent(80, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        
        # Dry cough and mucoid and purulent sputum mixed with blood
        elif cough=={1,2,3} and associated_symptoms=={1}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={7}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={8}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={9}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={1,7}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={1,8}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={1,9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={1,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={7,8}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={7,9}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={7,10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={8,9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={8,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={9,10}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={1,7,8}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={1,7,9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={1,7,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={1,8,9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={1,8,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={1,9,10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={7,8,9}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={7,8,10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={7,9,10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={8,9,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={1,7,8,9}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={1,7,8,10}:
            console.print(printpercent(60, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={1,7,9,10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={1,8,9,10}:
            console.print(printpercent(65, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={7,8,9,10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={1,7,8,9,10}:
            console.print(printpercent(70, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        
        #Dry cough and mucoid sputum and purulent sputum full of blood
        elif cough=={1,2,5} and associated_symptoms=={1}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={7}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={8}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={1,7}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={1,8}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={1,9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={1,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={7,8}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={7,9}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={7,10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={8,9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={8,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={9,10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={1,7,8}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={1,7,9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={1,7,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={1,8,9}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={1,8,10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={1,9,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={7,8,9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={7,8,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={7,9,10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={8,9,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={1,7,8,9}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={1,7,8,10}:
            console.print(printpercent(65, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={1,7,9,10}:
            console.print(printpercent(60, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={1,8,9,10}:
            console.print(printpercent(70, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={7,8,9,10}:
            console.print(printpercent(60, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={1,7,8,9,10}:
            console.print(printpercent(75, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        
        #Mucoid and purulent sputum mixed with blood and purulent sputum completely bloody
        elif cough=={2,3,5} and associated_symptoms=={1}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={7}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={8}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={9}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={1,7}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={1,8}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={1,9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={1,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={7,8}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={7,9}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={7,10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={8,9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={8,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={9,10}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={1,7,8}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={1,7,9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={1,7,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={1,8,9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={1,8,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={1,9,10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={7,8,9}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={7,8,10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={7,8,10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={7,9,10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={8,9,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={1,7,8,9}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={1,7,8,10}:
            console.print(printpercent(60, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={1,7,9,10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={1,8,9,10}:
            console.print(printpercent(65, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={7,8,9,10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={1,7,8,9,10}:
            console.print(printpercent(70, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        
        #Dry cough and mucoid sputum and purulent sputum mixed with blood and purulent sputum completely bloody
        elif cough=={1,2,3,5} and associated_symptoms=={1}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={7}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={8}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={1,7}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={1,8}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={1,9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={1,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={7,8}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={7,9}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={7,10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={8,9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={8,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={9,10}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={1,7,8}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={1,7,9}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={1,7,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={1,8,9}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={1,8,10}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={1,9,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={7,8,9}:
            console.print(printpercent(35, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={7,8,10}:
            console.print(printpercent(45, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={7,9,10}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={8,9,10}:
            console.print(printpercent(50, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={1,7,8,9}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={1,7,8,10}:
            console.print(printpercent(65, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={1,7,9,10}:
            console.print(printpercent(60, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={1,8,9,10}:
            console.print(printpercent(70, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={7,8,9,10}:
            console.print(printpercent(60, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={1,7,8,9,10}:
            console.print(printpercent(75, "pulmonary tuberculosis"))
            disease="Pulmonary tuberculosis"
        
        # No associated symptoms
        elif cough=={1} and associated_symptoms=={16}:
            console.print(printpercent(30, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2} and associated_symptoms=={16}:
            console.print(printpercent(25, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3} and associated_symptoms=={16}:
            console.print(printpercent(80, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={5} and associated_symptoms=={16}:
            console.print(printpercent(65, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2} and associated_symptoms=={16}:
            console.print(printpercent(40, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,3} and associated_symptoms=={16}:
            console.print(printpercent(70, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,5} and associated_symptoms=={16}:
            console.print(printpercent(55, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3} and associated_symptoms=={16}:
            console.print(printpercent(75, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,5} and associated_symptoms=={16}:
            console.print(printpercent(60, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={3,5} and associated_symptoms=={16}:
            console.print(printpercent(72, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3} and associated_symptoms=={16}:
            console.print(printpercent(80, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,5} and associated_symptoms=={16}:
            console.print(printpercent(65, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={2,3,5} and associated_symptoms=={16}:
            console.print(printpercent(75, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"
        elif cough=={1,2,3,5} and associated_symptoms=={16}:
            console.print(printpercent(80, "pulmonary tuberculosis"))
            disease="pulmonary tuberculosis"



        #lung abscess
        #purulent sputum stained with blood blood
        if cough=={3} and associated_symptoms=={1}:
            console.print(printpercent(35, "lung abscess"))
            disease="lung abscess"
        elif cough=={3} and associated_symptoms=={12}:
            console.print(printpercent(40, "lung abscess"))
            disease="lung abscess"
        elif cough=={3} and associated_symptoms=={1,12}:
            console.print(printpercent(45, "lung abscess"))
            disease="lung abscess"
        
        #purulent sputum without blood
        elif cough=={4} and associated_symptoms=={1}:
            console.print(printpercent(30, "lung abscess"))
            disease="lung abscess"
        elif cough=={4} and associated_symptoms=={12}:
            console.print(printpercent(35, "lung abscess"))
            disease="Lung abscess"
        elif cough=={4} and associated_symptoms=={1,12}:
            console.print(printpercent(40, "lung abscess"))
            disease="Lung abscess"
        
        #Purulent sputum completely bloody
        elif cough=={5} and associated_symptoms=={1}:
            console.print(printpercent(40, "lung abscess"))
            disease="Lung abscess"
        elif cough=={5} and associated_symptoms=={12}:
            console.print(printpercent(45, "lung abscess"))
            disease="Lung abscess"
        elif cough=={5} and associated_symptoms=={1,12}:
            console.print(printpercent(50, "lung abscess"))
            disease="Lung abscess"
        
        #Purulent sputum without blood and purulent sputum stained with blood
        elif cough=={3,4} and associated_symptoms=={1}:
            console.print(printpercent(35, "lung abscess"))
            disease="Lung abscess"
        elif cough=={3,4} and associated_symptoms=={12}:
            console.print(printpercent(40, "lung abscess"))
            disease="Lung abscess"
        elif cough=={3,4} and associated_symptoms=={1,12}:
            console.print(printpercent(45, "lung abscess"))
            disease="Lung abscess"
        
        #Purulent sputum without blood and purulent sputum stained with blood
        elif cough=={3,5} and associated_symptoms=={1}:
            console.print(printpercent(40, "lung abscess"))
            disease="Lung abscess"
        elif cough=={3,5} and associated_symptoms=={12}:
            console.print(printpercent(45, "lung abscess"))
            disease="Lung abscess"
        elif cough=={3,5} and associated_symptoms=={1,12}:
            console.print(printpercent(50, "lung abscess"))
            disease="Lung abscess"
        
        #Sputum Purulent sputum without blood and purulent sputum completely bloody
        elif cough=={3,5} and associated_symptoms=={1}:
            console.print(printpercent(35, "lung abscess"))
            disease="Lung abscess"
        elif cough=={3,5} and associated_symptoms=={12}:
            console.print(printpercent(40, "lung abscess"))
            disease="Lung abscess"
        elif cough=={3,5} and associated_symptoms=={1,12}:
            console.print(printpercent(45, "lung abscess"))
            disease="Lung abscess"
        
        #Purulent sputum with blood and purulent sputum with blood
        elif cough=={4,5} and associated_symptoms=={1}:
            console.print(printpercent(45, "lung abscess"))
            disease="Lung abscess"
        elif cough=={4,5} and associated_symptoms=={12}:
            console.print(printpercent(50, "lung abscess"))
            disease="Lung abscess"
        elif cough=={4,5} and associated_symptoms=={1,12}:
            console.print(printpercent(55, "lung abscess"))
            disease="Lung abscess"
        
        #Purulent sputum without blood and purulent sputum with blood and purulent sputum with blood
        elif cough=={4,5} and associated_symptoms=={1}:
            console.print(printpercent(45, "lung abscess"))
            disease="Lung abscess"
        elif cough=={4,5} and associated_symptoms=={12}:
            console.print(printpercent(50, "lung abscess"))
            disease="lung abscess"
        elif cough=={4,5} and associated_symptoms=={1,12}:
            console.print(printpercent(55, "lung abscess"))
            disease="lung abscess"
        
        #No associated symptoms
        elif cough=={3} and associated_symptoms=={16}:
            console.print(printpercent(65, "lung abscess"))
            disease="lung abscess"
        elif cough=={5} and associated_symptoms=={16}:
            console.print(printpercent(75, "lung abscess"))
            disease="lung abscess"
        elif cough=={4,5} and associated_symptoms=={16}:
            console.print(printpercent(70, "lung abscess"))
            disease="lung abscess"
        #Asthama
        #mucous phlegm
        if cough=={2} and associated_symptoms=={3}:
            console.print(printpercent(60, "asthma"))
            disease="asthma"
        elif cough=={2} and associated_symptoms=={13}:
            console.print(printpercent(45, "asthma"))
            disease="asthma"
        elif cough=={2} and associated_symptoms=={15}:
            console.print(printpercent(55, "asthma"))
            disease="asthma"
        elif cough=={2} and associated_symptoms=={3}:
            console.print(printpercent(30, "asthma"))
            disease="asthma"
        elif cough=={2} and associated_symptoms=={3,13}:
            console.print(printpercent(70, "asthma"))
            disease="asthma"
        elif cough=={2} and associated_symptoms=={3,15}:
            console.print(printpercent(75, "asthma"))
            disease="asthma"
        elif cough=={2} and associated_symptoms=={13,15}:
            console.print(printpercent(60, "asthma"))
            disease="asthma"
        elif cough=={2} and associated_symptoms=={1,13,15}:
            console.print(printpercent(80, "asthma"))
            disease="asthma"
        elif cough=={2} and associated_symptoms=={16}:
            console.print(printpercent(15, "asthma"))
            disease="asthma"
        
        
        #gastric reflux
        #chronic cough especially at night
        if cough=={6} and associated_symptoms=={14}:
            console.print(printpercent(50, "gastric reflux"))
            disease="gastric reflux"
        elif cough=={6} and associated_symptoms=={15}:
            console.print(printpercent(40, "gastric reflux"))
            disease="gastric reflux"
        elif cough=={6} and associated_symptoms=={14,15}:
            console.print(printpercent(60, "gastric reflux"))
            disease="gastric reflux"
        elif cough=={6} and associated_symptoms=={16}:
            console.print(printpercent(30, "gastric reflux"))
            disease="gastric reflux"
        
        
        #Chemical particles
        #Cough that varies at specific times and places
        if cough=={7} and associated_symptoms=={11}:
            console.print(printpercent(60, "contact with chemical particles"))
            disease="contact with chemical particles"
        elif cough=={7} and associated_symptoms=={16}:
            console.print(printpercent(30, "contact with chemical particles"))
            disease="contact with particles Chemical"
        
        #Treatments
        if disease == "Viral lung infection":
            Treatment="Our recommended treatment for viral lung infection is antivirals. However, the percentage of probability mentioned is approximate. Be sure to consult a doctor for the exact dosage of the drug and the type of antiviral."
            print(Treatment)
        elif disease=="Bacterial lung infection":
            Treatment="Our recommended treatment for bacterial lung infection is antibiotics. However, the percentage of probability mentioned is approximate. Be sure to consult a doctor for the exact dosage of the drug and the type of antibiotic."
            print(Treatment)
        elif disease=="Viral or bacterial sinusitis or allergies":
            Treatment="Our recommended treatment for sinusitis, if it is viral, is an anti-inflammatory such as acetaminophen. If it is bacterial, you need antibiotics. If it is allergic, you need antihistamines. The percentage of probability mentioned is approximate. Be sure to consult a doctor for the exact dosage of the drug and the type of antibiotic or anti-inflammatory drug."
            print(Treatment)
        elif disease=="Tuberculosis Pulmonary":
            Treatment="Our solution for lung abscess is to see a doctor, take antibiotics and it should be examined and if it is serious, surgery should be done. The percentage of probability mentioned is approximate, be sure to see a doctor for examination"
            print(Treatment)
        elif disease=="Lung abscess":
            Treatment="Our solution is to see a doctor, take antibiotics and it should be examined and if it is serious, surgery should be done. The percentage of probability mentioned is approximate, be sure to see a doctor for examination"
            print(Treatment)
        elif disease=="Asthma":
            Treatment="Our solution for asthma is to use 'Salbutamol spray' first and if it does not get better, use 'Fludrocortisone' corticosteroid spray in the next stage. 'Salmetrol' spray can also be used as an airway dilator\n. The percentage of probability mentioned is approximate, be sure to see a doctor for examination"
            print(Treatment)
        elif disease=="Gastroesophageal reflux":
            Treatment="Our solution for Gastroesophageal reflux is the use of gastric syrups such as aluminum-MGS syrup. The use of omeprazole and if it is very severe, the use of injectable pentaprazole is recommended\n. The percentage of probability mentioned is approximate. Be sure to consult a doctor for examination"
            print(Treatment)
        elif disease=="Contact with chemical particles":
            Treatment="Our recommended solution for cough due to the chemical nature is to rest and that the person no longer comes into contact with the pollutant. The percentage of probability mentioned is approximate. Be sure to consult a doctor for examination"
            print(Treatment)
            
            
    #########################################################3
    elif A == 4:
        print("You have back pain.")
        print("Now I need to know what symptoms you are experiencing. Choose from the following.")
        print("1.Tenderness of the muscles behind the chest\n2.Tenderness of the spine\n3.Pain when walking\n4.Shooting pain from the knee down to the calf\n5.Numbness and weakness\n6.Tenderness of the muscles near the sciatic nerve\n7.Pain worsens with sneezing, coughing, and straining to defecate\n8.Weakness and hyperreflexia in the lower back when bending forward\n9.Pain in the leg after 30 seconds of back extension\n10.Reduced range of motion of the spine\n11.Pain throughout the spine\n12.A dull, deep pain\n13.Local tenderness of the vertebrae\n14.Painful movement of the spine")
        print()
        print("Note: Tenderness means the affected area is tender")
        print()
        associated_symptoms = input("Which of the associated symptoms do you have? You can choose multiple ones, just put , between the numbers.")
        associated_symptoms=set(map(int,associated_symptoms.split(",")))
        
        #Mechanical Back Pain
        if associated_symptoms == {1}:
            console.print(printpercent(11.8, "Mechanical Back Pain"))
            disease="Mechanical Back Pain"
        elif associated_symptoms == {2}:
            console.print(printpercent(17.6, "Mechanical Back Pain"))
            disease="Mechanical Back Pain"
        elif associated_symptoms == {3}:
            console.print(printpercent(23.5, "Mechanical Back Pain"))
            disease="Mechanical Back Pain"
        elif associated_symptoms == {1, 2}:
            console.print(printpercent(29.4, "Mechanical Back Pain"))
            disease="Mechanical Back Pain"
        elif associated_symptoms == {1, 3}:
            console.print(printpercent(35.3, "mechanical low back pain"))
            disease="mechanical low back pain"
        elif associated_symptoms == {2, 3}:
            console.print(printpercent(41.2, "mechanical low back pain"))
            disease="mechanical low back pain"
        elif associated_symptoms == {1, 2, 3}:
            console.print(printpercent(35.3, "mechanical low back pain"))
            disease="mechanical low back pain"
        
        
        #sciatica
        if associated_symptoms == {4}:
            console.print(printpercent(14.3, "sciatica pain"))
            disease="sciatica"
        elif associated_symptoms == {5}:
            console.print(printpercent(21.4, "sciatica pain"))
            disease="sciatica"
        elif associated_symptoms == {6}:
            console.print(printpercent(28.6, "sciatica pain"))
            disease="sciatica"
        elif associated_symptoms == {7}:
            console.print(printpercent(35.7, "sciatica pain"))
            disease="sciatica"
        elif associated_symptoms == {4, 5}:
            console.print(printpercent(35.7, "sciatica pain"))
            disease="sciatica"
        elif associated_symptoms == {4, 6}:
            console.print(printpercent(42.9, "sciatica pain"))
            disease="sciatica"
        elif associated_symptoms == {4, 7}:
            console.print(printpercent(50, "sciatica pain"))
            disease="sciatica"
        elif associated_symptoms == {5, 6}:
            console.print(printpercent(50, "sciatica pain"))
            disease="sciatica"
        elif associated_symptoms == {5, 7}:
            console.print(printpercent(57.1, "sciatica pain"))
            disease="sciatica"
        elif associated_symptoms == {6, 7}:
            console.print(printpercent(64.3, "sciatica pain"))
            disease="sciatica"
        elif associated_symptoms == {4, 5, 6}:
            console.print(printpercent(64.3, "sciatica pain"))
            disease="sciatica"
        elif associated_symptoms == {4, 5, 7}:
            console.print(printpercent(71.4, "sciatica pain"))
            disease="sciatica"
        elif associated_symptoms == {4, 6, 7}:
            console.print(printpercent(78.6, "sciatica pain"))
            disease="sciatica"
        elif associated_symptoms == {5, 6, 7}:
            console.print(printpercent(85.7, "sciatica pain"))
            disease="sciatica"
        
        #lumbar spinal stenosis
        if associated_symptoms == {8}:
            console.print(printpercent(21.4, "sciatica pain"))
            disease="Spinal stenosis"
        elif associated_symptoms == {9}:
            console.print(printpercent(28.6, "Lumbar spinal stenosis"))
            disease="Spinal stenosis"
        elif associated_symptoms == {8, 9}:
            console.print(printpercent(50, "Lumbar spinal stenosis"))
            disease="Spinal stenosis"
        
        #rheumatologic
        if associated_symptoms == {10}:
            console.print(printpercent(23.3, "Chronic pain due to rheumatologic diseases"))
            disease="rheumatologic"
        elif associated_symptoms == {11}:
            console.print(printpercent(26.7, "Chronic pain due to rheumatologic diseases"))
            disease="rheumatologic"
        elif associated_symptoms == {10, 11}:
            console.print(printpercent(50, "Chronic pain due to rheumatologic diseases"))
            disease="rheumatologic"
        
        #Referred back pain
        if associated_symptoms == {12}:
            console.print(printpercent(6.7, "Referred back pain"))
            disease="Referred back pain"
        elif associated_symptoms == {13}:
            console.print(printpercent(10, "Referred back pain"))
            disease="Referred pain from abdomen and back"
        elif associated_symptoms == {14}:
            console.print(printpercent(8, "Referred pain from abdomen and back"))
            disease="Referred pain from abdomen and back"
        elif associated_symptoms == {12, 13}:
            console.print(printpercent(16.7, "Referred pain from abdomen and back"))
            disease="Referred pain from abdomen and back"
        elif associated_symptoms == {12, 14}:
            console.print(printpercent(15, "Referred pain from abdomen and back"))
            disease="Referred pain from abdomen and back"
        elif associated_symptoms == {13, 14}:
            console.print(printpercent(18.3, "Referred pain from abdomen and back"))
            disease="Referred pain from abdomen and back"
        elif associated_symptoms == {12, 13, 14}:
            console.print(printpercent(25, "Pain Referred from the abdomen and back"))
            disease="Referred pain from the abdomen and back"
        
        
        #Treatments
        if disease=="Mechanical back pain":
            Treatment="For mechanical back pain, it is recommended to rest and take painkillers if the pain increases. See a doctor for a detailed diagnosis and treatment."
            print(Treatment)
        elif disease=="Sciatica":
            Treatment="For sciatica, it is recommended to rest and take painkillers. If the pain increases, see a doctor for a detailed diagnosis and treatment, including receiving corticosteroids and evaluating the need for surgery."
            print(Treatment)
        elif disease=="Spinal stenosis":
            Treatment="For spinal stenosis, it is recommended to rest and avoid lifting heavy objects. If the pain increases, see a doctor for a detailed diagnosis and treatment, including receiving corticosteroids and assessing the need for surgery."
            print(Treatment)
        elif disease=="Rheumatologic":
            Treatment="For rheumatologic, it is recommended that you rest and if the pain increases, see a doctor for a detailed diagnosis and treatment, including receiving corticosteroids and assessing the need for surgery."
            print(Treatment)
        elif disease=="Referred pain from the abdomen and back":
            Treatment="For referred pain from the abdomen and back, it is recommended that you see a doctor for treatment of the underlying causes."
            print(Treatment)
        
        
    ###########################################################
    elif A == 5:
        print("You have shortness of breath.")
        # Identify associated symptoms
        print("Choose from the following symptoms.")
        print("(If you have more than one choice, put a comma (,) between the numbers.\nExample: 1,10,11)")
        print("1- Cough\n2- Nighttime shortness of breath\n3- Wheezing (double air exhalation sound from the lungs)\n4- Wheezing\n5- Chest tightness\n6- Mucoid (gelatinous) sputum\n7- Fever\n8- Heart palpitations\n9- Dizziness\n10- Numbness and tingling in the hands and feet\n11- No associated symptoms")
        print()
        Associated_symptoms=input("What symptoms do you have? ")
        Associated_symptoms = set(map(int,Associated_symptoms.split(",")))
        
        # while True : # Shortness of breath / Loop to enter associated symptoms correctly
        #     Associated_symptoms = input("What symptoms do you have? ")
        # try:
        #     Associated_symptoms = set(map(int,Associated_symptoms.split(",")))
        #     break # Stop the second loop/ Stop if the accompanying symptoms data is entered correctly
        # except ValueError :
        #     print()
        #     print("Please observe the following when entering data and enter the data again:\n1- Change your keyboard to English.\n2- Be sure to put commas (,) between numbers.\n3- Do not use the space button.\nExample: 11,10,1")
        
        # Diagnose the patient's underlying conditions
        
        print("Your accompanying symptoms have been recorded.")
        print()
        print (" Now we need to see what underlying conditions have affected your disease. ")
        print()
        print("Choose from the following conditions.")
        print("(If you have more than one choice, put a comma (,) between the numbers.\nExample: 1,7,6)")
        print("1- History of heart disease\n2- Environmental conditions\n3- Smoking history\n4- Pollutant\n5- Variable\n6- Chest pain\n7- No underlying conditions")
        print()
        Predisposing_factors=input("Which underlying conditions do you have? ")
        Predisposing_factors=set(map(int,Predisposing_factors.split(",")))
        # while True : #loop to correctly enter the underlying conditions
        #     Predisposing_factors=input("Which underlying conditions do you have? ")
        # try:
        #     Predisposing_factors=set(map(int,Predisposing_factors.split(",")))
        #     break
        # except ValueError :
        #     print()
        #     print("Please observe the following when entering data and re-enter the data:\n1- Change your keyboard to English.\n2- Be sure to put a comma (,) between the numbers.\n3- Do not use the space button.\nExample: 6,7,1")
        
        # Disease 1 : Heart Failure
        
        # History : Heart Disease
        if Predisposing_factors=={1} and Associated_symptoms=={1}:
            console.print(printpercent(60, "Heart Failure"))
            disease="Heart Failure"
        elif Predisposing_factors=={1} and Associated_symptoms=={2}:
            console.print(printpercent(70, "Heart Failure"))
            disease="Heart Failure"
        elif Predisposing_factors=={1} and Associated_symptoms=={3}:
            console.print(printpercent(50, "Heart Failure"))
            disease="Heart Failure"
        elif Predisposing_factors=={1} and Associated_symptoms=={1,2}:
            console.print(printpercent(80, "Heart Failure"))
            disease="Heart Failure"
        elif Predisposing_factors=={1} and Associated_symptoms=={1,3}:
            console.print(printpercent(65, "Heart Failure"))
            disease="Heart Failure"
        elif Predisposing_factors=={1} and Associated_symptoms=={2,3}:
            console.print(printpercent(75, "Heart Failure"))
            disease="Heart Failure"
        elif Predisposing_factors=={1} and Associated_symptoms=={1,2,3}:
            console.print(printpercent(85, "Heart Failure"))
            disease="Heart Failure"
        elif Predisposing_factors=={1} and Associated_symptoms=={11}:
            console.print(printpercent(10, "Heart Failure"))
            disease="Heart Failure"
        
        # Disease 1 : Heart Failure
        
        # History : No conditions
        
        elif Predisposing_factors=={7} and Associated_symptoms=={1}:
            console.print(printpercent(20, "Heart Failure"))
            disease="Heart Failure"
        elif Predisposing_factors=={7} and Associated_symptoms=={2}:
            console.print(printpercent(25, "Heart Failure"))
            disease="Heart Failure"
        elif Predisposing_factors=={7} and Associated_symptoms=={3}:
            console.print(printpercent(15, "Heart Failure"))
            disease="Heart Failure"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,2}:
            console.print(printpercent(30, "Heart Failure"))
            disease="Heart Failure"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,3}:
            console.print(printpercent(20, "Heart Failure"))
            disease="Heart Failure"
        elif Predisposing_factors=={7} and Associated_symptoms=={2,3}:
            console.print(printpercent(25, "Heart Failure"))
            disease="Heart Failure"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,2,3}:
            console.print(printpercent(30, "Heart Failure"))
            disease="Heart Failure"
        elif Predisposing_factors=={7} and Associated_symptoms=={11}:
            console.print(printpercent(5, "Heart Failure"))
            disease="Heart Failure"
            
        # Disease 2: Asthma

        # History: Environmental Conditions

        if Predisposing_factors=={1} and Associated_symptoms=={1}:
            console.print(printpercent(60, "asthma"))
            disease="asthma"
        elif Predisposing_factors=={1} and Associated_symptoms=={4}:
            console.print(printpercent(75, "asthma"))
            disease="asthma"
        elif Predisposing_factors=={1} and Associated_symptoms=={5}:
            console.print(printpercent(70, "asthma"))
            disease="asthma"
        elif Predisposing_factors=={1} and Associated_symptoms=={1,4}:
            console.print(printpercent(85, "asthma"))
            disease="asthma"
        elif Predisposing_factors=={1} and Associated_symptoms=={1,5}:
            console.print(printpercent(80, "asthma"))
            disease="Asthma"
        elif Predisposing_factors=={1} and Associated_symptoms=={4,5}:
            console.print(printpercent(58, "Asthma"))
            disease="Asthma"
        elif Predisposing_factors=={1} and Associated_symptoms=={1,4,5}:
            console.print(printpercent(90, "Asthma"))
            disease="Asthma"
        elif Predisposing_factors=={1} and Associated_symptoms=={11}:
            console.print(printpercent(30, "Asthma"))
            disease="Asthma"
        
        # Disease 2: Asthma
        
        # History: No conditions
        
        elif Predisposing_factors=={7} and Associated_symptoms=={1}:
            console.print(printpercent(40, "Asthma"))
            disease="Asthma"
        elif Predisposing_factors=={7} and Associated_symptoms=={4}: 
            console.print(printpercent(55, "Asthma"))
            disease="asthma"
        elif Predisposing_factors=={7} and Associated_symptoms=={5}:
             console.print(printpercent(50, "Asthma"))
             disease="asthma"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,4}:
             console.print(printpercent(65, "Asthma"))
             disease="asthma"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,5}:
             console.print(printpercent(60, "asthma"))
             disease="asthma"
        elif Predisposing_factors=={7} and Associated_symptoms=={4,5}:
            console.print(printpercent(65, "Asthma"))
            disease="asthma"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,4,5}:
            console.print(printpercent(70, "Asthma"))
            disease="asthma"
        elif Predisposing_factors=={7} and Associated_symptoms=={11}:
             console.print(printpercent(10, "asthma"))
             disease="asthma"
        
        
        
        
        # Disease 3: COPD
        
        # History: smoking
        
        
        if Predisposing_factors=={3} and Associated_symptoms=={1}:
         console.print(printpercent(70, "COPD"))
         disease="COPD"
        elif Predisposing_factors=={3} and Associated_symptoms=={6}:
         console.print(printpercent(75, "COPD"))
         disease="COPD"
        elif Predisposing_factors=={3} and Associated_symptoms=={1,6}:
         console.print(printpercent(80, "COPD"))
         disease="COPD"
        elif Predisposing_factors=={3} and Associated_symptoms=={11}:
         console.print(printpercent(30, "COPD"))
         disease="COPD"
        
        
        
         # Disease 3: COPD
        
         # History: Pollutant
        
        
        elif Predisposing_factors=={4} and Associated_symptoms=={1}:
         console.print(printpercent(65, "COPD"))
         disease="COPD"
        elif Predisposing_factors=={4} and Associated_symptoms=={6}:
         console.print(printpercent(70, "COPD"))
         disease="COPD"
        elif Predisposing_factors=={4} and Associated_symptoms=={1,6}:
         console.print(printpercent(75, "COPD"))
         disease="COPD"
        elif Predisposing_factors=={4} and Associated_symptoms=={11}:
         console.print(printpercent(25, "COPD"))
         disease="COPD"
        
        # Disease 3 : COPD

        # History : No conditions
            
        elif Predisposing_factors=={7} and Associated_symptoms=={1}:
            console.print(printpercent(60, "COPD"))
            disease="COPD"
        elif Predisposing_factors=={7} and Associated_symptoms=={6}:
            console.print(printpercent(65, "COPD"))
            disease="COPD"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,6}:
            console.print(printpercent(70, "COPD"))
            disease="COPD"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,6}:
            console.print(printpercent(70, "COPD"))
            disease="COPD"
        elif Predisposing_factors=={7} and Associated_symptoms=={11}:
            console.print(printpercent(20, "COPD"))
            disease="COPD"
            
        # Disease 3 : COPD
            
        # History : Smoking and pollutants
            
        elif Predisposing_factors=={3,4} and Associated_symptoms=={1}:
            console.print(printpercent(75, "COPD"))
            disease="COPD"
        elif Predisposing_factors=={3,4} and Associated_symptoms=={6}:
            console.print(printpercent(80, "COPD"))
            disease="COPD"
        elif Predisposing_factors=={3,4} and Associated_symptoms=={1,6}:
            console.print(printpercent(85, "COPD"))
            disease="COPD"
        elif Predisposing_factors=={3,4} and Associated_symptoms=={11}:
            console.print(printpercent(35, "COPD"))
            disease="COPD"
        
        # Disease 4 : Lung Infection (Pneumonia)
            
        # History : Variable Conditions
            
        if Predisposing_factors=={5} and Associated_symptoms=={1}:
            console.print(printpercent(70, "Lung Infection"))
            disease="Lung Infection"
        elif Predisposing_factors=={5} and Associated_symptoms=={6}:
            console.print(printpercent(75, "Lung Infection"))
            disease="Lung Infection"
        elif Predisposing_factors=={5} and Associated_symptoms=={7}:
            console.print(printpercent(70, "Lung Infection"))
            disease="Lung Infection"
        elif Predisposing_factors=={5} and Associated_symptoms=={1,6}:
            console.print(printpercent(80, "Lung Infection"))
            disease="Lung Infection"
        elif Predisposing_factors=={5} and Associated_symptoms=={1,7}:
            console.print(printpercent(75, "Lung Infection"))
            disease="Lung Infection"
        elif Predisposing_factors=={5} and Associated_symptoms=={6,7}:
            console.print(printpercent(75, "Lung Infection"))
            disease="Lung Infection"
        elif Predisposing_factors=={5} and Associated_symptoms=={1,6,7}:
            console.print(printpercent(85, "Lung Infection"))
            disease="Lung Infection"
        elif Predisposing_factors=={5} and Associated_symptoms=={11}:
            console.print(printpercent(40, "Lung Infection"))
            disease="Lung Infection"
            
        # Disease 4: Lung Infection (Pneumonia)
            
        # History: No conditions
            
        elif Predisposing_factors=={7} and Associated_symptoms=={1}:
            console.print(printpercent(60, "Lung Infection"))
            disease="Lung Infection"
        elif Predisposing_factors=={7} and Associated_symptoms=={6}:
            console.print(printpercent(65, "Lung Infection"))
            disease="Lung Infection"
        elif Predisposing_factors=={7} and Associated_symptoms=={7}:
            console.print(printpercent(60, "Lung Infection"))
            disease="Lung Infection"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,6}:
            console.print(printpercent(70, "Lung Infection"))
            disease="Lung Infection"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,7}:
            console.print(printpercent(65, "Lung Infection"))
            disease="Lung Infection"
        elif Predisposing_factors=={7} and Associated_symptoms=={6,7}:
            console.print(printpercent(65, "Lung Infection"))
            disease="Lung Infection"
        elif Predisposing_factors=={7} and Associated_symptoms=={1,6,7}:
            console.print(printpercent(75, "Lung Infection"))
            disease="Lung Infection"
        elif Predisposing_factors=={7} and Associated_symptoms=={11}:
            console.print(printpercent(20, "Lung Infection"))
            disease="Lung Infection"
        
        # Disease 5: Associated anxiety (hyperventilation)

        # History: Chest pain
            
        if Predisposing_factors=={6} and Associated_symptoms=={8}:
            console.print(printpercent(75, "Associated anxiety or hyperventilation"))
            disease="Associated anxiety or hyperventilation"
        elif Predisposing_factors=={6} and Associated_symptoms=={9}:
            console.print(printpercent(80, "Associated anxiety or hyperventilation"))
            disease="Associated anxiety or hyperventilation"
        elif Predisposing_factors=={6} and Associated_symptoms=={10}:
            console.print(printpercent(75, "Associated anxiety or hyperventilation"))
            disease="Associated anxiety or hyperventilation"
        elif Predisposing_factors=={6} and Associated_symptoms=={8,9}:
            console.print(printpercent(85, "Anxiety associated or hyperventilation"))
            disease="Associated anxiety or hyperventilation"
        elif Predisposing_factors=={6} and Associated_symptoms=={8,10}:
            console.print(printpercent(80, "Associated anxiety or hyperventilation"))
            disease="Associated anxiety or hyperventilation"
        elif Predisposing_factors=={6} and Associated_symptoms=={9,10}:
            console.print(printpercent(85, "Associated anxiety or hyperventilation"))
            disease="Associated anxiety or hyperventilation"
        elif Predisposing_factors=={6} and Associated_symptoms=={8,9,10}:
            console.print(printpercent(90, "Associated anxiety or hyperventilation"))
            disease="Associated anxiety or hyperventilation"
        elif Predisposing_factors=={6} and Associated_symptoms=={11}:
            console.print(printpercent(50, "Associated anxiety or hyperventilation"))
            disease="Associated anxiety or hyperventilation"
            
        # Disease 5 : Associated anxiety (hyperventilation)
            
        # History : No conditions
            
        elif Predisposing_factors=={7} and Associated_symptoms=={8}:
            console.print(printpercent(55, "Associated anxiety or hyperventilation"))
            disease="Associated anxiety or hyperventilation"
        elif Predisposing_factors=={7} and Associated_symptoms=={9}:
            console.print(printpercent(60, "Associated anxiety or hyperventilation"))
            disease="Associated anxiety or hyperventilation"
        elif Predisposing_factors=={7} and Associated_symptoms=={10}:
            console.print(printpercent(55, "Associated anxiety or hyperventilation"))
            disease="Associated anxiety or hyperventilation"
        elif Predisposing_factors=={7} and Associated_symptoms=={8,9}:
            console.print(printpercent(65, "Combined anxiety or hyperventilation"))
            disease="Combined anxiety or hyperventilation"
        elif Predisposing_factors=={7} and Associated_symptoms=={8,10}:
            console.print(printpercent(60, "Combined anxiety or hyperventilation"))
            disease="Combined anxiety or hyperventilation"
        elif Predisposing_factors=={7} and Associated_symptoms=={9,10}:
            console.print(printpercent(65, "Combined anxiety or hyperventilation"))
            disease="Combined anxiety or hyperventilation"
        elif Predisposing_factors=={7} and Associated_symptoms=={8,9,10}:
            console.print(printpercent(70, "Combined anxiety or hyperventilation"))
            disease="Combined anxiety or hyperventilation"
        elif Predisposing_factors=={7} and Associated_symptoms=={11}:
            console.print(printpercent(30, "Anxiety or Hyperventilation"))
            disease="Anxiety or Hyperventilation"
        else:
            print("Sorry, the information in this program does not currently support this disease. The program is being completed.")
            
        #Treatment of diseases
        if disease=="Heart failure":
            Treatment="Recommended treatment for heart failure: \n1- You can use beta-blocker drugs such as 'propranolol'.\n2- You can also use diuretics."
            print(Treatment)
        elif disease=="Asthma":
            Treatment="Recommended treatment: \n1- Use 'Salbutamol spray' first.\n2- If there is no improvement, you can use 'Fludrocortisone spray'.\n3- You can also use 'Salmeterol spray' as an airway dilator."
            print(Treatment)
        elif disease=="COPD":
            Treatment="Recommended treatment for COPD:\n1- If you are a smoker, quit smoking.\n2- You can use airway dilators or asthma medications such as Atrovent."
            print(Treatment)
        elif disease=="Lung infection":
            Treatment="Recommended treatment for lung infection:\n1- If the infection is bacterial, you can use 'Antibiotics'.\n2- If the infection is viral, you can use 'Antivirals'."
            print(Treatment)
        elif disease=="Comorbid anxiety or hyperventilation":
            Treatment="Suggested treatment for comorbid anxiety or hyperventilation: \n1- See a psychiatrist.\n2- Get some rest."
            print(Treatment)
        
        
        
        # Get the form

        Question=int(input("Do you want to get the form?\n1- Yes\n2- No\n"))
        
        if Question==1:
            print()
            print(f"Name : {Name}")
            print(f"Family_name : {Family_name}")
            print(f"Age : {Age}")
            print(f"Gender : {Gender}")
            Title="Patient's history : "
            print(Title + disease)
            Title_2="Treatment recommendation : "
            print(Title_2 + Treatment )
        else:
            print()
            print("No form was issued.")
        
        print("\nThis is only for the initial diagnosis of the disease, please see a doctor for an accurate diagnosis and additional tests and take medication after consulting a doctor.\nThank you\nSaris Programming Group")
        #End 403/10/18   3:15 a.m