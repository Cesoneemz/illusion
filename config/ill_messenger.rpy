#################################################################################
### Telegram Messenger
#################################################################################
init python:
    
    style_button_back = "#282E33" 
    style_button_hovr = "#5F6C77"
    style_button_inst = "#14171A"

    
    style.btn = Style(style.default)
    style.btn.background = style_button_back
    style.btn.hover_background = style_button_hovr
    style.btn.insensitive_background = style_button_inst
    
    style.bar_vert = Style(style.default)
    style.bar_vert.right_bar = style_button_inst 
    style.bar_vert.left_bar = style_button_inst 
    style.bar_vert.thumb = style_button_hovr
    style.bar_vert.bar_vertical = True
    style.bar_vert.bar_invert = True
    style.bar_vert.xalign = 1.0
    style.bar_vert.yalign = 0.6
    style.bar_vert.xsize = 10
    style.bar_vert.ysize = 780
    
    style.txt_base = Style(style.default)
    style.txt_base.font = "illusion/res/fonts/tahoma.ttf"
    style.txt_base.xalign = 0.5
    style.txt_base.yalign = 0.5
    style.txt_base.size = 30
    style.txt_base.color = "#fff"


    yadj = ui.adjustment()

    def ill_msg(txt, who=False, sound=False):
        global m_msg, yadj
        m_msg.append((who, txt, sound))
        yadj.value = yadj.range+300
        renpy.restart_interaction()
        if who:
            renpy.play("illusion/res/music/sfx/sfx_message.mp3", "sound")
        renpy.pause()

    def ill_del_last_msg():
        global m_msg
        del m_msg[-1]

    def ill_del_all_msg():
        global m_msg
        m_msg = []

screen ill_messenger():
    frame background "illusion/res/images/messenger/back.png" xysize (600,975) align (0.1,.5):
        frame background None xysize (560, 810) align (0.5,0.58):
            viewport id "vp_msg" mousewheel True  yadjustment yadj:
                vbox spacing 15 xsize 550 xalign 0.4 box_reverse True:
                    for message in m_msg[::-1]:
                        $ who, txt, sound = message
                        $ xgn = 0.0 if who else 1.0
                        if sound:
                            imagebutton auto "illusion/res/images/messenger/sound_%s.png" xalign xgn action Play("sound", sound)
                        else: 
                            button xalign xgn xmaximum 580 xpadding 20 ypadding 10 background Frame("illusion/res/images/messenger/box.png", 25, 25):
                                text "%s"%(txt) style "txt_base"

        
        text "%s"%(msg_name) style "txt_base" size 35 xalign 0.31 xanchor 0.0 yalign 0.04       
        add "illusion/res/images/messenger/av/"+msg_name.lower().replace(' ', '_')+".png" pos (100,27)       
        imagebutton auto "illusion/res/images/messenger/arr_%s.png" pos (10, 33) action NullAction()       
#        button background style_button_inst hover_background style_button_hovr xalign 0.99 yalign 0.03 action( Hide("ill_messenger"), Show("ill_messenger_active")) xysize (60,60):
#            text "  x  " style "txt_base" size 40 pos (36, -2) 
        vbar value YScrollValue("vp_msg") style "bar_vert"

#################################################################################


#################################################################################
# by sDextra 
# old Sota
#################################################################################
