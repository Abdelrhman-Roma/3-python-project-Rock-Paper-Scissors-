import random  # استيراد مكتبة random لاختيار حركة الكمبيوتر بشكل عشوائي
rock_paper_scissors = ["rock","paper","scissors"]  # قائمة بالحركات الممكنة

def rock_paper_scissors_game():  # تعريف دالة اللعبة
    user_wins = 0  # عداد نقاط اللاعب
    computer_wins = 0  # عداد نقاط الكمبيوتر
    best_of = 0  # عدد الجولات التي سيتم اللعب عليها
    print("Rock PAPER SCISSORS GAME".center(50,"-"))  # طباعة عنوان اللعبة بشكل جميل
    want_to_play = input("do you want to play!! (yes or no): ").lower().strip()  # سؤال اللاعب إذا يريد اللعب
    if want_to_play == 'no':  # إذا اللاعب اختار لا
        print("thanks!")  # شكر اللاعب
        return  # إنهاء الدالة
    else:
        user_name = input("please enter your name: ").capitalize()  # إدخال اسم اللاعب وتحويله لحرف أول كبير
        best_of = int(input("do you want play best of (3,5,7,9)"))  # اختيار عدد الجولات بصيغة best of
        winning_score = best_of // 2 +1  # تحديد النقاط اللازمة للفوز (النصف + 1)
        print("Welcome to the game")  # رسالة ترحيبية
        while True:  # حلقة اللعب المستمرة حتى يصل أحد للفوز
              user_chose = input("please chose rock , paper or scissors: ").lower().strip()  # إدخال حركة اللاعب
              if user_chose not in rock_paper_scissors:  # التحقق من صحة إدخال اللاعب
                   print("Invalid choice, try again.")  # رسالة خطأ إذا كانت الحركة غير صحيحة
                   continue  # العودة لبدء الجولة مرة أخرى
              computer_chose = random.choice(rock_paper_scissors)  # اختيار حركة الكمبيوتر بشكل عشوائي
              winning_case = {'rock' : 'scissors',  # حالات الفوز لللاعب
                              'paper':'rock',
                              'scissors':'paper'}
              if user_chose == computer_chose:  # إذا كانت حركة اللاعب والكمبيوتر متساوية
                   print(f"{user_chose} VS {computer_chose}")  # طباعة النتيجة
                   print("Draw".center(20,'-'))  # إعلان التعادل

              elif winning_case[user_chose] == computer_chose:  # إذا فاز اللاعب على الكمبيوتر
                    print(f"{user_chose} VS {computer_chose}")  # طباعة النتيجة
                    print("you win")  # إعلان فوز اللاعب
                    user_wins += 1  # زيادة نقاط اللاعب
                    if user_wins == winning_score or computer_wins == winning_score:  # التحقق إذا وصل أحد للفوز
                        break  # الخروج من حلقة اللعب
              else:  # إذا فاز الكمبيوتر
                    print(f"{user_chose} VS {computer_chose}")  # طباعة النتيجة
                    print("computer Win")  # إعلان فوز الكمبيوتر
                    computer_wins +=1  # زيادة نقاط الكمبيوتر
                    if user_wins == winning_score or computer_wins == winning_score:  # التحقق إذا وصل أحد للفوز
                        break  # الخروج من حلقة اللعب
              
        # بعد انتهاء اللعبة
        print("thanks To play")  # شكر اللاعب
        print(f"Current score -> {user_name}: {user_wins} | Computer: {computer_wins}".center(50,'-'))  # طباعة النتيجة النهائية
        if user_wins > computer_wins:  # إذا فاز اللاعب
                  print(f"{user_name} Win".center(50,'-'))  # إعلان فوز اللاعب
        elif user_wins < computer_wins:  # إذا فاز الكمبيوتر
                  print(f"Computer Win".center(50,'-'))  # إعلان فوز الكمبيوتر
        else:  # إذا كانت النتيجة تعادل
                  print("It's a Tie!!".center(50,'-'))  # إعلان التعادل
        want_to_play = input("do you want to play again!! (yes or no): ").lower().strip()  # سؤال اللاعب إذا يريد اللعب مرة أخرى
        if want_to_play == 'yes':  # إذا نعم
              rock_paper_scissors_game()  # إعادة تشغيل اللعبة
        else:  # إذا لا
              print("thanks to play")  # شكر اللاعب
              quit()  # إنهاء البرنامج
              
rock_paper_scissors_game()  # استدعاء دالة اللعبة لتبدأ
