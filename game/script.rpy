﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define d = Character('Damian', color="#a48ce1")
define u = Character('???', color="ffffff")
default answered_questions1 = []

#music and sounds
define audio.musicnormal = "music/calmmelodytoi.mp3"
define audio.tick = "music/slowticking.mp3"
define audio.musicmenu = "music/musmenu.mp3"
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
play music musicmenu

# Игра начинается здесь:
label start:
    play music musicnormal #чтобы отключить stop music fadeout 1(количество секунд сколько она будет затухать)

    scene bg roomnight
    with dissolve

    show damian222
    with dissolve

    u "Черт... Эти кошмары невыносимы."
    hide damian222

    show damian312

    u "Сейчас ночь или утро?.."
    hide damian312

    show damian221

    u "Ох, опять эта комната.."

    hide damian221

    scene bg black
    with dissolve
    u "На документе, который я подписывал ранее, было сказано что я узнал об этом эксперименте через моего друга с института. "
    u "Он узнал что я не могу справиться с утратой всей моей семьи и предложил мне.. "
    u "..найти себе место в обществе, где я ощущал себя бесполезным.
"
    u "Я решил принять участие в психологическом эксперименте, где нам сперва стирают память." 
    u "Потом мы прорабатываем свои травмы в психотерапиях, проводим психологическую реабилитацию, учавствуя на дискуссиях и совместных занятиях.
"
    u "Теперь я живу в подобии вивария, где все люди это подопытные, а над ними проводят эксперименты.
"
    u "И эта комната - мое место жительства."

    scene bg roomnight
    with dissolve

    show damian222
    u "По всей видимости, сейчас вечер, за окном не так темно."
    hide damian222

    show damian111
    u "Но почему я ничего не помню что было?"
    hide damian111

    show damian112
    u "Что то точно должно было что то быть.."
    hide damian112

    show damian322

    u "Надо бы осмотреть комнату, может вспомню что-либо."
    hide damian322

    jump room_questions

    return

label room_questions:
    menu:
        u "С чего бы начать.."
        "Кровать" if 0 not in answered_questions1:
            u "Небольшая кровать. Сначала казалось не удобной, но потом привык."
            $ answered_questions1.append(0)
            jump room_questions

        "Тумбочка" if 1 not in answered_questions1:
            u "На тумбочке стоит переносной светильник, достаточно неплохой."
            u "Еще между тумбочкой и кроватью сидит какой-то фиолетовый кролик с красными глазами" 
            u "Так, что там у нас дальше?.."
            u "Хм, в верхнем выдвижном ящиике лежат ножницы и всякая острая и “опасная” канцелярия."
            u "Из-за того что у меня не наблюдаются суицидальные наклонности, мне позволяют хранить их и пользоваться ими, но не давать другим пациентам."
            u "Итак, в нижнем выдвижном ящике должны лежать три моих комплекта чистой одежды, четвертый на мне"
            u "*Вытащил все комплекты."
            u "Третий комплект испачкан кровью?"
            u "Что то тут произошло, но не могу понять что именно. Я ничего не помню."
            $ answered_questions1.append(1)
            jump room_questions

        "Окна" if 2 not in answered_questions1:
            u "Здесь большие чистые окна без каких-либо решеток снаружи."
            u "За окном внизу виден город, в котором я кажется никогда до этого не бывал."
            u "Моя комната располагается на теневой стороне, так что я не задергиваю шторы, чтобы было побольше естественного света."
            u "Для меня так лучше читать книги"
            $ answered_questions1.append(2)
            jump room_questions

        "Рабочий стол "if 3 not in answered_questions1:
            u "Тут я читаю книги или делаю домашнюю работу. К примеру, психотерапевт может задать вести дневник, или преподаватель Сиерра может задать что либо креативное."
            u "Типа сделать коллаж с цветной бумагой или просто нарисовать что-либо."
            u "Детское занятие, но весьма неплохое."
            $ answered_questions1.append(3)
            jump room_questions

    show damian111
    u "Очень странно что сейчас вечер, а света под дверью нет, он всегда там есть."
    u "Никто за мной не приходил и не будил. Тут не приветствуется вечерний сон, ибо пациенты все должны соблюдать здоровый режим сна."
    hide damian111

    show damian222
    u "Да еще и моя одежда испачкана кровью. На мне же нет никаких повреждений, тогда чья эта кровь?."
    hide damian

    show damian231
    u "Что-то тут определенно не так."
    hide damian231

    show damian222
    u "Надо выйти из комнаты и осмотреться."
    hide damian222

    menu:
        "Выйти из комнаты": #сделать второй выбор, где он останется в комнате и умрет от страха и голода. Или задохнется от трупного запаха хаха
            jump dorms
        "Остаться в комнате":
            jump first_ending
    return

