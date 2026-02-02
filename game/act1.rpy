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

    # TODO: Add work noise

    customer "У вас есть трубочки для коктейлей?"
    player """
    {static}{i}Боже, ну каким же тупым можно быть...{/i}{/static}

    Они лежат прямо на подносе, посмотрите внимательнее.
    """
    customer "Спасибо."
    hide silhouette 1 with dissolve

    player "Эххх"

    show silhouette 2 at silhouette with dissolve
    player """
    {i}вздыхает{/i}

    {static}{i}И почему все жалобы должен выслушивать именно я...{/i}{/static}

    Вы читали состав?

    В этом бургере всего три кусочка салата.

    {i}про себя{/i}

    Надо было учиться читать, пока была возможность...
    """
    customer "С чего это я должен его читать?!"
    player """
    Наверное, потому что вы за него платите?

    Очевидно же.

    У нас есть веганские позиции, там овощей больше.
    """
    customer """
    Мне нужен менеджер!

    Пацан, не тебе меня жизни учить!
    """
    player """
    {i}про себя{/i}

    Ну всё...

    Типичная «Карен»...

    Хорошо.
    """

    # NOTE: Good place for some choice
    "[player] немедленно идет звать менеджера."

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

    Где вы его вообще откопали?
    """
    manager """
    {i}прочищает горло{/i}

    Уверен, мы сможем это обсудить.

    Пройдемте в мой кабинет?

    Чтобы найти компромисс.

    {i}лучезарно улыбается{/i}
    """
    customer "{i}чуть громче{/i}{p}Хорошо."

    hide silhouette
    hide manager
    with dissolve
    scene bg fastfood night with fade

    "Оставшаяся часть смены прошла обыденно"
    player "{static}{i}Наконец-то это кончилось.{/i}{/static}"

    # Player leaving fastfood
    scene bg street with fade
    "{i}щелчок замка{/i}"

    """
    Холодный ночной воздух бьет в лицо.

    Но не приносит свежести — только запах мокрого асфальта
    и дешевого фритюра, въевшегося в одежду.

    [player] натягивает капюшон.
    """

    player """
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
    [player] падает на высокий стул в самом углу, подальше от ламп.

    Он чувствует себя тенью среди теней.
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
    player """
    {i}про себя{/i}

    За то, чтобы забыть.
    """

    "Мир начинает {shader=jitter}вибрировать и теряет что-то...{/shader}"

    # TODO: Add club dance music
    scene black
    with fade
    pause 2

label morning_scare:
    # TODO: Add alarm clock sound
    scene black

    show phone at truecenter
    with fade
    pause 2
    hide phone at truecenter
    with dissolve
    pause 3
    show phone at truecenter
    with dissolve
    pause 2

    scene bg bedroom evening with fade
    player "Ээээхх"

