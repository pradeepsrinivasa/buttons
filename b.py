# Importing required libraries
from kivy.app import App
from kivy.uix.button import Button

# Define the App class
class MyButtonApp(App):
    
    # Define the build method
    def build(self):
        # Creating a button
        button = Button(text='Click Me!', size_hint=(None, None), size=(200, 50), pos=(300, 250))
        
        # Binding a function to the button's on_press event
        button.bind(on_press=self.on_button_click)
        
        # Return the button as the root widget of the application
        return button
    
    # Function to be called when the button is clicked
    def on_button_click(self, instance):
        print('Button clicked!')

# Run the application
if __name__ == '__main__':
    MyButtonApp().run()
