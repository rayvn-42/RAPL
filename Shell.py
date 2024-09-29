import rapl

while True:
    try:
        text = input('rapl> ')
        if text.strip() == "":
            continue
        result, error = rapl.run('<stdin>', text)

        if error:
            print(error.as_string())
        elif result:
            if len(result.elements) == 1:
                print(repr(result.elements[0]))
            else:
                print(repr(result))
    except KeyboardInterrupt:
        print("\nExiting RAPL.")
        break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
