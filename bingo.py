#  DON'T EDIT THIS FILE UNLESS YOU KNOW WHAT YOU ARE DOING
def bingo(
    bingo_card =list,
    bingo_name ="",
    free_space_text="",
    background_image_link="",
    grid_size="",
    output_file_name="",
    width=100,
    clickedColour="",
    audioClicked="",
    audioComplete="",
    audioType="",
    background_repeat="",
    textColour="",
    free_space_enabled=True
):
    import random, webbrowser
    if grid_size == "3x3":
        number_of_squares = 9
        row_size = 3
    elif grid_size == "5x5":
        number_of_squares = 25
        row_size = 5
    elif grid_size == "7x7":
        number_of_squares = 49
        row_size = 7
    else:
        print("Grid Size is not supported")
        input("Press return to quit")
        SystemExit()
        exit()
    if background_image_link != "":
        background_image = background_image_link+";"
    else:
        background_image = ""
    cards_to_generate = int(input("How many bingo cards do you want to generate?\n>> "))
    for card_number in range(1, cards_to_generate + 1):
        bingo_card_texts = bingo_card
        file = open(f"{output_file_name} - {card_number}.html", "w")
        # generated = [[], [], [], [], []]
        random.shuffle(bingo_card_texts)
        print(f"'New {bingo_name}' card made")
        print(f"{len(bingo_card_texts)} things randomized")
        if len(bingo_card_texts) < number_of_squares:
            print("Not enough bingo things added")
            input("Press return to quit")
            SystemExit()
            exit()
        file.write(
            """
<!DOCTYPE html>
<html>
<head>
    <title>"""
            + bingo_name
            + """</title>
    <style>
        * {
            color: """+textColour+""";
            user-select: none;
            text-overflow: ellipsis; 
            overflow-wrap: break-word; 
            hyphens: auto;
        }
        /* Small Screen landscape */
        @media only screen
        and (orientation: portrait) and (max-width: 610px) {
            .small_div {
                border: 2px solid white;
                float: left;
                height: """
            + str(width * 0.95)
            + """px;
                width: """
            + str(width * 0.95)
            + """px;
                margin: 0px;
                display: flex;
                justify-content: center;
                align-items: center;
                box-sizing: border-box;
                background-color: black;
            }
            .big_div {
                width: """
            + str(width * row_size * 0.95)
            + """px;
                height: """
            + str(width * row_size * 0.95)
            + """px;
                margin: auto;
            }
            .freespace {
                font-size: 20px;
                padding: 2px;
            }
            a {
                text-align: center;
                margin: 0px;
                font-size: 14px;
                padding: 2px;
                max-width: """
            + str(width * 0.95)
            + """px;
                max-height: """
            + str(width * 0.95)
            + """px;
            }
            .heading {
                margin: 0px auto;
                display: flex;
                width: """
            + str(width * row_size * 0.95)
            + """px;
                height: auto;
            }
            .heading_text {
                float: left;
                margin: 0px;
                display: flex;
                justify-content: center;
                align-items: center;
                box-sizing: border-box;
                font-size: 20px;
                width: """
            + str(width * 0.95)
            + """px;
                height: auto;
            }
        }
        /* Large Screen landscape */
        @media only screen
        and (orientation: portrait) and (min-width: 610px) {
            .small_div {
                border: 2px solid white;
                float: left;
                height: """
            + str(width * 1.75)
            + """px;
                width: """
            + str(width * 1.75)
            + """px;
                margin: 0px;
                display: flex;
                justify-content: center;
                align-items: center;
                box-sizing: border-box;
                background-color: black;
            }
            .big_div {
                width: """
            + str(width * row_size * 1.75)
            + """px;
                height: """
            + str(width * row_size * 1.75)
            + """px;
                margin: auto;
            }
            .freespace {
                font-size: 34px;
                padding: 2px;
            }
            a {
                text-align: center;
                margin: 0px;
                font-size: 26px;
                padding: 2px;
                max-width: """
            + str(width * 1.75)
            + """px;
                max-height: """
            + str(width * 1.75)
            + """px;
            }
            .heading {
                margin: 0px auto;
                display: flex;
                width: """
            + str(width * row_size * 1.75)
            + """px;
                height: auto;
            }
            .heading_text {
                float: left;
                margin: 0px;
                display: flex;
                justify-content: center;
                align-items: center;
                box-sizing: border-box;
                font-size: 34px;
                width: """
            + str(width * 1.75)
            + """px;
                height: auto;
            }
        }
        /* Small Screen landscape */
        @media only screen
        and (orientation: landscape) and (max-height: 500px) {
            .small_div {
                border: 2px solid white;
                float: left;
                height: """
            + str(width * 0.75)
            + """px;
                width: """
            + str(width * 0.75)
            + """px;
                margin: 0px;
                display: flex;
                justify-content: center;
                align-items: center;
                box-sizing: border-box;
                background-color: black;
            }
            .big_div {
                width: """
            + str(width * row_size * 0.75)
            + """px;
                height: """
            + str(width * row_size * 0.75)
            + """px;
                margin: auto;
            }
            .freespace {
                font-size: 18px;
                padding: 2px;
            }
            a {
                text-align: center;
                margin: 0px;
                font-size: 12px;
                padding: 2px;
                max-width: """
            + str(width * 0.75)
            + """px;
                max-height: """
            + str(width * 0.75)
            + """px;
            }
            .heading {
                margin: 0px auto;
                display: flex;
                width: """
            + str(width * row_size * 0.75)
            + """px;
                height: auto;
            }
            .heading_text {
                float: left;
                margin: 0px;
                display: flex;
                justify-content: center;
                align-items: center;
                box-sizing: border-box;
                font-size: 18px;
                width: """
            + str(width * 0.75)
            + """px;
                height: auto;
            }
        }
        /* Big Screen landscape */
        @media only screen
        and (orientation: landscape) and (min-height: 500px) {
            .small_div {
                border: 2px solid white;
                float: left;
                height: """
            + str(width)
            + """px;
                width: """
            + str(width)
            + """px;
                margin: 0px;
                display: flex;
                justify-content: center;
                align-items: center;
                box-sizing: border-box;
                background-color: black;
            }
            .big_div {
                width: """
            + str(width * row_size)
            + """px;
                height: """
            + str(width * row_size)
            + """px;
                margin: auto;
            }
            .freespace {
                font-size: 24px;
                padding: 2px;
            }
            a {
                text-align: center;
                margin: 0px;
                font-size: 16px;
                padding: 2px;
                max-width: """
            + str(width)
            + """px;
                max-height: """
            + str(width)
            + """px;
            }
            .heading { 
                margin: 0px auto;
                display: flex;
                width: """
            + str(width * row_size)
            + """px;
                height: auto;
            }
            .heading_text {
                float: left;
                margin: 0px;
                display: flex;
                justify-content: center;
                align-items: center;
                box-sizing: border-box;
                font-size: 24px;
                width: """
            + str(width)
            + """px;
                height: auto;
            }
        }
        .clicked {
            background-color: """
            + str(clickedColour)
            + """;
        }
        h1 {
            text-align: center;
            margin-left: 10px;
            margin-top: 5px;
            margin-bottom: 5px;
        }
        body {
            height: """
            + str(width * row_size + 110)
            + """px;
            background-color: grey;
            background-position: left, right;
            background-repeat: no-repeat, no-repeat;
            """+ background_repeat +
            "background-size: 50vw 100%;"
            + background_image
            + """
        }
        #winScreen {
            display: none; 
            background-color: pink; 
            margin: auto; 
            height: 12vw;
            position: absolute;
            width: 90vw;
            top: 55%;
            bottom: 50%;
            left: -50%;
            right: -50%;
        }
        #winScreenText {
            font-size: 10vw; 
            text-align: center; 
            width: 90vw;
            margin: 0;
            padding: 0;
        }
    </style>
</head>
<body id='body'>
    <div id="winScreen">
        <h3 id="winScreenText">Bingo!</h3>
    </div>
    <h1>"""
            + bingo_name
            + """</h1>
    <audio preload="metadata" id="audioClicked">
        <source src='"""
            + audioClicked
            + "' type='audio/"
            + audioType
            + """'>
    </audio>
    <audio preload="metadata" id="audioComplete">
        <source src='"""
            + audioComplete
            + "' type='audio/"
            + audioType
            + """'>
    </audio>
    <div class='heading'>
        <h3 class='heading_text'>B</h3>
        <h3 class='heading_text'>I</h3> 
        <h3 class='heading_text'>N</h3>
        <h3 class='heading_text'>G</h3>
        <h3 class='heading_text'>O</h3>    
    </div>
    <div class='big_div'>
"""
        )
        square = 0
        for y in range(0, int(number_of_squares**0.5)):
            for x in range(0, int(number_of_squares**0.5)):
                if square == number_of_squares // 2 and free_space_enabled:
                    # generated[y].append("Free Square")
                    file.write(
                        f"\t\t<div class='small_div' id='{square}' onclick='showClicked(this)'>\n"
                    )
                    file.write(
                        f"""\t\t\t<a class='freespace'><strong>{free_space_text}</strong></a>\n"""
                    )
                    file.write("\t\t</div>\n")
                else:
                    # generated[y].append(bingo_card_texts[square])
                    file.write(
                        f"\t\t<div class='small_div' id='{square}' onclick='showClicked(this)'>\n"
                    )
                    file.write(f"""\t\t\t<a>{bingo_card_texts[square]}</a>\n""")
                    file.write("\t\t</div>\n")
                square += 1
        file.write("</div>\n</body>")
        if number_of_squares == "25":
            file.write(
                """
            <script>
                function bingoCheck(element) {
                    // rows
                    if (document.getElementById("0").className == 'small_div clicked' && document.getElementById("1").className == 'small_div clicked' && document.getElementById("2").className == 'small_div clicked' && document.getElementById("3").className == 'small_div clicked' && document.getElementById("4").className == 'small_div clicked') {
                        document.getElementById('audioComplete').play();
                        document.getElementById('body').classList.add('won');
                        document.getElementById('winScreen').style.display='block';
                        document.getElementById('audioClicked').pause();
                    }
                    else if (document.getElementById("5").className == 'small_div clicked' && document.getElementById("6").className == 'small_div clicked' && document.getElementById("7").className == 'small_div clicked' && document.getElementById("8").className == 'small_div clicked' && document.getElementById("9").className == 'small_div clicked') {
                        document.getElementById('audioComplete').play();
                        document.getElementById('body').classList.add('won');
                        document.getElementById('winScreen').style.display='block';
                        document.getElementById('audioClicked').pause();
                    }
                    else if (document.getElementById("10").className == 'small_div clicked' && document.getElementById("11").className == 'small_div clicked' && document.getElementById("12").className == 'small_div clicked' && document.getElementById("13").className == 'small_div clicked' && document.getElementById("14").className == 'small_div clicked') {
                        document.getElementById('audioComplete').play();
                        document.getElementById('body').classList.add('won');
                        document.getElementById('winScreen').style.display='block';
                        document.getElementById('audioClicked').pause();
                    }
                    else if (document.getElementById("15").className == 'small_div clicked' && document.getElementById("16").className == 'small_div clicked' && document.getElementById("17").className == 'small_div clicked' && document.getElementById("18").className == 'small_div clicked' && document.getElementById("19").className == 'small_div clicked') {
                        document.getElementById('audioComplete').play();
                        document.getElementById('body').classList.add('won');
                        document.getElementById('winScreen').style.display='block';
                        document.getElementById('audioClicked').pause();
                    }
                    else if (document.getElementById("20").className == 'small_div clicked' && document.getElementById("21").className == 'small_div clicked' && document.getElementById("22").className == 'small_div clicked' && document.getElementById("23").className == 'small_div clicked' && document.getElementById("24").className == 'small_div clicked') {
                        document.getElementById('audioComplete').play();
                        document.getElementById('body').classList.add('won');
                        document.getElementById('winScreen').style.display='block';
                        document.getElementById('audioClicked').pause();
                    }
                    // columns
                    else if (document.getElementById("0").className == 'small_div clicked' && document.getElementById("5").className == 'small_div clicked' && document.getElementById("10").className == 'small_div clicked' && document.getElementById("15").className == 'small_div clicked' && document.getElementById("20").className == 'small_div clicked') {
                        document.getElementById('audioComplete').play();
                        document.getElementById('body').classList.add('won');
                        document.getElementById('winScreen').style.display='block';
                        document.getElementById('audioClicked').pause();
                    }
                    else if (document.getElementById("1").className == 'small_div clicked' && document.getElementById("6").className == 'small_div clicked' && document.getElementById("11").className == 'small_div clicked' && document.getElementById("16").className == 'small_div clicked' && document.getElementById("21").className == 'small_div clicked') {
                        document.getElementById('audioComplete').play();
                        document.getElementById('body').classList.add('won');
                        document.getElementById('winScreen').style.display='block';
                        document.getElementById('audioClicked').pause();
                    }
                    else if (document.getElementById("2").className == 'small_div clicked' && document.getElementById("7").className == 'small_div clicked' && document.getElementById("12").className == 'small_div clicked' && document.getElementById("17").className == 'small_div clicked' && document.getElementById("22").className == 'small_div clicked') {
                        document.getElementById('audioComplete').play();
                        document.getElementById('body').classList.add('won');
                        document.getElementById('winScreen').style.display='block';
                        document.getElementById('audioClicked').pause();
                    }
                    else if (document.getElementById("3").className == 'small_div clicked' && document.getElementById("8").className == 'small_div clicked' && document.getElementById("13").className == 'small_div clicked' && document.getElementById("18").className == 'small_div clicked' && document.getElementById("23").className == 'small_div clicked') {
                        document.getElementById('audioComplete').play();
                        document.getElementById('body').classList.add('won');
                        document.getElementById('winScreen').style.display='block';
                        document.getElementById('audioClicked').pause();
                    }
                    else if (document.getElementById("4").className == 'small_div clicked' && document.getElementById("9").className == 'small_div clicked' && document.getElementById("14").className == 'small_div clicked' && document.getElementById("19").className == 'small_div clicked' && document.getElementById("24").className == 'small_div clicked') {
                        document.getElementById('audioComplete').play();
                        document.getElementById('body').classList.add('won');
                        document.getElementById('winScreen').style.display='block';
                        document.getElementById('audioClicked').pause();
                    }
                    // cross
                    else if (document.getElementById("0").className == 'small_div clicked' && document.getElementById("6").className == 'small_div clicked' && document.getElementById("12").className == 'small_div clicked' && document.getElementById("18").className == 'small_div clicked' && document.getElementById("24").className == 'small_div clicked') {
                        document.getElementById('audioComplete').play();
                        document.getElementById('body').classList.add('won');
                        document.getElementById('winScreen').style.display='block';
                        document.getElementById('audioClicked').pause();
                    }
                    else if (document.getElementById("4").className == 'small_div clicked' && document.getElementById("8").className == 'small_div clicked' && document.getElementById("12").className == 'small_div clicked' && document.getElementById("16").className == 'small_div clicked' && document.getElementById("20").className == 'small_div clicked') {
                        document.getElementById('audioComplete').play();
                        document.getElementById('body').classList.add('won');
                        document.getElementById('winScreen').style.display='block';
                        document.getElementById('audioClicked').pause();
                    }
                    // not won
                    else {
                    if (element.className=='small_div clicked'){
                            document.getElementById('audioClicked').play();
                        }
                        document.getElementById('body').classList.remove('won');
                        document.getElementById('winScreen').style.display='none';
                    }
                }
                function showClicked(element) {
                    element.classList.toggle('clicked');
                    // if (element.className == 'small_div clicked') {
                    bingoCheck(element);
                    // }
                }
            </script>
            </html>"""
                )
        elif number_of_squares == 9:
            file.write(
            """
        <script>
            function bingoCheck(element) {
                // rows
                if (document.getElementById("0").className == 'small_div clicked' && document.getElementById("1").className == 'small_div clicked' && document.getElementById("2").className == 'small_div clicked') {
                    document.getElementById('audioComplete').play();
                    document.getElementById('body').classList.add('won');
                    document.getElementById('winScreen').style.display='block';
                    document.getElementById('audioClicked').pause();
                }
                else if (document.getElementById("3").className == 'small_div clicked' && document.getElementById("4").className == 'small_div clicked' && document.getElementById("5").className == 'small_div clicked') {
                    document.getElementById('audioComplete').play();
                    document.getElementById('body').classList.add('won');
                    document.getElementById('winScreen').style.display='block';
                    document.getElementById('audioClicked').pause();
                }
                else if (document.getElementById("6").className == 'small_div clicked' && document.getElementById("7").className == 'small_div clicked' && document.getElementById("8").className == 'small_div clicked') {
                    document.getElementById('audioComplete').play();
                    document.getElementById('body').classList.add('won');
                    document.getElementById('winScreen').style.display='block';
                    document.getElementById('audioClicked').pause();
                }
                // columns
                else if (document.getElementById("0").className == 'small_div clicked' && document.getElementById("3").className == 'small_div clicked' && document.getElementById("6").className == 'small_div clicked' ) {
                    document.getElementById('audioComplete').play();
                    document.getElementById('body').classList.add('won');
                    document.getElementById('winScreen').style.display='block';
                    document.getElementById('audioClicked').pause();
                }
                else if (document.getElementById("1").className == 'small_div clicked' && document.getElementById("4").className == 'small_div clicked' && document.getElementById("7").className == 'small_div clicked' ) {
                    document.getElementById('audioComplete').play();
                    document.getElementById('body').classList.add('won');
                    document.getElementById('winScreen').style.display='block';
                    document.getElementById('audioClicked').pause();
                }
                else if (document.getElementById("2").className == 'small_div clicked' && document.getElementById("5").className == 'small_div clicked' && document.getElementById("8").className == 'small_div clicked' && document.getElementById("17").className == 'small_div clicked' && document.getElementById("22").className == 'small_div clicked') {
                    document.getElementById('audioComplete').play();
                    document.getElementById('body').classList.add('won');
                    document.getElementById('winScreen').style.display='block';
                    document.getElementById('audioClicked').pause();
                }
                // cross
                else if (document.getElementById("0").className == 'small_div clicked' && document.getElementById("4").className == 'small_div clicked' && document.getElementById("8").className == 'small_div clicked' ) {
                    document.getElementById('audioComplete').play();
                    document.getElementById('body').classList.add('won');
                    document.getElementById('winScreen').style.display='block';
                    document.getElementById('audioClicked').pause();
                }
                else if (document.getElementById("2").className == 'small_div clicked' && document.getElementById("4").className == 'small_div clicked' && document.getElementById("6").className == 'small_div clicked') {
                    document.getElementById('audioComplete').play();
                    document.getElementById('body').classList.add('won');
                    document.getElementById('winScreen').style.display='block';
                    document.getElementById('audioClicked').pause();
                }
                // not won
                else {
                if (element.className=='small_div clicked'){
                        document.getElementById('audioClicked').play();
                    }
                    document.getElementById('body').classList.remove('won');
                    document.getElementById('winScreen').style.display='none';
                }
            }
            function showClicked(element) {
                element.classList.toggle('clicked');
                // if (element.className == 'small_div clicked') {
                bingoCheck(element);
                // }
            }
        </script>
        </html>"""
            )
        else:
            file.write(
                """
            <script>
                function bingoCheck(element) {
                    return
                }
                function showClicked(element) {
                    element.classList.toggle('clicked');
                    // if (element.className == 'small_div clicked') {
                    bingoCheck(element);
                    // }
                }
            </script>
            </html>"""
            )
    file.close()
    ######################################################################
    open_file = input("Do you wish to view these cards just now?\n>> ")
    if open_file in "Yy" and open_file != "" and open_file != "\n":
        print("Opening html file(s)")
        for card_number in range(1, 1 + cards_to_generate):
            webbrowser.open(f"{output_file_name} - {card_number}.html")
