from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.video import Video
from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class AnatomyApp(App):
    def build(self):
        # Create a screen manager
        self.sm = ScreenManager()

        # Create the main screen
        main_screen = Screen(name='main')
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Welcome to the Heart Anatomy App!')
        heart_button = Button(text='Start Learning', on_release=self.show_heart_picture)
        layout.add_widget(label)
        layout.add_widget(heart_button)
        main_screen.add_widget(layout)

        # Create the heart image screen
        heart_image_screen = Screen(name='heart_image')
        heart_image_layout = BoxLayout(orientation='vertical')
        self.heart_image = Image(source='C:\\Users\\fptsh\\Downloads\\humanheart.png', size_hint=(None, None), size=(500, 500))
        self.heart_image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        heart_image_layout.add_widget(self.heart_image)

        # Add buttons to return to the main screen or show the heart anatomy
        back_button_heart = Button(text='Back to Main', on_release=self.go_back_to_main)
        next_button_bones = Button(text='Explore', on_release=self.show_heart_anatomy_png)
        self.heart_anatomy_picture = Image(source='C:\\Users\\fptsh\\Downloads\\heartanatomy.png', size_hint=(None, None), size=(500, 500))
        button_layout_heart = BoxLayout(orientation='horizontal')
        button_layout_heart.add_widget(back_button_heart)
        button_layout_heart.add_widget(next_button_bones)
        heart_image_layout.add_widget(button_layout_heart)
        heart_image_screen.add_widget(heart_image_layout)

        # Create the heart anatomy image screen
        heart_anatomy_png_screen = Screen(name='heart_anatomy_png')
        heart_anatomy_png_layout = BoxLayout(orientation='vertical')
        heart_anatomy_png_image = Image(source='C:\\Users\\fptsh\\Downloads\\heartanatomy.png', size_hint=(None, None), size=(500, 500))
        heart_anatomy_png_image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        back_button_heart_anatomy_png = Button(text='Back to Previous', on_release=self.go_back_to_heart_image)
        learn_button_heart_anatomy = Button(text='Learn', on_release=self.learn_heart_anatomy)
        heart_anatomy_png_layout.add_widget(heart_anatomy_png_image)
        heart_anatomy_png_layout.add_widget(back_button_heart_anatomy_png)
        heart_anatomy_png_layout.add_widget(learn_button_heart_anatomy)
        heart_anatomy_png_screen.add_widget(heart_anatomy_png_layout)

        # Create the learn screen
        learn_screen = Screen(name='learn')
        learn_layout = BoxLayout(orientation='vertical')
        learn_label = Label(text='Heart Anatomy')
        learn_layout.add_widget(learn_label)
        heart_chamber_button = Button(text='Chambers', on_release=self.show_heart_chamber)
        learn_layout.add_widget(heart_chamber_button)
        heart_valve_button = Button(text='Valves', on_release=self.show_heart_valve)
        learn_layout.add_widget(heart_valve_button)
        heart_septum_button = Button(text='Septums', on_release=self.show_heart_septum)
        learn_layout.add_widget(heart_septum_button)
        heart_vessels = Button(text='Vessels', on_release=self.show_heart_vessels)
        learn_layout.add_widget(heart_vessels)
        learn_screen.add_widget(learn_layout)
        back_button_learn = Button(text='Back to Previous', on_release=self.go_back_to_heart_anatomy_png)
        learn_layout.add_widget(back_button_learn)

        #Create a new screen for Heart Chambers
        heart_chamber_screen = Screen(name='heart_chamber')
        heart_chamber_layout = BoxLayout(orientation='vertical')
        heart_chamber_label = Label(text='Heart Chambers')
        heart_chamber_layout.add_widget(heart_chamber_label)
        heart_chamber_screen.add_widget(heart_chamber_layout)
        right_atrium_button = Button(text='Right Atrium', on_release=self.show_right_atrium)
        heart_chamber_layout.add_widget(right_atrium_button)
        left_atrium_button = Button(text='Left Atrium', on_release=self.show_left_atrium)
        heart_chamber_layout.add_widget(left_atrium_button)
        right_ventricle_button = Button(text='Right Ventricle', on_release=self.show_right_ventricle)
        heart_chamber_layout.add_widget(right_ventricle_button)
        left_ventricle_button = Button(text='Left Ventricle', on_release=self.show_left_ventricle)
        heart_chamber_layout.add_widget(left_ventricle_button)
        back_to_learn_button = Button(text='Back to Learn', on_release=self.go_to_learn_screen)
        heart_chamber_layout.add_widget(back_to_learn_button)


        #Create a new screen for Heart Valves
        heart_valves_screen = Screen(name='heart_valves')
        heart_valves_layout = BoxLayout(orientation='vertical')
        heart_valves_label = Label(text='Heart Valves')
        heart_valves_screen.add_widget(heart_valves_layout)
        heart_valves_layout.add_widget(heart_valves_label)
        tricuspid_valve_button = Button(text='Tricuspid Valve', on_release=self.show_tricuspid_valve)
        heart_valves_layout.add_widget(tricuspid_valve_button)
        pulmonary_valve_button = Button(text='Pulmonary Valve', on_release=self.show_pulmonary_valve)
        heart_valves_layout.add_widget(pulmonary_valve_button)
        mitral_valve_button = Button(text='Mitral Valve', on_release=self.show_mitral_valve)
        heart_valves_layout.add_widget(mitral_valve_button)
        aortic_valve_button = Button(text='Aortic Valve', on_release=self.show_aortic_valve)
        heart_valves_layout.add_widget(aortic_valve_button)
        back_to_learn_button = Button(text='Back to Learn', on_release=self.go_to_learn_screen)
        heart_valves_layout.add_widget(back_to_learn_button)

        #Create a new screen for Heart Septums
        heart_septum_screen = Screen(name='heart_septum')
        heart_septum_layout = BoxLayout(orientation='vertical')
        heart_septum_label = Label(text='Heart Septum')
        heart_septum_layout.add_widget(heart_septum_label)
        heart_septum_screen.add_widget(heart_septum_layout)
        interatrial_septum_button = Button(text='Interatrial Septum', on_release=self.show_interatrial_septum)
        heart_septum_layout.add_widget(interatrial_septum_button)
        interventricular_septum_button = Button(text='Interventricular Septum', on_release=self.show_interventricular_septum)
        heart_septum_layout.add_widget(interventricular_septum_button)
        back_to_learn_button = Button(text='Back to Learn', on_release=self.go_to_learn_screen)
        heart_septum_layout.add_widget(back_to_learn_button)

        #Create a new screen for Heart Vessels
        heart_vessels_screen = Screen(name='heart_vessels')
        heart_vessels_layout = BoxLayout(orientation='vertical')
        heart_vessels_label = Label(text='Heart Vessels')
        heart_vessels_screen.add_widget(heart_vessels_layout)
        heart_vessels_layout.add_widget(heart_vessels_label)
        superior_vena_cava_button = Button(text='Superior Vena Cava', on_release=self.show_superior_vena_cava)
        heart_vessels_layout.add_widget(superior_vena_cava_button)
        inferior_vena_cava_button = Button(text='Inferior Vena Cava', on_release=self.show_inferior_vena_cava)
        heart_vessels_layout.add_widget(inferior_vena_cava_button)
        pulmonary_arteries_button = Button(text='Pulmonary Arteries', on_release=self.show_pulmonary_arteries)
        heart_vessels_layout.add_widget(pulmonary_arteries_button)
        pulmonary_veins_button = Button(text='Pulmonary Veins', on_release=self.show_pulmonary_veins)
        heart_vessels_layout.add_widget(pulmonary_veins_button)
        aorta_button = Button(text='Aorta', on_release=self.show_aorta)
        heart_vessels_layout.add_widget(aorta_button)
        back_to_learn_button = Button(text='Back to Learn', on_release=self.go_to_learn_screen)
        heart_vessels_layout.add_widget(back_to_learn_button)


        # Create a new screen for Superior Vena Cava information
        superior_vena_cava_screen = Screen(name='superior_vena_cava')
        superior_vena_cava_layout = BoxLayout(orientation='vertical')
        superior_vena_cava_label = Label(text='Superior Vena Cava Information')
        back_button_superior_vena_cava = Button(text='Back to Heart Vessels', on_release=self.show_heart_vessels)
        superior_vena_cava_image = Image(source='C:\\Users\\fptsh\\Downloads\\aorta.png', size_hint=(None, None), size=(600, 600))
        superior_vena_cava_image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        superior_vena_cava_content = Label(text='The Superior Vena Cava is a large vein that carries deoxygenated blood from the upper body to the heart.')
        superior_vena_cava_layout.add_widget(superior_vena_cava_label)
        superior_vena_cava_layout.add_widget(superior_vena_cava_image)
        superior_vena_cava_layout.add_widget(superior_vena_cava_content)
        superior_vena_cava_layout.add_widget(back_button_superior_vena_cava)
        superior_vena_cava_screen.add_widget(superior_vena_cava_layout)

        # Create a new screen for Aorta information
        aorta_screen = Screen(name='aorta')
        aorta_layout = BoxLayout(orientation='vertical')
        aorta_label = Label(text='Aorta Information')
        back_button_aorta = Button(text='Back to Heart Vessels', on_release=self.show_heart_vessels)
        aorta_image = Image(source='C:\\Users\\fptsh\\Downloads\\aorta.png', size_hint=(None, None), size=(600, 600))
        aorta_image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        aorta_content = Label(text='The Aorta is the largest artery in the body, originating from the left ventricle of the heart and supplying oxygenated blood to all parts of the body. It branches into various arteries that distribute blood to different organs and tissues.')
        aorta_layout.add_widget(aorta_label)
        aorta_layout.add_widget(aorta_image)
        aorta_layout.add_widget(aorta_content)
        aorta_layout.add_widget(back_button_aorta)
        aorta_screen.add_widget(aorta_layout)

        # Create a new screen for Inferior Vena Cava information
        inferior_vena_cava_screen = Screen(name='inferior_vena_cava')
        inferior_vena_cava_layout = BoxLayout(orientation='vertical')
        inferior_vena_cava_label = Label(text='Inferior Vena Cava Information')
        back_button_inferior_vena_cava = Button(text='Back to Heart Vessels', on_release=self.show_heart_vessels)
        inferior_vena_cava_image = Image(source='C:\\Users\\fptsh\\Downloads\\inferior_vena_cava.png', size_hint=(None, None), size=(600, 600))
        inferior_vena_cava_image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        inferior_vena_cava_content = Label(text='The Inferior Vena Cava is a large vein that carries deoxygenated blood from the lower body to the heart.')
        inferior_vena_cava_layout.add_widget(inferior_vena_cava_label)
        inferior_vena_cava_layout.add_widget(inferior_vena_cava_image)
        inferior_vena_cava_layout.add_widget(inferior_vena_cava_content)
        inferior_vena_cava_layout.add_widget(back_button_inferior_vena_cava)
        inferior_vena_cava_screen.add_widget(inferior_vena_cava_layout)

        # Create a new screen for Pulmonary Arteries information
        pulmonary_arteries_screen = Screen(name='pulmonary_arteries')
        pulmonary_arteries_layout = BoxLayout(orientation='vertical')
        pulmonary_arteries_label = Label(text='Pulmonary Arteries Information')
        back_button_pulmonary_arteries = Button(text='Back to Heart Vessels', on_release=self.show_heart_vessels)
        pulmonary_arteries_image = Image(source='C:\\Users\\fptsh\\Downloads\\pulmonary_arteries.png', size_hint=(None, None), size=(600, 600))
        pulmonary_arteries_image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        pulmonary_arteries_content = Label(text='The Pulmonary Arteries carry deoxygenated blood from the heart to the lungs for oxygenation.')
        pulmonary_arteries_layout.add_widget(pulmonary_arteries_label)
        pulmonary_arteries_layout.add_widget(pulmonary_arteries_image)
        pulmonary_arteries_layout.add_widget(pulmonary_arteries_content)
        pulmonary_arteries_layout.add_widget(back_button_pulmonary_arteries)
        pulmonary_arteries_screen.add_widget(pulmonary_arteries_layout)

        # Create a new screen for Pulmonary Veins information
        pulmonary_veins_screen = Screen(name='pulmonary_veins')
        pulmonary_veins_layout = BoxLayout(orientation='vertical')
        pulmonary_veins_label = Label(text='Pulmonary Veins Information')
        back_button_pulmonary_veins = Button(text='Back to Heart Vessels', on_release=self.show_heart_vessels)
        pulmonary_veins_image = Image(source='C:\\Users\\fptsh\\Downloads\\pulmonary_veins.png', size_hint=(None, None), size=(600, 600))
        pulmonary_veins_image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        pulmonary_veins_content = Label(text='The Pulmonary Veins carry oxygenated blood from the lungs to the heart.')
        pulmonary_veins_layout.add_widget(pulmonary_veins_label)
        pulmonary_veins_layout.add_widget(pulmonary_veins_image)
        pulmonary_veins_layout.add_widget(pulmonary_veins_content)
        pulmonary_veins_layout.add_widget(back_button_pulmonary_veins)
        pulmonary_veins_screen.add_widget(pulmonary_veins_layout)

        #Create a new screen for Right Atrium
        right_atrium_screen = Screen(name='right_atrium')
        right_atrium_layout = BoxLayout(orientation='vertical')
        right_atrium_label = Label(text='Right Atrium Information')
        back_button_right_atrium = Button(text='Back to Heart Chambers', on_release=self.show_heart_chamber)
        right_atrium_image = Image(source='C:\\Users\\fptsh\\Downloads\\lmao.png', size_hint=(None, None), size=(600, 600))
        right_atrium_image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        right_atrium_content = Label(text='Receives oxygen-poor blood from the body')
        right_atrium_layout.add_widget(right_atrium_label)
        right_atrium_layout.add_widget(right_atrium_image)
        right_atrium_layout.add_widget(right_atrium_content)
        right_atrium_layout.add_widget(back_button_right_atrium)
        right_atrium_screen.add_widget(right_atrium_layout)

        #Create a new screen for Left Atrium
        left_atrium_screen = Screen(name='left_atrium')
        left_atrium_layout = BoxLayout(orientation='vertical')
        left_atrium_label = Label(text='Left Atrium Information')
        back_button_left_atrium = Button(text='Back to Heart Chambers', on_release=self.show_heart_chamber)
        left_atrium_image = Image(source='C:\\Users\\fptsh\\Downloads\\lmao.png', size_hint=(None, None),size=(600, 600))
        left_atrium_image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        left_atrium_content = Label(text='Receives oxygen-rich blood from the lungs')
        left_atrium_layout.add_widget(left_atrium_label)
        left_atrium_layout.add_widget(left_atrium_image)
        left_atrium_layout.add_widget(left_atrium_content)
        left_atrium_layout.add_widget(back_button_left_atrium)
        left_atrium_screen.add_widget(left_atrium_layout)

        #Create a new screen for Right Ventricle
        right_ventricle_screen = Screen(name='right_ventricle')
        right_ventricle_layout = BoxLayout(orientation='vertical')
        right_ventricle_label = Label(text='Right Ventricle Information')
        back_button_right_ventricle = Button(text='Back to Heart Chambers', on_release=self.show_heart_chamber)
        right_ventricle_image = Image(source='C:\\Users\\fptsh\\Downloads\\lmao.png', size_hint=(None, None), size=(600, 600))
        right_ventricle_image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        right_ventricle_content = Label(text='Pumps oxygen-poor blood to the lungs.')
        right_ventricle_layout.add_widget(right_ventricle_label)
        right_ventricle_layout.add_widget(right_ventricle_image)
        right_ventricle_layout.add_widget(right_ventricle_content)
        right_ventricle_layout.add_widget(back_button_right_ventricle)
        right_ventricle_screen.add_widget(right_ventricle_layout)

        #Create a new screen for Left Ventricle
        left_ventricle_screen = Screen(name='left_ventricle')
        left_ventricle_layout = BoxLayout(orientation='vertical')
        left_ventricle_label = Label(text='Left Ventricle Information')
        back_button_left_ventricle = Button(text='Back to Heart Chambers', on_release=self.show_heart_chamber)
        left_ventricle_image = Image(source='C:\\Users\\fptsh\\Downloads\\lmao.png', size_hint=(None, None), size=(600, 600))
        left_ventricle_image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        left_ventricle_content = Label(text='Pumps oxygen-rich blood to the body.')
        left_ventricle_layout.add_widget(left_ventricle_label)
        left_ventricle_layout.add_widget(left_ventricle_image)
        left_ventricle_layout.add_widget(left_ventricle_content)
        left_ventricle_layout.add_widget(back_button_left_ventricle)
        left_ventricle_screen.add_widget(left_ventricle_layout)

        #Create a new screen for Tricuspid Valve
        tricuspid_valve_screen = Screen(name='tricuspid_valve')
        tricuspid_valve_layout = BoxLayout(orientation='vertical')
        tricuspid_valve_label = Label(text='Tricuspid Valve Information')
        back_button_tricuspid_valve = Button(text='Back to Valves', on_release=self.show_heart_valve)
        tricuspid_valve_image = Image(source='C:\\Users\\fptsh\\Downloads\\valve.png', size_hint=(None, None), size=(600, 600))
        tricuspid_valve_image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        tricuspid_valve_content = Label(text='Located between the right atrium and right ventricle. Prevents backflow of blood from the ventricle to the atrium.')
        tricuspid_valve_layout.add_widget(tricuspid_valve_label)
        tricuspid_valve_layout.add_widget(tricuspid_valve_image)
        tricuspid_valve_layout.add_widget(tricuspid_valve_content)
        tricuspid_valve_layout.add_widget(back_button_tricuspid_valve)
        tricuspid_valve_screen.add_widget(tricuspid_valve_layout)

        #Create a new screen for Pulmonary Valve
        pulmonary_valve_screen = Screen(name='pulmonary_valve')
        pulmonary_valve_layout = BoxLayout(orientation='vertical')
        pulmonary_valve_label = Label(text='Pulmonary Valve Information')
        back_button_pulmonary_valve = Button(text='Back to Valves', on_release=self.show_heart_valve)
        pulmonary_valve_image = Image(source='C:\\Users\\fptsh\\Downloads\\valve.png', size_hint=(None, None),size=(600, 600))
        pulmonary_valve_image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        pulmonary_valve_content = Label(text='Guards the entrance to the pulmonary artery. Allows blood to flow from the right ventricle to the lungs.')
        pulmonary_valve_layout.add_widget(pulmonary_valve_label)
        pulmonary_valve_layout.add_widget(pulmonary_valve_image)
        pulmonary_valve_layout.add_widget(pulmonary_valve_content)
        pulmonary_valve_layout.add_widget(back_button_pulmonary_valve)
        pulmonary_valve_screen.add_widget(pulmonary_valve_layout)

        #Create a new screen for Mitral Valve
        mitral_valve_screen = Screen(name='mitral_valve')
        mitral_valve_layout = BoxLayout(orientation='vertical')
        mitral_valve_label = Label(text='Mitral (Bicuspid) Valve Information')
        back_button_mitral_valve = Button(text='Back to Valves', on_release=self.show_heart_valve)
        mitral_valve_image = Image(source='C:\\Users\\fptsh\\Downloads\\valve.png', size_hint=(None, None),size=(600, 600))
        mitral_valve_image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        mitral_valve_content = Label(text='Found between the left atrium and left ventricle. Ensures one-way flow of blood from atrium to ventricle.')
        mitral_valve_layout.add_widget(mitral_valve_label)
        mitral_valve_layout.add_widget(mitral_valve_image)
        mitral_valve_layout.add_widget(mitral_valve_content)
        mitral_valve_layout.add_widget(back_button_mitral_valve)
        mitral_valve_screen.add_widget(mitral_valve_layout)

        #Create a new screen for Aortic Valve
        aortic_valve_screen = Screen(name='aortic_valve')
        aortic_valve_layout = BoxLayout(orientation='vertical')
        aortic_valve_label = Label(text='Aortic Valve Information')
        back_button_aortic_valve = Button(text='Back to Valves', on_release=self.show_heart_valve)
        aortic_valve_image = Image(source='C:\\Users\\fptsh\\Downloads\\valve.png', size_hint=(None, None),size=(600, 600))
        aortic_valve_image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        aortic_valve_content = Label(text='Guards the entrance to the aorta and Allows oxygen-rich blood to leave the left ventricle. ')
        aortic_valve_layout.add_widget(aortic_valve_label)
        aortic_valve_layout.add_widget(aortic_valve_image)
        aortic_valve_layout.add_widget(aortic_valve_content)
        aortic_valve_layout.add_widget(back_button_aortic_valve)
        aortic_valve_screen.add_widget(aortic_valve_layout)

        #Create a new screen for Interatrial Septum
        interatrial_septum_screen = Screen(name='interatrial_septum')
        interatrial_septum_layout = BoxLayout(orientation='vertical')
        interatrial_septum_label = Label(text='Interatrial Septum Information')
        back_button_interatrial_septum = Button(text='Back to Septums', on_release=self.show_heart_septum)
        interatrial_septum_image = Image(source='C:\\Users\\fptsh\\Downloads\\lmao.png',size_hint=(None, None), size=(600, 600))
        interatrial_septum_image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        interatrial_septum_content = Label(text='TThe interatrial septum separates the left and right atria')
        interatrial_septum_layout.add_widget(interatrial_septum_label)
        interatrial_septum_layout.add_widget(interatrial_septum_image)
        interatrial_septum_layout.add_widget(interatrial_septum_content)
        interatrial_septum_layout.add_widget(back_button_interatrial_septum)
        interatrial_septum_screen.add_widget(interatrial_septum_layout)

        #Create a new screen for interventricular septum
        interventricular_septum_screen = Screen(name='interventricular_septum')
        interventricular_septum_layout = BoxLayout(orientation='vertical')
        interventricular_septum_label = Label(text='Interventricular Septum Information')
        back_button_interventricular_septum = Button(text='Back to Septums', on_release=self.show_heart_septum)
        interventricular_septum_image = Image(source='C:\\Users\\fptsh\\Downloads\\lmao.png',size_hint=(None, None), size=(600, 600))
        interventricular_septum_image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        interventricular_septum_content = Label(text='The interventricular septum divides the left and right ventricles.')
        interventricular_septum_layout.add_widget(interventricular_septum_label)
        interventricular_septum_layout.add_widget(interventricular_septum_image)
        interventricular_septum_layout.add_widget(interventricular_septum_content)
        interventricular_septum_layout.add_widget(back_button_interventricular_septum)
        interventricular_septum_screen.add_widget(interventricular_septum_layout)

        # Add screens to the screen manager
        self.sm.add_widget(main_screen)
        self.sm.add_widget(heart_image_screen)
        self.sm.add_widget(heart_anatomy_png_screen)
        self.sm.add_widget(learn_screen)
        self.sm.add_widget(superior_vena_cava_screen)
        self.sm.add_widget(aorta_screen)
        self.sm.add_widget(inferior_vena_cava_screen)
        self.sm.add_widget(pulmonary_arteries_screen)
        self.sm.add_widget(pulmonary_veins_screen)
        self.sm.add_widget(right_atrium_screen)
        self.sm.add_widget(left_atrium_screen)
        self.sm.add_widget(right_ventricle_screen)
        self.sm.add_widget(left_ventricle_screen)
        self.sm.add_widget(tricuspid_valve_screen)
        self.sm.add_widget(pulmonary_valve_screen)
        self.sm.add_widget(mitral_valve_screen)
        self.sm.add_widget(aortic_valve_screen)
        self.sm.add_widget(interatrial_septum_screen)
        self.sm.add_widget(interventricular_septum_screen)
        self.sm.add_widget(heart_chamber_screen)
        self.sm.add_widget(heart_valves_screen)
        self.sm.add_widget(heart_septum_screen)
        self.sm.add_widget(heart_vessels_screen)

        return self.sm


    def show_heart_picture(self, instance):
        self.sm.current = 'heart_image'

    def show_heart_anatomy_png(self, instance):
        self.sm.current = 'heart_anatomy_png'

    def go_back_to_main(self, instance):
        self.sm.current = 'main'

    def go_back_to_heart_image(self, instance):
        self.sm.current = 'heart_image'

    def learn_heart_anatomy(self, instance):
        self.sm.current = 'learn'

    def go_to_learn_screen(self, instance):
        self.sm.current = 'learn'

    def go_back_to_heart_anatomy_png(self, instance):
        self.sm.current = 'heart_anatomy_png'

    def show_superior_vena_cava(self, instance):
        self.sm.current = 'superior_vena_cava'

    def show_aorta(self, instance):
        self.sm.current = 'aorta'

    def show_inferior_vena_cava(self, instance):
        self.sm.current = "inferior_vena_cava"

    def show_pulmonary_arteries(self, instance):
        self.sm.current = 'pulmonary_arteries'

    def show_pulmonary_veins(self, instance):
        self.sm.current = 'pulmonary_veins'

    def show_right_atrium(self, instance):
        self.sm.current = 'right_atrium'

    def show_left_atrium(self, instance):
        self.sm.current = 'left_atrium'

    def show_right_ventricle(self, instance):
        self.sm.current= 'right_ventricle'

    def show_left_ventricle(self, instance):
        self.sm.current = 'left_ventricle'

    def show_tricuspid_valve(self, instance):
        self.sm.current = 'tricuspid_valve'

    def show_pulmonary_valve(self, instance):
        self.sm.current = 'pulmonary_valve'

    def show_mitral_valve(self, instance):
        self.sm.current = 'mitral_valve'

    def show_aortic_valve(self, instance):
        self.sm.current = 'aortic_valve'

    def show_interatrial_septum(self, instance):
        self.sm.current = 'interatrial_septum'

    def show_interventricular_septum(self, instance):
        self.sm.current = 'interventricular_septum'

    def show_heart_chamber(self, instance):
        self.sm.current = 'heart_chamber'

    def show_heart_valve(self, instance):
        self.sm.current = 'heart_valves'

    def show_heart_septum(self, instance):
        self.sm.current = 'heart_septum'

    def show_heart_vessels(self, instance):
        self.sm.current = 'heart_vessels'


if __name__ == '__main__':
    AnatomyApp().run()