label first_ending:
    stop music
    show damian122
    u "Хотя.. Может остаться тут будет более безопасно"
    u "Мало ли что там снаружи может твориться.."
    hide damian122

    u "По итогу, я остался в комнате"
    u "Прошло уже много времени с тех пор как я проснулся"
    u "Я обдумывал все варианты событий"
    u "Вдруг там лежат трупы, а я просто лежу в своей комнате"
    u "Чем больше я придумывал, тем страшнее мне становилось"
    u "Вдруг, даже если я выйду, то все равно не смогу выбраться и умру.."
    u "..."
    u "Спустя время я уже начал философствовать о смысле жизни"
    u "А потом думать о Боге"
    u "Начал задавать ему вопросы"
    u "Потом он мне начал отвечать на вопросы"
    u "Я уже лежал очень долгое время и мной будто обладел кататонический синдром..."
    u "........"
    "Если ты разговариваешь с Богом, то это молитва"
    "А если Бог разговаривает с тобой, то это.."
    "ШИЗОФРЕНИЯ"




label dorms:
    scene bg dormitory_hall

    u "В коридоре дормитория пахнет немного застоявшимся воздухом, будто не работает вентиляция."

    u "Тут пусто и темно, лишь переносные светильники слабо светят из комнат других пациентов."

    u "У некоторых палат открыты нараспашку, а у некоторых закрыты."

    u "Я чувствую какую-то тревожность из-за того что никого нет и выглядит все так, как будто жизнь тут умерла."

    u "Прежде чем выйти из дормитория, мне следует посмотреть палаты других пациентов, может найду какие-нибудь подсказки?.."

    scene bg black
    play sound tick
    u "..."

    scene bg dormitory_hall

    u "Я обыскал все комнаты, но там нет ничего необычного."

    u "У некоторых людей порядок на столе, у кого-то вообще пусто."

    u "Никаких подсказок присутствия людей и медперсонала здесь нет."

    u "Я все время откладывал это, но придется войти в основной коридор и медблок, где мы проводили все наше время пребывания тут, кроме сна."

    u "Там нет ничего страшного, наоборот, там довольно приятная атмосфера."

    u " Но что-то мне подсказывает что там что-то не так.. "

    show damian231
    u "Черт, мое сердце будто разрывается от тревоги..."
    hide damian231


    show damian232
    u "От основного коридора так пахнет металлическим запахом крови."
    u "Я должен посмотреть что там.."
    hide damian232

    scene bg mainhall

    u "Войдя в основной коридор, я увидел нашего помощника лаборанта и три подопытных людей, как и я.."
    u "Двое из испытуемых лежали на полу, Галвин на животе, Харпер на спине."

    u " Другая испытуемая Донован и лаборант Риис прислонились спиной к стене и будто уснули. "
    u "Я подошел к Риису и попытался нащупать пульс или хоть узнать есть ли дыхание"
    u "Мои руки дрожали"
   
    show damian232
    u " Может из-за того что у меня нет опыта в этом я не могу определить?"
    u "Дыхание.. оно или еле ощутимо, или его вообще нет."
    hide damian232

    show damian132
    u "Сомневаюсь, что с другими людьми здесь тут другая ситуация.."
    u "Я и вправду не могу определить."
    hide damian132

    show damian332
    u "А вдруг они все мертвы?"
    u "Я не вижу никаких телесных повреждений, ни капли крови."
    u "Хотя тут и присутствует стойкий запах крови."
    hide damian332

    show damian122
    u "Надо.. надо поискать маленькое зеркало, стекло или что-то металлическое.."
    u "Они должны хоть немного запотеть, если человек все таки дышит."
    hide damian122

    show damian322
    u "Если все мертвы, как я узнаю ответы на мои вопросы о происходящем тут?"
    hide damian322

    u "Тут везде мать его почти бездыханные тела, которым я никак не могу оказать помощь."
    u "Я не могу пошевелиться."
    u "Очертания людей на полу становятся неясными и.. повсюду появляется кровь будто так и было."
    u "На полу, на стенах, на одеждах моих знакомых без сознания.. везде кровь."
    u "Такое чувство, будто их убило что-то нечеловеческое.. что-то большое и сильное.. "
    u "Монстр?.."

    show damian322
    u "Что мне делать, что мне делать? Меня так трясет и будто вот вот стошнит."
    u "Мне надо успокоиться.."
    hide damian322

    show damian111
    u "Я видел плюшевого кролика в своей комнате, он должен помочь."
    hide damian111

    u "Я падаю и пытаюсь доползти до своей комнаты"

    scene bg roomnight

    u "Выдох."

    show damian212
    u "Так странно, что это за видения? Или просто галлюцинации? Почему все они в крови?"
    hide damian212

    show damian222
    d "Демиан, не беспокойся, это вряд ли они и вправду умерли такой жестокой смертью.."
    hide damian222
    show damian322
    d " Надо двигаться дальше."
    hide damian322

    scene bg black

    return


