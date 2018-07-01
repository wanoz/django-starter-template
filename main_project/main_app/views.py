from django.shortcuts import render
from main_app.forms import Text_input, Choice_input

# Django view functions
def page_index(request):

    parsed_text = None
    parsed_choice = None

    if request.method == 'POST':
        text_data = Text_input(request.POST)
        choice_data = Choice_input(request.POST)
        print('Status: POST request received')

        # Parsing information
        if text_data.is_valid():
            print('Status: text entry from POST request is valid')
            parsed_text = text_data.cleaned_data['text_input']
            print('Input text: ' + parsed_text)

            # Do things with parsed text data
            
        if choice_data.is_valid():
            print('Status: choice entry from POST request is valid')
            parsed_choice = choice_data.cleaned_data['choice_input']
            print('Input choice: ' + parsed_choice)

            # Do things with parsed choice data

    else:
        text_data = Text_input()
        choice_data = Choice_input()

    # Data to be passed into the web document
    data_content = {
        'text_form' : text_data,
        'choice_form' : choice_data,
    }

    return render(request, 'main_app/index.html', context=data_content)
