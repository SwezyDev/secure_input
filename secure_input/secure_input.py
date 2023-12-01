def secure_input(prompt):
    password = []
    print(prompt, end='', flush=True)

    try:
        import msvcrt
        while True:
            key = msvcrt.getch()
            key = key.decode('utf-8')
            if key == '\r': 
                print()
                break
            elif key == '\b': 
                if password:
                    password.pop()
                    print('\b \b', end='', flush=True)
            else:
                password.append(key)
                print('*', end='', flush=True)

    except ImportError:
        import termios
        import sys
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setcbreak(fd)
            while True:
                key = sys.stdin.read(1)
                if key == '\r':
                    print()
                    break
                elif key == '\b':
                    if password:
                        password.pop()
                        sys.stdout.write('\b \b')
                else:
                    password.append(key)
                    sys.stdout.write('*')
                sys.stdout.flush()

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ''.join(password)

