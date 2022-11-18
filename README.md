About:
I made pos tagger to classify words in the text to Noun ,Verb ,Particle using -tafeila- of word , I used 2 test corpuses and i try the efficiency of the algorithm , I used 2 Golden corpuses written by expert of Arabic language to calculate the accuracy of the algorithm and it shows as follow:
First test corpus gives accuracy for around 90% because I made rules based on first corpus.

Approach:
I separated words in the text using split() method in python , I will explain why I used it in GUI paragraph
I made algorithm using rule based approach based on - tafela- of word :
1-وضعت قائمة تحتوي على جميع احرف اللغة العربية ولان الاحرف تاتي في النص كما هي دون زيادات فقد طابقت بين كلمة النص وبين القائمة التي تحتوي على احرف اللغة العربية واذا تم التطابق يقوم البرنامج باعطاء الكلمة حرف.
2-وضعت 12 تفعيلة للاسم وهما بداية اذا بدات الكلمة ب ال فانها تكون اسم او اذا كانت على الاوزان التالية أفعال ,تفعيل ,فاعل ,مفعول ,مفعال ,انفعال, استفعال , افعلال , مفاعلات او اذا انتهت الكلمة بتاء مربوطة.
3-اما الأفعال فقد وضعت لها قاعدة انها اذا بدات بأحد احرف المضارعة -ناتي- او -تاتي- فانها تكون فعل.
4-اذا ما استطاع البرنامج التمييز حسب ما تم ذكره سابقا فانه يقوم باعطاء الكلمة نوع اسم لان غالبية الكلام في النص يكون من نوع أسماء.
