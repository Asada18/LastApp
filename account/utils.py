from django.core.mail import send_mail


# def send_activation_code(email, activation_code):
#     activation_url = f'http://localhost:8000/v1/api/account/activate/{activation_code}'
#     message = f"""
#             Thank you for signing up
#             Please, activate your account.
#             Activation link: {activation_url}
#     """
#
#     send_mail(
#         'Activate your account',
#         message,
#         'test@gmail.com',
#         [email, ],
#         fail_silently=False
#     )


def send_activation_code(email, activation_code):
    print(activation_code)
    subject = 'Активация Аккаунта'
    message = f"""Приветствую.\n
     Спасибо за регистрацию на нашем сайте.\n
     Для активации Вашего аккаунта пожалуйста перейдите по ссылке: 
     http://127.0.0.1:8000/api/v1/accounts/activate/{activation_code}/
     """

    from_ = 'test@gmail.com'
    emails = [email, ]

    send_mail(subject, message, from_, emails)










