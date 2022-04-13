import ascii_magic


class Ascii:
    @staticmethod
    def start():
        try:
            output = ascii_magic.from_image_file("./img/start.jpg", columns=45, char="#")
            ascii_magic.to_terminal(output)
        except Exception as e:
            print("Error start() func => ", e)

    @staticmethod
    def lose():
        try:
            output = ascii_magic.from_image_file("./img/lose.jpg", columns=120, char="#")
            ascii_magic.to_terminal(output)
        except Exception as e:
            print("Error lose() func => ", e)

    @staticmethod
    def bye():
        try:
            output = ascii_magic.from_image_file("./img/bye.jpeg", columns=85, char="#")
            ascii_magic.to_terminal(output)
        except Exception as e:
            print("Error bye() func => ", e)
    
    @staticmethod
    def win():
        try:
            output = ascii_magic.from_image_file("./img/win.jpg", columns=65, char="#")
            ascii_magic.to_terminal(output)
        except Exception as e:
            print("Error win() func => ", e)
