# Created by: Anwyl Gabutero
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui

from game_scene import * 
from help_scene import *

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        center_of_screen = self.size/2
        
        # add MT blue background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = '#2b74ff', 
                                     parent = self, 
                                     size = self.size)
                                     
         # add start button 
        start_button_position = Vector2(self.size_of_screen_x * 0.50, self.size_of_screen_y * 0.50)
    	self.start_button = SpriteNode('./assets/sprites/start.png',
    								   parent = self, 
    								   position = start_button_position,
    								   scale = 1.3)
    	# add help button 
        help_button_position = Vector2(self.size_of_screen_x * 0.09, self.size_of_screen_y * 0.12)
        self.help_button = SpriteNode('./assets/sprites/help.png',
                                       parent = self,
                                       position = help_button_position,
                                       scale = 0.5)
         # add game title
        title_position = Vector2(self.size_of_screen_x * 0.50, self.size_of_screen_y * 0.80)
        self.title = LabelNode(text = 'Munchie Monster',
         								font =('Avenir', 50),
         								color = '#80cdff',
         								parent = self,
         								scale = 2,
         								position = title_position)
         								
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
        
        if self.start_button.frame.contains_point(touch.location):
            self.present_modal_scene(GameScene())
            
        # if start button is pressed, goto game scene
        if self.help_button.frame.contains_point(touch.location):
            self.present_modal_scene(HelpScene())
    
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
    
