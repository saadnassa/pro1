from kivymd.app import MDApp                # kivyاستدعاء واجهة المستخدم من مكتبة 
from kivy.lang import Builder               # داخل ملف بايثون ky خاصية من أجل كتابة كود 
from kivy.core.window import Window         #التحكم في خصائص النافذة مثل الحجم ومواقعها  
from kivy.uix.screenmanager import Screen, ScreenManager    #إدارة شاشات التطبيق
Window.size = (400, 600)                                    # تحديد حجم النافذة
Window.borderless = True                                    #إظهار وإخفاء شريط التحكم بالنافذة
import math
####################################################################################################

kv = '''                           # Kv بداية كود 
ScreenManager:                     # العنصر الأساسي الذي يحتوى على النوافذ المختلفة 
    FirstScreen:                   # النافذة الأولى التي تظهر عند بدء التطبيق    
    secondScreen:
<FirstScreen>:                     # تعريف النافذة لتصبح جاهزة لعرض المكونات الداخلية
    name: 'FirstScreen'            # اسم النافذة خلي بالك هنستخدموا الاسم ده في الكود بعدين
#####################################################################################################
    MDFloatLayout:                 # حاوية عناصر واجهة المستخدم مع تحديد مكانها بشكل حر 
        Image:                                             # إدراج صورة كخلفية للنافذة
            source: 'image22.webp'                          # ضع اسم ملف الصورة هنا
            keep_ratio: False                              # تمديد أبعاد الصورة مع حجم النافذة
            allow_stretch: True
#######################################################################################################
        Image:                                             # LOGO إدراج صورة على النافذة 
            source: 'logo.png'                             # ضع اسم ملف الصورة هنا
            size_hint: (0.28, 0.28)                        # تحديد حجم الصورة الطول والعرض
            pos_hint: {"center_x": 0.5, "center_y": 0.86}  # تحديد موقع الصورة على النافذة 
########################################################################################################
        MDLabel:                                           # Label إدراج أداة العنوان 
            text:"Welcome to My Application"               # النص الظاهر على أداة العنوان
            halign:"center"                                # محازاة النص داخل أداة العنوان 
            font_style:"H5"                                # حجم النص
            theme_text_color:"Custom"                      # لون النص
            text_color: 1, 1, 1, 1                         # لون النص
            font_name:"PermanentMarker-Regular.ttf"        # اسـم الخط
            pos_hint: {"center_x": 0.5, "center_y": 0.74}  # تحديد موقع أداة العنوان على النافذة
##################################### السابقة Label نفس أداة ##########################################
        MDLabel:
            text:"Dr.saad nassar"
            halign:"center"
            font_style:"H6"
            theme_text_color:"Custom"
            text_color:1, 1, 0, 1
            pos_hint:{"center_x": 0.5, "center_y": 0.70}
            font_name:"EduAUVICWANTGuides-VariableFont_wght.ttf"
#########################################################################################################
        MDTextField:                                  # MDTextField  إدراج أداة الإدخال   
            id: radius                                # اسم أداة الإدخال وخلي بالك هنستخدمه في الكود بعد شوية
            mode: "round"                         # (round-rectangle-fill-line)وضع أو شكل أداة الإدخال
            hint_text: "Enter the radius"             # النص الظاهر على أداة الإدخال 
            helper_text: "Input radius of the circle" # النص الإرشادي لصندوق الإدخال
            helper_text_mode: "on_focus"              # وضع ظهور النص الإرشادي
            pos_hint: {"center_x": 0.5, "center_y": 0.58} # تحديد موقع أداة الإدخال  على النافذة
            size_hint_x: 0.8                              # حجم أداة الإدخال 
###########################################################################################################
        MDRaisedButton:                                   # زر إستدعاء دالة حساب مساحة الدائرة
            text: "Calculate Area"                        # النص الظاهر على الزر
            font_name: "COOPBL.TTF"                       # نوع الخط
            pos_hint: {"center_x": 0.5, "center_y": 0.48} # تحديد موقع الزر على النافذة
            on_release:app.calculate_area()               # حدث النقر للزر لتنفيذ دالة حساب مساحة الدائرة
#############################################################################################################
                                                               # زر لإغلاق التطبيق مع الأيقونة
        MDIconButton:
            icon: "close"                                      # تحديد أيقونة الزر
            size_hint_x: 0.20                                  # تحديد حجم الزر
            on_release: app.stop()                             # حدث النقر للزر لإستدعاء دالة إغلاق التطبيق
            pos_hint: {"center_x": 0.94, "center_y": 0.966}    # تحديد موقع الزر على النافذة
            
###############################################################################################################               
                    # أداة العنوان لعرض نتيجة حساب مساحة الدائرة عليها
        MDLabel:                                  
            id:area_label                                #اسم أداة العنوان وخلي بالك هنستخدموا في الكود بعد شوية
            text: "Area will be shown here"              # النص الظاهر على أداة العنوان
            halign: "center"                             # محازاة النص داخل أداة العنوان
            theme_text_color: "Custom"                   # لون النص
            text_color: 1, 1, 1          
            font_name: "COOPBL.TTF"                       # نوع الخط
            pos_hint: {"center_x": 0.5, "center_y": 0.40} # تحديد موقع أداة العنوان على النافذة
###############################################################################################################           
        MDRaisedButton:
            text: "Next"
            font_name: "COOPBL.TTF"
            pos_hint: {"center_x": 0.5, "center_y": 0.05}
            size_hint_x: 0.8
            md_bg_color: 1, 0, 0, 0.40
            on_release:
                app.root.current="secondScreen"
                root.manager.transition.direction = 'left'
###############################################################################################################
            
<secondScreen>: 
    name: 'secondScreen'
    MDFloatLayout:
        Image:                                             # إدراج صورة كخلفية للنافذة
            source: 'image22.webp'                          # ضع اسم ملف الصورة هنا
            keep_ratio: False                              # تمديد أبعاد الصورة مع حجم النافذة
            allow_stretch: True
#######################################################################################################
        Image:                                             # LOGO إدراج صورة على النافذة 
            source: 'logo2.png'                             # ضع اسم ملف الصورة هنا
            size_hint: (0.28, 0.28)                        # تحديد حجم الصورة الطول والعرض
            pos_hint: {"center_x": 0.5, "center_y": 0.86}  # تحديد موقع الصورة على النافذة 
########################################################################################################
        MDLabel:                                           # Label إدراج أداة العنوان 
            text:"Welcome to My Application"               # النص الظاهر على أداة العنوان
            halign:"center"                                # محازاة النص داخل أداة العنوان 
            font_style:"H5"                                # حجم النص
            theme_text_color:"Custom"                      # لون النص
            text_color: 1, 1, 1, 1                         # لون النص
            font_name:"PermanentMarker-Regular.ttf"        # اسـم الخط
            pos_hint: {"center_x": 0.5, "center_y": 0.74}  # تحديد موقع أداة العنوان على النافذة
        MDLabel:
            text:"Dr.saad nassar"
            halign:"center"
            font_style:"H6"
            theme_text_color:"Custom"
            text_color:1, 1, 0, 1
            pos_hint:{"center_x": 0.5, "center_y": 0.70}
            font_name:"EduAUVICWANTGuides-VariableFont_wght.ttf"
        MDTextField:
            id: side_a
            hint_text: "Enter side A"
            pos_hint: {"center_x": 0.5, "center_y": 0.62}
            size_hint_x: 0.8
            mode: "rectangle"

        MDTextField:
            id: side_b
            hint_text: "Enter side B"
            pos_hint: {"center_x": 0.5, "center_y": 0.52}
            size_hint_x: 0.8
            mode: "rectangle"

        MDTextField:
            id: side_c
            hint_text: "Enter side C"
            pos_hint: {"center_x": 0.5, "center_y": 0.42}
            size_hint_x: 0.8
            mode: "rectangle"

        MDRaisedButton:
            text: "Calculate Area"
            font_name: "COOPBL.TTF"
            pos_hint: {"center_x": 0.5, "center_y": 0.25}
            on_release: app.calculate_triangle()
          # أداة العنوان لعرض نتيجة حساب مساحة الدائرة عليها
        MDLabel:                                  
            id:result_label                                #اسم أداة العنوان وخلي بالك هنستخدموا في الكود بعد شوية
            text: "Area will be shown here"              # النص الظاهر على أداة العنوان
            halign: "center"                             # محازاة النص داخل أداة العنوان
            theme_text_color: "Custom"                   # لون النص
            text_color: 1, 1, 1          
            font_name: "COOPBL.TTF"                       # نوع الخط
            pos_hint: {"center_x": 0.5, "center_y": 0.15} # تحديد موقع أداة العنوان على النافذة 
        MDRaisedButton:
            text: "Back"
            font_name: "COOPBL.TTF"
            pos_hint: {"center_x": 0.5, "center_y": 0.05}
            size_hint_x: 0.8
            md_bg_color: 1, 0, 0, 0.40
            on_release:
                app.root.current="FirstScreen"
                root.manager.transition.direction = 'right' 

                                                                            # زر لإغلاق التطبيق مع الأيقونة
        MDIconButton:
            icon: "close.png"                                      # تحديد أيقونة الزر
            size_hint_x: 0.30                                  # تحديد حجم الزر
            on_release: app.stop()                             # حدث النقر للزر لإستدعاء دالة إغلاق التطبيق
            pos_hint: {"center_x": 0.94, "center_y": 0.966}    # تحديد موقع الزر على النافذة
                    
'''
###################################################################################################################

