#there is 56 tokens in this paragraph
text = "تقديم المكافات المادية و المعنوية ل الاطفال المتفوقين فذلك يساعد على تعزيز و رفع روح المنافسة بين الطلاب كما يدفع الطالب ل بذل جهد مضاعف ل الحصول على المكافئة تخصيص حصة في الاسبوع ل عرض فيلم كرتوني خاص ب تعليم القراءة و الكتابة فهناك العديد من البرامج المتخصصة في انتاج افلام كرتونية ل تطوير المهارات العقلية"
tokens = text.split()
def processing(par):
    particles =["من","الى","عن","على","في","ب","ت","ل","ك","ف","و","ثم","بل","لا","لكن","حتى","او","ام","ان","لن","كي","حتى","لم","لما","لا","ل","ان","كان","لكن","ليت","لعل","كي","ما","لو","يا","ايا","هيا","اي","اجل","بلى","نعم","لا","هل"]
    for k in particles:
        if k == par:
            return "حرف"
    try:
        for i in par:
            #احرف المضارعة ناتي او تاتي
            if par[0]=="ي":
                return "فعل"
            elif par[0]=="ت":
                return "فعل"
            elif par[0]=="ن":
                return "فعل"
            #----------------------------------------------
            #تفعيلة عامة اي كلمة تبدا ب ال التعريف تكون اسم
            elif par[0]=="ا" and par[1]=="ل":
                 return "اسم"
             #اذا كانت الكلمة على وزن افعال
            elif par[0]=="ا" and par[3]=="ا":
                tagging.append("اسم")
            #اسم على وزن تفعيل
            elif par[0]=="ت" and par[3]=="ي":
                 return "اسم"
             #اسم على وزن افعال
            elif par[0]=="ا" and par[3]=="ل":
                 return "اسم"
            #اي اسم ينتهي ب ة
            elif par[len(par)-1]=="ة":
                return "اسم"
            #كلمة على وزن فاعل
            elif par[1]=="ا":
                return "ااسم"
            #كلمة على وزن مفعول
            elif par[0]=="م" and par[3]=="و":
                return "ااسم"
            #كلمة على وزن مفعال
            elif par[0]=="م" and par[3]=="ا":
                return "اسم"
            #كلمة على وزن انفعال
            elif par[0]=="ا" and par[1]=="ن" and par[4]=="ا":
                return "اسم"
            #كلمة على وزن استفعال
            elif par[0]=="" and par[1]=="" and par[2]=="" and par[5]=="ا":
                return "اسم"
            #وزن افعلال
            elif par[0]=="ا" and par[4]=="ا" and par[5]=="ل":
                return "اسم"
            #على وزن مفاعلات
            elif par[0]=="م" and par[2]=="ا" and par[4]=="ل" and par[5]=="ا" and par[6]=="ت" :
                  return "اسم"
            #------------------------------------------------
            else:
               return "اسم"
    except:
        return "اسم"
tagging = []
for i in tokens:
    tagging.append(processing(i))
print("-----------------------------------") 
#this for loop is to print word vs tag 
print("N","\t","Tag","\t \t \t","Word")
for i in range(len(tokens)):
    print(i,"\t",tokens[i],"\t \t \t",tagging[i])
# print("-----------------------------------")  
