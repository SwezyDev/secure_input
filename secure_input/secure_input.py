def secure_input(prompt, show=str):
    password = []
    print(prompt, end='', flush=True)

    try:
        import msvcrt
        while True:
            key = msvcrt.getch()
            try:
                key = key.decode('utf-8')
                if key == '\r': 
                    print()
                    break
                elif key == '\b': 
                    if password:
                        password.pop()
                        print('\b \b', end='', flush=True)
                elif key.isprintable():
                    password.append(key)
                    print(show, end='', flush=True)
            except UnicodeDecodeError:
                pass

    except ImportError:
        import termios
        import sys
        import tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setcbreak(fd)
            while True:
                key = sys.stdin.read(1)
                try:
                    if key == '\r':
                        print()
                        break
                    elif key == '\b':
                        if password:
                            password.pop()
                            sys.stdout.write('\b \b')
                    elif key.isprintable():
                        password.append(key)
                        sys.stdout.write('*')
                    sys.stdout.flush()
                except UnicodeDecodeError:
                    pass

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ''.join(password)