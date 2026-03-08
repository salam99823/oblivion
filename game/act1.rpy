#
# Он стоит за кассой, принимает заказы, люди силуэты.
# Видны лишь детали и потом после смены сразу идет в бар.
# После нескольких рюмок все силуэты обретают лица полные счастья.
# Танцы, игры, драка и резко он просыпается в постели с похмельем.
# Под глазами мешки и надо бежать на работу, он регулярно опаздывает,
# но начальник не может его уволить потому что ему жалко его.
#
label act1:
label work_day_at_fastfood:
    scene bg fastfood with fade
    pause 1
    show silhouette 1 at silhouette
    with dissolve
    play music toes

    # TODO: Add work noise

    customer "У вас есть трубочки для коктейлей?"
    z """
    {static}{i}Боже, ну каким же тупым можно быть...{/i}{/static}

    Они лежат прямо на подносе, посмотрите внимательнее.
    """
    customer "Спасибо."
    hide silhouette 1 with dissolve

    z "Эххх"

    show silhouette 2 at silhouette with dissolve
    z """
    {i}вздыхает{/i}

    {static}{i}И почему все жалобы должен выслушивать именно я...{/i}{/static}

    Вы читали состав?

    В этом бургере всего три кусочка салата.

    {static}{i}Надо было учиться читать, пока была возможность...{/i}{/static}
    """
    customer "С чего это я должен его читать?!"
    z """
    Наверное, потому что Вы за него платите?

    Очевидно же.

    У нас есть веганские позиции, там овощей больше.
    """
    customer """
    Мне нужен менеджер!
    """
    z """
    {static}{i}Типичная «Карен»...{/i}{/static}

    Хорошо.
    """

    # NOTE: Good place for some choice
    "[z] немедленно идет звать менеджера."

    show silhouette 2 at right_center
    with move
    show manager at silhouette, left_center
    with dissolve
    manager "Здравствуйте, я менеджер."
    customer """
    Я хочу вернуть свои деньги!

    {i}меняет тон{/i}

    Но Ваш сотрудник отказал в моей просьбе.
    """
    customer """
    У него мешки под глазами больше, чем этот бургер.

    Где Вы его вообще откопали?
    """
    manager """
    {i}прочищает горло{/i}

    Уверен, мы сможем это обсудить.

    Пройдемте в мой кабинет?

    Надеюсь нам удастся все уладить.

    {i}лучезарно улыбается{/i}
    """
    customer "{i}чуть громче{/i}{p}Хорошо."

    hide silhouette
    hide manager
    with dissolve
    scene bg fastfood night with fade

    "Оставшаяся часть смены прошла обыденно"
    z "{static}{i}Наконец-то это кончилось.{/i}{/static}"

    scene bg street with fade
    "{i}щелчок замка{/i}"

    """
    Холодный ночной воздух бьет в лицо.

    Но не приносит свежести — только запах мокрого асфальта
    и дешевого фритюра, въевшегося в одежду.
    """

    z """
    Еще один день впустую.

    Еще одна пачка часов, брошенная в шредер.
    """

    """
    В голове начинают всплывать обрывки старых лиц, голоса из прошлого,
    ошибки, которые он обещал себе забыть.

    Они липкие, как пролитая кола на прилавке.

    Чтобы заглушить их, нужен другой шум.

    Подойдя к бару он толкает тяжелую дубовую дверь.
    """

label bar_scene:
    scene bg bar with fade
    """
    [z] падает на высокий стул в самом углу, подальше от ламп.

    Я чувствовал себя тенью среди теней.
    """

    show boris at right
    with dissolve
    """
    Бармен, не задавая вопросов, 
    привычным жестом пускает стакан по отполированной стойке.

    Стекло со стуком останавливается прямо перед его рукой.
    """
    hide boris
    with dissolve

    # TODO: Add drinking sound
    z """
    За то, чтобы забыть.
    """

    "Мир начинает {shader=jitter}вибрировать и теряет что-то...{/shader}"

    # TODO: Add club dance music
    scene black
    with fade
    pause 2

label morning_scare:
    # TODO: Add alarm clock sound
    image animated_phone:
        "phone.png"
        truecenter, rotate 25
        block:
            block:
                linear 0.05 rotate 23.0 counterclockwise
                linear 0.05 rotate 27.0 clockwise
                repeat 10
            pause 1
            repeat
    show animated_phone
    with fade
    pause 5
    hide animated_phone
    with dissolve
    pause 5
    show animated_phone
    with dissolve
    pause 5

    scene bg bedroom evening with fade
    z "Ээээхх"

