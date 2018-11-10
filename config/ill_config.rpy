init python:

    def ill_chapter(chapter):
        global save_name
        renpy.block_rollback()
        renpy.music.stop(channel='music', fadeout=3)
        renpy.music.stop(channel='ambience', fadeout=3)
        renpy.music.stop(channel='sound', fadeout=3)
        renpy.transition(dissolve)
        renpy.scene("bg black")
        if chapter == 0:
            save_name = "Иллюзион\nПролог"
            renpy.show("Пролог",[ill_right_chapter(0.15)],what=Text(u"Пролог",style=style.ill_backdrop_text,yalign=0.25))
        elif chapter == 12:
            save_name = "Иллюзион\nЭпилог"
            renpy.show("Эпилог",[ill_right_chapter(0.15)],what=Text(u"Эпилог",style=style.ill_backdrop_text,yalign=0.25))
        else:
            save_name = "Иллюзион\nГлава " + str(chapter)
            ill_ch = u"Глава"' %d'%(chapter)
            renpy.show("Глава",[ill_right_chapter(0.15)],what=Text(ill_ch,style=style.ill_backdrop_text,yalign=0.25))
            if chapter == 1:
                renpy.show("Chapter_name",[ill_left_chapter(0.85)],what=Text(u"Странный сон",style=style.ill_backdrop_text,yalign=0.75))
            elif chapter == 2:
                renpy.show("Chapter_name",[ill_left_chapter(0.85)],what=Text(u"Сплетенная реальность",style=style.ill_backdrop_text,yalign=0.75))

    def ill_get_achievement(ach): # Получение определённой ачивки
        if persistent.ill_ach[ach] == False:
            persistent.ill_ach[ach] = True
            renpy.play(sfx_achievement, channel = "sound")
            renpy.show("ill_ach_" + ach, [ill_get_achievement_atl])
            renpy.pause(3.0)
            renpy.hide("ill_ach_" + ach)

    def ill_get_all_achievements(): # Получить все ачивки сразу(дебаг)
        for ach in ill_ach_list:
            ach_name = ach[0]
            ill_get_achievement(ach_name)

    def ill_take_photo(photo): # Функция фотографии
        renpy.transition(flash)
        renpy.show("ill_photo_" + photo, [ill_photo])
        renpy.play(ill_sfx_photo, channel = "sound")
        renpy.pause(4, hard=True)
        renpy.transition(dissolve)
        renpy.hide("ill_photo_" + photo)
        ill_get_achievement(photo)

    def ill_meet(who, name): # Знакомство
        gl = globals()
        global store
        store.names[who] = name
        gl[who+"_name"] = store.names[who]

    def ill_route_complete(route):
        if persistent.ill_route_complete_count <= 5 and not persistent.ill_routes[route]:
            persistent.ill_route_complete_count += 1
            persistent.ill_routes[route] = True
        ill_get_achievement(route)

    # Дальше идёт огромная куча функций, которые отвечают за загрузку мода

    def ill_download_rpa(): #Загрузка rpa файла, со всей музыкой, звуками, артами и прочим визуалом
        from urllib2 import urlopen
        import os, shutil
        ill_file_url = "https://github.com/Cesoneemz/illusion/raw/master/music/april_lie.mp3"
        #ill_mfolder = "illusion/"
        ill_destination = renpy.config.basedir + "/game/illusion/res/"
        #iill_destination = ill_destination + ill_mfolder
        ill_file_name = "ill_res_archive.rpa"
        try:
            os.mkdir(ill_destination)
            from urllib2 import urlopen
            response = urlopen(ill_file_url)
            CHUNK = 16 * 1024
            with open(ill_file_name, 'wb') as f:
                while True:
                    chunk = response.read(CHUNK)
                    if not chunk:
                        break
                    f.write(chunk)
            os.rename(ill_file_name, ill_destination + ill_file_name)
        except IOError as e:
            nfo_text = 'Ошибка!'
            m_nfo_text = 'Мы не знаем, как это произошло... Возможно ошибка на сервере.\nМожет быть, у вас проблемы с интернет-соединением либо атрибутами папок...'
            renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
            renpy.pause (5, hard=True)
            renpy.show("git_es_rst")
            renpy.utter_restart()

    def ill_download_rpyc(): #Загрузка rpyc файлов сценария и конфигов
        from urllib2 import urlopen
        import os, shutil

        ill_file_url_1 = "https://github.com/Cesoneemz/illusion/raw/master/music/april_lie.mp3"
        ill_file_url_2 = "https://github.com/Cesoneemz/illusion/raw/master/music/april_lie.mp3"
        ill_file_url_3 = "https://github.com/Cesoneemz/illusion/raw/master/music/april_lie.mp3"
        ill_file_url_4 = "https://github.com/Cesoneemz/illusion/raw/master/music/april_lie.mp3"
        ill_file_url_5 = "https://github.com/Cesoneemz/illusion/raw/master/music/april_lie.mp3"

        for i in range(1, 5):
            ill_file_url = ill_file_url_ + str(i)


        ill_chapterss = ["illusion_prologue"]

        for i in ill_chapterss:
            ill_file_url =
        #ill_mfolder = "illusion/"
        ill_destination = renpy.config.basedir + "/game/illusion/res/"
        #iill_destination = ill_destination + ill_mfolder
        ill_file_name = "ill_res_archive.rpa"
        try:
            os.mkdir(ill_destination)
            from urllib2 import urlopen
            response = urlopen(ill_file_url)
            CHUNK = 16 * 1024
            with open(ill_file_name, 'wb') as f:
                while True:
                    chunk = response.read(CHUNK)
                    if not chunk:
                        break
                    f.write(chunk)
            os.rename(ill_file_name, ill_destination + ill_file_name)
        except IOError as e:
            nfo_text = 'Ошибка!'
            m_nfo_text = 'Мы не знаем, как это произошло... Возможно ошибка на сервере.\nМожет быть, у вас проблемы с интернет-соединением либо атрибутами папок...'
            renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
            renpy.pause (5, hard=True)
            renpy.show("git_es_rst")
            renpy.utter_restart()
