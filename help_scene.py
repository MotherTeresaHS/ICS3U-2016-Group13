# Created by: Anwyl Gabutero
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the help scene.

from scene import *
import ui

from main_menu_scene import *

class HelpScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        center_of_screen = self.size/2
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = '#80ffcd', 
                                     parent = self, 
                                     size = self.size)
    	# add back button
        back_button_position = Vector2(self.size_of_screen_x * 0.07, self.size_of_screen_y * 0.90)
        self.back_button = SpriteNode('assets/sprites/back_button.PNG',
        							   parent = self,
        							   position = back_button_position,
        							   scale = 0.20)
       	# add the title
        help_title_position = Vector2(self.size_of_screen_x * 0.50, self.size_of_screen_y * 0.90)
        self.help_title = LabelNode(text = 'Welcome to Munchie Monster!',
                                      font=('Avenir', 45),
                                      parent = self,
                                      position = help_title_position,
                                      scale = 1)
        # add the lL                        
        help_position = Vector2(self.size_of_screen_x * 0.50, self.size_of_screen_y * 0.65)
        self.credits = LabelNode(text = 'Your objective of the game is to get every\ncookie possible that is on the screen',
                                 font = ('Avenir', 20),
                                 parent = self,
                                 position = help_position,
                                 scale = 1.5)
      
        help_position_two = Vector2(self.size_of_screen_x * 0.50, self.size_of_screen_y * 0.50)
        self.credits = LabelNode(text = 'Use the controls to move your character',
                                 font = ('Avenir', 20),
                                 parent = self,
                                 position = help_position_two,
                                 scale = 1.5)
                                 
        help_position_three = Vector2(self.size_of_screen_x * 0.50, self.size_of_screen_y * 0.39)
        self.help = LabelNode(text = 'You only have 30 seconds',
                                 font = ('Avenir', 20),
                                 parent = self,
                                 position = help_position_three,
                                 scale = 1.5)
      
        help_position_four = Vector2(self.size_of_screen_x * 0.50, self.size_of_screen_y * 0.20)
        self.help = LabelNode(text = 'GOOD LUCK!',
                                 font = ('Avenir', 20),
                                 parent = self,
                                 position = help_position_four,
                                 scale = 3)
                                    
        help_position_four = Vector2(self.size_of_screen_x * 0.88, self.size_of_screen_y * 0.10)
        self.help = LabelNode(text = 'Created by Anwyl Gabutero\n Created with Pythonista',
                                 font = ('Avenir', 20),
                                 parent = self,
                                 position = help_position_four,
                                 scale = 0.8)
                                     
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, goto game scene
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    

