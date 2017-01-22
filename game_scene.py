# Created by: Anwyl Gabutero
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the main game.

from scene import *
import ui
import random
import sound

class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.center_of_screen_x = self.size.x
        self.center_of_screen_y = self.size.y
        self.score_position_x = self.size.x
        self.score_position_y = self.size.y
        center_of_screen = self.size/2
        self.left_button_down = False
        self.right_button_down = False
        self.face_move_speed = 30.0
        self.cookies = [] 
        self.cookie_fall_rate = 8
        self.score = 0
        self.game_over = False
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = '#d5e3ff', 
                                     parent = self, 
                                     size = self.size)
              
                                       
        left_button_position = Vector2(self.center_of_screen_x * 0.05, self.center_of_screen_y * 0.10)
        self.left_button = SpriteNode('./assets/sprites/left_button.png',  
                                       parent = self,
                                       position = left_button_position,
                                       alpha = 0.3,
                                       scale = 0.7)
                                      
      
        right_button_position = Vector2(self.center_of_screen_x * 0.20, self.center_of_screen_y * 0.10)
        self.right_button = SpriteNode('./assets/sprites/right_button.png',
                                       parent = self,
                                       position = right_button_position,
                                       alpha = 0.3,
                                       scale = 0.7)
       
        face_position = Vector2(self.center_of_screen_x * 0.50, self.center_of_screen_y * 0.10)
        self.face = SpriteNode('./assets/sprites/face.PNG',
         						 parent = self,
         						 position = face_position,
         						 scale = 0.10)
       
        score_position = Vector2(self.score_position_x * 0.09, self.score_position_y * 0.89)
        self.score_label = LabelNode(text = 'Score: ',
           						     font = ('Avenir', 40),
           						     parent = self,
           						     position = score_position)
       
        self.menu_button = SpriteNode('assets/sprites/menu_button.png',
        					          parent = self,
        					          position = self.size/2,
        					          scale = 0.9,
        					          alpha = 0.0)
    def update(self):  
        # this method is called, hopefully, 60 times a second
       
        if self.left_button_down == True:
            faceMove = Action.move_by(-1 * self.face_move_speed, 
                                           0.0, 
                                           0.4)
            self.face.run_action(faceMove)
        
        if self.right_button_down == True:
            faceMove = Action.move_by(self.face_move_speed, 
                                           0.0, 
                                           0.4)
            self.face.run_action(faceMove)
          
        cookies_create_chance = random.randint(1,20)
        if cookies_create_chance == 7 and self.game_over == False:
            self.add_cookie()
            
        for cookie in self.cookies:
            if cookie.frame.intersects(self.face.frame):
                cookie.remove_from_parent()
                self.cookies.remove(cookie)
                self.score = self.score + 1
                sound.play_effect('./assets/sounds/Woosh_2.caf')
      
        for cookie in self.cookies:
            if cookie.position.y < -50:
                cookie.remove_from_parent()
                self.cookies.remove(cookie)
                self.game_over = True
        
        self.score_label.text = 'Score:' + str(self.score)
      
        #self.game_over = True
    
        if self.game_over == True:
            self.menu_button.alpha = 1
            self.face.remove_from_parent()
            self.menu_button_created = True
        
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
     
        if self.left_button.frame.contains_point(touch.location):
            self.left_button_down = True
        
        if self.right_button.frame.contains_point(touch.location):
            self.right_button_down = True
            
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        self.left_button_down = False
        self.right_button_down = False
        if self.menu_button.frame.contains_point(touch.location) and self.game_over == True:
            self.menu_button.scale = 0.5
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
    
    def add_cookie(self):
        cookie_start_position = Vector2(0,0)
        cookie_start_position.x = random.randint(100, 
                                         self.size_of_screen_x - 100)
        cookie_start_position.y = self.size_of_screen_y + 100
        
        cookie_end_position = Vector2()
        cookie_end_position.x = random.randint(100, 
                                        self.size_of_screen_x - 100)
        cookie_end_position.y = - 100
        
        self.cookies.append(SpriteNode('./assets/sprites/cookie.PNG',
                             position = cookie_start_position,
                             parent = self,
                             scale = 0.2))
     
        cookiesMoveAction = Action.move_to(cookie_end_position.x,
           								   cookie_end_position.y,
           								   self.cookie_fall_rate,
           								   TIMING_SINODIAL)
        
        self.cookies[len(self.cookies)- 1].run_action(cookiesMoveAction)


        
    

