from utils.translator import translate_text


def handle_translation(input_state, target_lang_var, output_text_var):
    text = input_state.get()
    target_lang_code = target_lang_var.get()
    result = translate_text(text, target_lang_code)
    print(result)
    output_text_var.set(result)