from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# ضبط لون خلفية التطبيق ليكون مريحاً للعين
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class CalculatorApp(App):
    def build(self):
        self.title = "الحاسبة الذكية"
        
        # تخطيط الشاشة الرئيسي
        root_layout = BoxLayout(orientation='vertical', padding=15, spacing=15)
        
        # حقل إدخال وعرض النتيجة
        self.solution = TextInput(
            text="0", 
            readonly=True, 
            font_size=50, 
            halign="right", 
            valign="middle",
            background_color=(0.15, 0.15, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            size_hint=(1, 0.25)
        )
        root_layout.add_widget(self.solution)
        
        # صفوف الأزرار للآلة الحاسبة
        buttons = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['.', '0', 'DEL', '=']
        ]
        
        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(
                    text=label,
                    font_size=28,
                    background_color=(0.2, 0.6, 0.8, 1) if label not in ['C', 'DEL', '='] else (0.8, 0.3, 0.2, 1),
                    color=(1, 1, 1, 1)
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            root_layout.add_widget(h_layout)
            
        return root_layout

    def on_button_press(self, instance):
        current_text = self.solution.text
        text = instance.text
        
        if text == 'C':
            self.solution.text = "0"
        elif text == 'DEL':
            if len(current_text) > 1:
                self.solution.text = current_text[:-1]
            else:
                self.solution.text = "0"
        elif text == '=':
            try:
                # حساب النتيجة بأمان
                response = str(eval(current_text))
                self.solution.text = response
            except Exception:
                self.solution.text = "خطأ"
        else:
            if current_text == "0" or current_text == "خطأ":
                self.solution.text = text
            else:
                self.solution.text += text

if __name__ == '__main__':
    CalculatorApp().run()