class FirstScreen(Screen):
    pass
class secondScreen(Screen):
    pass

class MyApp(MDApp):
    def build(self):
        self.title = 'My KivyMD App'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(kv)
###############################دالة حساب مساحة الدائرة############################################
    def calculate_area(self):
        try:                             # بداية جملة اكتشاف الأخطاء 
            r = float(self.root.get_screen('FirstScreen').ids.radius.text)      # r تخصيص القيمة المدخلة في صندوق لنص لمتغير نصف القطر 
            area = 3.14 * r * r          # معادلة حساب مساحة الدائرة
            self.root.get_screen('FirstScreen').ids.area_label.text = f"{area:.2f}" # area_labelالعنوان المسماه بـ text للخاصية  area تعين قيمة ناتج حساب مساحة الدائرة 
        except ValueError:               # الجزء الثاني من جملة إكتشاف الأخطاء
            self.root.get_screen('FirstScreen').ids.area_label.text = "Invalid input! Please enter a number." #  النص الذي يظهر على أداة العنوان عند حدوث الخطأ
######################################################################################################
    def calculate_triangle(self):
        # جلب قيمة الأطوال
        try:
            side_a = float(self.root.get_screen('secondScreen').ids.side_a.text)
            side_b = float(self.root.get_screen('secondScreen').ids.side_b.text)
            side_c = float(self.root.get_screen('secondScreen').ids.side_c.text)

            # حساب المحيط
            perimeter = side_a + side_b + side_c

            # حساب المساحة باستخدام صيغة هيرون
            s = perimeter / 2
            area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))

            
            # عرض النتائج
            result_text = f"perimeter:{perimeter:.2f}\nArea: {area:.2f}"
            self.root.get_screen('secondScreen').ids.result_label.text = result_text
        except ValueError:
            self.root.get_screen('secondScreen').ids.result_label.text = "Invalid input! Please enter a number."

######################################################################################################
MyApp().run()                            # أمر تشغيل وعرض التطبيق

