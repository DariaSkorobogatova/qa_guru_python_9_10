class RegPageLocators:
    first_name_loc = '#firstName'
    last_name_loc = '#lastName'
    email_loc = '#userEmail'
    phone_number_loc = '#userNumber'
    date_of_birth_input_loc = '#dateOfBirthInput'
    choose_month_of_birth_loc = '.react-datepicker__month-select'
    choose_year_of_birth_loc = '.react-datepicker__year-select'
    subject_loc = '#subjectsInput'
    scroll_to_hobby_loc = '[for=hobbies-checkbox-2]'
    choose_hobby_loc = '.custom-checkbox'
    upload_pic_loc = '#uploadPicture'
    current_address_loc = '#currentAddress'
    state_loc = '#state'
    city_loc = '#city'
    choose_state_city_loc = '[id^=react-select][id*=option]'
    submit_button_loc = '#submit'
    final_form_header_loc = '.modal-header'
    final_form_loc = '.table'
    fields_with_user_info_loc = 'td:nth-of-type(even)'
    close_button_loc = '#closeLargeModal'


def choose_day_of_birth(day):
    return f'.react-datepicker__day--0{day}'


def choose_gender(gender):
    return f'[name=gender][value={gender}]+label'
